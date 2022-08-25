library(MASS)
library(Matrix)
library(reticulate)

np <- import("numpy")
npz1 <- np$load("sce_10xPBMC_rna_skip.npz")
npz1$files
npz1$files["arr_0"]
