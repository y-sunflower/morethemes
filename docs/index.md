

<!-- Automatically generated, do not change by hand. Use docs/index.qmd instead. -->

# `morethemes`: more themes for matplotlib

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/morethemes/image.png?raw=true" alt="morethemes logo" align="right" width="150px"/>

**`morethemes`** provides themes for
[matplotlib](https://matplotlib.org/). More themes, better plots, one
line of code.

[![](https://static.pepy.tech/badge/morethemes)](https://pepy.tech/projects/morethemes)

<br>

## Themes

**`morethemes`** offers 14 themes at the moment:

=== "WSJ"

    ![](img/wsj.png)

    ```python
    import morethemes as mt
    mt.set_theme("wsj")
    ```

    A refined, newspaper-style theme inspired by the Wall Street Journal.

=== "URBAN"

    ![](img/urban.png)

    ```python
    import morethemes as mt
    mt.set_theme("urban")
    ```

    A clean, professional theme featuring the Urbanist font and muted tones.

=== "MINIMAL"

    ![](img/minimal.png)

    ```python
    import morethemes as mt
    mt.set_theme("minimal")
    ```

    A pure, distraction-free theme with a simple monochrome palette.

=== "FT"

    ![](img/ft.png)

    ```python
    import morethemes as mt
    mt.set_theme("ft")
    ```

    A sophisticated, no-nonsense theme with a muted palette and strong typographic clarity, echoing the Financial Times' aesthetic.

=== "NATURE"

    ![](img/nature.png)

    ```python
    import morethemes as mt
    mt.set_theme("nature")
    ```

    A calming theme inspired by natural landscapes, with earthy tones and organic shapes.

=== "ECONOMIST"

    ![](img/economist.png)

    ```python
    import morethemes as mt
    mt.set_theme("economist")
    ```

    A crisp, data-focused theme with subtle gridlines and sharp contrasts.

=== "GREENWAVE"

    ![](img/greenwave.png)

    ```python
    import morethemes as mt
    mt.set_theme("greenwave")
    ```

    A sleek, dark-themed aesthetic with vibrant green accents, inspired by modern streaming interfaces. Designed for clarity and style, with bold typography and a focus on visual harmony.

=== "VSCODE-DARK"

    ![](img/vscode-dark.png)

    ```python
    import morethemes as mt
    mt.set_theme("vscode-dark")
    ```

    A dark theme inspired by Visual Studio Code's dark mode.

=== "NORD"

    ![](img/nord.png)

    ```python
    import morethemes as mt
    mt.set_theme("nord")
    ```

    A crisp, Arctic-inspired theme based on the Nord color palette with frosty blues and clean contrasts

=== "RETRO"

    ![](img/retro.png)

    ```python
    import morethemes as mt
    mt.set_theme("retro")
    ```

    A nostalgic theme inspired by vintage graphics and retro gaming.

=== "LIGHTER"

    ![](img/lighter.png)

    ```python
    import morethemes as mt
    mt.set_theme("lighter")
    ```

    A clean, modern theme inspired by the lighter aesthetic, perfect for technical charts.

=== "DARKER"

    ![](img/darker.png)

    ```python
    import morethemes as mt
    mt.set_theme("darker")
    ```

    A sleek, no-frills dark theme with high contrast and a modern feel

=== "YELLOWISH"

    ![](img/yellowish.png)

    ```python
    import morethemes as mt
    mt.set_theme("yellowish")
    ```

    A bold, National Geographic-inspired theme with a warm yellow backdrop

=== "MONOBLUE"

    ![](img/monoblue.png)

    ```python
    import morethemes as mt
    mt.set_theme("monoblue")
    ```

    A high-contrast theme using shades of blue to emphasize data trends and maintain a clean, professional aesthetic.

<br>

## Installation

``` bash
pip install morethemes
```

Don't want to add **`morethemes`** as a dependency? You can either
browse the [source
code](https://github.com/y-sunflower/morethemes/blob/main/morethemes/themes.py)
to find the rcParams, or use the `mt.get_rcparams("theme_name")`
function.
