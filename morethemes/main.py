import matplotlib as mpl
import matplotlib.pyplot as plt
from difflib import get_close_matches

from .themes import ALL_THEMES


def set_theme(theme_name, reset_to_default=True):
    """
    Apply a dictionary of rcParams to the global matplotlib configuration.

    Parameters
    ----------
    theme_name : str
        Name of the theme to apply (case insensitive).
    reset_to_default : bool
        Whether to first reset to default matplotlib theme before applying the theme.
        If not, themes can stack on top of each other.
    """
    if theme_name == "default":
        plt.rcParams.update(mpl.rcParamsDefault)
    else:
        theme_name = theme_name.lower()
        try:
            theme_dict = ALL_THEMES[theme_name]["theme"]
        except KeyError:
            suggestions = get_close_matches(
                theme_name, ALL_THEMES.keys(), n=3, cutoff=0.01
            )
            raise KeyError(
                f"Theme '{theme_name}' not found. Did you mean: {', '.join(suggestions)}?\n\n"
            )
        if reset_to_default:
            plt.rcParams.update(mpl.rcParamsDefault)
        for key, value in theme_dict.items():
            plt.rcParams[key] = value
