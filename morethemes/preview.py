import matplotlib.pyplot as plt
import morethemes as mt
import numpy as np


def preview_theme(theme=None):
    if theme is not None:
        mt.set_theme(theme)
    np.random.seed(0)

    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(8, 5), layout="tight", dpi=200)

    axs[0, 0].scatter(np.random.normal(size=100), np.random.normal(size=100), s=70)

    for i in range(3):
        np.random.seed(i)
        axs[0, 1].plot(list(range(20)), np.random.normal(size=20))

    axs[1, 1].barh(
        ["France", "Italy", "Germany", "Australia"], [1000, 2000, 3000, 2000]
    )

    axs[1, 0].pie(
        [20, 40, 20, 20],
        labels=["A", "B", "C", "D"],
        explode=[0.08] * 4,
    )
    axs[1, 0].pie([1], colors=[fig.get_facecolor()], radius=0.5)

    fig.text(x=0.5, y=1, s=f"Preview of theme: {theme}", size=20, ha="center")

    return fig
