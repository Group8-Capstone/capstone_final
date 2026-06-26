import os
import joblib

from tensorflow.keras.models import load_model

from utils.logger import log_message

BASE_MODEL_DIR = "outputs/trained_models"

# ============================================================
# GLOBAL MODEL CACHE
# ============================================================

MODELS = {}

# ============================================================
# MODEL PATHS
# ============================================================

MODEL_PATHS = {

    "autoencoder": f"{BASE_MODEL_DIR}/autoencoder/autoencoder.keras",

    "cnn_lstm": f"{BASE_MODEL_DIR}/cnn_lstm/cnn_lstm.keras",

    "transformer": f"{BASE_MODEL_DIR}/transformer/transformer.keras",

    "fraud_detection": f"{BASE_MODEL_DIR}/fraud_detection/fraud_model.pkl",

    "lanl": f"{BASE_MODEL_DIR}/lanl/lanl_model.pkl"

}


# ============================================================
# INITIALIZE ALL MODELS
# ============================================================

def initialize_models():

    print("=" * 70)
    print("CHECKING TRAINED MODELS")
    print("=" * 70)

    log_message("Checking trained models")

    check_and_initialize_model(
        "Autoencoder",
        MODEL_PATHS["autoencoder"],
        train_autoencoder_model
    )

    check_and_initialize_model(
        "CNN-LSTM",
        MODEL_PATHS["cnn_lstm"],
        train_cnn_lstm_model
    )

    check_and_initialize_model(
        "Transformer",
        MODEL_PATHS["transformer"],
        train_transformer_model_pipeline
    )

    check_and_initialize_model(
        "Fraud Detection",
        MODEL_PATHS["fraud_detection"],
        train_fraud_detection_model
    )

    check_and_initialize_model(
        "LANL",
        MODEL_PATHS["lanl"],
        train_lanl_pipeline
    )

    # ======================================================
    # LOAD ALL MODELS INTO MEMORY
    # ======================================================

    load_models()

    print("=" * 70)
    print("ALL MODELS READY")
    print("=" * 70)

    log_message("All models initialized successfully")

    generate_all_outputs()


# ============================================================
# TRAIN IF MODEL DOESN'T EXIST
# ============================================================

def check_and_initialize_model(model_name, model_path, trainer):

    try:

        if os.path.exists(model_path):

            print(f"{model_name} model already exists")

            log_message(f"{model_name} model found")

        else:

            print(f"{model_name} model not found")

            print(f"Training {model_name}...")

            trainer()

            print(f"{model_name} training completed")

            log_message(f"{model_name} trained successfully")

    except Exception as e:

        print(f"{model_name} initialization failed : {e}")

        log_message(f"{model_name} initialization failed : {e}")


# ============================================================
# LOAD MODELS
# ============================================================

def load_models():

    print("=" * 70)
    print("LOADING MODELS")
    print("=" * 70)

    try:

        MODELS["autoencoder"] = load_model(
            MODEL_PATHS["autoencoder"]
        )

        print("✓ Autoencoder Loaded")

    except Exception as e:

        print(e)

    try:

        MODELS["cnn_lstm"] = load_model(
            MODEL_PATHS["cnn_lstm"]
        )

        print("✓ CNN-LSTM Loaded")

    except Exception as e:

        print(e)

    try:

        MODELS["transformer"] = load_model(
            MODEL_PATHS["transformer"]
        )

        print("✓ Transformer Loaded")

    except Exception as e:

        print(e)

    try:

        MODELS["fraud_detection"] = joblib.load(
            MODEL_PATHS["fraud_detection"]
        )

        print("✓ Fraud Model Loaded")

    except Exception as e:

        print(e)

    try:

        MODELS["lanl"] = joblib.load(
            MODEL_PATHS["lanl"]
        )

        print("✓ LANL Model Loaded")

    except Exception as e:

        print(e)


# ============================================================
# GET MODEL
# ============================================================

def get_model(name):

    return MODELS.get(name)


# ============================================================
# GENERATE OUTPUTS
# ============================================================

def generate_all_outputs():

    try:

        print("=" * 70)
        print("GENERATING OUTPUTS")
        print("=" * 70)

        from pipelines.visualization_pipeline import (
            run_visualization_pipeline
        )

        run_visualization_pipeline()

        from pipelines.evaluation_pipeline import (
            run_evaluation_pipeline
        )

        run_evaluation_pipeline()

        from pipelines.inference_pipeline import (
            run_inference_pipeline
        )

        run_inference_pipeline()

        from utils.dashboard_metrics import (
            generate_dashboard_metrics
        )

        generate_dashboard_metrics()

        print("Output generation completed.")

    except Exception as e:

        print(e)


# ============================================================
# TRAINERS
# ============================================================

def train_autoencoder_model():

    from pipelines.train_autoencoder import train_autoencoder

    train_autoencoder()


def train_cnn_lstm_model():

    from pipelines.train_cnn_lstm import train_cnn_lstm

    train_cnn_lstm()


def train_transformer_model_pipeline():

    from pipelines.train_transformer import train_transformer

    train_transformer()


def train_fraud_detection_model():

    from pipelines.train_fraud_model import train_fraud_model

    train_fraud_model()


def train_lanl_pipeline():

    from pipelines.train_lanl_model import train_lanl_model

    train_lanl_model()