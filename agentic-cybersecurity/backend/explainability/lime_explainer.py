import os
import joblib
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from lime.lime_tabular import LimeTabularExplainer

from utils.plot_style import apply_plot_style


def generate_lime_plot(
    model,
    X_train,
    X_sample,
    model_name="fraud_detection",
    output_dir="outputs/explainability/lime"
):
    """
    Generate LIME explanation using real feature names.
    """

    print("=" * 60)
    print("GENERATING LIME EXPLANATION")
    print("=" * 60)

    try:

        apply_plot_style()

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        # ---------------------------------
        # Load saved feature names
        # ---------------------------------

        feature_path = (
            f"outputs/trained_models/"
            f"{model_name}/feature_names.pkl"
        )

        if os.path.exists(feature_path):
            feature_names = joblib.load(feature_path)
        else:
            feature_names = [
                f"Feature_{i}"
                for i in range(X_train.shape[1])
            ]

        # ---------------------------------
        # Build LIME explainer
        # ---------------------------------

        explainer = LimeTabularExplainer(
            training_data=np.asarray(X_train),
            feature_names=feature_names,
            class_names=["Normal", "Attack"],
            mode="classification"
        )

        explanation = explainer.explain_instance(
            np.asarray(X_sample),
            model.predict_proba,
            num_features=min(10, len(feature_names))
        )

        explanation_list = explanation.as_list()

        features = [x[0] for x in explanation_list]
        scores = [abs(x[1]) for x in explanation_list]

        order = np.argsort(scores)

        features = np.array(features)[order]
        scores = np.array(scores)[order]

        # ---------------------------------
        # Bar Chart
        # ---------------------------------

        apply_plot_style()

        plt.figure(figsize=(12, 6))
        plt.barh(features, scores)
        plt.xlabel("Importance")
        plt.title("LIME Feature Importance")
        plt.tight_layout()

        plt.savefig(
            os.path.join(output_dir, "lime_explanation.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.close()

        # ---------------------------------
        # Trend
        # ---------------------------------

        plt.figure(figsize=(10, 5))
        plt.plot(
            range(len(scores)),
            scores,
            marker="o"
        )
        plt.xticks(
            range(len(features)),
            features,
            rotation=45,
            ha="right"
        )
        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "lime_trend.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.close()

        # ---------------------------------
        # Pie
        # ---------------------------------

        plt.figure(figsize=(8, 8))
        plt.pie(
            scores,
            labels=features,
            autopct="%1.1f%%"
        )
        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "lime_pie.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.close()

        # ---------------------------------
        # Area
        # ---------------------------------

        plt.figure(figsize=(12, 6))
        plt.fill_between(
            range(len(scores)),
            scores,
            alpha=0.4
        )
        plt.plot(scores, marker="o")
        plt.xticks(
            range(len(features)),
            features,
            rotation=45,
            ha="right"
        )
        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "lime_area.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.close()

        # ---------------------------------
        # Histogram
        # ---------------------------------

        plt.figure(figsize=(10, 5))
        plt.hist(scores, bins=min(10, len(scores)))
        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "lime_histogram.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.close()

        print("LIME explanation generated successfully.")

    except Exception as e:
        print(f"LIME generation error: {e}")
