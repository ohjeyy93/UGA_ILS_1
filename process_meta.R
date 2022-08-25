#install.packages("tidyr", repos = "http://cran.us.r-project.org")
#BiocManager::install('htmlwidgets')
#install.packages("SeuratObject")
#BiocManager::install('SeuratObject')
#install.packages("rgeos", repos = "http://cran.us.r-project.org")
#install.packages("SeuratObject", repos = "http://cran.us.r-project.org")
#SeuratObject
#install.packages("SeuratObject_4.1.0.tar.gz", repos = NULL, type ="source")
library(tidyr)
#library(SeuratObject)
library(Matrix)


data <- read.table(file = "data/snRNA.raw.metadata.txt", header = TRUE)
#print(rownames(data))
#raw_ATAC <- readRDS("data/scATAC.raw.sparse.rds")
raw_RNA <- readRDS("data/snRNA.raw.sparse.rds")
#raw_RNA <- readRDS("data/snRNA.raw.sparse_fixed.rds")
raw_RNA <- raw_RNA[,colnames(raw_RNA) %in% rownames(data)]
saveRDS(raw_RNA, file = "data/snRNA.raw.sparse_referenced.rds")
#raw_RNA <- readRDS("data/snRNA.raw.sparse_fixed.rds")


data2 <- read.table(file = "data/maize_282.v8.3.scATAC_ALL_CELLs.metadata_reference.txt", header = TRUE)
#print(rownames(data))
raw_ATAC <- readRDS("data/scATAC.raw.sparse.rds")
#raw_ATAC <- readRDS("data/scATAC.raw.sparse.rds")
#S4ToList(raw_ATAC)
rownames(data2) <- data2[,1]
raw_ATAC <- raw_ATAC[,colnames(raw_ATAC) %in% rownames(data2)]
saveRDS(raw_ATAC, file = "data/scATAC.raw.sparse_referenced.rds")

#saveRDS(raw_RNA, file = "data/snRNA.raw.sparse_fixed.rds")
#raw_ATAC <- readRDS("data/snRNA.raw.sparse_fixed.rds")
#print(raw_ATAC)

#raw_RNA2 <- S4ToList(raw_RNA)
#print(raw_RNA2[2][0])
#print(raw_RNA2[4][1])
#print(length(raw_RNA2))
#print(raw_RNA2[1])

#print()
#print(length(colnames(raw_RNA)))
#print(length(rownames(raw_RNA)))
#lengths(raw_RNA2)
#dim(raw_RNA2)
#print(colnames(raw_RNA))
#print(rownames(raw_RNA))



#print((raw_RNA))

#as.data.frame(raw_RNA)

#typeof(data) 
#typeof(raw_RNA) 


#print(dim(raw_ATAC))
#print(dim(raw_RNA))

#print(colnames(data))
#print(data orig.ident)
#print(data$orig.ident)
#print(data[,0])
#print(rownames(data))

#print(as.data.frame(raw_RNA))

#raw_RNA <- raw_RNA[colnames(raw_RNA) %in% rownames(data)]

#saveRDS(raw_RNA, file = "data/snRNA.raw.sparse_fixed.rds")

#raw_RNA <- readRDS("data/snRNA.raw.sparse_fixed.rds")
#print(raw_RNA)


#######
#library(Matrix)

#data2 <- read.table(file = "data/maize_282.v8.3.celltype_metadata.scJoint.txt", header = TRUE)
#print(rownames(data))
#raw_ATAC <- readRDS("data/scATAC.raw.sparse.rds")
#raw_ATAC <- readRDS("data/scATAC.raw.sparse.rds")
#S4ToList(raw_ATAC)
#raw_ATAC <- raw_ATAC[,colnames(raw_ATAC) %in% rownames(data2)]
#saveRDS(raw_ATAC, file = "data/scATAC.raw.sparse_fixed.rds")

#raw_ATAC <- readRDS("data/snRNA.raw.sparse_fixed.rds")
#print(raw_ATAC)



#print()

#mask = raw_RNA.set_index(c).index.isin(data.set_index(c).index)


#if (class(raw_ATAC) == "matrix" | class(raw_ATAC) == "data.frame") {
#  size <- dim(raw_ATAC)
#} else {
#  size <- length(raw_ATAC)
#}

#size


#if (class(raw_RNA) == "matrix" | class(raw_RNA) == "data.frame") {
#  size <- dim(raw_RNA)
#} else {
#  size <- length(raw_RNA)
#}

#size


#DIM <- function( ... ){
#    args <- list(...)
#    lapply( args , function(x) { if( is.null( dim(x) ) )
#                                    return( length(x) )
#                                 dim(x) } )


#DIM(raw_ATAC,raw_RNA)


#raw_RNA %>% 
#  filter(rownames(raw_RNA) %in% rownames(data))

#b <- SingleCellExperiment(list(counts=a))