import os
import numpy as np
import pandas as pd

from utils.save_attack_distribution import (
    save_attack_distribution
)


def preprocess_cicids(dataset_folder):

    print("=" * 60)
    print("PREPROCESSING CICIDS DATASET")
    print("=" * 60)

    all_dataframes = []

    # =====================================
    # VALIDATE DATASET PATH
    # =====================================

    if not os.path.exists(dataset_folder):

        raise FileNotFoundError(

            f"Dataset folder not found: "
            f"{dataset_folder}"
        )

    # =====================================
    # LOAD ALL CSV FILES
    # =====================================

    csv_files = [

        file_name

        for file_name in os.listdir(
            dataset_folder
        )

        if file_name.endswith('.csv')
    ]

    if len(csv_files) == 0:

        raise Exception(
            "No CSV files found "
            "inside dataset folder"
        )

    print(
        f"CSV Files Found: "
        f"{len(csv_files)}"
    )

    for file_name in csv_files:

        file_path = os.path.join(

            dataset_folder,

            file_name
        )

        print(
            f'Loading: {file_name}'
        )

        try:

            df = pd.read_csv(

                file_path,

                low_memory=False
            )

            print(
                f"Loaded Shape: "
                f"{df.shape}"
            )

            all_dataframes.append(df)

        except Exception as e:

            print(
                f'Error loading '
                f'{file_name}: {e}'
            )

    # =====================================
    # MERGE ALL FILES
    # =====================================

    print(
        "Merging all CICIDS files..."
    )

    combined_df = pd.concat(

        all_dataframes,

        ignore_index=True
    )

    print(
        "Dataset merged successfully"
    )

    print(
        f"Merged Shape: "
        f"{combined_df.shape}"
    )

    # =====================================
    # CLEAN COLUMN NAMES
    # =====================================

    combined_df.columns = (

        combined_df.columns
        .str.strip()
    )

    # =====================================
    # HANDLE NULL VALUES
    # =====================================

    null_count = combined_df.isnull().sum().sum()

    print(
        f"Total Null Values: "
        f"{null_count}"
    )

    combined_df = combined_df.fillna(0)

    # =====================================
    # HANDLE INFINITY VALUES
    # =====================================

    combined_df.replace(

        [np.inf, -np.inf],

        0,

        inplace=True
    )

    print(
        "Infinity values handled"
    )

    # =====================================
    # REMOVE DUPLICATES
    # =====================================

    before_duplicates = combined_df.shape[0]

    combined_df = combined_df.drop_duplicates()

    after_duplicates = combined_df.shape[0]

    print(
        f"Removed Duplicates: "
        f"{before_duplicates - after_duplicates}"
    )

    # =====================================
    # GENERATE ATTACK DISTRIBUTION
    # =====================================

    if 'Label' in combined_df.columns:

        print("=" * 60)
        print("GENERATING ATTACK DISTRIBUTION")
        print("=" * 60)

        try:

            save_attack_distribution(
                combined_df['Label']
            )

            print(
                "Attack distribution "
                "visualization generated"
            )

        except Exception as e:

            print(
                f"Attack visualization "
                f"error: {e}"
            )

    else:

        print(
            "Label column not found"
        )

    # =====================================
    # FINAL DATASET INFO
    # =====================================

    print("=" * 60)

    print(
        f'Total Records: '
        f'{combined_df.shape[0]}'
    )

    print(
        f'Total Columns: '
        f'{combined_df.shape[1]}'
    )

    if 'Label' in combined_df.columns:

        print(
            f"Attack Classes: "
            f"{combined_df['Label'].nunique()}"
        )

    print(
        "CICIDS preprocessing completed"
    )

    print("=" * 60)

    return combined_df