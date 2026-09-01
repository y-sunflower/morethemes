This document explains everything you need to get started using **`morethemes`**.

<br>

## `mt.set_theme()`

`mt.set_theme()` is the **main function** you'll need. It basically has 2 arguments:

- `theme_name`: the name of the theme you want to apply. It can be a built-in theme or `"brand"`.
- `reset_to_default`: whether to reset to default matplotlib theme before applying the theme. If not, themes can stack on top of each other. Default is `True` (and recommended).

Once the function is called, it will apply the theme to the **global matplotlib configuration**. You can reset to default theme by calling `mt.set_theme("default")`

```python
import morethemes as mt

mt.set_theme("wsj")  # Wall Street Journal
```

### The `brand` theme

The `brand` theme reads a Posit [`_brand.yml`](https://posit-dev.github.io/brand-yml/) file and generates Matplotlib rcParams from its colors and typography. Install the optional dependency first:

```bash
pip install "morethemes[brand]"
```

Then call it from a project containing `_brand.yml` (or configure the path using the `brand_yml` package's supported discovery settings):

```python
import morethemes as mt

mt.set_theme("brand")
```

The generated theme uses the brand foreground/background colors, primary and secondary colors, palette colors for the plot color cycle, and base/heading typography settings supported by Matplotlib. System and Google fonts are supported; local-file and Bunny font sources are not.

<br>

## `mt.get_rcparams()`

You can get the current rcParams of a given theme by calling `mt.get_rcparams()`. It takes one argument: `theme_name` and returns a dictionary of rcParams.

```python
import morethemes as mt

wsj_rcparams = mt.get_rcparams("wsj")
```

`mt.get_rcparams("brand")` dynamically parses the discovered `_brand.yml` file and returns the generated rcParams.

Then you can apply them to your matplotlib configuration with:

```python
import morethemes as mt
import matplotlib.pyplot as plt

wsj_rcparams = mt.get_rcparams("wsj")
plt.rcParams.update(wsj_rcparams)
```

Another usage of this function is to avoid adding **`morethemes`** in your dependencies. Just copy the output of `mt.get_rcparams()` and paste it in your code.

<br>

## `mt.preview_theme()`

A convenient function when creating a theme. It will make many different charts and you'll easily be able to view how your theme currently looks like. Learn more in [create your theme page](./create-your-theme.md).

<br><br>
