import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from utils.plot_style import (
    apply_plot_style
)


def save_training_plot(

    history,

    model_name
):

    print("=" * 60)
    print("GENERATING TRAINING VISUALIZATIONS")
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
            'outputs/reports/accuracy_plots'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # EXTRACT TRAINING HISTORY
        # =====================================

        train_loss = history.history.get(
            'loss',
            []
        )

        val_loss = history.history.get(
            'val_loss',
            []
        )

        train_accuracy = history.history.get(
            'accuracy',
            []
        )

        val_accuracy = history.history.get(
            'val_accuracy',
            []
        )

        # =====================================
        # LOSS CURVE
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(10, 5))

        plt.plot(

            train_loss,

            label='Train Loss',

            linewidth=2
        )

        if len(val_loss) > 0:

            plt.plot(

                val_loss,

                label='Validation Loss',

                linewidth=2
            )

        plt.title(
            f'{model_name} Training Loss'
        )

        plt.xlabel(
            'Epoch'
        )

        plt.ylabel(
            'Loss'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        loss_path = os.path.join(

            output_dir,

            f'{model_name}_loss.png'
        )

        plt.savefig(

            loss_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Loss plot saved: '
            f'{loss_path}'
        )

        # =====================================
        # ACCURACY CURVE
        # =====================================

        if len(train_accuracy) > 0:

            apply_plot_style()

            plt.figure(figsize=(10, 5))

            plt.plot(

                train_accuracy,

                label='Train Accuracy',

                linewidth=2
            )

            if len(val_accuracy) > 0:

                plt.plot(

                    val_accuracy,

                    label='Validation Accuracy',

                    linewidth=2
                )

            plt.title(
                f'{model_name} Accuracy'
            )

            plt.xlabel(
                'Epoch'
            )

            plt.ylabel(
                'Accuracy'
            )

            plt.legend()

            plt.grid(True)

            plt.tight_layout()

            accuracy_path = os.path.join(

                output_dir,

                f'{model_name}_accuracy.png'
            )

            plt.savefig(

                accuracy_path,

                dpi=300,

                bbox_inches='tight'
            )

            plt.close()

            print(
                f'Accuracy plot saved: '
                f'{accuracy_path}'
            )

        # =====================================
        # COMBINED PLOT
        # =====================================

        apply_plot_style()

        plt.figure(figsize=(12, 5))

        # Loss subplot
        plt.subplot(1, 2, 1)

        plt.plot(
            train_loss,
            label='Train Loss'
        )

        if len(val_loss) > 0:

            plt.plot(
                val_loss,
                label='Validation Loss'
            )

        plt.title('Loss')

        plt.xlabel('Epoch')

        plt.ylabel('Loss')

        plt.legend()

        plt.grid(True)

        # Accuracy subplot
        plt.subplot(1, 2, 2)

        if len(train_accuracy) > 0:

            plt.plot(
                train_accuracy,
                label='Train Accuracy'
            )

        if len(val_accuracy) > 0:

            plt.plot(
                val_accuracy,
                label='Validation Accuracy'
            )

        plt.title('Accuracy')

        plt.xlabel('Epoch')

        plt.ylabel('Accuracy')

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        combined_path = os.path.join(

            output_dir,

            f'{model_name}_combined.png'
        )

        plt.savefig(

            combined_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            f'Combined plot saved: '
            f'{combined_path}'
        )

        # =====================================
        # LOSS DIFFERENCE VISUALIZATION
        # =====================================

        if len(val_loss) > 0:

            apply_plot_style()

            loss_gap = [

                abs(t - v)

                for t, v in zip(
                    train_loss,
                    val_loss
                )
            ]

            plt.figure(figsize=(10, 5))

            plt.plot(

                loss_gap,

                marker='o'
            )

            plt.title(
                f'{model_name} Loss Gap Analysis'
            )

            plt.xlabel(
                'Epoch'
            )

            plt.ylabel(
                'Loss Difference'
            )

            plt.grid(True)

            plt.tight_layout()

            gap_path = os.path.join(

                output_dir,

                f'{model_name}_loss_gap.png'
            )

            plt.savefig(

                gap_path,

                dpi=300,

                bbox_inches='tight'
            )

            plt.close()

            print(
                f'Loss gap plot saved: '
                f'{gap_path}'
            )

        # =====================================
        # ACCURACY DISTRIBUTION HISTOGRAM
        # =====================================

        if len(train_accuracy) > 0:

            apply_plot_style()

            plt.figure(figsize=(10, 5))

            plt.hist(

                train_accuracy,

                bins=10
            )

            plt.title(
                f'{model_name} Accuracy Distribution'
            )

            plt.xlabel(
                'Accuracy'
            )

            plt.ylabel(
                'Frequency'
            )

            plt.grid(True)

            plt.tight_layout()

            histogram_path = os.path.join(

                output_dir,

                f'{model_name}_accuracy_histogram.png'
            )

            plt.savefig(

                histogram_path,

                dpi=300,

                bbox_inches='tight'
            )

            plt.close()

            print(
                f'Accuracy histogram saved: '
                f'{histogram_path}'
            )

        print("=" * 60)
        print("TRAINING VISUALIZATIONS COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Training plot error: {e}"
        )