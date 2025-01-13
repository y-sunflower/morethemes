import matplotlib as mpl
import matplotlib.pyplot as plt

from .themes import ALL_THEMES

ALL_VALID_KEYS = set(plt.rcParams.keys())


def set_theme(theme_name, reset_to_default=True):
    """
    Apply a dictionary of rcParams to the global matplotlib configuration.

    Parameters
    ----------
    theme_name : str
        Name of the theme to apply.
    reset_to_default : bool
        Whether to first reset to default matplotlib theme before applying the theme.
        If not, themes can stack on top of each other.
    """
    if theme_name == "default":
        plt.rcParams.update(mpl.rcParamsDefault)
    else:
        try:
            theme_dict = ALL_THEMES[theme_name]["theme"]
        except KeyError:
            raise KeyError(
                f"Invalid theme name: {theme_name}. It must be one of:\n\n{list(ALL_THEMES.keys())}"
            )
        if reset_to_default:
            plt.rcParams.update(mpl.rcParamsDefault)
        for key, value in theme_dict.items():
            if key in ALL_VALID_KEYS:
                plt.rcParams[key] = value
            else:
                raise ValueError(
                    f"Invalid key: {key}. It must be one of:\n\n{ALL_VALID_KEYS}."
                )
