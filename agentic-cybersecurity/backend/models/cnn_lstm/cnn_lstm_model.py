from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Input,
    Conv1D,
    MaxPooling1D,
    LSTM,
    Dense,
    Dropout,
    BatchNormalization
)

from tensorflow.keras.optimizers import Adam


def build_cnn_lstm(input_shape, num_classes):

    print("=" * 60)
    print("BUILDING CNN-LSTM MODEL")
    print("=" * 60)

    model = Sequential()

    # ==================================================
    # INPUT
    # ==================================================

    model.add(
        Input(shape=input_shape)
    )

    # ==================================================
    # CNN BLOCK 1
    # ==================================================

    model.add(
        Conv1D(
            filters=64,
            kernel_size=3,
            activation="relu",
            padding="same"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        MaxPooling1D(pool_size=2)
    )

    model.add(
        Dropout(0.30)
    )

    # ==================================================
    # CNN BLOCK 2
    # ==================================================

    model.add(
        Conv1D(
            filters=128,
            kernel_size=3,
            activation="relu",
            padding="same"
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(
        MaxPooling1D(pool_size=2)
    )

    model.add(
        Dropout(0.30)
    )

    # ==================================================
    # LSTM
    # ==================================================

    model.add(
        LSTM(
            64,
            return_sequences=False
        )
    )

    model.add(
        Dropout(0.30)
    )

    # ==================================================
    # DENSE
    # ==================================================

    model.add(
        Dense(
            128,
            activation="relu"
        )
    )

    model.add(
        Dropout(0.30)
    )

    model.add(
        Dense(
            64,
            activation="relu"
        )
    )

    # ==================================================
    # OUTPUT
    # ==================================================

    model.add(
        Dense(
            num_classes,
            activation="softmax"
        )
    )

    # ==================================================
    # COMPILE
    # ==================================================

    model.compile(

        optimizer=Adam(
            learning_rate=0.0001
        ),

        loss="sparse_categorical_crossentropy",

        metrics=["accuracy"]

    )

    print("CNN-LSTM model built successfully")
    print("Input Shape :", input_shape)
    print("Classes     :", num_classes)
    print("=" * 60)

    return model