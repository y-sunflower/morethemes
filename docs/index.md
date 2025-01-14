# morethemes: more themes for matplotlib

`morethemes` was built to provide more themes to matplotlib. It has been created and is maintained by [Joseph Barbier](https://www.barbierjoseph.com/) and [Yan Holtz](https://www.yan-holtz.com/).

## Quick start

```python
import matplotlib.pyplot as plt
import morethemes as mt

mt.set_theme("darker")

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 5))
ax1.barh(
    ["France", "Italy", "Germany", "Australia"],
    [1000, 2000, 3000, 2000]
)
```
