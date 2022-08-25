with open('data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference.txt', "r") as r1:
	with open('data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed.txt', "w") as w1:
		count=0
		for lines in r1:
			#print(lines)
			#count+=1
			#if count==20:
			#	break
			#print(lines.split("\t")[-6]+"\n")
			w1.write(lines.split("\t")[-6]+"\n")
			#print(lines.split("\t")[-2])
			#if "reference" in lines:
			#	w1.write(lines)

		#for items in lines.split("\t")[11]:
		#break
		#print(lines)
		#break
		#count=0
		#for lines in r1:
		#	if count==50000:
		#		break
		#	w1.write(lines)
		#	count+=1