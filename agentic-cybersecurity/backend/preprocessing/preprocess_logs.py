import pandas as pd

from sklearn.preprocessing import LabelEncoder


def preprocess_logs(dataset_path):

    print("=" * 60)
    print("PREPROCESSING HDFS LOG DATASET")
    print("=" * 60)

    df = pd.read_csv(
        dataset_path
    )

    print(
        f"Original Shape: {df.shape}"
    )

    df = df.fillna(0)

    encoder = LabelEncoder()

    for column in df.columns:

        if df[column].dtype == 'object':

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

    df = df.select_dtypes(
        include=[
            'float64',
            'int64',
            'float32',
            'int32'
        ]
    )

    print(
        f"Processed Shape: {df.shape}"
    )

    return df