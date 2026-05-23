import pandas as pd


def save_predictions(
    predictions,
    model_name
):

    df = pd.DataFrame({
        'Prediction': predictions.flatten()
    })

    save_path = (
        'outputs/predictions/'
        f'{model_name}_predictions.csv'
    )

    df.to_csv(
        save_path,
        index=False
    )

    print(f'Predictions saved: {save_path}')