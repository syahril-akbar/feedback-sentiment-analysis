from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

def kmeans_clustering(matrix, range_k=(2, 10)):
    """
    Jalankan K-Means clustering dan cari jumlah klaster optimal menggunakan Silhouette Score.
    """
    best_score = -1
    best_k = 2
    best_labels = []

    for k in range(*range_k):
        model = KMeans(n_clusters=k, random_state=42, n_init='auto')
        labels = model.fit_predict(matrix)
        score = silhouette_score(matrix, labels)
        if score > best_score:
            best_score = score
            best_k = k
            best_labels = labels

    print(f"Silhouette Score terbaik: {best_score:.4f} pada k = {best_k}")
    return best_labels, best_k
