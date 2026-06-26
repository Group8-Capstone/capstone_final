import os
import json
import joblib

from sklearn.ensemble import IsolationForest

from preprocessing.preprocess_lanl import (
    preprocess_lanl
)


def train_lanl_model():

    print("=" * 60)
    print("TRAINING LANL UEBA MODEL")
    print("=" * 60)

    os.makedirs(
        "outputs/trained_models/lanl",
        exist_ok=True
    )

    dataset_path = (
        "datasets/lanl/auth.txt"
    )

    # =====================================
    # PREPROCESS DATA
    # =====================================

    df = preprocess_lanl(
        dataset_path
    )

    print(
        "LANL dataset preprocessed"
    )

    print(
        f"Sampled Shape: {df.shape}"
    )

    # =====================================
    # SAVE FEATURE NAMES
    # =====================================

    feature_names = df.columns.tolist()

    print(
        f"Total Features: {len(feature_names)}"
    )

    # =====================================
    # TRAIN DATA
    # =====================================

    X = df.values

    # =====================================
    # TRAIN ISOLATION FOREST
    # =====================================

    model = IsolationForest(

        n_estimators=100,

        contamination=0.02,

        random_state=42,

        verbose=1
    )

    model.fit(X)

    print("LANL model trained")

    # =====================================
    # PREDICTIONS
    # =====================================

    predictions = model.predict(X)

    total_records = len(predictions)

    anomalies_detected = int(
        (predictions == -1).sum()
    )

    normal_records = int(
        (predictions == 1).sum()
    )

    anomaly_percentage = round(
        (anomalies_detected / total_records) * 100,
        2
    )

    # =====================================
    # METRICS
    # =====================================

    metrics = {

        "model": "LANL UEBA",

        "algorithm": "Isolation Forest",

        "total_records": total_records,

        "anomalies_detected": anomalies_detected,

        "normal_records": normal_records,

        "anomaly_percentage": anomaly_percentage,

        "unique_users": int(
            df.iloc[:, 0].nunique()
        ),

        "unique_computers": int(
            df.iloc[:, 1].nunique()
        )
    }

    metrics_path = (
        "outputs/trained_models/"
        "lanl/metrics.json"
    )

    with open(
        metrics_path,
        "w"
    ) as f:
        json.dump(
            metrics,
            f,
            indent=4
        )

    print("Metrics saved successfully.")

    # =====================================
    # SAVE MODEL
    # =====================================

    model_path = (
        "outputs/trained_models/"
        "lanl/lanl_model.pkl"
    )

    feature_path = (
        "outputs/trained_models/"
        "lanl/feature_names.pkl"
    )

    joblib.dump(
        model,
        model_path
    )

    joblib.dump(
        feature_names,
        feature_path
    )

    print("=" * 60)
    print("LANL MODEL SAVED SUCCESSFULLY")
    print("=" * 60)

    print(
        f"Model Saved At: {model_path}"
    )

    print(
        f"Feature Names Saved At: {feature_path}"
    )

    print(
        f"Metrics Saved At: {metrics_path}"
    )


if __name__ == "__main__":

    train_lanl_model()