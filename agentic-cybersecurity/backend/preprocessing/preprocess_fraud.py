import pandas as pd


def preprocess_fraud(file_path):

    df = pd.read_csv(file_path)

    df = df.dropna()

    return df