import h5py
f = h5py.File("data/maize_snRNA.logcounts.h5", 'r')

#print(list(f.keys()))

#list_RNA=[]
dset2 = f['matrix']
#for items in dset2["features"]["name"][::]:


f2 = h5py.File("data/maize_282.v8.3.raw_gene_activity.scJoint.h5", 'r')

#print(list(f.keys()))
list_common_genes=[]
dset3 = f2['matrix']
for items in dset2["features"]["name"][::]:
	if items in dset3["features"]["name"][::]:
		list_common_genes+=[items]

print(len(list_common_genes))

