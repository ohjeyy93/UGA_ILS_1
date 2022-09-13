library(MASS)
library(Matrix)
library(reticulate)
np <- import("numpy")

# read rds 
#sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_fixed.rds")
#print(sce_10xPBMC_atac)
sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_referenced.rds")
sce_10xPBMC_rna <- readRDS("data/snRNA.raw.sparse_referenced.rds")
print(sce_10xPBMC_rna)