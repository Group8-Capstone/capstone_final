import os
import joblib
import numpy as np

from tensorflow.keras.models import load_model


class MLAgent:

    def __init__(self):

        print("=" * 60)
        print("ML AGENT INITIALIZED")
        print("=" * 60)

        self.base = "outputs/trained_models"

        self.cnn_model = None
        self.cnn_scaler = None
        self.cnn_encoder = None

        self.transformer_model = None
        self.transformer_scaler = None
        self.transformer_encoder = None

    # =====================================================
    # LOAD MODELS ONLY WHEN REQUIRED
    # =====================================================

    def load_models(self):

        if self.cnn_model is not None:
            return

        # ------------------------------------
        # CNN-LSTM
        # ------------------------------------

        cnn_dir = os.path.join(
            self.base,
            "cnn_lstm"
        )

        cnn_model_path = os.path.join(
            cnn_dir,
            "cnn_lstm.keras"
        )

        if not os.path.exists(cnn_model_path):

            raise FileNotFoundError(

                f"CNN-LSTM model not found:\n{cnn_model_path}"

            )

        self.cnn_model = load_model(
            cnn_model_path
        )

        self.cnn_scaler = joblib.load(

            os.path.join(

                cnn_dir,

                "scaler.pkl"

            )

        )

        self.cnn_encoder = joblib.load(

            os.path.join(

                cnn_dir,

                "label_encoder.pkl"

            )

        )

        # ------------------------------------
        # TRANSFORMER
        # ------------------------------------

        transformer_dir = os.path.join(

            self.base,

            "transformer"

        )

        transformer_model_path = os.path.join(

            transformer_dir,

            "transformer.keras"

        )

        if not os.path.exists(transformer_model_path):

            raise FileNotFoundError(

                f"Transformer model not found:\n"

                f"{transformer_model_path}"

            )

        self.transformer_model = load_model(

            transformer_model_path

        )

        self.transformer_scaler = joblib.load(

            os.path.join(

                transformer_dir,

                "scaler.pkl"

            )

        )

        self.transformer_encoder = joblib.load(

            os.path.join(

                transformer_dir,

                "label_encoder.pkl"

            )

        )

        print("CNN-LSTM Loaded")

        print("Transformer Loaded")

   # =====================================================
    # PREDICTION
    # =====================================================

    def predict(self, data):

        try:

            if not isinstance(data, np.ndarray):

                data = np.array(data)

            data = data.astype(np.float32)

            # ------------------------------------
            # VALIDATE INPUT
            # ------------------------------------

            if data.ndim == 1:

                data = data.reshape(1, -1)

            feature_count = data.shape[1]

            # ------------------------------------
            # ML MODELS SUPPORT ONLY CICIDS (78 FEATURES)
            # ------------------------------------

            if feature_count != 78:

                print(
                    f"ML Agent skipped "
                    f"(received {feature_count} features, "
                    f"expected 78)"
                )

                return {

                    "prediction": "Not Applicable",

                    "confidence": 0,

                    "cnn_confidence": 0,

                    "transformer_confidence": 0,

                    "message":
                    "ML models are only applicable for "
                    "CICIDS2017 (78-feature) data."

                }

            # ------------------------------------
            # LOAD MODELS
            # ------------------------------------

            self.load_models()

            # ------------------------------------
            # CNN-LSTM
            # ------------------------------------

            cnn_x = self.cnn_scaler.transform(data)

            cnn_x = cnn_x.reshape(

                cnn_x.shape[0],

                cnn_x.shape[1],

                1

            )

            cnn_prob = self.cnn_model.predict(

                cnn_x,

                verbose=0

            )

            cnn_class = np.argmax(

                cnn_prob,

                axis=1

            )[0]

            cnn_score = float(

                np.max(cnn_prob)

            )

            # ------------------------------------
            # TRANSFORMER
            # ------------------------------------

            trans_x = self.transformer_scaler.transform(data)

            trans_prob = self.transformer_model.predict(

                trans_x,

                verbose=0

            )

            trans_class = np.argmax(

                trans_prob,

                axis=1

            )[0]

            trans_score = float(

                np.max(trans_prob)

            )

            # ------------------------------------
            # ENSEMBLE
            # ------------------------------------

            final_score = (

                cnn_score +

                trans_score

            ) / 2

            if cnn_score >= trans_score:

                prediction = self.cnn_encoder.inverse_transform(

                    [cnn_class]

                )[0]

            else:

                prediction = self.transformer_encoder.inverse_transform(

                    [trans_class]

                )[0]

            return {

                "prediction": prediction,

                "confidence": round(

                    final_score,

                    4

                ),

                "cnn_confidence": round(

                    cnn_score,

                    4

                ),

                "transformer_confidence": round(

                    trans_score,

                    4

                )

            }

        except Exception as e:

            print(f"ML Agent Error: {e}")

            return {

                "prediction": "Unknown",

                "confidence": 0,

                "cnn_confidence": 0,

                "transformer_confidence": 0,

                "error": str(e)

            }