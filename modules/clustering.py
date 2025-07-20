from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
import config

def kmeans_clustering(matrix, range_k=(2, 11)):
    """
    Jalankan K-Means clustering dan cari jumlah klaster optimal menggunakan Silhouette Score.
    Mengembalikan model K-Means terbaik, jumlah klaster (k), label, dan skor siluet untuk setiap k.
    NOTE: range_k sebaiknya diatur dari file config.py melalui main.py.
    """
    best_score = -1
    best_k = 2
    best_model = None
    silhouette_scores = {}

    for k in range(*range_k):
        # Gunakan n_init='auto' untuk versi scikit-learn yang lebih baru
        model = KMeans(n_clusters=k, random_state=config.RANDOM_SEED, n_init='auto')
        model.fit(matrix)
        labels = model.labels_
        
        # Hindari galat silhouette_score dengan 1 klaster
        if len(np.unique(labels)) < 2:
            silhouette_scores[k] = -1 # Atau nilai penalti lain
            continue
            
        score = silhouette_score(matrix, labels)
        silhouette_scores[k] = score
        
        if score > best_score:
            best_score = score
            best_k = k
            best_model = model

    if best_model:
        return best_model, best_k, best_model.labels_, silhouette_scores
    else:
        # Opsi mundur jika tidak ada model yang valid ditemukan
        model = KMeans(n_clusters=2, random_state=config.RANDOM_SEED, n_init='auto')
        model.fit(matrix)
        # Hitung skor siluet untuk model mundur
        fallback_labels = model.labels_
        fallback_score = silhouette_score(matrix, fallback_labels) if len(np.unique(fallback_labels)) > 1 else -1
        silhouette_scores[2] = fallback_score
        return model, 2, fallback_labels, silhouette_scores

def get_top_keywords_per_cluster(kmeans_model, vectorizer, n_top_words):
    """
    Mendapatkan kata kunci paling representatif untuk setiap klaster berdasarkan centroid.
    Ini adalah metode standar untuk menginterpretasikan topik dari sebuah klaster.

    Args:
        kmeans_model: Model KMeans yang sudah dilatih.
        vectorizer: TfidfVectorizer yang sudah dilatih.
        n_top_words (int): Jumlah kata kunci yang ingin diambil per klaster.

    Returns:
        dict: Dictionary dengan kunci cluster_id dan nilai berupa list kata kunci.
    """
    keywords = {}
    terms = vectorizer.get_feature_names_out()
    
    # Tidak perlu mengurutkan semua centroid, cukup gunakan np.argpartition
    # untuk efisiensi pada kosakata yang besar.
    for i in range(kmeans_model.n_clusters):
        # Ambil centroid untuk klaster i
        centroid_vector = kmeans_model.cluster_centers_[i]
        # Dapatkan indeks dari n skor teratas
        top_indices = np.argpartition(centroid_vector, -n_top_words)[-n_top_words:]
        # Urutkan hanya n skor teratas tersebut
        sorted_top_indices = top_indices[np.argsort(centroid_vector[top_indices])][::-1]
        # Ambil nama kata dari indeks
        top_words = [terms[idx] for idx in sorted_top_indices]
        keywords[i] = top_words
        
    return keywords

def analisis_klaster(df, tfidf_matrix, kmeans_model, vectorizer, n_top_words):
    """
    Menganalisis dan menampilkan hasil clustering K-Means.
    Fungsi ini sekarang menggunakan model KMeans untuk mendapatkan kata kunci
    dari centroid, yang merupakan representasi inti dari setiap klaster.
    Mengembalikan kamus kata kunci teratas per klaster.
    """
    # a. Melaporkan nilai Silhouette Score
    silhouette_avg = silhouette_score(tfidf_matrix, df['klaster'])
    print(f"Nilai Silhouette Score: {silhouette_avg:.3f}\n")

    # b. Menampilkan distribusi komentar per klaster
    print("Distribusi Komentar per Klaster:")
    print(df['klaster'].value_counts().sort_index().to_string())

    # c. Mengidentifikasi dan menampilkan kata-kata kunci utama per klaster
    print(f"\nKata Kunci Utama per Klaster (Top {n_top_words}):")
    
    # Menggunakan fungsi baru untuk mendapatkan kata kunci dari centroid
    top_keywords = get_top_keywords_per_cluster(kmeans_model, vectorizer, n_top_words=n_top_words)
    
    for cluster_id, keywords in top_keywords.items():
        print(f"  - Klaster {cluster_id}: {', '.join(keywords)}")

    return top_keywords

