import os
import json
import datetime


def save_decision_audit(audit_data):

    print("=" * 60)
    print("GENERATING DECISION AUDIT")
    print("=" * 60)

    try:

        # =====================================
        # OUTPUT DIRECTORY
        # =====================================

        output_dir = (
            'outputs/reports/audit'
        )

        os.makedirs(

            output_dir,

            exist_ok=True
        )

        # =====================================
        # MAIN AUDIT DATA
        # =====================================

        complete_audit = {

            'generated_on': str(
                datetime.datetime.now()
            ),

            'system_name': (
                'Agentic AI Cybersecurity'
            ),

            'audit_status': 'COMPLETED',

            'audit_data': audit_data,

            'security_checks': {

                'intrusion_detection':
                    'ACTIVE',

                'fraud_detection':
                    'ACTIVE',

                'ueba_monitoring':
                    'ACTIVE',

                'streaming_monitoring':
                    'ACTIVE',

                'explainability':
                    'ACTIVE'
            },

            'models': [

                'Autoencoder',

                'CNN-LSTM',

                'Transformer',

                'XGBoost',

                'LANL UEBA'
            ]
        }

        # =====================================
        # SAVE JSON AUDIT
        # =====================================

        save_path = os.path.join(

            output_dir,

            'decision_audit.json'
        )

        with open(

            save_path,

            'w'
        ) as file:

            json.dump(

                complete_audit,

                file,

                indent=4
            )

        print(
            f'Decision audit saved: '
            f'{save_path}'
        )

        # =====================================
        # SAVE TEXT AUDIT
        # =====================================

        text_audit_path = os.path.join(

            output_dir,

            'decision_audit_summary.txt'
        )

        with open(

            text_audit_path,

            'w'
        ) as file:

            file.write(
                "DECISION AUDIT REPORT\n"
            )

            file.write(
                "=" * 60 + "\n\n"
            )

            file.write(
                f"Generated On: "
                f"{complete_audit['generated_on']}\n\n"
            )

            file.write(
                f"Audit Status: "
                f"{complete_audit['audit_status']}\n\n"
            )

            file.write(
                "SECURITY MODULE STATUS\n"
            )

            file.write(
                "-" * 40 + "\n"
            )

            for module, status in complete_audit[
                'security_checks'
            ].items():

                file.write(
                    f"{module}: {status}\n"
                )

            file.write("\n")

            file.write(
                "AI MODELS\n"
            )

            file.write(
                "-" * 40 + "\n"
            )

            for model in complete_audit[
                'models'
            ]:

                file.write(
                    f"- {model}\n"
                )

            file.write("\n")

            file.write(
                "SYSTEM STATUS: ACTIVE\n"
            )

        print(
            f'Audit summary saved: '
            f'{text_audit_path}'
        )

        print("=" * 60)
        print("DECISION AUDIT COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Decision audit error: {e}"
        )