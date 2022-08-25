import h5py
f = h5py.File("data/maize_snRNA.logcounts.h5", 'r')

#print(list(f.keys()))
dset2 = f['matrix']
print(dset2["barcodes"][::])
print(dset2["data"][::])
print(dset2["features"]["name"][::])

f2 = h5py.File("data/maize_282.v8.3.raw_gene_activity.scJoint.h5", 'r')

#print(list(f.keys()))
dset3 = f2['matrix']
print(dset3["barcodes"][::])
print(dset3["data"][::])
print(dset3["features"]["name"][::])

f3 = h5py.File("data/asapseq_control_atac.h5", 'r')

#print(list(f.keys()))
dset4 = f3['matrix']
print(dset4["barcodes"][::])
print(dset4["data"][::])
print(dset4["features"][::])

