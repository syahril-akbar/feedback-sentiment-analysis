from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

def kmeans_clustering(matrix, range_k=(2, 10)):
    """
    Jalankan K-Means clustering dan cari jumlah klaster optimal menggunakan Silhouette Score.
    Mengembalikan model K-Means terbaik, jumlah klaster (k), dan label untuk setiap data.
    """
    best_score = -1
    best_k = 2
    best_model = None

    for k in range(*range_k):
        # Gunakan n_init='auto' untuk versi scikit-learn yang lebih baru
        model = KMeans(n_clusters=k, random_state=42, n_init='auto')
        model.fit(matrix)
        labels = model.labels_
        
        # Hindari error silhouette_score dengan 1 cluster
        if len(np.unique(labels)) < 2:
            continue
            
        score = silhouette_score(matrix, labels)
        
        if score > best_score:
            best_score = score
            best_k = k
            best_model = model

    if best_model:
        return best_model, best_k, best_model.labels_
    else:
        # Fallback jika tidak ada model yang valid ditemukan (kasus langka)
        # Latih model dengan k=2 sebagai default
        model = KMeans(n_clusters=2, random_state=42, n_init='auto')
        model.fit(matrix)
        return model, 2, model.labels_

def get_top_keywords_per_cluster(kmeans_model, vectorizer, n_top_words=15):
    """
    Mendapatkan kata kunci paling representatif untuk setiap cluster berdasarkan centroid.
    Ini adalah metode standar untuk menginterpretasikan topik dari sebuah cluster.

    Args:
        kmeans_model: Model KMeans yang sudah dilatih.
        vectorizer: TfidfVectorizer yang sudah dilatih.
        n_top_words (int): Jumlah kata kunci yang ingin diambil per cluster.

    Returns:
        dict: Dictionary dengan key cluster_id dan value berupa list kata kunci.
    """
    keywords = {}
    terms = vectorizer.get_feature_names_out()
    
    # Tidak perlu mengurutkan semua centroid, cukup gunakan np.argpartition
    # untuk efisiensi pada vocabulary yang besar.
    for i in range(kmeans_model.n_clusters):
        # Ambil centroid untuk cluster i
        centroid_vector = kmeans_model.cluster_centers_[i]
        # Dapatkan indeks dari n skor teratas
        top_indices = np.argpartition(centroid_vector, -n_top_words)[-n_top_words:]
        # Urutkan hanya n skor teratas tersebut
        sorted_top_indices = top_indices[np.argsort(centroid_vector[top_indices])][::-1]
        # Ambil nama kata dari indeks
        top_words = [terms[idx] for idx in sorted_top_indices]
        keywords[i] = top_words
        
    return keywords

def analisis_klaster(df, tfidf_matrix, kmeans_model, vectorizer):
    """
    Menganalisis dan menampilkan hasil clustering K-Means.
    Fungsi ini sekarang menggunakan model KMeans untuk mendapatkan kata kunci
    dari centroid, yang merupakan representasi inti dari setiap cluster.
    """
    # a. Melaporkan nilai Silhouette Score
    silhouette_avg = silhouette_score(tfidf_matrix, df['klaster'])
    print(f"Nilai Silhouette Score: {silhouette_avg:.3f}\n")

    # b. Menampilkan distribusi komentar per klaster
    print("Distribusi Komentar per Klaster:")
    print(df['klaster'].value_counts().sort_index().to_string())

    # c. Mengidentifikasi dan menampilkan kata-kata kunci utama per klaster
    print("\nKata Kunci Utama per Klaster (Top 15):")
    
    # Menggunakan fungsi baru untuk mendapatkan kata kunci dari centroid
    top_keywords = get_top_keywords_per_cluster(kmeans_model, vectorizer, n_top_words=15)
    
    for cluster_id, keywords in top_keywords.items():
        print(f"  - Klaster {cluster_id}: {', '.join(keywords)}")
