import os

from utils.logger import (
    log_message
)

BASE_MODEL_DIR = (
    'outputs/trained_models'
)


def initialize_models():

    print("=" * 60)
    print("CHECKING TRAINED MODELS")
    print("=" * 60)

    log_message(
        "Checking trained models"
    )

    # =====================================
    # MODEL PATHS
    # =====================================

    model_paths = {

        'autoencoder': (

            f'{BASE_MODEL_DIR}/'
            'autoencoder/autoencoder.keras'
        ),

        'cnn_lstm': (

            f'{BASE_MODEL_DIR}/'
            'cnn_lstm/cnn_lstm.keras'
        ),

        'transformer': (

            f'{BASE_MODEL_DIR}/'
            'transformer/transformer.keras'
        ),

        'fraud_detection': (

            f'{BASE_MODEL_DIR}/'
            'fraud_detection/fraud_model.pkl'
        ),

        'lanl': (

            f'{BASE_MODEL_DIR}/'
            'lanl/lanl_model.pkl'
        )
    }

    # =====================================
    # AUTOENCODER
    # =====================================

    check_and_initialize_model(

        model_name='Autoencoder',

        model_path=model_paths[
            'autoencoder'
        ],

        trainer_function=train_autoencoder_model
    )

    # =====================================
    # CNN-LSTM
    # =====================================

    check_and_initialize_model(

        model_name='CNN-LSTM',

        model_path=model_paths[
            'cnn_lstm'
        ],

        trainer_function=train_cnn_lstm_model
    )

    # =====================================
    # TRANSFORMER
    # =====================================

    check_and_initialize_model(

        model_name='Transformer',

        model_path=model_paths[
            'transformer'
        ],

        trainer_function=train_transformer_model_pipeline
    )

    # =====================================
    # FRAUD DETECTION
    # =====================================

    check_and_initialize_model(

        model_name='Fraud Detection',

        model_path=model_paths[
            'fraud_detection'
        ],

        trainer_function=train_fraud_detection_model
    )

    # =====================================
    # LANL
    # =====================================

    check_and_initialize_model(

        model_name='LANL',

        model_path=model_paths[
            'lanl'
        ],

        trainer_function=train_lanl_pipeline
    )

    print("=" * 60)
    print("ALL MODELS READY")
    print("=" * 60)

    log_message(
        "All models initialized successfully"
    )

    # =====================================
    # IMPORTANT
    # GENERATE OUTPUTS EVEN IF
    # MODELS ALREADY EXIST
    # =====================================

    generate_all_outputs()


def check_and_initialize_model(

    model_name,

    model_path,

    trainer_function
):

    try:

        if os.path.exists(model_path):

            print(
                f"{model_name} model already exists"
            )

            log_message(
                f"{model_name} model loaded"
            )

        else:

            print(
                f"{model_name} model not found"
            )

            print(
                f"Training {model_name}..."
            )

            log_message(
                f"Training started for "
                f"{model_name}"
            )

            trainer_function()

            print(
                f"{model_name} training completed"
            )

            log_message(
                f"{model_name} training completed"
            )

    except Exception as e:

        print(
            f"{model_name} initialization failed: {e}"
        )

        log_message(
            f"{model_name} error: {e}"
        )


# ==========================================
# GENERATE OUTPUTS
# ==========================================

def generate_all_outputs():

    try:

        print("=" * 60)
        print("GENERATING OUTPUT ARTIFACTS")
        print("=" * 60)

        log_message(
            "Generating visualization outputs"
        )

        # =====================================
        # VISUALIZATION PIPELINE
        # =====================================

        from pipelines.visualization_pipeline import (
            run_visualization_pipeline
        )

        run_visualization_pipeline()

        # =====================================
        # XAI PIPELINE
        # =====================================

        from pipelines.xai_pipeline import (
            run_xai_pipeline
        )

        run_xai_pipeline()

        # =====================================
        # EVALUATION PIPELINE
        # =====================================

        from pipelines.evaluation_pipeline import (
            run_evaluation_pipeline
        )

        run_evaluation_pipeline()

        # =====================================
        # INFERENCE PIPELINE
        # =====================================

        from pipelines.inference_pipeline import (
            run_inference_pipeline
        )

        run_inference_pipeline()

        # =====================================
        # DASHBOARD METRICS
        # =====================================

        from utils.dashboard_metrics import (
            generate_dashboard_metrics
        )

        generate_dashboard_metrics()

        print("=" * 60)
        print("OUTPUT GENERATION COMPLETED")
        print("=" * 60)

        log_message(
            "All outputs generated"
        )

    except Exception as e:

        print(
            f"Output generation failed: {e}"
        )

        log_message(
            f"Output generation error: {e}"
        )


# ==========================================
# LAZY IMPORTS
# ==========================================

def train_autoencoder_model():

    from pipelines.train_autoencoder import (
        train_autoencoder
    )

    train_autoencoder()


def train_cnn_lstm_model():

    from pipelines.train_cnn_lstm import (
        train_cnn_lstm
    )

    train_cnn_lstm()


def train_transformer_model_pipeline():

    from pipelines.train_transformer import (
        train_transformer
    )

    train_transformer()


def train_fraud_detection_model():

    from pipelines.train_fraud_model import (
        train_fraud_model
    )

    train_fraud_model()


def train_lanl_pipeline():

    from pipelines.train_lanl_model import (
        train_lanl_model
    )

    train_lanl_model()