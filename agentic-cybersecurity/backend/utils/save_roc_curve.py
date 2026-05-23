import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from sklearn.metrics import (
    roc_curve,
    auc
)

from utils.plot_style import (
    apply_plot_style
)


def save_roc_curve(

    y_test,

    prediction_probabilities,

    model_name
):

    print("=" * 60)
    print("GENERATING ROC CURVE")
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
            'outputs/reports/roc_curves'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # COMPUTE ROC
        # =====================================

        fpr, tpr, thresholds = roc_curve(

            y_test,

            prediction_probabilities
        )

        roc_auc = auc(
            fpr,
            tpr
        )

        print(
            f"AUC Score: {roc_auc:.4f}"
        )

        # =====================================
        # ROC CURVE PLOT
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 6))

        plt.plot(

            fpr,

            tpr,

            linewidth=2,

            label=(
                f'AUC = {roc_auc:.4f}'
            )
        )

        # Random baseline
        plt.plot(

            [0, 1],

            [0, 1],

            linestyle='--'
        )

        plt.xlabel(
            'False Positive Rate'
        )

        plt.ylabel(
            'True Positive Rate'
        )

        plt.title(
            f'ROC Curve - {model_name}'
        )

        plt.legend(
            loc='lower right'
        )

        plt.grid(True)

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            f'{model_name}_roc.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'ROC curve saved: '
            f'{save_path}'
        )

        # =====================================
        # THRESHOLD VISUALIZATION
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            thresholds,

            tpr[:-1],

            label='TPR'
        )

        plt.plot(

            thresholds,

            fpr[:-1],

            label='FPR'
        )

        plt.xlabel(
            'Threshold'
        )

        plt.ylabel(
            'Score'
        )

        plt.title(
            f'ROC Threshold Analysis - '
            f'{model_name}'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        threshold_path = os.path.join(

            output_dir,

            f'{model_name}_threshold_analysis.png'
        )

        plt.savefig(

            threshold_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Threshold analysis saved: '
            f'{threshold_path}'
        )

        # =====================================
        # TPR VS FPR COMPARISON
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            tpr,

            label='True Positive Rate'
        )

        plt.plot(

            fpr,

            label='False Positive Rate'
        )

        plt.title(
            f'TPR vs FPR Comparison - '
            f'{model_name}'
        )

        plt.xlabel(
            'Index'
        )

        plt.ylabel(
            'Rate'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        comparison_path = os.path.join(

            output_dir,

            f'{model_name}_tpr_fpr_comparison.png'
        )

        plt.savefig(

            comparison_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'TPR/FPR comparison saved: '
            f'{comparison_path}'
        )

        # =====================================
        # AUC SCORE BAR CHART
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(6, 5))

        plt.bar(

            ['AUC Score'],

            [roc_auc]
        )

        plt.ylim(0, 1)

        plt.title(
            f'{model_name} AUC Score'
        )

        plt.ylabel(
            'AUC Value'
        )

        plt.tight_layout()

        auc_bar_path = os.path.join(

            output_dir,

            f'{model_name}_auc_bar.png'
        )

        plt.savefig(

            auc_bar_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'AUC bar chart saved: '
            f'{auc_bar_path}'
        )

        print("=" * 60)
        print("ROC CURVE COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"ROC curve error: {e}"
        )