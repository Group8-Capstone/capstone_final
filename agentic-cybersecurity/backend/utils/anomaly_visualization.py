import matplotlib.pyplot as plt


def save_anomaly_plot(scores):

    plt.figure(figsize=(10, 5))

    plt.plot(scores)

    plt.title('Anomaly Scores')

    plt.xlabel('Samples')

    plt.ylabel('Score')

    save_path = (
        'outputs/visualizations/anomaly_detection/'
        'anomaly_scores.png'
    )

    plt.savefig(save_path)

    plt.close()

    print(f'Anomaly plot saved: {save_path}')