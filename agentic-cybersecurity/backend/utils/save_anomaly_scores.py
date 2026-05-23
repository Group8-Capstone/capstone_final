import os
import pandas as pd
import numpy as np


def save_anomaly_scores(scores):

    print("=" * 60)
    print("SAVING ANOMALY SCORES")
    print("=" * 60)

    try:

        # =====================================
        # OUTPUT DIRECTORY
        # =====================================

        output_dir = (
            'outputs/reports/anomaly_reports'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # CONVERT TO NUMPY
        # =====================================

        scores = np.array(scores)

        # =====================================
        # CREATE DATAFRAME
        # =====================================

        threshold = np.mean(scores) + (
            2 * np.std(scores)
        )

        anomaly_labels = np.where(

            scores > threshold,

            'Anomaly',

            'Normal'
        )

        df = pd.DataFrame({

            'FlowID': range(
                1,
                len(scores) + 1
            ),

            'AnomalyScore': scores,

            'Threshold': threshold,

            'Prediction': anomaly_labels
        })

        # =====================================
        # SAVE CSV REPORT
        # =====================================

        save_path = os.path.join(

            output_dir,

            'anomaly_scores.csv'
        )

        df.to_csv(

            save_path,

            index=False
        )

        print(
            f'Anomaly scores saved: '
            f'{save_path}'
        )

        # =====================================
        # SAVE SUMMARY REPORT
        # =====================================

        total_records = len(df)

        total_anomalies = len(

            df[
                df['Prediction']
                == 'Anomaly'
            ]
        )

        total_normal = len(

            df[
                df['Prediction']
                == 'Normal'
            ]
        )

        summary_path = os.path.join(

            output_dir,

            'anomaly_summary.txt'
        )

        with open(

            summary_path,

            'w'
        ) as file:

            file.write(
                "AUTOENCODER ANOMALY REPORT\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )

            file.write(
                f"Total Records: "
                f"{total_records}\n"
            )

            file.write(
                f"Total Anomalies: "
                f"{total_anomalies}\n"
            )

            file.write(
                f"Total Normal: "
                f"{total_normal}\n"
            )

            file.write(
                f"Threshold: "
                f"{threshold:.6f}\n"
            )

            file.write(
                f"Maximum Score: "
                f"{scores.max():.6f}\n"
            )

            file.write(
                f"Minimum Score: "
                f"{scores.min():.6f}\n"
            )

            file.write(
                f"Average Score: "
                f"{scores.mean():.6f}\n"
            )

        print(
            f'Anomaly summary saved: '
            f'{summary_path}'
        )

        # =====================================
        # SAVE TOP ANOMALIES
        # =====================================

        top_anomalies = df.sort_values(

            by='AnomalyScore',

            ascending=False
        ).head(20)

        top_path = os.path.join(

            output_dir,

            'top_anomalies.csv'
        )

        top_anomalies.to_csv(

            top_path,

            index=False
        )

        print(
            f'Top anomalies saved: '
            f'{top_path}'
        )

        print("=" * 60)
        print("ANOMALY SCORE SAVING COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Anomaly score saving error: {e}"
        )