with open('data/maize_282.v8.3.celltype_metadata.scJoint_fixed_50000.txt', "r") as r1:
	with open('data/maize_282.v8.3.celltype_metadata.scJoint_fixed_50000_selected.txt', "w") as w1:
		count=0
		for lines in r1:
			if count==50000:
				break
			w1.write(lines)
			count+=1