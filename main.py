"""
main.py - run the whole regression study on all three datasets with one
command:

    python main.py

For each dataset (house prices, student grades, tomorrow's temperature) it:
    1. downloads (once) and checks the data, and draws its overview plots,
    2. keeps 20% of the rows back as a test set (for the weather, the most
       recent days),
    3. fits Linear Regression, a Random Forest benchmark and an "always
       predict the average" baseline, tuned with 5-fold cross-validation,
    4. scores them on the test set (MAE, RMSE, R²) and plots predicted
       against real values,
    5. explains Linear Regression: its weights, permutation importance and
       its largest errors,
    6. saves the models for the app.
Then it writes docs/results.md from the saved tables.
Figures and tables go to outputs/<dataset>/, models to models/<dataset>/.
"""

import os

import pandas as pd

from pxlab.common import MODELS_FOLDER, save_table, set_plot_style, write_results_doc
from pxlab.tabular.data import check_columns, input_summary, plot_correlations, plot_target, quality_report, split_data
from pxlab.tabular.evaluate import (
    comparison_table,
    largest_errors,
    plot_predicted_vs_actual,
    plot_residuals,
    test_scores,
)
from pxlab.tabular.explain import (
    coefficients_table,
    permutation_importance_table,
    plot_coefficients,
    plot_permutation_importance,
)
from pxlab.tabular.train import best_model_name, save_models, train_models
from regression_lab.data import load_dataset
from regression_lab.explain import persistence_row
from regression_lab.report import results_sections
from regression_lab.spec import SPECS


def run_dataset(spec):
    """
    The full study for one dataset.

    Input:
        spec: one of the SPECs in spec.py.
    Returns:
        Nothing.
    """
    folder = spec["folder"]
    print(f"\n=== {spec['name']} ===")
    data = load_dataset(spec)
    check_columns(data, spec)
    quality_report(data, spec, f"{folder}/data_quality.csv")
    plot_target(data, spec, f"{folder}/target.png")
    plot_correlations(data, spec, f"{folder}/correlations.png")

    train_features, test_features, train_target, test_target = split_data(data, spec)
    model_folder = os.path.join(MODELS_FOLDER, folder)
    os.makedirs(model_folder, exist_ok=True)
    train_features.assign(**{spec["target"]: train_target}).to_csv(os.path.join(model_folder, "train.csv"), index=False)
    test_features.assign(**{spec["target"]: test_target}).to_csv(os.path.join(model_folder, "test.csv"), index=False)

    print("Fitting with 5-fold cross-validation:")
    results = train_models(spec, train_features, train_target)
    table = comparison_table(results, test_features, test_target, spec, f"{folder}/model_comparison.csv")
    if spec.get("time_order"):
        table = pd.concat([table, pd.DataFrame([persistence_row(test_features, test_target)])], ignore_index=True)
        save_table(table, f"{folder}/model_comparison.csv")
    print(table.to_string(index=False))
    plot_predicted_vs_actual(results, test_features, test_target, spec, f"{folder}/predicted_vs_actual.png")

    linear = results["Linear Regression"]["pipeline"]
    weights = coefficients_table(linear, spec, f"{folder}/coefficients.csv")
    plot_coefficients(weights, filename=f"{folder}/coefficients.png")
    plot_residuals(linear, test_features, test_target, spec, "Linear Regression", f"{folder}/residuals.png")
    save_table(largest_errors(linear, test_features, test_target, spec), f"{folder}/largest_errors.csv")

    # The baseline has no inputs to shuffle, so it is left out here.
    explained = {name: result for name, result in results.items() if result["role"] != "Baseline"}
    importance = permutation_importance_table(
        explained, test_features, test_target, spec, filename=f"{folder}/permutation_importance.csv"
    )
    plot_permutation_importance(importance, filename=f"{folder}/permutation_importance.png")

    model_info = {
        "dataset": spec["name"],
        "best_model": best_model_name(results),
        "test_scores": {
            name: test_scores(r["pipeline"], test_features, test_target, spec) for name, r in results.items()
        },
        "cv_scores": {name: r["cv_score"] for name, r in results.items()},
    }
    model_info.update(input_summary(train_features, spec))
    save_models(results, model_info, folder=model_folder)


def main():
    """
    Run the study on every dataset, then write docs/results.md.

    Returns:
        Nothing.
    """
    set_plot_style()
    for spec in SPECS:
        run_dataset(spec)
    sections = [(f"{spec['name']}: {heading}", items) for spec in SPECS for heading, items in results_sections(spec)]
    write_results_doc(
        "Results",
        "Produced by `python main.py`. Test sets are 20% of each dataset (the most recent days for the weather) "
        "and were not used for fitting or model choice.",
        sections,
    )
    print("\nDone. Figures and tables are in outputs/, models in models/. Run: streamlit run app.py")


if __name__ == "__main__":
    main()
