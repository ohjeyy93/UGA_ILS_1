import numpy as np
import scipy.sparse
import h5py
import sys
import os
import pandas as pd
import seaborn as sns

h5_atac = h5py.File("data/asapseq_control_atac.h5", 'r')
h5_rna = h5py.File("data/citeseq_control_rna.h5", 'r')
dset_atac = h5_atac['matrix']
dset_rna = h5_rna['matrix']
dset_atac["data"][::]

df_atac = pd.DataFrame(np.array(h5_atac['matrix/data']))
df_atac.columns =h5_atac['matrix/barcodes']
df_atac.rows = h5_atac['matrix/features']

df_rna = pd.DataFrame(np.array(h5_rna['matrix/data']))
df_rna.columns =h5_rna['matrix/barcodes']
df_rna.rows = h5_rna['matrix/features']

corrMatrix = df_atac.corr()
print (corrMatrix)
#pvf_atac=pd.pivot_table(df_atac)
#pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
#sns.heatmap(pvf_atac)

#print(dset_atac["data"][::])

#print(h5_data_atac)