library(MASS)
library(Matrix)
library(reticulate)
library(data.table)
#library(readr)
set.seed(1) 

np <- import("numpy")

# read txt
#x4 <- sample(0:82283, 30305, replace=T)
x4 <- sample(0:30305, 10000, replace=T)

#my_data <- read.delim("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed.txt")
#my_data <- my_data[c(x4),]
#print(x4)
cat(x4,file="ran_gen_x4_num.txt",sep="\n")
#print(my_data[30577])
#writeLines(my_data, "output.txt")

#y4 <- sample(0:34408, 16000, replace=T)

#my_data <- read.delim("data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed.txt")
#my_data <- my_data[c(x4),]
#print(x4)

#cat(y4,file="ran_gen_x4_num_row.txt",sep="\n")

#print(my_data[30577])
#writeLines(my_data, "output.txt")

#print(my_data)
#write(my_data, file = "data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed_random.txt")
#cat(my_data, sep = "\n", file = "data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference_fixed_random.txt")
# read rds 
sce_10xPBMC_atac <- readRDS("data/scATAC.raw.sparse_referenced.rds")
sce_10xPBMC_rna <- readRDS("data/snRNA.raw.sparse_right_path.rds")
common_genes <- intersect(rownames(sce_10xPBMC_atac),
                          rownames(sce_10xPBMC_rna))
length(common_genes)
# normalize and log transform counts
norm.cnts <- log1p((sce_10xPBMC_atac[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_atac[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
#norm.cnts <- t(norm.cnts)
exprs_atac <- norm.cnts[,c(x4)]
#exprs_atac <- norm.cnts[c(y4),]
exprs_atac
#cat(rownames(norm.cnts),file="ran_gen_x4_rows.txt",sep="\n")
#np$save("sce_10xPBMC_atac_skip_referenced_random_new_corrected_features.npy", norm.cnts)
#dim(norm.cnts)
#x4 <- sample(0:82283, 30305, replace=T)
#norm.cnts[norm.cnts$fct %in% vc,]
norm.cnts <- log1p((sce_10xPBMC_rna[common_genes, ]) %*% Diagonal(x=1e4/Matrix::colSums(sce_10xPBMC_rna[common_genes, ])))
#csc_matrix <- r_to_py(norm.cnts)
#norm.cnts <- t(norm.cnts)
exprs_rna <- norm.cnts[,c(x4)]
#exprs_rna
#exprs_rna <- norm.cnts[c(y4),]
#exprs_rna
#dim(norm.cnts)
#dim(norm.cnts)
#np$save("sce_10xPBMC_rna_skip_referenced_random__new_corrected_features.npy", norm.cnts)
#source("data_to_h5.R")
#write_h5_scJoint(exprs_list = list(rna = exprs_rna,
#                                   atac = exprs_atac), 
#                 h5file_list = c("data_10x/exprs_10xPBMC_rna_features2.h5", 
#                                 "data_10x/exprs_10xPBMC_atac_features2.h5"))
#write_csv_scJoint(cellType_list =  list(rna = sce_10xPBMC_rna$cellTypes),
#                  csv_list = c("data_10x/cellType_10xPBMC_rna.csv"))
#print(x4)