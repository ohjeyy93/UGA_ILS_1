import pandas as pd
with open("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed_random.txt", "r") as t1:
	#with open("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed_random.csv", "w") as w1:
		count=0
		#w1.write("\"\""+","+"\"X\""+"\n")
		for lines in t1:
			count+=1
			#w1.write("\""+str(count)+"\""+",")
			#print(lines)
			#w1.write("\""+lines.split("\t")[0].strip("\n")+"\""+"\n")
print(count)
with open("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata.txt", "r") as r1:
	with open("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata_fixed.txt", "w") as w1:
		#w1.write("\"\""+","+"\"X\""+"\n")
		count2=0
		for lines in r1:
			if count2==count:
				break 
			w1.write(lines.split("\t")[-1].strip("\n")+"\n")
			#w1.write("\""+lines.split("\t")[-1].strip("\n")+"\""+"\n")
			count2+=1