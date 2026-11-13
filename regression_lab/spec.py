"""
spec.py - the three datasets and the models trained on each.

The pxlab engine reads these dictionaries: which column to predict, which
columns are inputs, readable names, and the models with the settings that
grid search tries.
"""

from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from pxlab.common import RANDOM_STATE


def regression_models():
    """
    The models compared on every dataset.

    Linear Regression is the model this project is about. It predicts with
    one weight per input: prediction = intercept + w1*x1 + w2*x2 + ...
    Inputs are standardised first so the weights can be compared.

    "Average" always predicts the training average. Any useful model has to
    beat it. Random Forest is a benchmark beyond the course: it shows how
    much a model that can bend (non-linear) gains over a straight line.

    Returns:
        The SPEC["models"] dictionary.
    """
    return {
        "Linear Regression": {"estimator": LinearRegression(), "grid": {}, "scale": True, "role": "Main"},
        "Random Forest": {
            "estimator": RandomForestRegressor(n_estimators=300, random_state=RANDOM_STATE, n_jobs=1),
            "grid": {"min_samples_leaf": [1, 5, 20]},
            "scale": False,
            "role": "Benchmark beyond the course",
        },
        "Average": {"estimator": DummyRegressor(strategy="mean"), "grid": {}, "scale": False, "role": "Baseline"},
    }


HOUSE_SPEC = {
    "name": "House prices",
    "folder": "houses",
    "task": "regression",
    "target": "SalePrice",
    "numeric": [
        "GrLivArea",
        "TotalBsmtSF",
        "LotArea",
        "BedroomAbvGr",
        "FullBath",
        "GarageCars",
        "OverallQual",
        "Age",
    ],
    "categorical": ["Neighborhood"],
    "whole_numbers": [
        "GrLivArea",
        "TotalBsmtSF",
        "LotArea",
        "BedroomAbvGr",
        "FullBath",
        "GarageCars",
        "OverallQual",
        "Age",
    ],
    "labels": {
        "GrLivArea": "Living area (sq ft)",
        "TotalBsmtSF": "Basement area (sq ft)",
        "LotArea": "Lot area (sq ft)",
        "BedroomAbvGr": "Bedrooms",
        "FullBath": "Full bathrooms",
        "GarageCars": "Garage size (cars)",
        "OverallQual": "Overall quality (1 to 10)",
        "Age": "Age when sold (years)",
        "Neighborhood": "Neighbourhood",
        "SalePrice": "Sale price ($)",
    },
    "help": {
        "GrLivArea": "Finished living area above ground.",
        "OverallQual": "The assessor's rating of materials and finish: 1 very poor, 10 very excellent.",
        "Neighborhood": "Neighbourhood within Ames, Iowa. This is the location input.",
        "Age": "Year sold minus year built.",
    },
    "value_format": "${:,.0f}",
    "test_size": 0.2,
    "scoring": "r2",
    "models": regression_models(),
}

STUDENT_SPEC = {
    "name": "Student grades",
    "folder": "students",
    "task": "regression",
    "target": "G3",
    "numeric": ["G1", "G2", "studytime", "absences", "failures"],
    "categorical": [],
    "whole_numbers": ["G1", "G2", "studytime", "absences", "failures"],
    "labels": {
        "G1": "First-term grade (0 to 20)",
        "G2": "Second-term grade (0 to 20)",
        "studytime": "Weekly study time (band)",
        "absences": "Absences",
        "failures": "Past class failures",
        "G3": "Final grade (0 to 20)",
    },
    "help": {
        "studytime": "1 = under 2 hours, 2 = 2 to 5 hours, 3 = 5 to 10 hours, 4 = over 10 hours.",
        "absences": "School absences in the year. This is the attendance input.",
        "G1": "Earlier assessment mark.",
        "G2": "Earlier assessment mark.",
    },
    "value_format": "{:.1f} / 20",
    "test_size": 0.2,
    "scoring": "r2",
    "models": regression_models(),
}

WEATHER_SPEC = {
    "name": "Tomorrow's temperature",
    "folder": "weather",
    "task": "regression",
    "target": "temp_tomorrow",
    "numeric": [
        "temp_mean",
        "temp_max",
        "temp_min",
        "humidity",
        "precipitation",
        "wind_max",
        "pressure",
        "pressure_change",
        "cloud_cover",
        "radiation",
    ],
    "categorical": ["month"],
    "labels": {
        "temp_mean": "Mean temperature today (°C)",
        "temp_max": "Highest temperature today (°C)",
        "temp_min": "Lowest temperature today (°C)",
        "humidity": "Mean humidity (%)",
        "precipitation": "Rain and snow (mm)",
        "wind_max": "Strongest wind (km/h)",
        "pressure": "Mean sea-level pressure (hPa)",
        "pressure_change": "Pressure change since yesterday (hPa)",
        "cloud_cover": "Mean cloud cover (%)",
        "radiation": "Sunshine energy (MJ/m²)",
        "month": "Month",
        "temp_tomorrow": "Mean temperature tomorrow (°C)",
    },
    "help": {
        "pressure_change": "Falling pressure often means a front, and a change in temperature, is coming.",
        "radiation": "Total solar radiation reaching the ground over the day.",
        "month": "1 = January. Captures the season.",
    },
    "value_format": "{:.1f} °C",
    # Days are in date order: train on the earlier years, test on the last ones.
    "time_order": True,
    "test_size": 0.2,
    "scoring": "r2",
    "models": regression_models(),
}

SPECS = [HOUSE_SPEC, STUDENT_SPEC, WEATHER_SPEC]
