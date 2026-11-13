"""
app.py - the regression lab demo. Run it with:

    streamlit run app.py

Pick a dataset, then:
    Overview   what the project is and how linear regression works,
    Predict    enter the inputs (or start from a real test example), see
               the prediction and how much each input pushed it up or down,
    Results    the saved tables and figures from main.py.
It needs the saved models, so run `python main.py` once first.
"""

import os

import pandas as pd
import streamlit as st

from pxlab.app import input_form, setup_page, show_markdown_file, show_results_tabs, signed_bars
from pxlab.common import MODELS_FOLDER
from pxlab.tabular.data import label_for
from pxlab.tabular.train import load_models, models_are_saved
from regression_lab.explain import linear_contributions
from regression_lab.report import results_sections
from regression_lab.spec import SPECS

SPECS_BY_NAME = {spec["name"]: spec for spec in SPECS}
TYPICAL = "Typical values"
TEST_EXAMPLES = 15


@st.cache_resource
def load_dataset_models(folder):
    """
    Load the saved models and the training and test sets for one dataset
    (cached, so this happens once per dataset).

    Input:
        folder: the dataset folder name inside models/.
    Returns:
        (model_info, models, train table, test table)
    """
    model_folder = os.path.join(MODELS_FOLDER, folder)
    model_info, models = load_models(model_folder)
    train = pd.read_csv(os.path.join(model_folder, "train.csv"))
    test = pd.read_csv(os.path.join(model_folder, "test.csv"))
    return model_info, models, train, test


def signed(spec, value):
    """
    A change in the predicted value with its sign, in the dataset's units.

    Inputs:
        spec: the dataset SPEC.
        value: the change.
    Returns:
        Text like "+$12,300" or "−0.4 °C".
    """
    return ("+" if value >= 0 else "−") + spec["value_format"].format(abs(value))


def show_predict_page(spec, model_info, models, train, test):
    """
    The Predict tab: inputs on the left; the prediction and its explanation
    on the right.

    Inputs:
        spec: the dataset SPEC.
        model_info, models: from load_models().
        train, test: the saved training and test tables.
    Returns:
        Nothing.
    """
    inputs = list(spec["numeric"]) + list(spec["categorical"])
    target_label = label_for(spec, spec["target"])
    left, right = st.columns([3, 2], gap="large")
    with left:
        picker, model_box = st.columns(2)
        test_options = [
            f"Test example {number + 1} (real: {spec['value_format'].format(test[spec['target']].iloc[number])})"
            for number in range(min(TEST_EXAMPLES, len(test)))
        ]
        start = picker.selectbox(
            "Start from",
            [TYPICAL, *test_options],
            help="Typical values are the training medians (most common category). "
            "Test examples are real rows the models never saw.",
        )
        model_name = model_box.selectbox("Model", list(models), index=list(models).index("Linear Regression"))
        if start == TYPICAL:
            start_values, real_value = model_info["default_values"], None
        else:
            row = test.iloc[test_options.index(start)]
            start_values, real_value = row[inputs].to_dict(), float(row[spec["target"]])
        example = input_form(spec, model_info, start_values, key_prefix=f"{spec['folder']}-{start}-")

    pipeline = models[model_name]
    prediction = float(pipeline.predict(example)[0])
    with right:
        st.metric(f"Predicted {target_label[0].lower() + target_label[1:]}", spec["value_format"].format(prediction))
        if real_value is not None:
            st.caption(
                f"Real value of this test example: {spec['value_format'].format(real_value)} "
                "(before any changes you make to the inputs)."
            )
        if model_name == "Linear Regression":
            average, contributions = linear_contributions(pipeline, example, train[inputs], spec)
            st.subheader("How it got there", anchor=False)
            st.caption(
                f"Average prediction over the training data: {spec['value_format'].format(average)}. "
                "Each bar is how far one input moves this prediction from that average."
            )
            signed_bars(contributions, lambda value: signed(spec, value))
        else:
            st.caption("Pick Linear Regression to see the prediction split into one push per input.")


def main():
    """
    Build the page.

    Returns:
        Nothing.
    """
    setup_page("Regression lab")
    dataset_name = st.radio("Dataset", list(SPECS_BY_NAME), horizontal=True)
    spec = SPECS_BY_NAME[dataset_name]
    if not models_are_saved(os.path.join(MODELS_FOLDER, spec["folder"])):
        st.error("No saved models yet. Run `python main.py` first.")
        st.stop()
    model_info, models, train, test = load_dataset_models(spec["folder"])

    overview, predict, results = st.tabs(["Overview", "Predict", "Results"])
    with overview:
        show_markdown_file("app_overview.md")
    with predict:
        show_predict_page(spec, model_info, models, train, test)
    with results:
        show_results_tabs(results_sections(spec))


main()
