library(TCGAbiolinks)
library(SummarizedExperiment)

# Download gene expression data
query.met.KIRC <- GDCquery(project = "TCGA-KIRC", 
                           legacy = TRUE,
                           data.category = "Gene expression",
                           data.type = "Gene expression quantification",
                           file.type = "rsem.genes.normalized_results"
)
GDCdownload(query.met.KIRC)

query.met.KIRC.2=query.met.KIRC
tmp=query.met.KIRC.2$results[[1]]
tmp=tmp[which(!duplicated(tmp$cases)),]
query.met.KIRC.2$results[[1]]=tmp

dataKIRC <- GDCprepare(query = query.met.KIRC.2,
                       save = TRUE, 
                       save.filename = "KIRC_genexpression.rda",
                       summarizedExperiment = TRUE)
                       
#------------------------------------------------------------------------------
# expression data
KIRC_expression <- assay(data)

# clinical data
clinical = data@colData



