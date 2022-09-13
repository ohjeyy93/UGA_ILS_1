from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
with open("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata.txt", "r") as r1:
	count=1
	for lines in r1:
		count+=1
		print(lines.split("\t"))
		print(len(lines.split("\t")))
		#print(lines.split("\t"))
		if count==3:
			break
#x = np.arange(12)
#y = np.random.rand(len(x)) * 20
#c = np.random.rand(len(x)) * 3 + 1.5
#df = pd.DataFrame({"x": x, "y": y, "c": c})
#fig, ax = plt.subplots()
#cmap = plt.cm.hot
#norm = colors.Normalize(vmin=2.0, vmax=5.0)
#ax.scatter(df.x, df.y, color=cmap(norm(df.c.values)))
#ax.set_xticks(df.x)
#sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
#fig.colorbar(sm)
#plt.show()