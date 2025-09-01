```python
# mkdocs: hidecode
# mkdocs: hideoutput
# mkdocs: render
import morethemes as mt

mt.set_theme("default")
```

This document will explain how to change a theme when working with **`morethemes`**. It can be useful to change a small part of a theme without having to create a new one.

<br>

## Example

Under the hood, **`morethemes`** uses the `matplotlib` `rcParams` to change the theme. Therefore, all the parameters you can change with `matplotlib` can be changed with **`morethemes`**.

For example, the `yellowish` theme has a yellow background.

```python
# mkdocs: render
import morethemes as mt

mt.set_theme("yellowish")
mt.preview_theme()
```

Let's say we want to change the background color. The background color is set using 2 parameters:

- `figure.facecolor`: the background color of the figure
- `axes.facecolor`: the background color of the axes

Here, they have the same color, so we have to change both. If we want to set a blue background, we can do the following:

```python
# mkdocs: render
import morethemes as mt
import matplotlib.pyplot as plt

mt.set_theme("yellowish")
plt.rcParams["figure.facecolor"] = "skyblue"
plt.rcParams["axes.facecolor"] = "skyblue"

mt.preview_theme()
```

There is no easy way to know what parameters you need to change to fit your exact needs, but you can find more info in the [create your theme page](./create-your-theme.md).

<br><br>
