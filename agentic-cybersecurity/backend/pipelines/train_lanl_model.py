import joblib

from sklearn.ensemble import IsolationForest

from preprocessing.preprocess_lanl import (
    preprocess_lanl
)


def train_lanl_model():

    print("=" * 60)
    print("TRAINING LANL UEBA MODEL")
    print("=" * 60)

    dataset_path = (
        'datasets/lanl/auth.txt'
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
    # USE FULL DATASET
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
    # SAVE MODEL
    # =====================================

    save_path = (

        'outputs/trained_models/'
        'lanl/lanl_model.pkl'
    )

    joblib.dump(
        model,
        save_path
    )

    print("=" * 60)
    print("LANL MODEL SAVED SUCCESSFULLY")
    print("=" * 60)

    print(
        f"Saved at: {save_path}"
    )


if __name__ == "__main__":

    train_lanl_model()