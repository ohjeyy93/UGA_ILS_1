library(MASS)
library(Matrix)
library(reticulate)
library(data.table)
#library(readr)

sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_referenced.rds")
sce_10xPBMC_rna <- readRDS("data/snRNA.raw.sparse_right_path.rds")
common_genes <- intersect(rownames(sce_10xPBMC_atac),
                          rownames(sce_10xPBMC_rna))
length(common_genes)
# normalize and log transform counts
norm.cnts <- log1p((sce_10xPBMC_atac[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_atac[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
norm.cnts <- t(norm.cnts)
norm.cnts <- norm.cnts[c(x4),]
cat(rownames(norm.cnts),file="ran_gen_x4_rows.txt",sep="\n")
np$save("sce_10xPBMC_atac_skip_referenced_random_new_corrected.npy", norm.cnts)
dim(norm.cnts)
#x4 <- sample(0:82283, 30305, replace=T)
#norm.cnts[norm.cnts$fct %in% vc,]
norm.cnts <- log1p((sce_10xPBMC_rna[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_rna[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
norm.cnts <- t(norm.cnts)
dim(norm.cnts)
#dim(norm.cnts)
np$save("sce_10xPBMC_rna_skip_referenced_random__new_corrected.npy", norm.cnts)

#print(x4)