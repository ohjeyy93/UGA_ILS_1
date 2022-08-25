from numpy import load

data = load('data/maize_snRNA.logcounts.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])