import os


MODEL_REGISTRY = {

    'autoencoder': {

        'path': (
            'outputs/trained_models/'
            'autoencoder/autoencoder.keras'
        ),

        'type': 'deep_learning'
    },

    'cnn_lstm': {

        'path': (
            'outputs/trained_models/'
            'cnn_lstm/cnn_lstm.keras'
        ),

        'type': 'deep_learning'
    },

    'transformer': {

        'path': (
            'outputs/trained_models/'
            'transformer/transformer.keras'
        ),

        'type': 'deep_learning'
    },

    'fraud_detection': {

        'path': (
            'outputs/trained_models/'
            'fraud_detection/fraud_model.pkl'
        ),

        'type': 'xgboost'
    },

    'lanl': {

        'path': (
            'outputs/trained_models/'
            'lanl/lanl_model.pkl'
        ),

        'type': 'ueba'
    }
}


def get_model_path(model_name):

    return MODEL_REGISTRY.get(

        model_name,

        {}
    ).get('path')


def model_exists(model_name):

    model_path = get_model_path(
        model_name
    )

    return os.path.exists(
        model_path
    )