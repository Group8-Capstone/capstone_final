import matplotlib.pyplot as plt


def save_fraud_chart(predictions):

    fraud_count = sum(predictions)

    normal_count = len(predictions) - fraud_count

    labels = ['Normal', 'Fraud']

    values = [normal_count, fraud_count]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    save_path = (
        'outputs/visualizations/'
        'fraud/fraud_distribution.png'
    )

    plt.savefig(save_path)

    plt.close()

    print(f'Fraud visualization saved: {save_path}')