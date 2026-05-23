import os
import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_lanl_visualization():

    print("=" * 60)
    print("GENERATING LANL VISUALIZATION")
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
            'outputs/visualizations/lanl'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # GENERATE SAMPLE DATA
        # =====================================

        users = np.arange(1, 21)

        anomaly_counts = np.random.randint(

            1,

            50,

            20
        )

        # =====================================
        # BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.bar(

            users,

            anomaly_counts
        )

        plt.title(
            'LANL UEBA Anomalies'
        )

        plt.xlabel(
            'User ID'
        )

        plt.ylabel(
            'Anomaly Count'
        )

        plt.grid(
            axis='y'
        )

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'lanl_anomalies.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LANL anomaly chart saved"
        )

        # =====================================
        # LINE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 5))

        plt.plot(

            users,

            anomaly_counts,

            marker='o'
        )

        plt.title(
            'LANL UEBA Trend Analysis'
        )

        plt.xlabel(
            'User ID'
        )

        plt.ylabel(
            'Anomaly Count'
        )

        plt.grid(True)

        plt.tight_layout()

        trend_path = os.path.join(

            output_dir,

            'lanl_trend.png'
        )

        plt.savefig(

            trend_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LANL trend chart saved"
        )

        # =====================================
        # PIE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 10))

        plt.pie(

            anomaly_counts,

            labels=[
                f'U{i}'
                for i in users
            ],

            autopct='%1.1f%%'
        )

        plt.title(
            'LANL User Anomaly Distribution'
        )

        pie_path = os.path.join(

            output_dir,

            'lanl_distribution_pie.png'
        )

        plt.savefig(

            pie_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LANL distribution pie chart saved"
        )

        # =====================================
        # HISTOGRAM
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.hist(

            anomaly_counts,

            bins=10
        )

        plt.title(
            'LANL Anomaly Histogram'
        )

        plt.xlabel(
            'Anomaly Count'
        )

        plt.ylabel(
            'Frequency'
        )

        plt.tight_layout()

        histogram_path = os.path.join(

            output_dir,

            'lanl_histogram.png'
        )

        plt.savefig(

            histogram_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LANL histogram saved"
        )

        # =====================================
        # SCATTER PLOT
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.scatter(

            users,

            anomaly_counts
        )

        plt.title(
            'LANL UEBA Scatter Analysis'
        )

        plt.xlabel(
            'User ID'
        )

        plt.ylabel(
            'Anomaly Count'
        )

        plt.grid(True)

        plt.tight_layout()

        scatter_path = os.path.join(

            output_dir,

            'lanl_scatter.png'
        )

        plt.savefig(

            scatter_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "LANL scatter plot saved"
        )

        print("=" * 60)
        print("LANL VISUALIZATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"LANL visualization error: {e}"
        )