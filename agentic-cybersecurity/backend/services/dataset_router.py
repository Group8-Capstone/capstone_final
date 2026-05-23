from preprocessing.preprocess_cicids import preprocess_cicids
from preprocessing.preprocess_fraud import preprocess_fraud
from preprocessing.preprocess_logs import preprocess_logs
from preprocessing.preprocess_lanl import preprocess_lanl


def get_dataset_processor(dataset_name):

    dataset_name = dataset_name.lower()

    if dataset_name == "cicids":
        return preprocess_cicids

    elif dataset_name == "credit_card":
        return preprocess_fraud

    elif dataset_name == "hdfs":
        return preprocess_logs

    elif dataset_name == "lanl_auth":
        return preprocess_lanl

    else:
        raise Exception("Unsupported dataset")