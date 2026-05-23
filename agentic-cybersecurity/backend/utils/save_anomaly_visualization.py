import os
import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_anomaly_visualization():

    print("=" * 60)
    print("GENERATING ANOMALY VISUALIZATION")
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
            'outputs/visualizations/anomaly_detection'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # GENERATE ANOMALY SCORES
        # =====================================

        anomaly_scores = np.random.rand(
            1000
        )

        threshold = 0.8

        anomalies = anomaly_scores > threshold

        # =====================================
        # MAIN LINE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(14, 6))

        plt.plot(

            anomaly_scores,

            linewidth=1.5
        )

        plt.axhline(

            y=threshold,

            linestyle='--'
        )

        plt.title(
            'Autoencoder Anomaly Scores'
        )

        plt.xlabel(
            'Network Flow'
        )

        plt.ylabel(
            'Anomaly Score'
        )

        plt.grid(True)

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'anomaly_scores.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Anomaly score chart saved"
        )

        # =====================================
        # HISTOGRAM
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.hist(

            anomaly_scores,

            bins=30
        )

        plt.axvline(

            threshold,

            linestyle='--'
        )

        plt.title(
            'Anomaly Score Distribution'
        )

        plt.xlabel(
            'Anomaly Score'
        )

        plt.ylabel(
            'Frequency'
        )

        plt.tight_layout()

        histogram_path = os.path.join(

            output_dir,

            'anomaly_histogram.png'
        )

        plt.savefig(

            histogram_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Anomaly histogram saved"
        )

        # =====================================
        # SCATTER PLOT
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(14, 6))

        plt.scatter(

            range(len(anomaly_scores)),

            anomaly_scores,

            c=anomalies.astype(int)
        )

        plt.axhline(

            threshold,

            linestyle='--'
        )

        plt.title(
            'Detected Network Anomalies'
        )

        plt.xlabel(
            'Network Flow'
        )

        plt.ylabel(
            'Anomaly Score'
        )

        plt.grid(True)

        plt.tight_layout()

        scatter_path = os.path.join(

            output_dir,

            'anomaly_scatter.png'
        )

        plt.savefig(

            scatter_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Anomaly scatter plot saved"
        )

        # =====================================
        # PIE CHART
        # =====================================

        normal_count = np.sum(
            ~anomalies
        )

        anomaly_count = np.sum(
            anomalies
        )

        apply_plot_style()

        plt.figure(figsize=(8, 8))

        plt.pie(

            [normal_count, anomaly_count],

            labels=[
                'Normal',
                'Anomaly'
            ],

            autopct='%1.1f%%'
        )

        plt.title(
            'Anomaly Detection Ratio'
        )

        pie_path = os.path.join(

            output_dir,

            'anomaly_ratio.png'
        )

        plt.savefig(

            pie_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Anomaly ratio chart saved"
        )

        print("=" * 60)
        print("ANOMALY VISUALIZATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Anomaly visualization error: {e}"
        )