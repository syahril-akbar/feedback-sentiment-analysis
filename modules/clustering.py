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

    return best_labels, best_k

def analisis_klaster(df, tfidf_matrix, vectorizer, feature_names):
    """
    Menganalisis dan menampilkan hasil clustering K-Means.
    """
    # a. Melaporkan nilai Silhouette Score
    silhouette_avg = silhouette_score(tfidf_matrix, df['klaster'])
    print(f"Nilai Silhouette Score: {silhouette_avg:.3f}\n")

    # b. Menampilkan distribusi komentar per klaster
    print("Distribusi Komentar per Klaster:")
    print(df['klaster'].value_counts().sort_index().to_string())

    # c. Mengidentifikasi dan menampilkan kata-kata kunci utama per klaster
    print("\nKata Kunci Utama per Klaster (Top 5):")
    for cluster_id in sorted(df['klaster'].unique()):
        cluster_comments = df[df['klaster'] == cluster_id]['teks_bersih']
        if not cluster_comments.empty:
            cluster_tfidf_matrix = vectorizer.transform(cluster_comments)
            sum_tfidf = cluster_tfidf_matrix.sum(axis=0)
            tfidf_scores = [(feature_names[i], sum_tfidf[0, i]) for i in range(len(feature_names))]
            sorted_tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
            top_keywords = [word for word, score in sorted_tfidf_scores[:5]]
            print(f"  - Klaster {cluster_id}: {', '.join(top_keywords)}")
