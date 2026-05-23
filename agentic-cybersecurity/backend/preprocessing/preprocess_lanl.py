import os
import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder
)


def preprocess_lanl(dataset_path):

    print("=" * 60)
    print("PREPROCESSING LANL AUTH DATASET")
    print("=" * 60)

    # =====================================
    # VALIDATE FILE
    # =====================================

    if not os.path.exists(dataset_path):

        raise FileNotFoundError(

            f"LANL dataset not found: "
            f"{dataset_path}"
        )

    # =====================================
    # LOAD DATASET
    # =====================================

    try:

        df = pd.read_csv(

            dataset_path,

            header=None,

            names=[

                'timestamp',

                'user',

                'computer'
            ]
        )

    except Exception as e:

        raise Exception(
            f"Error loading LANL dataset: {e}"
        )

    print(
        f"Original Shape: {df.shape}"
    )

    # =====================================
    # REMOVE NULL VALUES
    # =====================================

    null_values = df.isnull().sum().sum()

    print(
        f"Total Null Values: "
        f"{null_values}"
    )

    df = df.fillna(0)

    # =====================================
    # REMOVE DUPLICATES
    # =====================================

    before_duplicates = df.shape[0]

    df = df.drop_duplicates()

    after_duplicates = df.shape[0]

    print(
        f"Duplicates Removed: "
        f"{before_duplicates - after_duplicates}"
    )

    # =====================================
    # SAMPLE DATA
    # =====================================

    sample_size = min(
        50000,
        len(df)
    )

    df = df.sample(

        sample_size,

        random_state=42
    )

    print(
        f"Sampled Shape: {df.shape}"
    )

    # =====================================
    # LABEL ENCODING
    # =====================================

    print(
        "Encoding categorical columns..."
    )

    user_encoder = LabelEncoder()

    computer_encoder = LabelEncoder()

    df['user'] = (

        user_encoder.fit_transform(
            df['user']
        )
    )

    df['computer'] = (

        computer_encoder.fit_transform(
            df['computer']
        )
    )

    # =====================================
    # CONVERT TO NUMERIC
    # =====================================

    df = df.astype('float32')

    print(
        "Converted dataset to float32"
    )

    # =====================================
    # FINAL DATASET INFO
    # =====================================

    print("=" * 60)

    print(
        f"Processed Shape: {df.shape}"
    )

    print(
        f"Unique Users: "
        f"{df['user'].nunique()}"
    )

    print(
        f"Unique Computers: "
        f"{df['computer'].nunique()}"
    )

    print(
        "LANL preprocessing completed"
    )

    print("=" * 60)

    return df