import h5py
f = h5py.File("data/maize_snRNA.logcounts.h5", 'r')
#f="data/maize_snRNA.logcounts.h5"
print(list(f.keys()))
#dset=f['matrix']
#rint(dset.shape)
#import h5py

def traverse_datasets(hdf_file):

    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            path = f'{prefix}/{key}'
            if isinstance(item, h5py.Dataset): # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group): # test for group (go down)
                yield from h5py_dataset_iterator(item, path)

    for path, _ in h5py_dataset_iterator(hdf_file):
        yield path

with h5py.File("data/maize_snRNA.logcounts.h5", 'r') as f:
    for dset in traverse_datasets(f):
        print('Path:', dset)
        print('Shape:', f[dset].shape)
        print('Data type:', f[dset].dtype)

f2 = h5py.File("data/asapseq_control_atac.h5", 'r')
print(list(f2.keys()))

print("spread")

with h5py.File("data/asapseq_control_atac.h5", 'r') as f:
    for dset in traverse_datasets(f):
        print('Path:', dset)
        print('Shape:', f[dset].shape)
        print('Data type:', f[dset].dtype)

print("spread")
print("spread")
print("spread")

with h5py.File("data/maize_282.v8.3.raw_gene_activity.scJoint.h5", 'r') as f:
    for dset in traverse_datasets(f):
        print('Path:', dset)
        print('Shape:', f[dset].shape)
        print('Data type:', f[dset].dtype)

f2 = h5py.File("data/asapseq_control_atac.h5", 'r')

print(list(f2.keys()))
dset = f2['matrix']
print(dset["barcodes"][::])

print(list(f.keys()))
dset2 = f['matrix']
print(dset2["barcodes"][::])