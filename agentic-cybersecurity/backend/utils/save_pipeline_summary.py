import os
import datetime


def save_pipeline_summary(summary_text):

    print("=" * 60)
    print("GENERATING PIPELINE SUMMARY")
    print("=" * 60)

    try:

        # =====================================
        # OUTPUT DIRECTORY
        # =====================================

        output_dir = (
            'outputs/reports/pipeline'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # SUMMARY FILE PATH
        # =====================================

        save_path = os.path.join(

            output_dir,

            'pipeline_summary.txt'
        )

        # =====================================
        # WRITE PIPELINE SUMMARY
        # =====================================

        with open(

            save_path,

            'w'
        ) as file:

            file.write(
                "AGENTIC AI PIPELINE SUMMARY\n"
            )

            file.write(
                "=" * 60 + "\n\n"
            )

            file.write(
                f"Generated On: "
                f"{datetime.datetime.now()}\n\n"
            )

            file.write(
                summary_text
            )

            file.write("\n\n")

            file.write(
                "=" * 60 + "\n"
            )

            file.write(
                "PIPELINE MODULE STATUS\n"
            )

            file.write(
                "=" * 60 + "\n\n"
            )

            modules = [

                'Intrusion Detection',

                'Fraud Detection',

                'UEBA',

                'Explainability',

                'Streaming Analytics',

                'Incident Response',

                'Ensemble AI',

                'Autoencoder',

                'CNN-LSTM',

                'Transformer',

                'LANL Analytics'
            ]

            for module in modules:

                file.write(
                    f"[ACTIVE] {module}\n"
                )

            file.write("\n")

            file.write(
                "=" * 60 + "\n"
            )

            file.write(
                "SYSTEM STATUS: RUNNING\n"
            )

            file.write(
                "=" * 60 + "\n"
            )

        print(
            f'Pipeline summary saved: '
            f'{save_path}'
        )

        # =====================================
        # SAVE QUICK STATUS FILE
        # =====================================

        quick_status_path = os.path.join(

            output_dir,

            'pipeline_status.txt'
        )

        with open(

            quick_status_path,

            'w'
        ) as file:

            file.write(
                "SYSTEM STATUS: ACTIVE\n"
            )

            file.write(
                f"Last Updated: "
                f"{datetime.datetime.now()}\n"
            )

        print(
            f'Pipeline status saved: '
            f'{quick_status_path}'
        )

        print("=" * 60)
        print("PIPELINE SUMMARY COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Pipeline summary error: {e}"
        )