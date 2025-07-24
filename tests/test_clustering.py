import pytest
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from modules.clustering import kmeans_clustering, get_top_keywords_per_cluster, analisis_klaster
import config

# Contoh data untuk pengujian dalam Bahasa Indonesia
corpus_indonesia = [
    'ilmu data itu menyenangkan',
    'pembelajaran mesin itu menarik',
    'analisis data itu penting',
    'pembelajaran mendalam adalah bagian dari pembelajaran mesin',
    'saya suka ilmu data'
]

@pytest.fixture(scope="module")
def data_contoh():
    """Fixture untuk membuat matriks TF-IDF dan vectorizer dari data contoh."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus_indonesia)
    # Ubah ke array padat untuk clustering
    tfidf_matrix_dense = tfidf_matrix.toarray()
    
    # Pastikan matriks memiliki cukup sampel untuk pengujian clustering
    if tfidf_matrix_dense.shape[0] < 2:
        # Tambahkan data dummy jika korpus terlalu kecil
        dummy_matrix = np.zeros((2 - tfidf_matrix_dense.shape[0], tfidf_matrix_dense.shape[1]))
        tfidf_matrix_dense = np.vstack([tfidf_matrix_dense, dummy_matrix])

    return tfidf_matrix_dense, vectorizer

def test_kmeans_clustering_tipe_kembalian(data_contoh):
    """Menguji tipe data yang dikembalikan oleh fungsi kmeans_clustering."""
    matriks, _ = data_contoh
    if matriks.shape[0] < 2:
        pytest.skip("Sampel tidak cukup untuk clustering")
        
    model, k, labels, scores = kmeans_clustering(matriks, range_k=(2, 4))
    
    assert isinstance(model, KMeans)
    assert isinstance(k, int)
    assert isinstance(labels, np.ndarray)
    assert isinstance(scores, dict)
    assert k >= 2

def test_kmeans_clustering_range_k(data_contoh):
    """Menguji bahwa kmeans_clustering mematuhi parameter range_k."""
    matriks, _ = data_contoh
    if matriks.shape[0] < 2:
        pytest.skip("Sampel tidak cukup untuk clustering")

    _, k, _, scores = kmeans_clustering(matriks, range_k=(3, 5))
    
    assert k >= 3 and k < 5
    assert all(key >= 3 and key < 5 for key in scores.keys())

def test_get_top_keywords_per_cluster(data_contoh):
    """Menguji fungsi get_top_keywords_per_cluster."""
    matriks, vectorizer = data_contoh
    if matriks.shape[0] < 2:
        pytest.skip("Sampel tidak cukup untuk clustering")

    model, _, _, _ = kmeans_clustering(matriks, range_k=(2, 3))
    n_top_words = 3
    keywords = get_top_keywords_per_cluster(model, vectorizer, n_top_words)
    
    assert isinstance(keywords, dict)
    assert len(keywords) == model.n_clusters
    for cluster_id, words in keywords.items():
        assert isinstance(words, list)
        assert len(words) <= n_top_words
        assert all(isinstance(word, str) for word in words)

def test_analisis_klaster_berjalan_tanpa_error(data_contoh, capsys):
    """Menguji bahwa analisis_klaster berjalan tanpa menimbulkan eksepsi."""
    matriks, vectorizer = data_contoh
    if matriks.shape[0] < 2:
        pytest.skip("Sampel tidak cukup untuk clustering")

    model, k, labels, _ = kmeans_clustering(matriks, range_k=(2, 3))
    
    df = pd.DataFrame({'komentar': corpus_indonesia})
    df['klaster'] = labels
    
    n_top_words = 2
    
    try:
        top_keywords = analisis_klaster(df, matriks, model, vectorizer, n_top_words)
        captured = capsys.readouterr()
        
        assert "Nilai Silhouette Score" in captured.out
        assert "Distribusi Komentar per Klaster" in captured.out
        assert f"Kata Kunci Utama per Klaster (Top {n_top_words})" in captured.out
        assert isinstance(top_keywords, dict)

    except Exception as e:
        pytest.fail(f"analisis_klaster menimbulkan eksepsi: {e}")

def test_kmeans_clustering_skenario_satu_klaster():
    """
    Menguji kmeans_clustering dengan data yang kemungkinan besar membentuk satu klaster.
    Fungsi harus menangani ini dengan baik dengan memberikan skor penalti.
    """
    # Buat matriks di mana semua titik sangat berdekatan
    matriks = np.array([
        [1, 1, 1],
        [1, 1, 1.01],
        [1, 1, 1.02],
        [10, 10, 10], # Outlier untuk memastikan lebih dari satu klaster dapat terbentuk
        [10, 10, 10.01]
    ])
    
    try:
        model, k, labels, scores = kmeans_clustering(matriks, range_k=(2, 4))
        assert model is not None
        assert k is not None
        assert labels is not None
        assert scores is not None
    except ValueError as e:
        pytest.fail(f"kmeans_clustering gagal dengan ValueError: {e}")

def test_get_top_keywords_klaster_kosong(data_contoh):
    """
    Menguji get_top_keywords_per_cluster dengan model yang mungkin memiliki klaster kosong.
    Meskipun KMeans dari sklearn biasanya tidak menghasilkan klaster kosong, ini menguji ketahanan.
    """
    matriks, vectorizer = data_contoh
    if matriks.shape[0] < 2:
        pytest.skip("Sampel tidak cukup untuk clustering")

    model = KMeans(n_clusters=2, random_state=config.RANDOM_SEED, n_init='auto')
    model.fit(matriks)

    # Buat skenario manual dengan centroid "nol", mensimulasikan klaster kosong.
    model.cluster_centers_[1] = np.zeros_like(model.cluster_centers_[1])

    n_top_words = 3
    keywords = get_top_keywords_per_cluster(model, vectorizer, n_top_words)

    assert isinstance(keywords, dict)
    assert len(keywords) == model.n_clusters
    assert len(keywords[1]) <= n_top_words
