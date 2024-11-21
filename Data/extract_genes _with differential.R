library(SummarizedExperiment)
library(dplyr)

load("~/KIRC_genexpression.rda")
differential_res <- read.csv("~/STAD_diferentially expressed genes.csv")

KIRC <- data
KIRC_expression <- assay(data)

#Select tumor samples for the rest of analysis
tumorsamples <- KIRC_expression[ which(data$definition == "Primary solid Tumor")]
KIRC_1 <- tumorsamples[which(row.names(tumorsamples)  %in% differential_res$X),]

write.csv(KIRC_1, file = "~/STAD_tumor_diff_expression.csv",row.names = 1)

       
