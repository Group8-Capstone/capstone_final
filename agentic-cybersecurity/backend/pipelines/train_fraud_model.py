import pandas as pd

from models.fraud_detection.xgboost_model import FraudDetectionModel


def train_fraud_model():

    dataset_path = (
        'datasets/credit_card/creditcard.csv'
    )

    df = pd.read_csv(dataset_path)

    model = FraudDetectionModel()

    model.train(df)


if __name__ == '__main__':
    train_fraud_model()