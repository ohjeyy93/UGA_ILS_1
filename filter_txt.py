with open("data/snRNA.raw.metadata.txt", "r") as r1:
	for lines in r1:
		print(lines.split("\t")[0])