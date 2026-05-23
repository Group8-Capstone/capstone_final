import matplotlib.pyplot as plt


def apply_plot_style():

    plt.style.use('ggplot')

    plt.rcParams['figure.figsize'] = (
        10,
        5
    )

    plt.rcParams['axes.titlesize'] = 16

    plt.rcParams['axes.labelsize'] = 12

    plt.rcParams['xtick.labelsize'] = 10

    plt.rcParams['ytick.labelsize'] = 10

    plt.rcParams['legend.fontsize'] = 10

    plt.rcParams['lines.linewidth'] = 2

    plt.rcParams['grid.alpha'] = 0.3