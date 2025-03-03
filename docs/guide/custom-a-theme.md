This document will explain how to change a theme when working with `morethemes`. It can be useful to change a small part of a theme without having to create a new one.

<br>

## Usage

Under the hood, `morethemes` uses the `matplotlib` `rcParams` to change the theme. Therefore, all the parameters you can change with `matplotlib` can be changed with `morethemes`.

For example, the `yellowish` theme has a yellow background.

```python
import morethemes as mt

mt.set_theme("yellowish")
mt.preview_theme()
```

![](https://raw.githubusercontent.com/JosephBARBIERDARNAL/morethemes/refs/heads/main/docs/img/yellowish.png)

The background color is set using 2 parameters:

- `figure.facecolor`: the background color of the figure
- `axes.facecolor`: the background color of the axes

Here, they have the same color, so we have to change both. If we want to set a blue background, we can do the following:

```python
import morethemes as mt
import matplotlib.pyplot as plt

mt.set_theme("yellowish")
plt.rcParams["figure.facecolor"] = "skyblue"
plt.rcParams["axes.facecolor"] = "skyblue"

mt.preview_theme()
```

![](https://raw.githubusercontent.com/JosephBARBIERDARNAL/morethemes/refs/heads/main/docs/img/yellowish-updated.png)
