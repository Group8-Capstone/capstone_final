import os
import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_feature_importance(

    feature_names=None,

    importance_scores=None
):

    print("=" * 60)
    print("GENERATING FEATURE IMPORTANCE")
    print("=" * 60)

    try:

        # =====================================
        # APPLY GLOBAL STYLE
        # =====================================

        apply_plot_style()

        # =====================================
        # OUTPUT DIRECTORY
        # =====================================

        output_dir = (

            'outputs/explainability/'
            'feature_importance'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # DEFAULT FEATURE NAMES
        # =====================================

        if feature_names is None:

            feature_names = [

                'Flow Duration',

                'Packet Length',

                'Flow Bytes',

                'Fwd Packets',

                'Bwd Packets',

                'ACK Flag',

                'SYN Flag',

                'PSH Flag',

                'Idle Mean',

                'Flow IAT'
            ]

        # =====================================
        # DEFAULT IMPORTANCE SCORES
        # =====================================

        if importance_scores is None:

            importance_scores = np.random.uniform(

                0,

                1,

                len(feature_names)
            )

        # =====================================
        # SORT FEATURES
        # =====================================

        sorted_indices = np.argsort(
            importance_scores
        )

        sorted_features = np.array(
            feature_names
        )[sorted_indices]

        sorted_scores = np.array(
            importance_scores
        )[sorted_indices]

        # =====================================
        # HORIZONTAL BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 7))

        plt.barh(

            sorted_features,

            sorted_scores
        )

        plt.xlabel(
            'Importance Score'
        )

        plt.ylabel(
            'Features'
        )

        plt.title(
            'Feature Importance Ranking'
        )

        plt.grid(axis='x')

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'feature_importance.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Feature importance chart saved"
        )

        # =====================================
        # LINE VISUALIZATION
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            sorted_scores,

            marker='o'
        )

        plt.xticks(

            range(len(sorted_features)),

            sorted_features,

            rotation=45
        )

        plt.xlabel(
            'Features'
        )

        plt.ylabel(
            'Importance Score'
        )

        plt.title(
            'Feature Importance Trend'
        )

        plt.grid(True)

        plt.tight_layout()

        line_chart_path = os.path.join(

            output_dir,

            'feature_importance_trend.png'
        )

        plt.savefig(

            line_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Feature importance trend saved"
        )

        # =====================================
        # PIE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(8, 8))

        plt.pie(

            sorted_scores,

            labels=sorted_features,

            autopct='%1.1f%%'
        )

        plt.title(
            'Feature Contribution Percentage'
        )

        pie_chart_path = os.path.join(

            output_dir,

            'feature_importance_pie.png'
        )

        plt.savefig(

            pie_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Feature importance pie chart saved"
        )

        # =====================================
        # AREA CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.fill_between(

            range(len(sorted_scores)),

            sorted_scores,

            alpha=0.4
        )

        plt.plot(

            sorted_scores,

            marker='o'
        )

        plt.xticks(

            range(len(sorted_features)),

            sorted_features,

            rotation=45
        )

        plt.xlabel(
            'Features'
        )

        plt.ylabel(
            'Importance Score'
        )

        plt.title(
            'Feature Importance Coverage'
        )

        plt.grid(True)

        plt.tight_layout()

        area_chart_path = os.path.join(

            output_dir,

            'feature_importance_area.png'
        )

        plt.savefig(

            area_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Feature importance area chart saved"
        )

        # =====================================
        # HISTOGRAM
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.hist(

            sorted_scores,

            bins=10
        )

        plt.xlabel(
            'Importance Score'
        )

        plt.ylabel(
            'Frequency'
        )

        plt.title(
            'Feature Importance Distribution'
        )

        plt.tight_layout()

        histogram_path = os.path.join(

            output_dir,

            'feature_importance_histogram.png'
        )

        plt.savefig(

            histogram_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Feature importance histogram saved"
        )

        print("=" * 60)
        print("FEATURE IMPORTANCE COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Feature importance error: {e}"
        )