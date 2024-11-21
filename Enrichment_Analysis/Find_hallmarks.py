# Enriched data were extracted by g profiler
# The paper enriched terms are present in supplementary

import pandas as pd

enrich_data = pd.read_csv("~/KIRC_enrich_data.csv")
hallmarks = pd.read_csv("~/GO_hallmarks.csv")

intersect = pd.merge(hallmarks, enrich_data,how='inner', on='term_id')

intersect.to_csv("~/KIRC_hallmarks.csv", index = False)