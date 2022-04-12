import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('rfm-model.csv')

kmodels = KMeans(n_clusters=4)

for col in data.columns:
    kmodels.fit(data[[col]])
    print(col)
    centers = kmodels.cluster_centers_
    for centroid in centers:
        print(centroid[0])