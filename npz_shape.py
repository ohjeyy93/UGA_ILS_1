import numpy as np
import zipfile
import scipy.sparse


def npz_headers(npz):
    """
    Takes a path to an .npz file, which is a Zip archive of .npy files.
    Generates a sequence of (name, shape, np.dtype).
    """
    with zipfile.ZipFile(npz) as archive:
        for name in archive.namelist():
            if not name.endswith('.npy'):
                continue

            npy = archive.open(name)
            version = np.lib.format.read_magic(npy)
            shape, fortran, dtype = np.lib.format._read_array_header(npy, version)
            yield name[:-4], shape, dtype


#print(list(npz_headers("atac.npz")))

#load it
data = np.load("data/asapseq_control_atac.npz")

for key in data.keys():
    print("variable name:", key          , end="  ")
    print("type: "+ str(data[key].dtype) , end="  ")
    print("shape:"+ str(data[key].shape))


data = np.load("data/citeseq_control_rna.npz")

for key in data.keys():
    print("variable name:", key          , end="  ")
    print("type: "+ str(data[key].dtype) , end="  ")
    print("shape:"+ str(data[key].shape))





data = np.load("rna.npz")

for key in data.keys():
    print("variable name:", key          , end="  ")
    print("type: "+ str(data[key].dtype) , end="  ")
    print("shape:"+ str(data[key].shape))


#data = np.load("atac.npz")

#for key in data.keys():
#    print("variable name:", key          , end="  ")
#    print("type: "+ str(data[key].dtype) , end="  ")
#    print("shape:"+ str(data[key].shape))



#data=np.transpose(data)
#sparse_data = scipy.sparse.csr_matrix(data)
#scipy.sparse.save_npz("atac_transposed.npz", sparse_data)

#np.savez(data, "atac_transposed.npz")