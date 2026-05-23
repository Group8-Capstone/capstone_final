import matplotlib.pyplot as plt


def save_lanl_plot(data):

    plt.figure(figsize=(10, 5))

    plt.plot(data)

    plt.title('LANL Authentication Analysis')

    save_path = (
        'outputs/visualizations/lanl/'
        'lanl_analysis.png'
    )

    plt.savefig(save_path)

    plt.close()

    print(f'LANL plot saved: {save_path}')