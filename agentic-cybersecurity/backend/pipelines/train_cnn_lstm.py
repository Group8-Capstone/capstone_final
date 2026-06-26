import os
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from preprocessing.preprocess_cicids import preprocess_cicids
from models.cnn_lstm.cnn_lstm_model import build_cnn_lstm

from utils.save_training_plot import save_training_plot
from utils.save_confusion_matrix import save_confusion_matrix
from utils.save_classification_report import save_classification_report
from utils.save_roc_curve import save_roc_curve
from utils.save_predictions import save_predictions


MODEL_DIR = "outputs/trained_models/cnn_lstm"


def create_output_directory():
    os.makedirs(MODEL_DIR, exist_ok=True)


def save_metadata(feature_names, scaler, encoder):
    """
    Save all preprocessing objects required during inference.
    """

    metadata = {
        "feature_names": feature_names,
        "feature_count": len(feature_names),
        "model_type": "cnn_lstm",
        "dataset": "CICIDS2017"
    }

    joblib.dump(
        scaler,
        os.path.join(MODEL_DIR, "scaler.pkl")
    )

    joblib.dump(
        encoder,
        os.path.join(MODEL_DIR, "label_encoder.pkl")
    )

    joblib.dump(
        feature_names,
        os.path.join(MODEL_DIR, "feature_names.pkl")
    )

    joblib.dump(
        metadata,
        os.path.join(MODEL_DIR, "model_metadata.pkl")
    )

    with open(
        os.path.join(MODEL_DIR, "model_metadata.json"),
        "w"
    ) as f:
        json.dump(metadata, f, indent=4)

    print("Metadata saved successfully.")


def train_cnn_lstm():

    print("=" * 60)
    print("CNN-LSTM TRAINING PIPELINE STARTED")
    print("=" * 60)

    create_output_directory()

    dataset_folder = "datasets/cicids"

    #############################################################
    # Load Dataset
    #############################################################

    df = preprocess_cicids(dataset_folder)

    print("Dataset loaded successfully")
    print("Dataset Shape:", df.shape)

    #############################################################
    # Development Sampling
    #############################################################

    if len(df) > 50000:
        df = df.sample(
            50000,
            random_state=42
        )

    print("Working Shape:", df.shape)

    #############################################################
    # Clean Column Names
    #############################################################

    df.columns = df.columns.str.strip()

    #############################################################
    # Replace Invalid Values
    #############################################################

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    df.fillna(0, inplace=True)

    #############################################################
    # Label
    #############################################################

    if "Label" not in df.columns:
        raise Exception("Label column not found.")

    y = df["Label"]

    encoder = LabelEncoder()

    y = encoder.fit_transform(y)

    #############################################################
    # Features
    #############################################################

    X = df.select_dtypes(
        include=[
            "float64",
            "float32",
            "int64",
            "int32"
        ]
    )

    if "Label" in X.columns:
        X = X.drop(columns=["Label"])

    #############################################################
    # Save Dynamic Feature Names
    #############################################################

    feature_names = X.columns.tolist()

    print("\nNumber of Features :", len(feature_names))
    print("First 10 Features :", feature_names[:10])

    #############################################################
    # Convert datatype
    #############################################################

    X = X.astype(np.float32)

    #############################################################
    # Remove Extreme Values
    #############################################################

    X = X.clip(
        lower=-1e10,
        upper=1e10
    )

    #############################################################
    # Scale
    #############################################################

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    #############################################################
    # Save Metadata
    #############################################################

    save_metadata(
        feature_names,
        scaler,
        encoder
    )

    #############################################################
    # Train/Test Split
    #############################################################

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    #############################################################
    # CNN-LSTM Reshape
    #############################################################

    X_train = X_train.reshape(
        X_train.shape[0],
        X_train.shape[1],
        1
    )

    X_test = X_test.reshape(
        X_test.shape[0],
        X_test.shape[1],
        1
    )

    print("Training Shape :", X_train.shape)
    print("Testing Shape  :", X_test.shape)

    #############################################################
    # Build Model
    #############################################################

    model = build_cnn_lstm(
        input_shape=(X_train.shape[1], 1)
    )

    #############################################################
    # Train
    #############################################################

    history = model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=64,
        validation_split=0.20,
        verbose=1
    )

    #############################################################
    # Prediction
    #############################################################

    probabilities = model.predict(X_test)

    predictions = (
        probabilities > 0.5
    ).astype(int)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nAccuracy :", accuracy)

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    #############################################################
    # Reports
    #############################################################

    save_classification_report(
        y_test,
        predictions,
        "cnn_lstm"
    )

    save_predictions(
        predictions,
        "cnn_lstm"
    )

    save_confusion_matrix(
        y_test,
        predictions,
        "cnn_lstm"
    )

    save_training_plot(
        history,
        "cnn_lstm"
    )

    save_roc_curve(
        y_test,
        probabilities,
        "cnn_lstm"
    )

    #############################################################
    # Save Model
    #############################################################

    model.save(
        os.path.join(
            MODEL_DIR,
            "cnn_lstm.keras"
        )
    )

    print("\nCNN-LSTM model saved successfully.")
    print("Feature Count :", len(feature_names))
    print("Metadata Saved :", MODEL_DIR)


if __name__ == "__main__":
    train_cnn_lstm()