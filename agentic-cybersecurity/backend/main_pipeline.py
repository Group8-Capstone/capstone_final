import os
import time

from services.model_initializer import (
    initialize_models
)

from utils.logger import (
    log_message
)

from pipelines.visualization_pipeline import (
    run_visualization_pipeline
)

from pipelines.xai_pipeline import (
    run_xai_pipeline
)

from pipelines.evaluation_pipeline import (
    run_evaluation_pipeline
)

from pipelines.inference_pipeline import (
    run_inference_pipeline
)

from utils.dashboard_metrics import (
    generate_dashboard_metrics
)

BASE_OUTPUT_DIR = 'outputs'

TRAIN_MODELS = False


def initialize_system():

    print("=" * 70)
    print("AGENTIC AI CYBERSECURITY INITIALIZATION")
    print("=" * 70)

    start_time = time.time()

    log_message(
        "System initialization started"
    )

    try:

        # =====================================
        # CREATE OUTPUT DIRECTORIES
        # =====================================

        create_output_directories()

        # =====================================
        # INITIALIZE MODELS
        # =====================================

        if TRAIN_MODELS:

            initialize_models()

        else:

            print(
                "Skipping model training"
            )

        # =====================================
        # INITIALIZE AGENTS
        # =====================================

        initialize_agents()

        # =====================================
        # RUN XAI PIPELINE
        # =====================================

        run_xai_pipeline()

        # =====================================
        # RUN VISUALIZATION PIPELINE
        # =====================================

        run_visualization_pipeline()

        # =====================================
        # RUN EVALUATION PIPELINE
        # =====================================

        run_evaluation_pipeline()

        # =====================================
        # RUN INFERENCE PIPELINE
        # =====================================

        run_inference_pipeline()

        # =====================================
        # GENERATE DASHBOARD METRICS
        # =====================================

        generate_dashboard_metrics()

        # =====================================
        # HEALTH CHECK
        # =====================================

        system_health_check()

        total_time = round(
            time.time() - start_time,
            2
        )

        print("=" * 70)

        print(
            f"Initialization Time: "
            f"{total_time} seconds"
        )

        print("SYSTEM READY")

        print("=" * 70)

        log_message(
            "System initialization completed"
        )

    except Exception as e:

        print(
            f"System initialization failed: {e}"
        )

        log_message(
            f"Initialization error: {e}"
        )


def create_directory(path):

    os.makedirs(
        path,
        exist_ok=True
    )


def create_output_directories():

    directories = [

        # =====================================
        # ROOT
        # =====================================

        'dashboard',

        f'{BASE_OUTPUT_DIR}',

        f'{BASE_OUTPUT_DIR}/logs',

        f'{BASE_OUTPUT_DIR}/predictions',

        f'{BASE_OUTPUT_DIR}/trained_models',

        f'{BASE_OUTPUT_DIR}/reports',

        f'{BASE_OUTPUT_DIR}/explainability',

        f'{BASE_OUTPUT_DIR}/visualizations',

        f'{BASE_OUTPUT_DIR}/inference',

        f'{BASE_OUTPUT_DIR}/evaluation',

        # =====================================
        # REPORTS
        # =====================================

        f'{BASE_OUTPUT_DIR}/reports/accuracy_plots',

        f'{BASE_OUTPUT_DIR}/reports/classification_reports',

        f'{BASE_OUTPUT_DIR}/reports/confusion_matrix',

        f'{BASE_OUTPUT_DIR}/reports/roc_curves',

        f'{BASE_OUTPUT_DIR}/reports/ensemble',

        f'{BASE_OUTPUT_DIR}/reports/pipeline',

        f'{BASE_OUTPUT_DIR}/reports/audit',

        f'{BASE_OUTPUT_DIR}/reports/investigation',

        f'{BASE_OUTPUT_DIR}/reports/response',

        f'{BASE_OUTPUT_DIR}/reports/anomaly_reports',

        # =====================================
        # EXPLAINABILITY
        # =====================================

        f'{BASE_OUTPUT_DIR}/explainability/shap',

        f'{BASE_OUTPUT_DIR}/explainability/lime',

        f'{BASE_OUTPUT_DIR}/explainability/feature_importance',

        f'{BASE_OUTPUT_DIR}/explainability/permutation_importance',

        # =====================================
        # VISUALIZATIONS
        # =====================================

        f'{BASE_OUTPUT_DIR}/visualizations/anomaly_detection',

        f'{BASE_OUTPUT_DIR}/visualizations/streaming',

        f'{BASE_OUTPUT_DIR}/visualizations/lanl',

        f'{BASE_OUTPUT_DIR}/visualizations/ensemble',

        f'{BASE_OUTPUT_DIR}/visualizations/attacks',

        f'{BASE_OUTPUT_DIR}/visualizations/fraud',

        # =====================================
        # TRAINED MODELS
        # =====================================

        f'{BASE_OUTPUT_DIR}/trained_models/autoencoder',

        f'{BASE_OUTPUT_DIR}/trained_models/cnn_lstm',

        f'{BASE_OUTPUT_DIR}/trained_models/transformer',

        f'{BASE_OUTPUT_DIR}/trained_models/fraud_detection',

        f'{BASE_OUTPUT_DIR}/trained_models/lanl'
    ]

    for directory in directories:

        create_directory(
            directory
        )

    print(
        "Output directories initialized"
    )

    log_message(
        "Output directories initialized"
    )


def initialize_agents():

    print("=" * 60)
    print("INITIALIZING AGENTS")
    print("=" * 60)

    try:

        from agents.detection_agent import (
            DetectionAgent
        )

        from agents.investigation_agent import (
            InvestigationAgent
        )

        from agents.response_agent import (
            ResponseAgent
        )

        from agents.coordinator_agent import (
            CoordinatorAgent
        )

        detection_agent = DetectionAgent()

        investigation_agent = (
            InvestigationAgent()
        )

        response_agent = ResponseAgent()

        coordinator_agent = CoordinatorAgent(

            detection_agent,

            investigation_agent,

            response_agent
        )

        print(
            "Detection Agent Ready"
        )

        print(
            "Investigation Agent Ready"
        )

        print(
            "Response Agent Ready"
        )

        print(
            "Coordinator Agent Ready"
        )

        log_message(
            "All agents initialized"
        )

        return coordinator_agent

    except Exception as e:

        print(
            f"Agent initialization failed: {e}"
        )

        log_message(
            f"Agent initialization error: {e}"
        )


def system_health_check():

    print("=" * 60)
    print("SYSTEM HEALTH CHECK")
    print("=" * 60)

    checks = {

        # =====================================
        # DIRECTORIES
        # =====================================

        'Models Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models'
        ),

        'Reports Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/reports'
        ),

        'Explainability Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/explainability'
        ),

        'Visualization Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/visualizations'
        ),

        'Logs Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/logs'
        ),

        'Inference Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/inference'
        ),

        'Evaluation Directory':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/evaluation'
        ),

        'Dashboard Directory':

        os.path.exists(
            'dashboard'
        ),

        # =====================================
        # MODEL FILES
        # =====================================

        'Autoencoder Model':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models/'
            'autoencoder/autoencoder.keras'
        ),

        'CNN-LSTM Model':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models/'
            'cnn_lstm/cnn_lstm.keras'
        ),

        'Transformer Model':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models/'
            'transformer/transformer.keras'
        ),

        'Fraud Model':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models/'
            'fraud_detection/fraud_model.pkl'
        ),

        'LANL Model':

        os.path.exists(
            f'{BASE_OUTPUT_DIR}/trained_models/'
            'lanl/lanl_model.pkl'
        ),

        # =====================================
        # DASHBOARD FILE
        # =====================================

        'Dashboard Metrics':

        os.path.exists(
            'dashboard/dashboard_metrics.json'
        )
    }

    for module, status in checks.items():

        print(
            f"{module}: "
            f"{'OK' if status else 'FAILED'}"
        )

    log_message(
        "System health check completed"
    )


if __name__ == "__main__":

    initialize_system()