import os

from sklearn.metrics import (
    classification_report,
    accuracy_score
)

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt


def save_ensemble_report(

    y_test,

    ensemble_predictions,

    label_encoder=None
):

    print("=" * 60)
    print("GENERATING ENSEMBLE REPORT")
    print("=" * 60)

    try:

        # =====================================
        # OUTPUT DIRECTORY
        # =====================================

        output_dir = (
            'outputs/reports/ensemble'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # TARGET NAMES
        # =====================================

        if (

            label_encoder is not None and

            hasattr(
                label_encoder,
                'classes_'
            )
        ):

            target_names = [

                str(cls)

                for cls in (
                    label_encoder.classes_
                )
            ]

        else:

            target_names = [

                'Normal',

                'Attack'
            ]

        # =====================================
        # CLASSIFICATION REPORT
        # =====================================

        report = classification_report(

            y_test,

            ensemble_predictions,

            target_names=target_names,

            zero_division=0
        )

        save_path = os.path.join(

            output_dir,

            'ensemble_report.txt'
        )

        with open(save_path, 'w') as file:

            file.write(report)

        print(
            f'Ensemble report saved: '
            f'{save_path}'
        )

        # =====================================
        # ACCURACY CHART
        # =====================================

        accuracy = accuracy_score(

            y_test,

            ensemble_predictions
        )

        plt.figure(figsize=(8, 5))

        models = [

            'Ensemble Model'
        ]

        scores = [

            accuracy
        ]

        plt.bar(

            models,

            scores
        )

        plt.ylim(0, 1)

        plt.title(
            'Ensemble Accuracy'
        )

        plt.ylabel(
            'Accuracy'
        )

        chart_path = os.path.join(

            output_dir,

            'ensemble_accuracy.png'
        )

        plt.savefig(

            chart_path,

            dpi=300,

            bbox_inches='tight'
        )

        plt.close()

        print(
            "Ensemble accuracy chart saved"
        )

        print("=" * 60)
        print("ENSEMBLE REPORT COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Ensemble report error: {e}"
        )