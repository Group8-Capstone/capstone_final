from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Input,
    Dense,
    Dropout,
    BatchNormalization
)
from tensorflow.keras.optimizers import Adam


def build_transformer(input_shape, num_classes):

    print("=" * 60)
    print("BUILDING TRANSFORMER MODEL")
    print("=" * 60)

    model = Sequential()

    # =====================================
    # INPUT
    # =====================================

    model.add(
        Input(shape=input_shape)
    )

    # =====================================
    # BLOCK 1
    # =====================================

    model.add(
        Dense(
            512,
            activation="relu"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        Dropout(0.40)
    )

    # =====================================
    # BLOCK 2
    # =====================================

    model.add(
        Dense(
            256,
            activation="relu"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        Dropout(0.35)
    )

    # =====================================
    # BLOCK 3
    # =====================================

    model.add(
        Dense(
            128,
            activation="relu"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        Dropout(0.30)
    )

    # =====================================
    # BLOCK 4
    # =====================================

    model.add(
        Dense(
            64,
            activation="relu"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        Dropout(0.25)
    )

    # =====================================
    # BLOCK 5
    # =====================================

    model.add(
        Dense(
            32,
            activation="relu"
        )
    )

    # =====================================
    # OUTPUT
    # =====================================

    model.add(
        Dense(
            num_classes,
            activation="softmax"
        )
    )

    # =====================================
    # COMPILE
    # =====================================

    model.compile(
        optimizer=Adam(
            learning_rate=0.0001
        ),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    print("Transformer model built successfully")
    print("=" * 60)

    return model