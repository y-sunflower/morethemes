import os
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from cycler import cycler

RcParams = dict[str, Any]


def get_brand_rcparams() -> RcParams:
    """Load the discovered brand.yml file and convert it to Matplotlib rcParams."""
    brand = _load_brand()
    return _brand_to_rcparams(brand)


def _load_brand() -> Any:
    try:
        from brand_yml import Brand
    except ImportError as exc:
        raise ImportError(
            "The 'brand' theme requires the optional 'brand_yml' dependency. "
            "Install it with `pip install 'morethemes[brand]'`."
        ) from exc

    path = os.environ.get("BRAND_YML_PATH", Path.cwd())
    return Brand.from_yaml(path)


def _brand_to_rcparams(brand: Any) -> RcParams:
    rcparams: RcParams = {}
    color = getattr(brand, "color", None)
    typography = getattr(brand, "typography", None)

    _add_color_rcparams(rcparams, color)
    _add_typography_rcparams(rcparams, typography)

    return rcparams


def _add_color_rcparams(rcparams: RcParams, color: Any) -> None:
    if color is None:
        return

    foreground = getattr(color, "foreground", None)
    background = getattr(color, "background", None)
    primary = getattr(color, "primary", None)
    secondary = getattr(color, "secondary", None)

    if foreground is not None:
        rcparams.update(
            {
                "text.color": foreground,
                "axes.labelcolor": foreground,
                "axes.edgecolor": foreground,
                "xtick.color": foreground,
                "ytick.color": foreground,
            }
        )
    if background is not None:
        rcparams.update({"figure.facecolor": background, "axes.facecolor": background})
    if primary is not None:
        rcparams["axes.titlecolor"] = primary
    if secondary is not None:
        rcparams["legend.edgecolor"] = secondary

    palette = getattr(color, "palette", None)
    if isinstance(palette, Mapping) and palette:
        rcparams["axes.prop_cycle"] = cycler("color", list(palette.values()))


def _add_typography_rcparams(rcparams: RcParams, typography: Any) -> None:
    if typography is None:
        return

    base = getattr(typography, "base", None)
    headings = getattr(typography, "headings", None)

    if base is not None:
        family = getattr(base, "family", None)
        weight = getattr(base, "weight", None)
        size = getattr(base, "size", None)
        color = getattr(base, "color", None)

        if family is not None:
            rcparams["font.family"] = family
        if weight is not None:
            rcparams["font.weight"] = _font_weight(weight)
        if size is not None:
            rcparams["font.size"] = _font_size(size)
        if color is not None:
            rcparams["text.color"] = color

    if headings is not None:
        weight = getattr(headings, "weight", None)
        size = getattr(headings, "size", None)
        color = getattr(headings, "color", None)

        if weight is not None:
            rcparams["axes.titleweight"] = _font_weight(weight)
        if size is not None:
            rcparams["axes.titlesize"] = _font_size(size)
        if color is not None:
            rcparams["axes.titlecolor"] = color


def _font_weight(weight: Any) -> Any:
    if isinstance(weight, str):
        weights = {
            "thin": 100,
            "extra-light": 200,
            "extralight": 200,
            "light": 300,
            "normal": 400,
            "regular": 400,
            "medium": 500,
            "semi-bold": 600,
            "semibold": 600,
            "bold": 700,
            "extra-bold": 800,
            "extrabold": 800,
            "black": 900,
        }
        return weights.get(weight.lower(), weight)
    return weight


def _font_size(size: Any) -> Any:
    if isinstance(size, (int, float)):
        return size
    if not isinstance(size, str):
        return size

    value = size.strip().lower()
    for unit, factor in (("px", 0.75), ("pt", 1.0), ("rem", 12.0), ("em", 12.0)):
        if value.endswith(unit):
            return float(value[: -len(unit)]) * factor
    return size


def get_brand_font_source(brand: Any, family: str) -> str:
    """Return the declared source for a brand font family."""
    typography = getattr(brand, "typography", None)
    fonts = getattr(typography, "fonts", None) if typography is not None else None
    if not isinstance(fonts, Iterable):
        return "system"

    for font in fonts:
        if getattr(font, "family", None) == family:
            return getattr(font, "source", "system") or "system"
    return "system"
