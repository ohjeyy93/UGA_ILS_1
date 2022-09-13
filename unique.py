with open("data/maize_282.v8.3.celltype_metadata.scJoint_fixed.txt", "r") as r1:
	list_cell_type=[]
	for lines in r1:
		if lines not in list_cell_type:
			list_cell_type+=[lines]

	print(len(list_cell_type))