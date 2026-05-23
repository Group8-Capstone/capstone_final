import joblib

from tensorflow.keras.models import load_model


def load_autoencoder():

    return load_model(

        'outputs/trained_models/'
        'autoencoder/autoencoder.keras'
    )


def load_cnn_lstm():

    return load_model(

        'outputs/trained_models/'
        'cnn_lstm/cnn_lstm.keras'
    )


def load_transformer():

    return load_model(

        'outputs/trained_models/'
        'transformer/transformer.keras'
    )


def load_fraud_model():

    return joblib.load(

        'outputs/trained_models/'
        'fraud_detection/fraud_model.pkl'
    )


def load_lanl_model():

    return joblib.load(

        'outputs/trained_models/'
        'lanl/lanl_model.pkl'
    )