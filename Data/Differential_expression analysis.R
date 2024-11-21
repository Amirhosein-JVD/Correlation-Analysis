library(TCGAbiolinks)
library(SummarizedExperiment)

#--------------------------
load(file = "~/KIRC_genexpression.rda")
dataKIRC <- data

# normalization of genes
dataNorm <- TCGAanalyze_Normalization(tabDF = dataKIRC , geneInfo =  geneInfo)

write.csv(dataNorm,file="~/KIRC_NormalyzedGeneExp.csv")

# selection of normal samples "NT"
samplesNT <- TCGAquery_SampleTypes(barcode = colnames(dataNorm),
                                   typesample = c("NT"))

# selection of tumor samples "TP"
samplesTP <- TCGAquery_SampleTypes(barcode = colnames(dataNorm), 
                                   typesample = c("TP"))

# Diffenetial expression analysis (DEA)
dataDEGs <- TCGAanalyze_DEA(mat1 = dataNorm[,samplesNT],
                            mat2 = dataNorm[,samplesTP],
                            Cond1type = "Normal",
                            Cond2type = "Tumor",
                            fdr.cut = 0.05,
                            logFC.cut = 1.5,
                            method = "glmLRT"
)
write.csv(dataDEGs,file="~/KIRC_diferentially expressed genes.csv")



