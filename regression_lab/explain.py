"""
explain.py - how a linear regression arrives at one prediction, and the
"same as today" baseline for the weather data.

A linear model adds up one term per input: weight * (scaled input). If we
measure each input against its training average, the prediction splits
into the average prediction plus one push per input, up or down. That is
the whole explanation; nothing is hidden.
"""

import numpy as np
import pandas as pd

from pxlab.tabular.data import label_for
from pxlab.tabular.evaluate import regression_scores


def source_column(transformed_name, spec):
    """
    The original column a transformed column came from. One-hot columns are
    named like "Neighborhood_NAmes", so they map back to "Neighborhood".

    Inputs:
        transformed_name: a column name from the preprocessing step.
        spec: the dataset SPEC.
    Returns:
        The original column name.
    """
    if transformed_name in spec["numeric"]:
        return transformed_name
    for column in spec["categorical"]:
        if transformed_name.startswith(column + "_"):
            return column
    return transformed_name


def linear_contributions(pipeline, example, train_features, spec):
    """
    Split one linear-regression prediction into the average prediction plus
    one contribution per input.

    Inputs:
        pipeline: a fitted Linear Regression pipeline.
        example: a one-row DataFrame.
        train_features: the training inputs (their average is the reference).
        spec: the dataset SPEC.
    Returns:
        (average prediction, Series readable input name -> contribution,
        largest effect first).
    """
    preprocess = pipeline.named_steps["preprocess"]
    weights = np.ravel(pipeline.named_steps["model"].coef_)
    average_row = preprocess.transform(train_features).mean(axis=0)
    example_row = preprocess.transform(example)[0]
    average_prediction = float(pipeline.named_steps["model"].intercept_ + weights @ average_row)
    pushes = weights * (example_row - average_row)
    names = [source_column(name, spec) for name in preprocess.get_feature_names_out()]
    contributions = pd.Series(pushes).groupby(names).sum()
    contributions.index = [label_for(spec, column) for column in contributions.index]
    return average_prediction, contributions.reindex(contributions.abs().sort_values(ascending=False).index)


class SameAsToday:
    """
    The "persistence" forecast: tomorrow's mean temperature equals today's.
    It needs no training, and it is surprisingly hard to beat, so every
    weather model is compared with it. It has the predict() method that
    pxlab's regression_scores() calls.
    """

    def predict(self, features):
        """
        Today's mean temperature, as the prediction for tomorrow.

        Input:
            features: a DataFrame with a "temp_mean" column.
        Returns:
            A numpy array.
        """
        return features["temp_mean"].to_numpy()


def persistence_row(test_features, test_target):
    """
    The comparison-table row for the "same as today" forecast.

    Inputs:
        test_features, test_target: the weather test set.
    Returns:
        A dictionary with the same columns as the comparison table.
    """
    scores = regression_scores(SameAsToday(), test_features, test_target)
    return {"Model": "Same as today", "Role": "Baseline", **{name: round(value, 3) for name, value in scores.items()}}
