from tensorflow.keras.models import (
    Sequential
)

from tensorflow.keras.layers import (
    Conv1D,
    MaxPooling1D,
    LSTM,
    Dense,
    Dropout,
    BatchNormalization
)

from tensorflow.keras.optimizers import (
    Adam
)


def build_cnn_lstm(input_shape):

    print("=" * 60)
    print("BUILDING CNN-LSTM MODEL")
    print("=" * 60)

    model = Sequential()

    # =====================================
    # CNN BLOCK
    # =====================================

    model.add(

        Conv1D(

            filters=64,

            kernel_size=3,

            activation='relu',

            padding='same',

            input_shape=input_shape
        )
    )

    # =====================================
    # BATCH NORMALIZATION
    # =====================================

    model.add(
        BatchNormalization()
    )

    # =====================================
    # MAX POOLING
    # =====================================

    model.add(

        MaxPooling1D(
            pool_size=2
        )
    )

    # =====================================
    # DROPOUT
    # =====================================

    model.add(

        Dropout(0.3)
    )

    # =====================================
    # SECOND CNN BLOCK
    # =====================================

    model.add(

        Conv1D(

            filters=128,

            kernel_size=3,

            activation='relu',

            padding='same'
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(

        MaxPooling1D(
            pool_size=2
        )
    )

    model.add(

        Dropout(0.3)
    )

    # =====================================
    # LSTM LAYER
    # =====================================

    model.add(

        LSTM(

            64,

            return_sequences=False
        )
    )

    # =====================================
    # DENSE LAYER
    # =====================================

    model.add(

        Dense(

            64,

            activation='relu'
        )
    )

    model.add(

        Dropout(0.3)
    )

    # =====================================
    # OUTPUT LAYER
    # =====================================

    model.add(

        Dense(

            1,

            activation='sigmoid'
        )
    )

    # =====================================
    # COMPILE MODEL
    # =====================================

    model.compile(

        optimizer=Adam(
            learning_rate=0.0001
        ),

        loss='binary_crossentropy',

        metrics=['accuracy']
    )

    print(
        "CNN-LSTM model built successfully"
    )

    print("=" * 60)

    return model