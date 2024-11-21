# MY TCGA survival analysis
library("TCGAbiolinks")
library("SummarizedExperiment")
library("survival")
library("survminer")

load("~/KIRC_genexpression.rda")
tcga_data <- data

clinical = tcga_data@colData

clin_df = clinical[c("patient",
                     "vital_status",
                     "days_to_death",
                     "days_to_last_follow_up",
                     "gender"
                      )]

exp = rownames(clin_df)
# create a new boolean variable that has TRUE for dead patients
# and FALSE for live patients
clin_df$deceased = clin_df$vital_status == "Dead"

# create an "overall survival" variable that is equal to days_to_death
# for dead patients, and to days_to_last_follow_up for patients who
# are still alive
clin_df$overall_survival = ifelse(clin_df$deceased,
                                  clin_df$days_to_death,
                                  clin_df$days_to_last_follow_up)
# Select genes for survival analysis
top = read.csv("~/KIRC_diferentially expressed genes.csv")
exp = assay(tcga_data)

t = length(rownames(top))
surv_result = matrix(0,t,2)
for (i in 1:t){
  gene_name = top[i,1]
  gene_exps = exp [gene_name, ]
  median_value = median(gene_exps)
  clin_df$gene = ifelse(gene_exps >= median_value, "UP", "DOWN")
  
  # we can fit a survival model, like we did in the previous section
  fit = survfit(Surv(overall_survival, deceased) ~ gene, data=clin_df)
  
  # we can extract the survival p-value and print it
  pval = surv_pvalue(fit, data=clin_df)$pval
  surv_result [i,1] = gene_name
  surv_result [i,2] = pval
}
df[df$var1 == 'value1' & df$var2 > value2, ]

KIRC_survival = surv_result [surv_result $Pvalue < 0.05]

write.csv(surv_result,"~/KIRC_Survival.csv")