import os
import json
import datetime


def generate_dashboard_metrics():

    print("=" * 60)
    print("GENERATING DASHBOARD METRICS")
    print("=" * 60)

    try:

        # =====================================
        # CREATE DASHBOARD DIRECTORY
        # =====================================

        output_dir = 'dashboard'

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # COUNT TRAINED MODELS
        # =====================================

        model_count = 0

        model_extensions = [

            '.keras',

            '.pkl'
        ]

        for root, dirs, files in os.walk(

            'outputs/trained_models'
        ):

            for file in files:

                if any(

                    file.endswith(ext)

                    for ext in model_extensions
                ):

                    model_count += 1

        # =====================================
        # COUNT REPORTS
        # =====================================

        report_count = 0

        for root, dirs, files in os.walk(

            'outputs/reports'
        ):

            report_count += len(files)

        # =====================================
        # COUNT VISUALIZATIONS
        # =====================================

        visualization_count = 0

        image_extensions = [

            '.png',

            '.jpg',

            '.jpeg'
        ]

        for root, dirs, files in os.walk(

            'outputs/visualizations'
        ):

            for file in files:

                if any(

                    file.endswith(ext)

                    for ext in image_extensions
                ):

                    visualization_count += 1

        # =====================================
        # COUNT EXPLAINABILITY FILES
        # =====================================

        explainability_count = 0

        for root, dirs, files in os.walk(

            'outputs/explainability'
        ):

            explainability_count += len(files)

        # =====================================
        # COUNT PREDICTIONS
        # =====================================

        prediction_count = 0

        for root, dirs, files in os.walk(

            'outputs/predictions'
        ):

            prediction_count += len(files)

        # =====================================
        # BUILD DASHBOARD METRICS
        # =====================================

        metrics = {

            'system_status': 'ACTIVE',

            'generated_on': str(
                datetime.datetime.now()
            ),

            'trained_models': model_count,

            'reports_generated': report_count,

            'visualizations_generated':
                visualization_count,

            'explainability_outputs':
                explainability_count,

            'prediction_outputs':
                prediction_count,

            'modules': {

                'intrusion_detection':
                    'ACTIVE',

                'fraud_detection':
                    'ACTIVE',

                'ueba':
                    'ACTIVE',

                'streaming':
                    'ACTIVE',

                'incident_response':
                    'ACTIVE',

                'ensemble_ai':
                    'ACTIVE'
            },

            'models_loaded': [

                'Autoencoder',

                'CNN-LSTM',

                'Transformer',

                'XGBoost Fraud Detection',

                'LANL UEBA'
            ]
        }

        # =====================================
        # SAVE JSON FILE
        # =====================================

        save_path = os.path.join(

            output_dir,

            'dashboard_metrics.json'
        )

        with open(

            save_path,

            'w'
        ) as file:

            json.dump(

                metrics,

                file,

                indent=4
            )

        print(
            f"Dashboard metrics saved: "
            f"{save_path}"
        )

        # =====================================
        # SAVE TEXT SUMMARY
        # =====================================

        summary_path = os.path.join(

            output_dir,

            'dashboard_summary.txt'
        )

        with open(

            summary_path,

            'w'
        ) as file:

            file.write(
                "CYBERSECURITY DASHBOARD SUMMARY\n"
            )

            file.write(
                "=" * 60 + "\n\n"
            )

            file.write(
                f"Generated On: "
                f"{metrics['generated_on']}\n\n"
            )

            file.write(
                f"Trained Models: "
                f"{model_count}\n"
            )

            file.write(
                f"Reports Generated: "
                f"{report_count}\n"
            )

            file.write(
                f"Visualizations Generated: "
                f"{visualization_count}\n"
            )

            file.write(
                f"Explainability Outputs: "
                f"{explainability_count}\n"
            )

            file.write(
                f"Prediction Outputs: "
                f"{prediction_count}\n"
            )

            file.write("\n")

            file.write(
                "SYSTEM STATUS: ACTIVE\n"
            )

        print(
            f"Dashboard summary saved: "
            f"{summary_path}"
        )

        print("=" * 60)
        print("DASHBOARD METRICS COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Dashboard metrics error: {e}"
        )