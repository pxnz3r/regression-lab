# Methodology

## Question

How well does linear regression predict a number on three different kinds of data, and which inputs drive its predictions?

## Data

| | House prices | Student grades | Tomorrow's temperature |
| --- | --- | --- | --- |
| Rows | 1,460 sales | 649 students | 5,477 days |
| Predict | sale price ($) | final grade (0 to 20) | tomorrow's mean temperature (°C) |
| Inputs | living, basement and lot area, bedrooms, full bathrooms, garage size, overall quality, age, neighbourhood | first and second term grades, weekly study time band, absences, past failures | today's mean, high and low temperature, humidity, rain, wind, pressure and its change since yesterday, cloud cover, sunshine, month |
| Source | Ames housing, OpenML 42165 | UCI Student Performance (Portuguese course) | Open-Meteo archive, London 2010 to 2024 |

The brief's inputs map to these columns: area is living, basement and lot area; location is the neighbourhood; property age is year sold minus year built; attendance is absences; previous assessment marks are the two term grades.

## Steps

1. **Checks**: missing values, duplicates and ranges (`outputs/<dataset>/data_quality.csv`), the distribution of the target and correlations.
2. **Split**: 80% training, 20% test. Houses and students are split at random. The weather is split by date, the last 20% of days being the test set, because a forecast must only learn from the past.
3. **Models**, each in a scikit-learn Pipeline with its preprocessing (median fill for gaps, one-hot encoding for neighbourhood and month, standardising for Linear Regression), so preprocessing is fitted on training folds only:
   - Linear Regression (ordinary least squares), the model the project is about.
   - Average: always predicts the training mean. The floor.
   - Random Forest, 300 trees, with the minimum leaf size tuned. A benchmark beyond the course.
   - For the weather, also "same as today": tomorrow's mean equals today's.
4. **Cross-validation**: 5 folds on the training set, scored by R². The weather uses time-ordered folds (train on earlier years, validate on the next block).
5. **Test scores**: MAE, RMSE and R² on the test set, and predicted-against-real plots.
6. **Explanation**:
   - Linear Regression weights on standardised inputs: the change in the prediction when an input rises by one standard deviation, others fixed.
   - Permutation importance on the test set: shuffle one input 10 times and record the drop in R².
   - Residual plots and the 20 largest test errors.
   - In the app, a single prediction is split into the average prediction plus one contribution per input (weight times the input's distance from its training average).
7. **In-depth analysis** (`pxlab.tabular.study`): 1,000-round bootstrap 95% intervals for the headline test scores, next to a baseline that ignores the inputs; a Wilcoxon signed-rank test of the best model's errors against each other model's; learning curves; and an error analysis of size and bias across the range of the target, and per category where a dataset has category inputs. Each finding is one sentence in `outputs/<dataset>/key_findings.csv`.

## Limits

- House prices are skewed: a few expensive houses cause the largest errors. Predicting the logarithm of the price would suit a straight line better; the plain price was kept to stay with the brief.
- The weather data is reanalysis (a model blended with observations), not one weather station.
- Some students have a final grade of 0 (they left the course), which a straight line on their earlier grades can't predict. They are kept, and they appear in the largest errors.
- Weights show association in this data, not cause.
