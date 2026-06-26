import os
import joblib
import shap
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from utils.plot_style import apply_plot_style


def generate_shap_plot(
    model=None,
    X_sample=None,
    feature_names=None,
    model_name="fraud_detection"
):
    """
    Generate SHAP explanation using dynamic feature names.
    """

    print("=" * 60)
    print("GENERATING SHAP EXPLANATION")
    print("=" * 60)

    try:

        apply_plot_style()

        output_dir = "outputs/explainability/shap"

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        if model is None or X_sample is None:
            raise ValueError(
                "Model and input sample are required."
            )

        # ------------------------------------
        # Load feature names automatically
        # ------------------------------------

        if feature_names is None:

            feature_path = (
                f"outputs/trained_models/"
                f"{model_name}/feature_names.pkl"
            )

            if os.path.exists(feature_path):

                feature_names = joblib.load(
                    feature_path
                )

            else:

                feature_names = [
                    f"Feature_{i}"
                    for i in range(X_sample.shape[1])
                ]

        # ------------------------------------
        # Convert to DataFrame
        # ------------------------------------

        if not isinstance(X_sample, pd.DataFrame):

            X_sample = pd.DataFrame(
                X_sample,
                columns=feature_names
            )

        X_subset = X_sample.iloc[:100]

        # ------------------------------------
        # SHAP Explainer
        # ------------------------------------

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(
            X_subset
        )

        # ------------------------------------
        # Summary Plot
        # ------------------------------------

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        shap.summary_plot(
            shap_values,
            X_subset,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_dir,
                "shap_summary.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # ------------------------------------
        # Bar Plot
        # ------------------------------------

        plt.figure(figsize=(12, 6))

        shap.summary_plot(
            shap_values,
            X_subset,
            plot_type="bar",
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_dir,
                "shap_bar.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # ------------------------------------
        # Trend Plot
        # ------------------------------------

        values = np.abs(
            np.array(shap_values)
        )

        if values.ndim == 3:
            values = values[1]

        mean_values = values.mean(axis=0)

        order = np.argsort(mean_values)

        sorted_scores = mean_values[order]

        sorted_features = np.array(
            feature_names
        )[order]

        plt.figure(figsize=(12, 6))

        plt.plot(
            sorted_scores,
            marker="o"
        )

        plt.xticks(
            range(len(sorted_features)),
            sorted_features,
            rotation=90
        )

        plt.xlabel("Features")
        plt.ylabel("Mean SHAP Value")
        plt.title("SHAP Importance Trend")

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_dir,
                "shap_trend.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # ------------------------------------
        # Histogram
        # ------------------------------------

        plt.figure(figsize=(10, 5))

        plt.hist(
            mean_values,
            bins=15
        )

        plt.xlabel("Mean SHAP Value")
        plt.ylabel("Frequency")
        plt.title("SHAP Value Distribution")

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_dir,
                "shap_histogram.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("=" * 60)
        print("SHAP EXPLANATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"SHAP generation error: {e}"
        )
