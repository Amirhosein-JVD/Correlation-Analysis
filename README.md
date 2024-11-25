#Effects of Spearman’s and Pearson’s correlations on construction of cancer regulatory networks and biomarker selection

In the paper, Cancer regulatory networks are constructed based on four correlation matrices and finally discovered that spearman correlation is the best choice for construction of cancer regulatory networks based on expression data. We notice the Spearman superiority from different aspects.
 
To download the initial data (expression data), open the “Data” folder:
1.	Download the Data
2.	Find the genes with significant differential expression
3.	Extract the expression of genes with differential expression from initial data for just tumor samples (initial genes of network)
Then calculate the correlation between initial genes of network by:
4.	“Correlation calculation “
Network construction implemented in “Network analysis:
5.	Define network edges and node degree by “Network_gene_degree”
6.	Sort nodes by their degree (“Sorting_degree”)
To find survival related genes
7.	“Survival analysis”
8.	 Find the intersect between hub genes and survival related genes by “find_intersect”
To find enriched terms for hub genes of each network, import the hub names to g profiler (https://biit.cs.ut.ee/gprofiler/) and then find the cancer related ones by :
9.	“Enrichment analysis”

To plot the figures in the paper, use functions in “Results & plots”
![image](https://github.com/user-attachments/assets/3588222d-308d-4a3e-8bd2-470e83414208)
