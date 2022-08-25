import h5py
import numpy as np
#f = h5py.File("data/maize_282.v8.3.raw_gene_activity.scJoint.h5", 'r')
#f3 = h5py.File("data/citeseq_control_rna.h5", 'r')
#np.array((f3["matrix/data"])
#print(list(f3['matrix'].keys()))
#print((list(f3["matrix/data"][::])))



f = h5py.File("data/exprs_10xPBMC_rna_log_count.h5", 'r')
print(list(f.keys()))
#for items in np.nditer(f['data']['exprs_10xPBMC_rna.h5'][::]):
#	if items!=-0.0:
#		print(items)

#for i in np.nditer(X):
#    if i>0:
#        print(i)
#print((f['data']['exprs_10xPBMC_rna.h5'][::]))

#print((f['data']['exprs_10xPBMC_rna.h5']))
dset2 = f['matrix']
#print(dset2["barcodes"][::])
#print((dset2["data"][::]))
it=np.nditer(dset2["data"][::],flags=['multi_index'],op_flags=['readwrite'])
while not it.finished:
	#if it[0]>0:
	print(it[0], it.multi_index)
	it.iternext()
#print(len(dset2["data"][::]))
#print(dset2["features"]["name"][::])

#f2 = h5py.File("data/exprs_10xPBMC_rna.h5", 'r')
f2 = h5py.File("atac.h5", 'r')
#print(list(f.keys()))
dset3 = f2['matrix']
print(dset3["barcodes"][::])
print((dset3["data"][::]))
print(len(dset3["data"][::]))
print(dset3["features"]["name"][::])
