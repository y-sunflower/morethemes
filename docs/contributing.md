This document focuses on adding themes to **`morethemes`**, but other kind of contributions are possible. Feel free to [open an issue](https://github.com/JosephBARBIERDARNAL/morethemes/issues) to discuss it.

In this tutorial, I'll assume your theme is named `sunglasses`, as for the example. Remember to change it with the actual name of your theme.

### Setup your environment

- Fork the repository to your own GitHub account.

- Clone your forked repository to your local machine (ensure you have [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)):

```bash
git clone https://github.com/YOURUSERNAME/morethemes.git
cd morethemes
```

- Create a new branch for your theme:

```bash
git checkout -b sunglasses
```

- Set up your Python environment (ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)):

```bash
uv sync --all-extras
uv pip install -e .
uv run pre-commit install
```

- Check that everything works:

```bash
uv run pytest
```

### Add a new theme

- In `morethemes/themes.py`, add a new theme that looks like this:

```python
sunglasses_theme = {
    "name": "sunglasses", # the name of your theme
    "description": "A description of the theme",
    "theme": { # all arguments passed to plt.rcParams
        "axes.facecolor": "#232323",
        "figure.facecolor": "#282828",
    },
}
```

!!! note

    If you're looking how to make a (great) theme, check [this](../guide/create-your-theme).

- At the end of `morethemes/morethemes/themes.py`, add your theme to `ALL_THEMES`:

```python
ALL_THEMES = {
    "darker": darker_theme,
    "lighter": lighter_theme,
    "sunglasses": sunglasses_theme, # add your theme here
}
```

### Test the theme

- Test that everything works correctly by running:

```bash
uv run pytest
```

### Push changes

- Commit and push your changes:

```bash
git add -A
git commit -m "add sunglasses theme"
git push
```

- Go back to your fork and click on the "Open a PR" popup

Congrats! Once your PR is merged, it will be part of **`morethemes`** and accessible via `mt.set_theme("sunglasses")`. It'll be available once a new released is published on PyPI.

Feel free to ask me if you have any questions!

<br><br>
