import h5py

f2 = h5py.File("data/asapseq_control_atac.h5", 'r')

print(list(f2.keys()))
dset = f2['matrix']
print(dset["data"][::])
