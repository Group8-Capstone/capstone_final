from sklearn.metrics import classification_report


def save_classification_report(
    y_test,
    predictions,
    model_name
):

    report = classification_report(
        y_test,
        predictions
    )

    save_path = (
        'outputs/reports/classification_reports/'
        f'{model_name}_report.txt'
    )

    with open(save_path, 'w') as file:

        file.write(report)

    print(f'Classification report saved: {save_path}')