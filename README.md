<div align="center">

<h1>Regression lab</h1>

<p>Linear regression on three problems: house prices, student grades and tomorrow's temperature. How well it predicts, how it compares with simple baselines and a non-linear benchmark, and which inputs drive each prediction. Includes an interactive demo.</p>

<p>
<a href="https://github.com/pxnz3r/regression-lab/actions/workflows/ci.yml"><img src="https://github.com/pxnz3r/regression-lab/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
<img src="https://img.shields.io/badge/python-3.14-blue" alt="Python 3.14">
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license"></a>
</p>

<p><a href="docs/results.md">Results</a> · <a href="docs/methodology.md">Methodology</a> · <a href="docs/deploy.md">Deploy the demo</a></p>

<img src="outputs/figures/weather/predicted_vs_actual.png" width="720" alt="Predicted against real temperatures on the test years">

</div>

## How it works

1. **Load and check** three problems: house prices, student grades and tomorrow's temperature.
2. **Fit** linear regression against simple baselines and a non-linear benchmark, tuned with cross-validation.
3. **Score once** on a held-out test split and explain each model's inputs.
4. **Test how sure the scores are** with bootstrap intervals, a paired test against every rival, learning curves and a baseline that ignores the inputs.
5. **Study the errors** by price or grade range and by category, then **try it** in the Streamlit demo.

## Results

Test sets were not used for fitting or model choice: a random 20% for houses and students, and the last 20% of days (2022 to 2024) for the weather.

| Dataset | Model | MAE | RMSE | R² |
| --- | --- | --- | --- | --- |
| Tomorrow's temperature (5,477 days) | **Linear Regression** | **1.34 °C** | 1.74 °C | **0.900** |
| | Same as today (baseline) | 1.49 °C | 1.96 °C | 0.873 |
| | Random Forest (benchmark) | 1.37 °C | 1.77 °C | 0.896 |
| Student grades (649 students) | **Linear Regression** | **0.75** | 1.16 | **0.863** |
| | Random Forest (benchmark) | 0.73 | 1.21 | 0.850 |
| House prices (1,460 sales) | **Linear Regression** | **$21,800** | $35,800 | **0.833** |
| | Random Forest (benchmark) | $18,000 | $27,800 | 0.899 |

Always predicting the training average scores R² of about 0 on every dataset.

- **Weather**: a straight line on today's weather and the month beats the "same as today" forecast by about 10%. Today's highest temperature carries most of the signal.
- **Students**: the second-term grade explains nearly everything (permutation importance 1.35 against 0.03 for the first-term grade). Study time and absences add little once recent marks are known.
- **Houses**: living area, overall quality and neighbourhood matter most. Prices curve upward with size and quality, which a straight line misses and a forest catches, hence the gap.

Full tables and figures: [docs/results.md](docs/results.md). How it was done: [docs/methodology.md](docs/methodology.md).

## How sure the results are

**House prices: the forest is clearly ahead.** R² 0.899 (95% interval 0.862 to 0.927), and its errors are smaller than linear regression's on the Wilcoxon signed-rank test (p < 0.001). It still under-predicts the most expensive fifth of houses.

**Grades and temperature: linear regression is enough.** The forest's edge on grades (p = 0.232) and linear regression's on temperature (p = 0.127) could both be chance. Temperature reaches R² 0.900 (0.888 to 0.912).

**Linear regression never overfits here.** Training and validation R² stay within 0.03 on all three problems; the forest's gap on house prices is 0.15.

**All models pull towards the average.** The coldest days are predicted too warm by about 1.1 °C, and the best students' grades too low.

Every table and figure behind these is in [docs/results.md](docs/results.md).

## Run it

Needs Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python main.py
uv run streamlit run app.py
```

`main.py` downloads the three datasets once into `data/`, then writes figures and tables to `outputs/`, models to `models/` and the tables to `docs/results.md`. Outputs and models are committed, so the demo works without running it.

## The demo

- **Overview**: what linear regression is, how it is measured and what was found.
- **Predict**: start from typical values or a real test example, change the inputs and see the prediction. For Linear Regression, a chart shows how far each input moves the prediction from the average.
- **Results**: model comparison, weights, permutation importance, the largest errors and the data checks.

## Layout

```
regression_lab/   spec.py (datasets and models), data.py (downloads), explain.py (per-input contributions), report.py
pxlab/            shared engine (vendored): data checks, pipelines, tuning, evaluation, app helpers
main.py           the full study
app.py            the Streamlit demo
docs/             methodology, results, deploy
```

## Data

- **House prices**: Ames, Iowa housing data, De Cock (2011), *Journal of Statistics Education* 19(3), via [OpenML 42165](https://www.openml.org/d/42165).
- **Student grades**: Cortez and Silva (2008), [UCI Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance), CC BY 4.0. The Portuguese-course file.
- **Weather**: London (51.51 N, 0.13 W), 2010 to 2024, from the [Open-Meteo historical weather API](https://open-meteo.com/en/docs/historical-weather-api) (ERA5 reanalysis), CC BY 4.0.

## License

MIT
