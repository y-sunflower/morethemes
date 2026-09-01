import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest
from matplotlib.figure import Figure

import morethemes as mt


def test_version():
    assert mt.__version__ == "0.7.0"


def test_invalid_theme():
    """Check that an invalid theme name raises an error"""
    with pytest.raises(KeyError, match="Theme 'invalid key' not found. "):
        mt.set_theme("invalid key")


def test_valid_themes():
    """Check that all valid theme names don't raise an error"""
    for theme in mt.ALL_THEMES:
        assert "name" in mt.ALL_THEMES[theme]
        assert "theme" in mt.ALL_THEMES[theme]
        assert "description" in mt.ALL_THEMES[theme]
        assert len(mt.ALL_THEMES[theme]["description"]) < 200, (
            f"The description of theme {theme} has too many characters. "
            f"It must be below 200, not {len(mt.ALL_THEMES[theme]['description'])}"
        )


def test_valid_static_themes():
    """Check that all built-in themes can still be applied."""
    for theme in mt.ALL_THEMES:
        if theme != "brand":
            mt.set_theme(theme)


def test_brand_rcparams(tmp_path, monkeypatch):
    """Convert a brand.yml file into Matplotlib rcParams."""
    pytest.importorskip("brand_yml")
    (tmp_path / "_brand.yml").write_text(
        """
color:
  palette:
    blue: "#123456"
    orange: "#ff6600"
  foreground: blue
  background: "#ffffff"
  primary: orange
  secondary: blue
typography:
  base:
    family: DejaVu Sans
    weight: medium
    size: 16px
  headings:
    family: DejaVu Sans
    weight: semi-bold
    color: orange
""",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    rcparams = mt.get_rcparams("BRAND")

    assert rcparams["font.family"] == "DejaVu Sans"
    assert rcparams["font.weight"] == 500
    assert rcparams["font.size"] == 12
    assert rcparams["axes.titleweight"] == 600
    assert rcparams["axes.titlecolor"] == "#ff6600"
    assert rcparams["text.color"] == "#123456"
    assert rcparams["figure.facecolor"] == "#ffffff"
    assert rcparams["axes.facecolor"] == "#ffffff"
    assert rcparams["legend.edgecolor"] == "#123456"
    assert [color["color"] for color in rcparams["axes.prop_cycle"]] == [
        "#123456",
        "#ff6600",
    ]


def test_set_brand_theme(tmp_path, monkeypatch):
    """Apply a parsed brand theme to Matplotlib."""
    pytest.importorskip("brand_yml")
    (tmp_path / "_brand.yml").write_text(
        "color:\n  foreground: '#111111'\n  background: '#eeeeee'\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    mt.set_theme("brand")

    assert plt.rcParams["text.color"] == "#111111"
    assert plt.rcParams["figure.facecolor"] == "#eeeeee"


def test_brand_missing_dependency(monkeypatch):
    """Explain how to install the optional dependency."""
    monkeypatch.setitem(sys.modules, "brand_yml", None)

    with pytest.raises(ImportError, match=r"morethemes\[brand\]"):
        mt.get_rcparams("brand")


def test_brand_missing_file(tmp_path, monkeypatch):
    """Surface the parser's missing-file error."""
    pytest.importorskip("brand_yml")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(FileNotFoundError):
        mt.get_rcparams("brand")


def test_brand_invalid_file(tmp_path, monkeypatch):
    """Surface validation errors from brand_yml."""
    pytest.importorskip("brand_yml")
    (tmp_path / "_brand.yml").write_text("color: invalid\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(ValueError):
        mt.get_rcparams("brand")


def test_brand_unsupported_font_source(tmp_path, monkeypatch):
    """Reject font sources that cannot be registered by the Matplotlib adapter."""
    pytest.importorskip("brand_yml")
    (tmp_path / "_brand.yml").write_text(
        """
typography:
  fonts:
    - family: Brand Font
      source: bunny
  base: Brand Font
""",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    with pytest.raises(ValueError, match="does not support"):
        mt.set_theme("brand")


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
