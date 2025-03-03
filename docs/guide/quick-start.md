This document explains everything you need to get started using **`morethemes`**.

<br>

## Install

```bash
pip install morethemes
```

<br>

## Usage

### `mt.set_theme()`

`mt.set_theme()` is the main function you'll need. It basically has 2 arguments:

- `theme_name`: the name of the theme you want to apply. It must be one of the available themes: "wsj", "urban", "minimal", "ft", "nature", "economist", "retro", "yellowish", "darker", "monoblue".
- `reset_to_default`: whether to reset to default matplotlib theme before applying the theme. If not, themes can stack on top of each other.

Once the function is called, it will apply the theme to the global matplotlib configuration. You can reset to default theme by calling `mt.set_theme("default")`

```python
import morethemes as mt

mt.set_theme("wsj") # Wall Street Journal
```

<br>

### `mt.get_rcparams()`

You can get the current rcParams of a given theme by calling `mt.get_rcparams()`. It takes one argument: `theme_name` and returns a dictionary of rcParams.

```python
import morethemes as mt

wsj_rcparams = mt.get_rcparams("wsj")
```

Then you can apply them to your matplotlib configuration with:

```python
import morethemes as mt
import matplotlib.pyplot as plt

wsj_rcparams = mt.get_rcparams("wsj")
plt.rcParams.update(wsj_rcparams)
```

Another usage of this function is to avoid adding **`morethemes`** in your dependencies. Just copy the output of `mt.get_rcparams()` and paste it in your code.

<br>

### `mt.preview_theme()`

A convenient function when creating a theme. It will make many different charts and you'll easily be able to view how your theme currently looks like. Learn more in [create your theme page](../create-your-theme/).

<br><br>
