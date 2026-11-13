"""
report.py - which saved tables and figures make up the results. The app's
Results tab and docs/results.md both read this list, so they always match.
"""


def results_sections(spec):
    """
    The results for one dataset, grouped into sections.

    Input:
        spec: the dataset SPEC.
    Returns:
        A list of (section name, items) for pxlab's show_results_tabs() and
        write_results_doc().
    """
    folder = spec["folder"]
    return [
        (
            "Models",
            [
                ("table", "Test-set errors", f"{folder}/model_comparison.csv"),
                ("figure", f"{folder}/predicted_vs_actual.png"),
            ],
        ),
        (
            "Weights",
            [
                ("figure", f"{folder}/coefficients.png"),
                (
                    "table",
                    "Linear Regression weights (per standard deviation of each input)",
                    f"{folder}/coefficients.csv",
                ),
            ],
        ),
        (
            "Which inputs matter",
            [
                ("figure", f"{folder}/permutation_importance.png"),
                (
                    "table",
                    "Permutation importance (drop in R² when the input is shuffled)",
                    f"{folder}/permutation_importance.csv",
                ),
            ],
        ),
        (
            "Errors",
            [
                ("figure", f"{folder}/residuals.png"),
                ("table", "Largest Linear Regression errors on the test set", f"{folder}/largest_errors.csv"),
            ],
        ),
        (
            "Data",
            [
                ("table", "Data quality", f"{folder}/data_quality.csv"),
                ("figure", f"{folder}/target.png"),
                ("figure", f"{folder}/correlations.png"),
            ],
        ),
    ]
