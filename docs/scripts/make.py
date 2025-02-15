import matplotlib.pyplot as plt
import morethemes as mt

plt.rcParams["savefig.dpi"] = 200

## quick start

mt.set_theme("darker")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot([1, 2, 3, 4, 5])
ax.plot([7, 3, 5, 2, 1])
ax.plot([9, 0, 3, 2, 4])
plt.savefig("docs/img/quickstart.png", bbox_inches="tight")

## gallery

for theme in mt.ALL_THEMES:
    mt.preview_theme(theme=theme)
    plt.savefig(f"docs/img/{theme}.png", bbox_inches="tight")


def code_and_image(theme: str):
    content = f"""
### {theme.title()}

{mt.ALL_THEMES[theme]["description"]}

```python
import matplotlib.pyplot as plt
import morethemes as mt

mt.set_theme("{theme}")
```

<center>![](img/{theme}.png)</center>

<br>
"""
    return content


def top_of_README():
    content = """
<!-- Automatically generated, do not change by hand. Use docs/script/gallery.py instead. -->

"""
    return content


readme_content = top_of_README()
for theme in mt.ALL_THEMES:
    dataset_content = code_and_image(theme)
    readme_content += dataset_content

with open("docs/gallery.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
