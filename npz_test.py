import numpy as np
test1=np.load('data/exprs_10xPBMC_rna.npz')
print(test1.files)
#print(test1)
print((test1['shape']))
test2=np.load('data/exprs_10xPBMC_atac.npz')
#print(test2.files)
print((test2['shape']))
#print(test2)