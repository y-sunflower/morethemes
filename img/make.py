import matplotlib.pyplot as plt
import morethemes as mt

plt.rcParams["savefqig.dpi"] = 200

mt.set_theme("darker")

fig, ax = plt.subplots()
ax.barh(["Yes", "No"], [10, 20])
plt.savefig("img/quickstart.png", bbox_inches="tight")
plt.show()
