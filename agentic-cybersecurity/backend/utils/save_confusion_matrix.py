import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay
)

from utils.plot_style import (
    apply_plot_style
)


def save_confusion_matrix(

    y_true,

    y_pred,

    model_name
):

    print("=" * 60)
    print("GENERATING CONFUSION MATRIX")
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

            'outputs/reports/'
            'confusion_matrix'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # GENERATE MATRIX
        # =====================================

        cm = confusion_matrix(

            y_true,

            y_pred
        )

        print(
            f"Confusion Matrix Shape: "
            f"{cm.shape}"
        )

        # =====================================
        # PLOT MATRIX
        # =====================================

        apply_plot_style()

        fig, ax = plt.subplots(
            figsize=(8, 6)
        )

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm
        )

        disp.plot(
            ax=ax,
            cmap='Blues'
        )

        plt.title(
            f'{model_name} Confusion Matrix'
        )

        plt.tight_layout()

        save_path = os.path.join(

            output_dir,

            f'{model_name}_cm.png'
        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Confusion matrix saved: '
            f'{save_path}'
        )

        # =====================================
        # NORMALIZED MATRIX
        # =====================================

        apply_plot_style()

        fig, ax = plt.subplots(
            figsize=(8, 6)
        )

        normalized_cm = (

            cm.astype('float')

            / cm.sum(axis=1)[:, None]
        )

        normalized_disp = (
            ConfusionMatrixDisplay(
                confusion_matrix=normalized_cm
            )
        )

        normalized_disp.plot(
            ax=ax,
            cmap='Greens'
        )

        plt.title(
            f'{model_name} Normalized '
            f'Confusion Matrix'
        )

        plt.tight_layout()

        normalized_path = os.path.join(

            output_dir,

            f'{model_name}_normalized_cm.png'
        )

        plt.savefig(

            normalized_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Normalized confusion matrix '
            f'saved: {normalized_path}'
        )

        # =====================================
        # DIFFERENCE HEATMAP STYLE
        # =====================================

        apply_plot_style()

        fig, ax = plt.subplots(
            figsize=(8, 6)
        )

        heatmap = ax.imshow(
            cm,
            interpolation='nearest'
        )

        plt.colorbar(heatmap)

        plt.title(
            f'{model_name} Heatmap View'
        )

        plt.xlabel(
            'Predicted Label'
        )

        plt.ylabel(
            'True Label'
        )

        for i in range(cm.shape[0]):

            for j in range(cm.shape[1]):

                ax.text(
                    j,
                    i,
                    cm[i, j],
                    ha='center',
                    va='center'
                )

        heatmap_path = os.path.join(

            output_dir,

            f'{model_name}_heatmap.png'
        )

        plt.tight_layout()

        plt.savefig(

            heatmap_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Heatmap confusion matrix saved: '
            f'{heatmap_path}'
        )

        print("=" * 60)
        print("CONFUSION MATRIX COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Confusion matrix error: {e}"
        )