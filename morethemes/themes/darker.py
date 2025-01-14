from cycler import cycler

darker_theme = {
    "name": "darker",
    "author": "Joseph Barbier",
    "theme": {
        "axes.facecolor": "#282828",
        "figure.facecolor": "#282828",
        "axes.labelcolor": "#eeeeee",
        "axes.edgecolor": "#eeeeee",
        "xtick.color": "#eeeeee",
        "ytick.color": "#eeeeee",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "both",
        "grid.color": "#808080",
        "grid.linestyle": "--",
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "ytick.minor.visible": False,
        "scatter.marker": "H",
        "text.color": "#fff",
        "lines.linewidth": 1.5,
        "grid.alpha": 0.7,
        "axes.labelsize": 12,
        "axes.linewidth": 1.5,
        "axes.prop_cycle": cycler(
            "color", ["#FED789", "#A4BED5", "#72874E", "#023743", "#476F84", "#453947"]
        ),
    },
}

if __name__ == "__main__":
    import morethemes as mt

    mt.preview_theme("darker")
