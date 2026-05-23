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


def train_cnn_lstm():

    print("====================================")
    print("CNN-LSTM TRAINING PIPELINE STARTED")
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

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

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

    # Extract labels
    y = df['Label']

    # Encode labels
    encoder = LabelEncoder()

    y = encoder.fit_transform(y)

    # Select numeric features only
    X = df.select_dtypes(
        include=['float64', 'int64', 'float32', 'int32']
    )

    # Remove label column if exists
    if 'Label' in X.columns:
        X = X.drop('Label', axis=1)

    # Convert datatype
    X = X.astype('float32')

    # Clip huge values
    X = X.clip(
        lower=-1e10,
        upper=1e10
    )

    print("Extreme values clipped")

    # Verify invalid values
    print(
        "Remaining NaN:",
        np.isnan(X.values).sum()
    )

    print(
        "Remaining Inf:",
        np.isinf(X.values).sum()
    )

    # Feature scaling
    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    print("Feature scaling completed")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Reshape for CNN-LSTM
    X_train = X_train.reshape(
        (X_train.shape[0], X_train.shape[1], 1)
    )

    X_test = X_test.reshape(
        (X_test.shape[0], X_test.shape[1], 1)
    )

    print(f"Train Shape: {X_train.shape}")

    # Build model
    model = build_cnn_lstm(
        (X_train.shape[1], 1)
    )

    print("====================================")
    print("TRAINING CNN-LSTM MODEL")
    print("====================================")

    history = model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=64,
        validation_split=0.2,
        verbose=1
    )

    print("====================================")
    print("TRAINING COMPLETED")
    print("====================================")

    prediction_probabilities = model.predict(X_test)

    predictions = (
        prediction_probabilities > 0.5
    ).astype(int)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("Accuracy:", accuracy)

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    # Save classification report
    save_classification_report(
        y_test,
        predictions,
        'cnn_lstm'
    )

    # Save predictions
    save_predictions(
        predictions,
        'cnn_lstm'
    )

    # Save confusion matrix
    save_confusion_matrix(
        y_test,
        predictions,
        'cnn_lstm'
    )

    # Save training graph
    save_training_plot(
        history,
        'cnn_lstm'
    )

    # Save trained model
    model.save(
        'outputs/trained_models/'
        'cnn_lstm/cnn_lstm.keras'
    )

    print("====================================")
    print("CNN-LSTM MODEL SAVED SUCCESSFULLY")
    print("====================================")


if __name__ == '__main__':
    train_cnn_lstm()