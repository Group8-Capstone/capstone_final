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

    dataset_folder = 'datasets/cicids'

    # Load dataset
    df = preprocess_cicids(dataset_folder)

    print("Dataset loaded successfully")

    # Sample dataset for development
    df = df.sample(
        50000,
        random_state=42
    )

    print(f"Sampled Shape: {df.shape}")

    # Keep only numeric columns
    df = df.select_dtypes(
        include=[
            'float64',
            'int64',
            'float32',
            'int32'
        ]
    )

    print("Numeric columns selected")

    # Replace infinity values
    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    print("Infinity values replaced")

    # Replace NaN values
    df = df.fillna(0)

    print("NaN values replaced")

    # Convert to float32
    df = df.astype('float32')

    print("Converted dataset to float32")

    # Extra protection against huge values
    df = df.clip(
        lower=-1e10,
        upper=1e10
    )

    print("Extreme values clipped")

    # Verify remaining invalid values
    print(
        "Remaining NaN:",
        np.isnan(df.values).sum()
    )

    print(
        "Remaining Inf:",
        np.isinf(df.values).sum()
    )

    # Feature Scaling
    scaler = MinMaxScaler()

    X = scaler.fit_transform(
        df.values
    )

    print("Feature scaling completed")

    input_dim = X.shape[1]

    print(
        f"Input Dimension: {input_dim}"
    )

    # Build Autoencoder
    model = build_autoencoder(
        input_dim
    )

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

    # ====================================
    # Generate anomaly scores
    # ====================================

    print("Generating anomaly scores...")

    reconstructions = model.predict(
        X
    )

    mse = np.mean(
        np.power(
            X - reconstructions,
            2
        ),
        axis=1
    )

    save_anomaly_scores(
        mse
    )

    print("Anomaly scores saved")

    # ====================================
    # Save training visualization
    # ====================================

    save_training_plot(
        history,
        'autoencoder'
    )

    print("Training plot saved")

    # ====================================
    # Save trained model
    # ====================================

    model.save(
        'outputs/trained_models/'
        'autoencoder/autoencoder.keras'
    )

    print("====================================")
    print("AUTOENCODER MODEL SAVED SUCCESSFULLY")
    print("====================================")


if __name__ == '__main__':

    train_autoencoder()