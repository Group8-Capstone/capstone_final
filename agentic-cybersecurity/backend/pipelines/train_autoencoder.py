import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from preprocessing.preprocess_cicids import preprocess_cicids
from models.autoencoder.autoencoder_model import build_autoencoder
from utils.save_training_plot import save_training_plot
from utils.save_anomaly_scores import save_anomaly_scores


def train_autoencoder():

    print("====================================")
    print("AUTOENCODER TRAINING PIPELINE STARTED")
    print("====================================")

    dataset_folder = "datasets/cicids"

    df = preprocess_cicids(dataset_folder)

    print("Dataset loaded successfully")

    df = df.sample(
        50000,
        random_state=42
    )

    print(f"Sampled Shape: {df.shape}")

    df = df.select_dtypes(
        include=[
            "float64",
            "int64",
            "float32",
            "int32"
        ]
    )

    print("Numeric columns selected")

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    print("Infinity values replaced")

    df = df.fillna(0)

    print("NaN values replaced")

    df = df.astype("float32")

    print("Converted dataset to float32")

    df = df.clip(
        lower=-1e10,
        upper=1e10
    )

    print("Extreme values clipped")

    print("Remaining NaN:", np.isnan(df.values).sum())
    print("Remaining Inf:", np.isinf(df.values).sum())

    # -------------------------------
    # Dynamic Feature Names
    # -------------------------------
    feature_names = df.columns.tolist()

    print(f"Total Features: {len(feature_names)}")

    scaler = MinMaxScaler()

    X = scaler.fit_transform(df.values)

    print("Feature scaling completed")

    input_dim = X.shape[1]

    print(f"Input Dimension: {input_dim}")

    model = build_autoencoder(input_dim)

    print("====================================")
    print("TRAINING AUTOENCODER MODEL")
    print("====================================")

    history = model.fit(
        X,
        X,
        epochs=10,
        batch_size=64,
        validation_split=0.2,
        verbose=1
    )

    print("====================================")
    print("TRAINING COMPLETED")
    print("====================================")

    print("Generating anomaly scores...")

    reconstructions = model.predict(X)

    mse = np.mean(
        np.power(
            X - reconstructions,
            2
        ),
        axis=1
    )

    save_anomaly_scores(mse)

    print("Anomaly scores saved")

    save_training_plot(
        history,
        "autoencoder"
    )

    print("Training plot saved")

    model_dir = "outputs/trained_models/autoencoder/"

    model.save(
        model_dir + "autoencoder.keras"
    )

    joblib.dump(
        scaler,
        model_dir + "scaler.pkl"
    )

    joblib.dump(
        feature_names,
        model_dir + "feature_names.pkl"
    )

    print("====================================")
    print("AUTOENCODER MODEL SAVED SUCCESSFULLY")
    print("====================================")

    print(f"Model          : {model_dir}autoencoder.keras")
    print(f"Scaler         : {model_dir}scaler.pkl")
    print(f"Feature Names  : {model_dir}feature_names.pkl")


if __name__ == "__main__":
    train_autoencoder()
