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

from models.transformer.transformer_model import build_transformer

from utils.save_training_plot import save_training_plot
from utils.save_confusion_matrix import save_confusion_matrix
from utils.save_classification_report import save_classification_report
from utils.save_roc_curve import save_roc_curve
from utils.save_predictions import save_predictions


MODEL_DIR = "outputs/trained_models/transformer"


def save_metadata(feature_names, scaler, encoder):

    os.makedirs(MODEL_DIR, exist_ok=True)

    metadata = {
        "model_name": "transformer",
        "dataset": "CICIDS2017",
        "feature_count": len(feature_names),
        "feature_names": feature_names
    }

    joblib.dump(
        feature_names,
        os.path.join(MODEL_DIR, "feature_names.pkl")
    )

    joblib.dump(
        scaler,
        os.path.join(MODEL_DIR, "scaler.pkl")
    )

    joblib.dump(
        encoder,
        os.path.join(MODEL_DIR, "label_encoder.pkl")
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


def train_transformer():

    print("====================================")
    print("TRANSFORMER TRAINING PIPELINE STARTED")
    print("====================================")

    os.makedirs(MODEL_DIR, exist_ok=True)

    dataset_folder = "datasets/cicids"

    ############################################################
    # Load Dataset
    ############################################################

    df = preprocess_cicids(dataset_folder)

    print("Dataset loaded successfully")

    ############################################################
    # Sample Dataset
    ############################################################

    if len(df) > 50000:

        MAX_PER_CLASS = 3000

        df = (
            df.groupby("Label", group_keys=False)
            .apply(
                lambda x: x.sample(
                    min(len(x), MAX_PER_CLASS),
                    random_state=42
                )
            )
            .reset_index(drop=True)
        )

    print(df["Label"].value_counts())

    print(f"Sampled Shape: {df.shape}")

    ############################################################
    # Clean Columns
    ############################################################

    df.columns = df.columns.str.strip()

    ############################################################
    # Remove Invalid Values
    ############################################################

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    df.fillna(0, inplace=True)

    print("Invalid values handled.")

    ############################################################
    # Encode Labels
    ############################################################

    y = df["Label"]

    encoder = LabelEncoder()

    y = encoder.fit_transform(y)

    num_classes = len(np.unique(y))

    from tensorflow.keras.utils import to_categorical

    y = to_categorical(y, num_classes)

    ############################################################
    # Select Features
    ############################################################

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

    ############################################################
    # Save Dynamic Feature Names
    ############################################################

    feature_names = X.columns.tolist()

    print("\nTotal Features :", len(feature_names))
    print("First 10 Features :")

    for feature in feature_names[:10]:
        print(feature)

    ############################################################
    # Convert datatype
    ############################################################

    X = X.astype(np.float32)

    ############################################################
    # Clip huge values
    ############################################################

    X = X.clip(
        lower=-1e10,
        upper=1e10
    )

    print("Extreme values clipped")

    ############################################################
    # Verify invalid values
    ############################################################

    print(
        "Remaining NaN :",
        np.isnan(X.values).sum()
    )

    print(
        "Remaining Inf :",
        np.isinf(X.values).sum()
    )

    ############################################################
    # Feature Scaling
    ############################################################

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Feature scaling completed")

    ############################################################
    # Save Metadata
    ############################################################

    save_metadata(
        feature_names,
        scaler,
        encoder
    )

    ############################################################
    # Train Test Split
    ############################################################

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.20,
        random_state=42,
        stratify=np.argmax(y, axis=1)
    )

    print(f"Train Shape : {X_train.shape}")
    print(f"Test Shape  : {X_test.shape}")

    ############################################################
    # Build Transformer
    ############################################################

    model = build_transformer(
        input_shape=(X_train.shape[1],),
        num_classes=num_classes
    )

    print("====================================")
    print("TRAINING TRANSFORMER MODEL")
    print("====================================")

    history = model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=64,
        validation_split=0.20,
        verbose=1
    )

    print("====================================")
    print("TRAINING COMPLETED")
    print("====================================")

    ############################################################
    # Prediction
    ############################################################

    probabilities = model.predict(X_test)

    predictions = np.argmax(probabilities, axis=1)
    y_true = np.argmax(y_test, axis=1)

    accuracy = accuracy_score(
        y_true,
        predictions
    )

    print("\nAccuracy :", accuracy)

    print(
        classification_report(
            y_true,
            predictions
        )
    )

    report = classification_report(
        y_true,
        predictions,
        output_dict=True,
        zero_division=0
    )

    metrics = {
        "accuracy": round(float(accuracy) * 100, 2),
        "precision": round(float(report["weighted avg"]["precision"]) * 100, 2),
        "recall": round(float(report["weighted avg"]["recall"]) * 100, 2),
        "f1_score": round(float(report["weighted avg"]["f1-score"]) * 100, 2)
    }

    with open(
        os.path.join(MODEL_DIR, "metrics.json"),
        "w"
    ) as f:
        json.dump(metrics, f, indent=4)

    print("Metrics saved successfully.")

    ############################################################
    # Reports
    ############################################################

    save_classification_report(
        y_true,
        predictions,
        "transformer"
    )

    save_predictions(
        predictions,
        "transformer"
    )

    save_confusion_matrix(
        y_true,
        predictions,
        "transformer"
    )

    save_training_plot(
        history,
        "transformer"
    )

    try:
        save_roc_curve(
            y_true,
            probabilities,
            "transformer"
        )
    except Exception as e:
        print("ROC Curve skipped :", e)

    ############################################################
    # Save Model
    ############################################################

    model.save(
        os.path.join(
            MODEL_DIR,
            "transformer.keras"
        )
    )

    print("\n====================================")
    print("TRANSFORMER MODEL SAVED SUCCESSFULLY")
    print("====================================")
    print("Feature Count :", len(feature_names))
    print("Metadata Saved :", MODEL_DIR)


if __name__ == "__main__":
    train_transformer()