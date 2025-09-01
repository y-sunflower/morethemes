from matplotlib.figure import Figure
import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

import morethemes as mt


def test_version():
    assert mt.__version__ == "0.5.1"


def test_invalid_theme():
    """Check that an invalid theme name raises an error"""
    with pytest.raises(KeyError, match="Theme 'invalid key' not found. "):
        mt.set_theme("invalid key")


def test_valid_themes():
    """Check that all valid theme names don't raise an error"""
    for theme in mt.ALL_THEMES.keys():
        assert "name" in mt.ALL_THEMES[theme].keys()
        assert "theme" in mt.ALL_THEMES[theme].keys()
        assert "description" in mt.ALL_THEMES[theme].keys()
        assert len(mt.ALL_THEMES[theme]["description"]) < 200, (
            f"The description of theme {theme} has too many characters. "
            f"It must be below 200, not {len(mt.ALL_THEMES[theme]['description'])}"
        )
        mt.set_theme(theme)


def test_set_theme_default():
    """Check that resetting the default style actually works"""
    plt.rcParams["lines.linewidth"] = 3.1415
    plt.rcParams["axes.titlesize"] = "medium"

    mt.set_theme("default")

    for key, default_value in mpl.rcParamsDefault.items():
        assert plt.rcParams[key] == default_value


def test_preview_theme():
    """Check that preview theme works"""
    fig = mt.preview_theme("ft")
    assert isinstance(fig, Figure)
