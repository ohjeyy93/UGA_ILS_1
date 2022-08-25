library(MASS)
library(Matrix)
library(reticulate)
np <- import("numpy")

# read rds 
sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_referenced.rds")
sce_10xPBMC_rna <- readRDS("data/snRNA.raw.sparse_referenced.rds")
common_genes <- intersect(rownames(sce_10xPBMC_atac),
                          rownames(sce_10xPBMC_rna))
length(common_genes)
# normalize and log transform counts
norm.cnts <- log1p((sce_10xPBMC_atac[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_atac[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
norm.cnts <- t(norm.cnts)
np$save("sce_10xPBMC_atac_skip_referenced.npy", norm.cnts)
norm.cnts <- log1p((sce_10xPBMC_rna[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_rna[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
norm.cnts <- t(norm.cnts)
np$save("sce_10xPBMC_rna_skip_referenced.npy", norm.cnts)
#summary(norm.cnts)
#display(norm.cnts) 
#np$savez("sce_10xPBMC_rna_skip.npz", norm.cnts)