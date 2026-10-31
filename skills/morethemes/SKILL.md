---
name: morethemes
description: Apply and customize morethemes themes in Python Matplotlib plots. Use when a user asks to style a plot with morethemes or inspect its theme settings.
---

# Use morethemes with Matplotlib

Use `morethemes` when the user wants a package theme for a Matplotlib plot. Import it as `mt` and apply a theme before creating the plot:

```python
import matplotlib.pyplot as plt
import morethemes as mt

mt.set_theme("wsj")
fig, ax = plt.subplots()
```

Choose a theme by the visual style the user wants:

- `wsj`: Refined newspaper style with an editorial feel.
- `urban`: Clean, professional style with muted tones.
- `minimal`: Distraction-free, monochrome style.
- `ft`: Muted editorial style with clear, strong typography.
- `nature`: Calm, earthy colors inspired by natural landscapes.
- `economist`: Crisp, data-focused style with subtle gridlines and sharp contrast.
- `greenwave`: Dark style with bold typography and vivid green accents.
- `lumen`: Soft, light style with clear, color-blind-friendly colors.
- `ebonis`: Dark, high-contrast style with a color-blind-friendly palette.
- `lighter`: Clean, modern style suited to technical charts.
- `vscode-dark`: Dark style inspired by Visual Studio Code.
- `nord`: Cool Arctic blues with clean contrasts.
- `retro`: Nostalgic style inspired by vintage graphics and retro gaming.
- `darker`: Sleek, high-contrast dark style.
- `yellowish`: Bold style with a warm yellow background.
- `monoblue`: Professional, high-contrast style built around shades of blue.
- `brand`: Dynamic colors and typography generated from a Posit `_brand.yml` file.

`mt.set_theme(name)` updates Matplotlib's global `rcParams` and resets them to Matplotlib defaults first. Pass `reset_to_default=False` to preserve existing settings. To inspect a theme without applying it, use `mt.get_rcparams(name)`; make small adjustments through `plt.rcParams` after applying the theme. Use `mt.preview_theme(name)` to render a sample figure.

The `brand` theme requires the optional dependency installed with `pip install "morethemes[brand]"` and a discoverable `_brand.yml` file. If `morethemes` or this optional dependency is missing, explain the install command and ask before changing the project's dependencies.
