import pandas as pd
with open("data/maize_282.v8.3.celltype_metadata.scJoint.txt", "r") as t1:
	with open("data/maize_282.v8.3.celltype_metadata.scJoint_fixed.txt", "w") as w1:
		for lines in t1:
			w1.write(lines.split("\t")[1]+"\n")