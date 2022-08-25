import h5py
f = h5py.File("data_10x/atac_pbmc_10k_v1_filtered_peak_bc_matrix.h5", 'r')

#print(list(f.keys()))
dset2 = f['matrix']
print(dset2["barcodes"][::])
print(len(dset2["data"][::]))
print(dset2["features"]["name"][::])

f2 = h5py.File("data_10x/SC3_v3_NextGem_DI_PBMC_10K_filtered_feature_bc_matrix.h5", 'r')

#print(list(f.keys()))
dset3 = f2['matrix']
print(dset3["barcodes"][::])
print(len(dset3["data"][::]))
print(dset3["features"]["name"][::])
