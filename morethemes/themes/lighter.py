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

if __name__ == "__main__":
    import morethemes as mt

    mt.preview_theme("lighter")
