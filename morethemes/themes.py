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
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "ytick.minor.visible": False,
        "scatter.marker": "H",
        "text.color": "#fff",
        "lines.linewidth": 2.5,
        "axes.labelsize": 12,
        "axes.linewidth": 1.5,
        "axes.prop_cycle": cycler(
            "color", ["#FED789", "#A4BED5", "#72874E", "#023743", "#476F84", "#453947"]
        ),
    },
}


lighter_theme = {
    "name": "lighter",
    "author": "Joseph Barbier",
    "theme": {
        "axes.facecolor": "#f62b2b",
        "figure.facecolor": "#ebebeb",
        "axes.labelcolor": "#373737",
        "xtick.color": "#373737",
        "ytick.color": "#373737",
        "text.color": "#373737",
    },
}


ALL_THEMES = {
    "darker": darker_theme,
    "lighter": lighter_theme,
}
