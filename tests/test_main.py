import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

import morethemes as mt


def test_invalid_theme():
    """Check that an invalid theme name raises an error"""
    with pytest.raises(KeyError):
        mt.set_theme("invalid key")


def test_valid_themes():
    """Check that all valid theme names don't raise an error"""
    for theme in mt.ALL_THEMES.keys():
        assert "name" in mt.ALL_THEMES[theme].keys()
        assert "author" in mt.ALL_THEMES[theme].keys()
        assert "theme" in mt.ALL_THEMES[theme].keys()
        mt.set_theme(theme)


def test_set_theme_default():
    """Check that resetting the default style actually works"""
    plt.rcParams["lines.linewidth"] = 3.14
    plt.rcParams["axes.titlesize"] = "medium"

    mt.set_theme("default")

    for key, default_value in mpl.rcParamsDefault.items():
        assert plt.rcParams[key] == default_value
