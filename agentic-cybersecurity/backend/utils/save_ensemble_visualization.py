import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_ensemble_visualization():

    print("=" * 60)
    print("GENERATING ENSEMBLE VISUALIZATION")
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
            'outputs/visualizations/ensemble'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # MODEL PERFORMANCE DATA
        # =====================================

        labels = [

            'CNN-LSTM',

            'Transformer',

            'Ensemble'
        ]

        accuracy = [

            91,

            93,

            96
        ]

        # =====================================
        # BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 6))

        plt.bar(

            labels,

            accuracy
        )

        plt.title(
            "Ensemble Model Accuracy"
        )

        plt.xlabel(
            "Models"
        )

        plt.ylabel(
            "Accuracy (%)"
        )

        plt.ylim(80, 100)

        plt.grid(
            axis='y'
        )

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'ensemble_accuracy.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble accuracy chart saved"
        )

        # =====================================
        # LINE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            labels,

            accuracy,

            marker='o'
        )

        plt.title(
            "Ensemble Accuracy Trend"
        )

        plt.xlabel(
            "Models"
        )

        plt.ylabel(
            "Accuracy (%)"
        )

        plt.ylim(80, 100)

        plt.grid(True)

        plt.tight_layout()

        trend_path = os.path.join(

            output_dir,

            'ensemble_trend.png'
        )

        plt.savefig(

            trend_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble trend chart saved"
        )

        # =====================================
        # PIE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(8, 8))

        plt.pie(

            accuracy,

            labels=labels,

            autopct='%1.1f%%'
        )

        plt.title(
            "Ensemble Accuracy Distribution"
        )

        pie_path = os.path.join(

            output_dir,

            'ensemble_pie.png'
        )

        plt.savefig(

            pie_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble pie chart saved"
        )

        # =====================================
        # COMPARISON CHART
        # =====================================

        baseline = [85, 85, 85]

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            labels,

            accuracy,

            marker='o',

            label='Model Accuracy'
        )

        plt.plot(

            labels,

            baseline,

            linestyle='--',

            label='Baseline'
        )

        plt.title(
            "Ensemble vs Baseline"
        )

        plt.xlabel(
            "Models"
        )

        plt.ylabel(
            "Accuracy (%)"
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        comparison_path = os.path.join(

            output_dir,

            'ensemble_comparison.png'
        )

        plt.savefig(

            comparison_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble comparison chart saved"
        )

        # =====================================
        # RADAR STYLE PERFORMANCE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.fill_between(

            labels,

            accuracy,

            alpha=0.3
        )

        plt.plot(

            labels,

            accuracy,

            marker='o'
        )

        plt.title(
            "Ensemble Performance Coverage"
        )

        plt.xlabel(
            "Models"
        )

        plt.ylabel(
            "Accuracy (%)"
        )

        plt.ylim(80, 100)

        plt.grid(True)

        plt.tight_layout()

        coverage_path = os.path.join(

            output_dir,

            'ensemble_performance_coverage.png'
        )

        plt.savefig(

            coverage_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble performance coverage saved"
        )

        print("=" * 60)
        print("ENSEMBLE VISUALIZATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Ensemble visualization error: {e}"
        )