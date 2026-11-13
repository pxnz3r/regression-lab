### What this is

A study of **linear regression**: predicting a number from other numbers. One model, three problems:

- **House prices**: the sale price of 1,460 homes in Ames, Iowa, from living area, basement and lot size, bedrooms, bathrooms, garage, build quality, age and neighbourhood.
- **Student grades**: the final grade (0 to 20) of 649 students from their two earlier term grades, weekly study time, absences and past failures.
- **Tomorrow's temperature**: London's mean temperature tomorrow from today's weather, over 15 years of daily records.

### How linear regression works

It gives every input a weight and adds them up:

> prediction = starting value + weight₁ × input₁ + weight₂ × input₂ + …

Training picks the weights that make the squared errors on the training data as small as possible. Because the answer is a sum, every prediction can be taken apart: the **Predict** tab shows how far each input moves it from the average.

Each model is compared with two others:

- **Average**, which always predicts the training average. Anything useful must beat it.
- **Random Forest**, a benchmark beyond the course that can bend where a straight line can't.

For the weather there is also **Same as today**, the forecast that tomorrow will be like today. It is hard to beat.

### How the results are measured

On rows the models never saw: a random 20% for houses and students, the last three years for the weather (so the model never learns from the future).

- **MAE**: the average size of an error, in the target's units.
- **RMSE**: like MAE but big errors count more.
- **R²**: the share of the variation the model explains. 1 is perfect, 0 is no better than the average.

### What was found

- **Weather**: linear regression is off by 1.3 °C on average (R² 0.90), beating "same as today" (1.5 °C). Today's highest temperature and the season carry most of it.
- **Students**: R² 0.86, about 0.7 grade points off on average. The second-term grade does nearly all the work; study time and absences add almost nothing once it is known.
- **Houses**: R² 0.83, about $22,000 off on average. Living area, quality and neighbourhood matter most. The Random Forest does better (R² 0.90) because prices don't rise in a straight line with size or quality.

Code and every figure: [github.com/pxnz3r/regression-lab](https://github.com/pxnz3r/regression-lab).
