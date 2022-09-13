## Use n equally spaced breaks to assign each value to n-1 equal sized bins 
#ii <- cut(values, breaks = seq(min(values), max(values), len = 100), 
#          include.lowest = TRUE)
### Use bin indices, ii, to select color from vector of n-1 equally spaced colors
#colors <- colorRampPalette(c("lightblue", "blue"))(99)[ii]#

### This call then also produces the plot below
#image(seq_along(values), 1, as.matrix(seq_along(values)), col = colors,
#      axes = F)

my_data <- read.delim("data/maize_leaf_harmony_integrated.v3.subLEIDEN.metadata.txt")
#print((my_data[, c("library")]))
library <- my_data[, c("library")]
umi <- my_data[, c("umi")]
S.score <- my_data[, c("S.Score")]
G2M.score <- my_data[, c("G2M.Score")]

cat(library,file="library.txt",sep="\n")
cat(umi,file="umi.txt",sep="\n")
cat(S.score,file="S.score.txt",sep="\n")
cat(G2M.score,file="G2M.score.txt",sep="\n")


#print((my_data[, c("umi")]))
#print((my_data[, c("S.Score")]))
#print((my_data[, c("G2M.Score")]))

