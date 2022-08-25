import numpy as np

#np.savez_compressed("sce_10xPBMC_atac_skip.npy"#, **array_dict)
loaded = np.load("sce_10xPBMC_rna_skip_referenced.npy", allow_pickle=True)
z = loaded.item()
print(z.shape[1])
print(z.shape[0])
loaded = np.load("sce_10xPBMC_atac_skip_referenced.npy", allow_pickle=True)
z = loaded.item()
print(z.shape[1])
print(z.shape[0])
#print(['indices', 'indptr', 'format', 'shape', 'data']