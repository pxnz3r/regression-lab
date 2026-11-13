"""
data.py - download and prepare the three datasets. Each is downloaded once
into data/ and read from there afterwards.

House prices: the Ames, Iowa housing data (De Cock, 2011), 1,460 sales from
2006 to 2010, via OpenML (dataset 42165).
Student grades: UCI Student Performance (Cortez and Silva, 2008), 649
students of a Portuguese language course, CC BY 4.0.
Weather: daily observations for London, 2010 to 2024, from the Open-Meteo
historical weather API (ERA5 reanalysis, CC BY 4.0).
"""

import io
import json
import os
import zipfile

import pandas as pd
from sklearn.datasets import fetch_openml

from pxlab.common import DATA_FOLDER, download_once

STUDENT_URL = "https://archive.ics.uci.edu/static/public/320/student+performance.zip"
WEATHER_URL = (
    "https://archive-api.open-meteo.com/v1/archive?latitude=51.51&longitude=-0.13"
    "&start_date=2010-01-01&end_date=2024-12-31&timezone=Europe%2FLondon&daily="
    "temperature_2m_mean,temperature_2m_max,temperature_2m_min,relative_humidity_2m_mean,precipitation_sum,"
    "wind_speed_10m_max,pressure_msl_mean,cloud_cover_mean,shortwave_radiation_sum"
)


def load_houses():
    """
    The Ames house sales with the inputs this project uses. Age is worked
    out from the year built and the year sold.

    Returns:
        A DataFrame.
    """
    frame = fetch_openml(
        data_id=42165, as_frame=True, data_home=os.path.join(DATA_FOLDER, "openml"), parser="auto"
    ).frame
    frame["Age"] = frame["YrSold"].astype(int) - frame["YearBuilt"].astype(int)
    frame["Neighborhood"] = frame["Neighborhood"].astype(str)
    columns = [
        "GrLivArea",
        "TotalBsmtSF",
        "LotArea",
        "BedroomAbvGr",
        "FullBath",
        "GarageCars",
        "OverallQual",
        "Age",
        "Neighborhood",
        "SalePrice",
    ]
    return frame[columns].astype({"SalePrice": float})


def load_students():
    """
    The Portuguese-course students. The UCI download is a zip that holds
    another zip with the CSV files (separated by semicolons).

    Returns:
        A DataFrame.
    """
    path = download_once(STUDENT_URL, os.path.join(DATA_FOLDER, "student_performance.zip"))
    with zipfile.ZipFile(path) as outer, zipfile.ZipFile(io.BytesIO(outer.read("student.zip"))) as inner:
        frame = pd.read_csv(inner.open("student-por.csv"), sep=";")
    return frame[["G1", "G2", "studytime", "absences", "failures", "G3"]]


def load_weather():
    """
    Daily London weather, one row per day, with tomorrow's mean temperature
    as the value to predict. Rows stay in date order.

    Returns:
        A DataFrame with a "date" column, the inputs and "temp_tomorrow".
    """
    path = download_once(WEATHER_URL, os.path.join(DATA_FOLDER, "weather_london.json"))
    with open(path, encoding="utf-8") as file:
        daily = json.load(file)["daily"]
    frame = pd.DataFrame(daily).rename(
        columns={
            "time": "date",
            "temperature_2m_mean": "temp_mean",
            "temperature_2m_max": "temp_max",
            "temperature_2m_min": "temp_min",
            "relative_humidity_2m_mean": "humidity",
            "precipitation_sum": "precipitation",
            "wind_speed_10m_max": "wind_max",
            "pressure_msl_mean": "pressure",
            "cloud_cover_mean": "cloud_cover",
            "shortwave_radiation_sum": "radiation",
        }
    )
    frame["date"] = pd.to_datetime(frame["date"])
    frame["month"] = frame["date"].dt.month
    frame["pressure_change"] = frame["pressure"].diff().round(1)
    # The value to predict: the next row's mean temperature.
    frame["temp_tomorrow"] = frame["temp_mean"].shift(-1)
    # The first day has no yesterday and the last day no tomorrow.
    return frame.iloc[1:-1].reset_index(drop=True)


def load_dataset(spec):
    """
    The table for a SPEC.

    Input:
        spec: one of the SPECs in spec.py.
    Returns:
        A DataFrame.
    """
    loaders = {"houses": load_houses, "students": load_students, "weather": load_weather}
    return loaders[spec["folder"]]()
