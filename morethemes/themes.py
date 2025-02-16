from cycler import cycler
from morethemes.fonts import set_family_from_file

darker_theme = {
    "name": "darker",
    "description": "My very first theme. I wanted to create something simple and a dark theme.",
    "author": "Joseph Barbier",
    "theme": {
        "font.family": set_family_from_file("Oswald.ttf"),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "ytick.minor.visible": False,
        "scatter.marker": "H",
        "lines.linewidth": 2.5,
        "axes.labelsize": 12,
        "axes.linewidth": 1.5,
        "text.color": "#fff",
        "axes.facecolor": "#282828",
        "figure.facecolor": "#282828",
        "axes.labelcolor": "#eeeeee",
        "axes.edgecolor": "#eeeeee",
        "xtick.color": "#eeeeee",
        "ytick.color": "#eeeeee",
        "axes.prop_cycle": cycler(
            "color", ["#FED789", "#A4BED5", "#72874E", "#023743", "#476F84", "#453947"]
        ),
    },
}


yellowish_theme = {
    "name": "yellowish",
    "description": "The background yellow comes from a nice National Geographic visualisation, and I think it looks pretty cool with the black and white visuals.",
    "author": "Joseph Barbier",
    "theme": {
        "font.family": set_family_from_file("Delius.ttf"),
        "ytick.minor.visible": False,
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "ytick.major.pad": 5,
        "xtick.major.pad": 5,
        "axes.grid": True,
        "grid.linewidth": 0.6,
        "grid.alpha": 0.6,
        "grid.linestyle": "-",
        "grid.color": "#bcbcbc",
        "axes.edgecolor": "#be1414",
        "axes.labelcolor": "#be1414",
        "axes.titlecolor": "#be1414",
        "text.color": "#be1414",
        "axes.facecolor": "#ffcc04",
        "figure.facecolor": "#ffcc04",
        "axes.linewidth": 1.2,
        "axes.prop_cycle": cycler(
            "color", ["#000000", "#555555", "#7e7e7e", "#b1b1b1", "#ececec"]
        ),
    },
}

urban_theme = {
    "name": "urban",
    "description": "I wanted to make a theme that used the Urbanist font, with a clean professional look. And here it is.",
    "author": "Joseph Barbier",
    "theme": {
        "font.family": set_family_from_file("Urbanist.ttf"),
        "ytick.minor.visible": False,
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "ytick.major.pad": 5,
        "xtick.major.pad": 5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.linewidth": 0.6,
        "grid.alpha": 0.1,
        "grid.linestyle": "-",
        "axes.linewidth": 1.2,
        "grid.color": "#1e1d1d",
        "axes.edgecolor": "#efefef",
        "axes.facecolor": "#efefef",
        "figure.facecolor": "#efefef",
        "axes.prop_cycle": cycler(
            "color", ["#F56455", "#15134B", "#87C785", "#572F30"]
        ),
    },
}

wsj_theme = {
    "name": "wsj",
    "description": "A theme inspired by the Wall Street Journal.",
    "author": "Joseph Barbier",
    "theme": {
        "font.family": set_family_from_file("Crimson.ttf"),
        "ytick.minor.visible": False,
        "xtick.minor.visible": False,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "ytick.major.pad": 5,
        "xtick.major.pad": 5,
        "axes.grid": True,
        "grid.linewidth": 0.8,
        "grid.linestyle": "-",
        "axes.linewidth": 1.2,
        "grid.alpha": 0.1,
        "grid.color": "#1e1d1d",
        "axes.edgecolor": "#1f1f1f",
        "axes.facecolor": "#f8ecdc",
        "figure.facecolor": "#f8ecdc",
        "axes.prop_cycle": cycler(
            "color",
            [
                "#855C75",
                "#D9AF6B",
                "#AF6458",
                "#736F4C",
                "#526A83",
                "#625377",
                "#68855C",
                "#9C9C5E",
                "#A06177",
                "#8C785D",
                "#467378",
                "#7C7C7C",
            ],
        ),
    },
}

economist_theme = {
    "name": "economist",
    "description": "A theme inspired by The Economist.",
    "author": "Joseph Barbier",
    "theme": {
        "font.family": set_family_from_file("RobotoFlex.ttf"),
        "ytick.minor.visible": False,
        "xtick.minor.visible": True,
        "xtick.major.size": 4,
        "xtick.minor.size": 2,
        "ytick.major.size": 0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "ytick.major.pad": 5,
        "xtick.major.pad": 5,
        "axes.grid": True,
        "grid.linewidth": 0.4,
        "grid.linestyle": "-",
        "axes.linewidth": 1.2,
        "axes.grid.axis": "y",
        "text.color": "#3d3d3d",
        "grid.color": "#989797",
        "axes.edgecolor": "#1f1f1f",
        "axes.facecolor": "#e8f4f4",
        "figure.facecolor": "#e8f4f4",
        "axes.prop_cycle": cycler(
            "color",
            [
                "#DB444B",
                "#006BA2",
                "#3EBCD2",
                "#379A8B",
                "#EBB434",
                "#B4BA39",
                "#9A607F",
                "#D1B07C",
                "#758D99",
            ],
        ),
    },
}


ALL_THEMES = {
    "darker": darker_theme,
    "yellowish": yellowish_theme,
    "urban": urban_theme,
    "wsj": wsj_theme,
    "economist": economist_theme,
}
