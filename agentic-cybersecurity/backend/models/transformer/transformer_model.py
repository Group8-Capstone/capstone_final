from tensorflow.keras.models import (
    Sequential
)

from tensorflow.keras.layers import (
    Dense,
    Dropout,
    BatchNormalization
)

from tensorflow.keras.optimizers import (
    Adam
)


def build_transformer(input_shape):

    print("=" * 60)
    print("BUILDING TRANSFORMER MODEL")
    print("=" * 60)

    model = Sequential()

    # =====================================
    # INPUT LAYER
    # =====================================

    model.add(

        Dense(

            256,

            activation='relu',

            input_shape=input_shape
        )
    )

    # =====================================
    # NORMALIZATION
    # =====================================

    model.add(
        BatchNormalization()
    )

    # =====================================
    # DROPOUT
    # =====================================

    model.add(

        Dropout(0.3)
    )

    # =====================================
    # SECOND DENSE BLOCK
    # =====================================

    model.add(

        Dense(

            128,

            activation='relu'
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(

        Dropout(0.3)
    )

    # =====================================
    # THIRD DENSE BLOCK
    # =====================================

    model.add(

        Dense(

            64,

            activation='relu'
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(

        Dropout(0.2)
    )

    # =====================================
    # FOURTH DENSE BLOCK
    # =====================================

    model.add(

        Dense(

            32,

            activation='relu'
        )
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
        "Transformer model built successfully"
    )

    print("=" * 60)

    return model