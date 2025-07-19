import sys
import os
import pandas as pd
from modules import preprocessing, tfidf_vectorizer, clustering, sentiment_lexicon, evaluation, utils, visualization
import config

class Tee:
    """
    Sebuah objek file-like yang menulis output ke beberapa file sekaligus.
    """
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # Pastikan output langsung ditulis

    def flush(self):
        for f in self.files:
            f.flush()

def main():
    # Konfigurasi output
    log_dir = "output"
    log_file_path = os.path.join(log_dir, "laporan_akhir.txt")
    os.makedirs(log_dir, exist_ok=True)

    # Simpan stdout asli
    original_stdout = sys.stdout
    
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        # Alihkan stdout ke objek Tee yang akan menulis ke terminal dan file
        sys.stdout = Tee(original_stdout, log_file)

        try:
            print("="*50)
            print("ANALISIS CLUSTERING DAN SENTIMEN KRITIK & SARAN")
            print("="*50 + "\n")

            # [1] Muat & Pra-pemrosesan
            df = utils.load_data(config.DATA_PATH)
            df["teks_bersih"] = df["kritik dan saran"].apply(preprocessing.proses_teks)
            
            print("--- TAHAP 1: PREPROCESSING TEKS ---")
            print("Menampilkan 3 contoh hasil preprocessing:\n")
            for i in range(3):
                preprocessing.tampilkan_langkah_preprocessing(df["kritik dan saran"].iloc[i])
            
            # [2] Vektorisasi TF-IDF
            tfidf_matrix, feature_names, vectorizer = tfidf_vectorizer.ubah_ke_tfidf(df["teks_bersih"])
            print("\n--- TAHAP 2: TF-IDF VECTORIZATION ---")
            print(f"Teks telah diubah menjadi matriks TF-IDF dengan {tfidf_matrix.shape[1]} fitur unik.\n")

            # [3] Clustering K-Means
            kmeans_model, best_k, labels, silhouette_scores = clustering.kmeans_clustering(tfidf_matrix)
            df["klaster"] = labels
            print("--- TAHAP 3: CLUSTERING K-MEANS ---")
            print(f"Clustering selesai dengan k={best_k} (nilai k terbaik).")
            clustering.analisis_klaster(df, tfidf_matrix, kmeans_model, vectorizer)
            
            # [4] Analisis Sentimen & Makna
            lex_pos, lex_neg = sentiment_lexicon.load_lexicon(config.LEXICON_POS, config.LEXICON_NEG)
            # Terapkan fungsi dan gabungkan hasilnya ke DataFrame utama
            sentiment_results = df["teks_bersih"].apply(lambda teks: sentiment_lexicon.klasifikasi_sentimen(teks, lex_pos, lex_neg))
            df = pd.concat([df, sentiment_results], axis=1)
            
            df["makna"] = df["teks_bersih"].apply(sentiment_lexicon.cek_komentar_bermakna)
            df["skor_konstruktif"] = df["teks_bersih"].apply(sentiment_lexicon.analisis_konstruktif)

            print("\nContoh Komentar per Klaster:")
            visualization.contoh_komentar_per_klaster(df, n=10)

            print("\n--- TAHAP 4: ANALISIS SENTIMEN & MAKNA ---")
            visualization.tampilkan_analisis_sentimen_dan_makna(df)

            print("\n--- INFO DEBUG ---")
            print("Distribusi nilai pada kolom 'skor_konstruktif':")
            print(df['skor_konstruktif'].value_counts().sort_index())
            print("------------------\n")

            # [5] Evaluasi
            print("\n--- TAHAP 5: EVALUASI MODEL ---")
            print("Evaluasi performa klasifikasi Sentimen dan Makna berdasarkan data uji manual:")
            laporan_evaluasi = evaluation.evaluasi_manual(df, config.GROUND_TRUTH_PATH)
            print(laporan_evaluasi)

            print("\n--- INFO DEBUG ---")
            print("Distribusi nilai pada kolom 'makna':")
            print(df['makna'].value_counts())
            print("------------------\n")

            # [6] Simpan Hasil & Visualisasi
            utils.save_output(df, config.OUTPUT_PATH)
            utils.save_meaningful_comments(df, config.OUTPUT_MEANINGFUL_PATH)
            utils.save_constructive_comments(df, config.OUTPUT_CONSTRUCTIVE_PATH)
            visualization.visualisasi_semua(df)
            visualization.plot_silhouette_scores(silhouette_scores, best_k)
            visualization.tabel_statistik_per_klaster(df)
            
            print("\n--- TAHAP 6: PENYIMPANAN HASIL ---")
            print(f"-> Hasil analisis (CSV) telah disimpan di '{config.OUTPUT_PATH}'.")
            print(f"-> Komentar bermakna (CSV) telah disimpan di '{config.OUTPUT_MEANINGFUL_PATH}'.")
            print(f"-> Saran konstruktif (CSV) telah disimpan di '{config.OUTPUT_CONSTRUCTIVE_PATH}'.")
            print("-> Visualisasi (PNG) telah disimpan di folder 'output/'.")
            print(f"-> Word Cloud per klaster (PNG) telah disimpan di folder 'output/'.")
            print(f"-> Statistik per klaster (CSV) telah disimpan di 'output/statistik_per_klaster.csv'.")
            
            print("\n" + "="*50)
            print("ANALISIS SELESAI")
            print("="*50)

        finally:
            # Pastikan stdout dikembalikan ke kondisi semula meskipun terjadi error
            sys.stdout = original_stdout

    # Pesan terakhir ini hanya akan muncul di terminal
    print(f"\nLaporan analisis lengkap telah disimpan di: {log_file_path}")

if __name__ == "__main__":
    main()