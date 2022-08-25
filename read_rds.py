import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
readRDS = robjects.r['readRDS']
df = readRDS('data10x/sce_10xPBMC_atac.rds')
df = pandas2ri.ri2py(df)
# do something with the dataframe