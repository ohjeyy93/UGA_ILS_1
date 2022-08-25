library(MASS)
library(Matrix)
library(reticulate)
np <- import("numpy")

# read rds 
sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_fixed.rds")
print(sce_10xPBMC_atac)