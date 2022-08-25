with open("data/maize_cell_type.csv", "r") as t1:
	with open("data/maize_cell_type_organized.csv", "w") as w1:	
		w1.write("\"\",\"X\""+"\n")
		column_number1=0
		for lines in t1:
			column_number1+=1
			#print(lines.split(" "))
			w1.write("\""+str(column_number1)+"\""+","+"\""+lines.split("\t")[1]+"\""+"\n")
		