import h5py

with h5py.File('data/maize_snRNA.logcounts2.h5','w') as f_dest:
    with h5py.File('/scratch/apm25309/share/Je_Hoon/maize_snRNA.logcounts.h5','r') as f_src:
            f_src.copy(f_src,f_dest,"Dataset")