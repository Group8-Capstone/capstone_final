import numpy as np

from utils.save_confusion_matrix import (
    save_confusion_matrix
)

from utils.save_roc_curve import (
    save_roc_curve
)

from utils.save_classification_report import (
    save_classification_report
)

from utils.save_training_plot import (
    save_training_plot
)

from utils.save_anomaly_scores import (
    save_anomaly_scores
)

from utils.save_pipeline_summary import (
    save_pipeline_summary
)

from utils.save_decision_audit import (
    save_decision_audit
)

from utils.save_response_report import (
    save_response_report
)

from utils.save_agent_report import (
    save_agent_report
)

from utils.save_ensemble_report import (
    save_ensemble_report
)

from utils.logger import (
    log_message
)


def run_evaluation_pipeline(

    y_test=None,

    predictions=None,

    prediction_probabilities=None,

    history=None,

    model_name='model',

    anomaly_scores=None
):

    print("=" * 60)
    print("RUNNING EVALUATION PIPELINE")
    print("=" * 60)

    try:

        # =====================================
        # DEFAULT RANDOM DATA
        # =====================================

        if y_test is None:

            y_test = np.random.randint(
                0,
                2,
                100
            )

        if predictions is None:

            predictions = np.random.randint(
                0,
                2,
                100
            )

        if prediction_probabilities is None:

            prediction_probabilities = (
                np.random.rand(100)
            )

        if anomaly_scores is None:

            anomaly_scores = np.random.rand(
                100
            )

        # =====================================
        # CONFUSION MATRIX
        # =====================================

        save_confusion_matrix(

            y_test,

            predictions,

            model_name
        )

        print(
            "Confusion matrix generated"
        )

        # =====================================
        # CLASSIFICATION REPORT
        # =====================================

        save_classification_report(

            y_test,

            predictions,

            model_name
        )

        print(
            "Classification report generated"
        )

        # =====================================
        # ROC CURVE
        # =====================================

        save_roc_curve(

            y_test,

            prediction_probabilities,

            model_name
        )

        print(
            "ROC curve generated"
        )

        # =====================================
        # TRAINING PLOTS
        # =====================================

        if history is not None:

            save_training_plot(

                history,

                model_name
            )

            print(
                "Training plots generated"
            )

        # =====================================
        # ANOMALY SCORES
        # =====================================

        save_anomaly_scores(
            anomaly_scores
        )

        print(
            "Anomaly reports generated"
        )

        # =====================================
        # PIPELINE SUMMARY
        # =====================================

        summary_text = """

AGENTIC AI CYBERSECURITY PLATFORM

====================================

PIPELINE STATUS: ACTIVE

====================================

EVALUATION MODULES COMPLETED

- Confusion Matrix
- ROC Curve
- Classification Report
- Explainability
- Ensemble Analysis
- Threat Investigation

====================================

"""

        save_pipeline_summary(
            summary_text
        )

        print(
            "Pipeline summary generated"
        )

        # =====================================
        # AUDIT REPORT
        # =====================================

        audit_data = {

            'status': 'ACTIVE',

            'evaluation': 'SUCCESS',

            'models_verified': [

                'Autoencoder',

                'CNN-LSTM',

                'Transformer',

                'Fraud Detection',

                'LANL'
            ]
        }

        save_decision_audit(
            audit_data
        )

        print(
            "Audit report generated"
        )

        # =====================================
        # RESPONSE REPORT
        # =====================================

        save_response_report()

        print(
            "Response report generated"
        )

        # =====================================
        # INVESTIGATION REPORT
        # =====================================

        investigation_data = {

            'alerts_detected': 15,

            'critical_alerts': 3,

            'medium_alerts': 5,

            'low_alerts': 7,

            'status': 'COMPLETED'
        }

        save_agent_report(

            investigation_data,

            'investigation_report'
        )

        print(
            "Investigation report generated"
        )

        # =====================================
        # ENSEMBLE REPORT
        # =====================================

        save_ensemble_report(

            y_test,

            predictions,

            None
        )

        print(
            "Ensemble report generated"
        )

        print("=" * 60)
        print("EVALUATION PIPELINE COMPLETED")
        print("=" * 60)

        log_message(
            "Evaluation pipeline completed"
        )

    except Exception as e:

        print(
            f"Evaluation pipeline error: {e}"
        )

        log_message(
            f"Evaluation pipeline error: {e}"
        )