## quick start

import matplotlib.pyplot as plt
import morethemes as mt

plt.rcParams["savefig.dpi"] = 200

mt.set_theme("darker")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot([1, 2, 3, 4, 5])
ax.plot([7, 3, 5, 2, 1])
ax.plot([9, 0, 3, 2, 4])
plt.savefig("docs/img/quickstart.png", bbox_inches="tight")

##
