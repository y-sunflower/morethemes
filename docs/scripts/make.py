import matplotlib.pyplot as plt
import morethemes as mt

plt.rcParams["savefig.dpi"] = 250

for theme in mt.ALL_THEMES:
    fig = mt.preview_theme(theme)
    fig.savefig(f"docs/img/{theme}.png", dpi=200)


def tab_code_image(theme: str):
    if theme in ["wsj", "ft"]:
        theme_name = theme.upper()
    else:
        theme_name = theme.title()
    content = f"""
=== "{theme_name}"

    ![](img/{theme}.png)

    ```python
    import morethemes as mt
    mt.set_theme("{theme}")
    ```

    {mt.ALL_THEMES[theme]["description"]} Made by {mt.ALL_THEMES[theme]["author"]}.

    """
    return content


def image_readme(theme: str):
    if theme in ["wsj", "ft"]:
        theme_name = theme.upper()
    else:
        theme_name = theme.title()
    content = f"""
### {theme_name}

```python
import morethemes as mt
mt.set_theme("{theme}")
```

[![](https://raw.githubusercontent.com/JosephBARBIERDARNAL/morethemes/refs/heads/main/docs/img/{theme}.png)](https://josephbarbierdarnal.github.io/morethemes/)

    """
    return content


def top_of_file(is_README=False):
    if is_README:
        link_to_doc = (
            "[Documentation site](https://josephbarbierdarnal.github.io/morethemes/)"
        )
    else:
        link_to_doc = ""
    content = f"""
<!-- Automatically generated, do not change by hand. Use docs/script/make.py instead. -->

# `morethemes`: more themes for matplotlib

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/morethemes/image.png?raw=true" alt="morethemes logo" align="right" width="150px"/>

**`morethemes`** provides themes for [matplotlib](https://matplotlib.org/). More themes, better plots, one line of code.

![PyPI - Downloads](https://img.shields.io/pypi/dm/morethemes)

{link_to_doc}

"""
    return content


def theme_before():
    content = f"""
<br>

## Themes

**`morethemes`** offers {len(mt.ALL_THEMES)} themes at the moment:
    """
    return content


def install_snippet():
    content = """

<br>

## Installation

```bash
pip install morethemes
```

Don't want to add **`morethemes`** as a dependency? You can either browse the [source code](https://github.com/JosephBARBIERDARNAL/morethemes/blob/main/morethemes/themes.py) to find the rcParams, or use the `mt.get_rcparams("theme_name")` function.

    """
    return content


if __name__ == "__main__":
    index_content = top_of_file()
    index_content += theme_before()
    for theme in mt.ALL_THEMES:
        code_snippet = tab_code_image(theme)
        index_content += code_snippet
    index_content += install_snippet()

    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write(index_content)

    readme_content = top_of_file(is_README=True)
    readme_content += install_snippet()
    readme_content += theme_before()
    for theme in mt.ALL_THEMES:
        code_snippet = image_readme(theme)
        readme_content += code_snippet

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
