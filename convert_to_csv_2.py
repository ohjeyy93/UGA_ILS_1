import pandas as pd
with open("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata.txt", "r") as t1:
	with open("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata_fixed.txt", "w") as w1:
		for lines in t1:
			#print(lines.split("\t")[-1])
			w1.write(lines.split("\t")[1]+"\n")