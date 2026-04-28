from difflib import get_close_matches
from typing import Any, cast

import matplotlib as mpl
import matplotlib.pyplot as plt
from pyfonts import load_google_font, set_default_font

from morethemes.themes import ALL_THEMES

RcParams = dict[str, Any]


def set_theme(theme_name: str, reset_to_default: bool = True) -> None:
    """
    Apply a dictionary of rcParams to the global matplotlib configuration.

    Parameters
    ----------
    theme_name : str
        Name of the theme to apply (case insensitive). It must be one of the available
        themes: "wsj", "urban", "minimal", "ft", "nature", "economist", "retro",
        "yellowish", "darker", "monoblue".
    reset_to_default : bool
        Whether to first reset to default matplotlib theme before applying the theme.
        If not, themes can stack on top of each other.
    """
    if theme_name.lower() == "default":
        plt.rcParams.update(mpl.rcParamsDefault)
    else:
        theme_dict = get_rcparams(theme_name)
        try:
            font_family = theme_dict["font.family"]
        except KeyError:
            raise KeyError(
                f"Theme '{theme_name}' is missing the required 'font.family' rcParam."
            )
        if not isinstance(font_family, str):
            raise TypeError(
                f"Theme '{theme_name}' has invalid 'font.family': "
                f"expected str, got {type(font_family).__name__}."
            )
        set_default_font(load_google_font(font_family))
        if reset_to_default:
            plt.rcParams.update(mpl.rcParamsDefault)
        for key, value in theme_dict.items():
            plt.rcParams[key] = value


def get_rcparams(theme_name: str) -> RcParams:
    """
    Return the theme dictionary passed to rcParams for the given theme name.

    Parameters
    ----------
    theme_name : str
        Name of the theme to retrieve (case insensitive).

    Returns
    -------
    theme_dict : dict
        Dictionary of rcParams for the given theme.

    Raises
    ------
    KeyError
        If the theme name is not found.
    """
    theme_name = theme_name.lower()
    try:
        theme_dict = ALL_THEMES[theme_name]["theme"]
    except KeyError:
        suggestions = get_close_matches(theme_name, ALL_THEMES.keys(), n=3, cutoff=0.01)
        raise KeyError(
            f"Theme '{theme_name}' not found. Did you mean: {', '.join(suggestions)}?"
        )
    return cast(RcParams, theme_dict)
