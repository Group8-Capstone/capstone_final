import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_attack_distribution(labels):

    print("=" * 60)
    print("GENERATING ATTACK DISTRIBUTION")
    print("=" * 60)

    try:

        # =====================================
        # APPLY GLOBAL STYLE
        # =====================================

        apply_plot_style()

        # =====================================
        # CREATE OUTPUT DIRECTORY
        # =====================================

        output_dir = (
            'outputs/visualizations/attacks'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # VALUE COUNTS
        # =====================================

        attack_counts = labels.value_counts()

        print(
            attack_counts.head()
        )

        # =====================================
        # SORT VALUES
        # =====================================

        attack_counts = attack_counts.sort_values(
            ascending=False
        )

        # =====================================
        # BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(16, 8))

        attack_counts.plot(
            kind='bar'
        )

        plt.title(
            'Attack Distribution'
        )

        plt.xlabel(
            'Attack Type'
        )

        plt.ylabel(
            'Count'
        )

        plt.xticks(
            rotation=45
        )

        plt.grid(
            axis='y'
        )

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            'attack_distribution.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f"Attack distribution saved at:"
            f" {save_path}"
        )

        # =====================================
        # PIE CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 10))

        attack_counts.plot(
            kind='pie',
            autopct='%1.1f%%'
        )

        plt.ylabel('')

        plt.title(
            'Attack Distribution Percentage'
        )

        pie_chart_path = os.path.join(

            output_dir,

            'attack_distribution_pie.png'
        )

        plt.savefig(

            pie_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f"Attack pie chart saved at:"
            f" {pie_chart_path}"
        )

        # =====================================
        # LINE VISUALIZATION
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(14, 6))

        plt.plot(

            attack_counts.values,

            marker='o'
        )

        plt.xticks(

            range(len(attack_counts.index)),

            attack_counts.index,

            rotation=45
        )

        plt.xlabel(
            'Attack Type'
        )

        plt.ylabel(
            'Count'
        )

        plt.title(
            'Attack Distribution Trend'
        )

        plt.grid(True)

        plt.tight_layout()

        line_chart_path = os.path.join(

            output_dir,

            'attack_distribution_trend.png'
        )

        plt.savefig(

            line_chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f"Attack trend chart saved at:"
            f" {line_chart_path}"
        )

        print("=" * 60)
        print("ATTACK DISTRIBUTION COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Error generating attack "
            f"distribution: {e}"
        )