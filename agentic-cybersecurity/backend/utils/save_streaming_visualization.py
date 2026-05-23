import os
import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_streaming_visualization():

    print("=" * 60)
    print("GENERATING STREAMING VISUALIZATION")
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
            'outputs/visualizations/streaming'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # GENERATE STREAMING DATA
        # =====================================

        x = np.arange(100)

        y = np.random.randint(

            1,

            100,

            100
        )

        # =====================================
        # MAIN TRAFFIC VISUALIZATION
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.plot(

            x,

            y,

            linewidth=2
        )

        plt.title(
            "Streaming Network Traffic"
        )

        plt.xlabel(
            "Time Window"
        )

        plt.ylabel(
            "Traffic Volume"
        )

        plt.grid(True)

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'streaming_traffic.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Streaming traffic "
            "visualization saved"
        )

        # =====================================
        # AREA CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.fill_between(
            x,
            y,
            alpha=0.5
        )

        plt.title(
            "Streaming Traffic Area Chart"
        )

        plt.xlabel(
            "Time Window"
        )

        plt.ylabel(
            "Traffic Volume"
        )

        plt.grid(True)

        plt.tight_layout()

        area_chart_path = os.path.join(

            output_dir,

            'streaming_area_chart.png'
        )

        plt.savefig(

            area_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Streaming area chart saved"
        )

        # =====================================
        # HISTOGRAM
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.hist(
            y,
            bins=15
        )

        plt.title(
            "Traffic Distribution Histogram"
        )

        plt.xlabel(
            "Traffic Volume"
        )

        plt.ylabel(
            "Frequency"
        )

        plt.tight_layout()

        histogram_path = os.path.join(

            output_dir,

            'streaming_histogram.png'
        )

        plt.savefig(

            histogram_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Streaming histogram saved"
        )

        # =====================================
        # SCATTER PLOT
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 6))

        plt.scatter(
            x,
            y
        )

        plt.title(
            "Streaming Traffic Scatter Plot"
        )

        plt.xlabel(
            "Time Window"
        )

        plt.ylabel(
            "Traffic Volume"
        )

        plt.grid(True)

        plt.tight_layout()

        scatter_path = os.path.join(

            output_dir,

            'streaming_scatter.png'
        )

        plt.savefig(

            scatter_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Streaming scatter plot saved"
        )

        print("=" * 60)
        print("STREAMING VISUALIZATION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Streaming visualization "
            f"error: {e}"
        )