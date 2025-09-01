import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import morethemes as mt
import numpy as np


def preview_theme(theme=None) -> Figure:
    if theme is not None:
        mt.set_theme(theme)
    np.random.seed(0)

    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(8, 6), dpi=200)
    fig.subplots_adjust(
        wspace=0.25, hspace=0.38, top=0.84, bottom=0.08, left=0.07, right=0.93
    )

    axs[0, 0].scatter(np.random.normal(size=100), np.random.normal(size=100), s=70)
    axs[0, 0].text(
        x=0, y=1.05, s="A cool scatter", transform=axs[0, 0].transAxes, size=12
    )

    for i in range(3):
        np.random.seed(i)
        axs[0, 1].plot(list(range(20)), np.random.normal(size=20), label=f"{i} line")
    axs[0, 1].legend(loc="upper right", bbox_to_anchor=(1.1, 1.2))
    axs[0, 1].text(
        x=0, y=1.05, s="Multiple lines", transform=axs[0, 1].transAxes, size=12
    )
    axs[0, 1].set(xlabel="Time", ylabel="Temperature")

    labels = ["France", "Italy", "Germany", "Australia"]
    values = [900, 1800, 3300, 2400]
    axs[1, 1].barh(labels, values)
    for i in range(4):
        axs[1, 1].text(x=values[i] - 100, y=i, s=values[i], ha="right", va="center")
    axs[1, 1].text(
        x=0, y=1.05, s="Horizontal barplot", transform=axs[1, 1].transAxes, size=12
    )

    axs[1, 0].pie(
        [20, 40, 20, 20],
        labels=["A", "B", "C", "D"],
        explode=[0.08] * 4,
    )
    axs[1, 0].pie([1], colors=[fig.get_facecolor()], radius=0.5)
    axs[1, 0].text(
        x=0, y=1.05, s="(Apple) Pie chart", transform=axs[1, 0].transAxes, size=12
    )

    fig.text(x=0.5, y=0.93, s=f"Preview of theme: {theme}", size=20, ha="center")

    return fig
