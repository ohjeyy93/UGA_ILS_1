import random
random.seed(1)

with open("output/sce_10xPBMC_atac_skip_referenced_embeddings.txt", "r") as r1:
	count=0
	list_ran=[]
	list_count=[]
	for lines in r1:
		#print(lines)
		list_ran+=[[]]
		#list_count+=[]
		#count+=1
	#print(list_ran)
	#count=0
with open("output/sce_10xPBMC_atac_skip_referenced_embeddings.txt", "r") as r1:
	for lines in r1:
		#print(lines)
		list_ran[count]+=[lines]
		list_count+=[count]
		count+=1

with open("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed.txt", "r") as r2:
	count=0
	list_txt=[]
	for lines in r2:
		#print(lines)
		list_txt+=[[]]
		#count+=1
	#print(list_ran)
	#count=0
with open("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed.txt", "r") as r2:
	for lines in r2:
		#print(lines)
		list_txt[count]+=[lines]
		count+=1


#print(len(list_ran))

#list_ran_rna=random.sample(list_count, k=30587)
#list_txt_rna=random.sample(list_ran, k=30587)
list_count_rna=random.sample(list_count, k=30587)
#print(len(list_ran_rna))
print(list_count_rna)
with open("output/sce_10xPBMC_atac_skip_referenced_embeddings2.txt", "w") as w1:
	for item in list_count_rna:
		#print(''.join(item))
		w1.write(''.join(list_ran[item])+"\n")

with open("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed2.txt", "w") as w2:
	for item in list_count_rna:
		#print(''.join(item))
		w2.write(''.join(list_txt[item])+"\n")
	#print(list_ran)
	#print(list_ran[1])