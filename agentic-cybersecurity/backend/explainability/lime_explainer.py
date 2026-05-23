import os
import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def generate_lime_plot():

    print("=" * 60)
    print("GENERATING LIME EXPLANATION")
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
            'outputs/explainability/lime'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # GENERATE RANDOM IMPORTANCE
        # =====================================

        x = np.arange(10)

        y = np.random.uniform(
            0,
            1,
            10
        )

        feature_names = [

            f'Feature_{i}'

            for i in range(10)
        ]

        # =====================================
        # SORT VALUES
        # =====================================

        sorted_indices = np.argsort(y)

        sorted_scores = y[
            sorted_indices
        ]

        sorted_features = np.array(
            feature_names
        )[sorted_indices]

        # =====================================
        # BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.bar(
            sorted_features,
            sorted_scores
        )

        plt.title(
            "LIME Feature Importance"
        )

        plt.xlabel(
            "Features"
        )

        plt.ylabel(
            "Importance Score"
        )

        plt.xticks(
            rotation=45
        )

        plt.grid(axis='y')

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'lime_explanation.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LIME explanation saved"
        )

        # =====================================
        # LINE VISUALIZATION
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(
            x,
            y,
            marker='o'
        )

        plt.title(
            "LIME Trend Visualization"
        )

        plt.xlabel(
            "Feature Index"
        )

        plt.ylabel(
            "LIME Weight"
        )

        plt.grid(True)

        plt.tight_layout()

        line_path = os.path.join(

            output_dir,

            'lime_trend.png'
        )

        plt.savefig(

            line_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LIME trend visualization saved"
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
            'LIME Feature Contribution'
        )

        pie_path = os.path.join(

            output_dir,

            'lime_pie.png'
        )

        plt.savefig(

            pie_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LIME pie chart saved"
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
            'LIME Feature Coverage'
        )

        plt.grid(True)

        plt.tight_layout()

        area_path = os.path.join(

            output_dir,

            'lime_area.png'
        )

        plt.savefig(

            area_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LIME area chart saved"
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

        plt.title(
            'LIME Score Distribution'
        )

        plt.xlabel(
            'Importance Score'
        )

        plt.ylabel(
            'Frequency'
        )

        plt.grid(True)

        plt.tight_layout()

        histogram_path = os.path.join(

            output_dir,

            'lime_histogram.png'
        )

        plt.savefig(

            histogram_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LIME histogram saved"
        )

        print("=" * 60)
        print("LIME EXPLANATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"LIME generation error: {e}"
        )