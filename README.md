# **Effects of Spearman’s and Pearson’s Correlations on Construction of Cancer Regulatory Networks and Biomarker Selection**

In the paper, Cancer regulatory networks are constructed based on four correlation matrices and finally discovered that **Spearman correlation** is the best choice for construction of cancer regulatory networks based on expression data. We notice the **Spearman superiority** from different aspects.

---

## 📂 **To download the initial data (expression data), open the `Data` folder:**

1. 📥 **Download the Data**
2. 🧬 **Find the genes with significant differential expression**
3. 🔬 **Extract the expression of genes with differential expression** from initial data for just tumor samples (initial genes of network)

---

## 📊 **Then calculate the correlation between initial genes of network by:**

4. **`Correlation_Calculation`**

---

## 🕸️ **Network construction implemented in `Network_Analysis`:**

5. 🔗 **Define network edges and node degree** by **`network_genes_degree`**  
6. 📈 **Sort nodes by their degree** using **`sorting_degrees`**  
7. 🗂️ **Compare Gene Rankings Using Correlation Methods**:  
   In the **`rating.py`** file, the function **`rating`** generates output files in the form of **CSV files**,  
   where the **ranking of genes** is compared across two different correlation methods.

---

## 🩺 **To find survival related genes:**

8. ⚕️ **`Survival_Analysis`**  
9. 🔗 Find the intersect between hub genes and survival related genes by **`find_intersect`**

---

## 🧠 **To find enriched terms for hub genes of each network:**

1. 🌐 Import the hub names to **[g:Profiler](https://biit.cs.ut.ee/gprofiler/)**  
2. 🔬 Find the cancer-related ones using **`Enrichment_Analysis`**

---

## 🖼️ **To plot the figures in the paper, use functions in `Results & Plots`**
