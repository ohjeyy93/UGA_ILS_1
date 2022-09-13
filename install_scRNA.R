library(MASS)
library(Matrix)
library(reticulate)
library(data.table)
scATAC_ours <- readRDS("data/scATAC.raw.sparse_referenced.rds")
scRNA_ours <- readRDS("data/snRNA.raw.sparse_right_path.rds")
scATAC_theirs <- readRDS("sce_10xPBMC_atac.rds")
scRNA_theirs <- readRDS("sce_10xPBMC_rna.rds")

library(SingleCellExperiment)
library(DropletUtils)
library(scater)
library(ggplot2)

my_data = read.table("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata.txt")
meta_data.matrix <- as.matrix(my_data)
#print(dim(meta_data.matrix))




norm.cnts <- log1p(scRNA_ours %*% Diagonal(x=1e4/Matrix::colSums(scRNA_ours)))
cell_type_label <- meta_data.matrix[, c("celltype_full")]
#pretend.cell.labels <- sample(cell_type_label, ncol(scRNA_ours), replace=TRUE)
V <- as.list(as.data.frame(cell_type_label))
#b <- SingleCellExperiment(list(counts=scRNA_ours, logcounts=norm.cnts), colData=DataFrame(cell_type=V))

norm.cnts <- log1p(scRNA_ours %*% Diagonal(x=1e4/Matrix::colSums(scRNA_ours)))
#cell_type_label <- meta_data.matrix[, c("celltype_full")]
#pretend.cell.labels <- sample(cell_type_label, ncol(scRNA_ours), replace=TRUE)
b <- SingleCellExperiment(list(counts=scRNA_ours, logcounts=norm.cnts), colData=DataFrame(V))

pca_data <- prcomp(t(logcounts(b)), rank=20)

library(Rtsne)
set.seed(5252)
tsne_data <- Rtsne(pca_data$x[,1:50], pca = FALSE)