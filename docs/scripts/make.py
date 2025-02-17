import matplotlib.pyplot as plt
import morethemes as mt

plt.rcParams["savefig.dpi"] = 250

for theme in mt.ALL_THEMES:
    mt.preview_theme(theme)
    plt.savefig(f"docs/img/{theme}.png", bbox_inches="tight")


def tab_code_image(theme: str):
    if theme == "wsj":
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
    if theme in ["wsj"]:
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

`morethemes` provides themes for [matplotlib](https://matplotlib.org/). More themes, better plots. One line of code.

{link_to_doc}

<br>

## Themes

`morethemes` offers {len(mt.ALL_THEMES)} themes at the moment:

"""
    return content


def install_snippet():
    content = """

<br>

## Installation

```bash
pip install morethemes
```
    """
    return content


def end_of_index():
    content = """

<br>

## Learn matplotlib

This project is sponsored by [Matplotlib Journey](https://www.matplotlib-journey.com/){:target="\_blank"}, an online course designed to make you a matplotlib expert. If you're interested in learning matplotlib, have a look!

<center>[Join the course :fontawesome-solid-paper-plane:](https://www.matplotlib-journey.com/){ .md-button .md-button--primary  }</center>

<br>
    """
    return content


def end_of_readme():
    content = """

<br>

## Learn matplotlib

This project is sponsored by [Matplotlib Journey](https://www.matplotlib-journey.com/), an online course designed to make you a matplotlib expert. If you're interested in learning matplotlib, have a look!

<center>

[**Join the course**](https://www.matplotlib-journey.com/)

</center>

<br>
    """
    return content


if __name__ == "__main__":
    index_content = top_of_file()
    for theme in mt.ALL_THEMES:
        code_snippet = tab_code_image(theme)
        index_content += code_snippet
    index_content += install_snippet()
    index_content += end_of_index()

    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write(index_content)

    readme_content = top_of_file(is_README=True)
    for theme in mt.ALL_THEMES:
        code_snippet = image_readme(theme)
        readme_content += code_snippet
    readme_content += install_snippet()
    readme_content += end_of_readme()

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
