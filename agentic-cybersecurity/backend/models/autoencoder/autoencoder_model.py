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


def build_autoencoder(input_dim):

    print("=" * 60)
    print("BUILDING AUTOENCODER MODEL")
    print("=" * 60)

    model = Sequential()

    # =====================================
    # ENCODER
    # =====================================

    model.add(

        Dense(

            128,

            activation='relu',

            input_shape=(input_dim,)
        )
    )

    model.add(
        BatchNormalization()
    )

    model.add(

        Dropout(0.2)
    )

    # =====================================
    # ENCODER HIDDEN LAYER
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
    # BOTTLENECK LAYER
    # =====================================

    model.add(

        Dense(

            16,

            activation='relu'
        )
    )

    # =====================================
    # DECODER
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
    # DECODER HIDDEN LAYER
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

    # =====================================
    # OUTPUT LAYER
    # =====================================

    model.add(

        Dense(

            input_dim,

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

        loss='mse'
    )

    print(
        "Autoencoder model built successfully"
    )

    print("=" * 60)

    return model