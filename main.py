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
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

def main():
    # Pastikan direktori output ada
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    log_file_path = os.path.join(config.OUTPUT_DIR, config.LOG_FILE)

    original_stdout = sys.stdout
    
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        sys.stdout = Tee(original_stdout, log_file)

        try:
            print("="*50)
            print("ANALISIS CLUSTERING DAN SENTIMEN KRITIK & SARAN")
            print("="*50 + "\n")

            # [1] Muat & Pra-pemrosesan
            df = utils.load_data(config.DATA_PATH)
            
            # --- Langkah Diagnostik ---
            print("Nama kolom yang terdeteksi dalam file:", list(df.columns))
            
            if config.TARGET_COLUMN not in df.columns:
                print(f"\n[ERROR] Kolom '{config.TARGET_COLUMN}' tidak ditemukan dalam file data.")
                print("Pastikan nama kolom di file Excel atau di config.py sudah benar.")
                sys.exit(1)
            # --- Akhir Langkah Diagnostik ---

            df["teks_bersih"] = df[config.TARGET_COLUMN].apply(preprocessing.proses_teks)
            
            print("\n--- TAHAP 1: PREPROCESSING TEKS ---")
            print(f"Menampilkan {config.N_PREPROCESSING_EXAMPLES} contoh hasil preprocessing:\n")
            for i in range(min(config.N_PREPROCESSING_EXAMPLES, len(df))): # Pastikan tidak error jika data < contoh
                preprocessing.tampilkan_langkah_preprocessing(df[config.TARGET_COLUMN].iloc[i])
            
            # [2] Vektorisasi TF-IDF
            tfidf_matrix, feature_names, vectorizer = tfidf_vectorizer.ubah_ke_tfidf(df["teks_bersih"])
            print("\n--- TAHAP 2: TF-IDF VECTORIZATION ---")
            print(f"Teks telah diubah menjadi matriks TF-IDF dengan {tfidf_matrix.shape[1]} fitur unik.\n")

            # [3] Clustering K-Means
            kmeans_model, best_k, labels, silhouette_scores = clustering.kmeans_clustering(tfidf_matrix, range_k=config.K_RANGE)
            df["klaster"] = labels
            print("--- TAHAP 3: CLUSTERING K-MEANS ---")
            print(f"Clustering selesai dengan k={best_k} (nilai k terbaik).")
            top_keywords = clustering.analisis_klaster(df, tfidf_matrix, kmeans_model, vectorizer, n_top_words=config.N_TOP_WORDS)
            
            df['top_keywords'] = df['klaster'].map(lambda x: ', '.join(top_keywords.get(x, [])))

            # [4] Analisis Sentimen & Makna
            lex_pos, lex_neg = sentiment_lexicon.load_lexicon(config.LEXICON_POS, config.LEXICON_NEG)
            sentiment_results = df["teks_bersih"].apply(lambda teks: sentiment_lexicon.klasifikasi_sentimen(teks, lex_pos, lex_neg))
            df = pd.concat([df, sentiment_results], axis=1)
            
            df["makna"] = df["teks_bersih"].apply(sentiment_lexicon.cek_komentar_bermakna)
            df["skor_konstruktif"] = df["teks_bersih"].apply(sentiment_lexicon.analisis_konstruktif)

            print("\n--- TAHAP 4: ANALISIS SENTIMEN & MAKNA ---")
            visualization.tampilkan_analisis_sentimen_dan_makna(df)

            # [5] Evaluasi
            print("\n--- TAHAP 5: EVALUASI MODEL ---")
            print("Evaluasi performa klasifikasi Sentimen dan Makna berdasarkan data uji manual:")
            laporan_evaluasi = evaluation.evaluasi_manual(df, config.GROUND_TRUTH_PATH)
            print(laporan_evaluasi)

            # [6] Simpan Hasil & Visualisasi
            print("\n--- TAHAP 6: PENYIMPANAN HASIL & VISUALISASI ---")
            
            # Menggunakan path dari config untuk menyimpan semua output
            output_dir = config.OUTPUT_DIR
            utils.save_output(df, os.path.join(output_dir, config.OUTPUT_CSV))
            utils.save_meaningful_comments(df, os.path.join(output_dir, config.OUTPUT_MEANINGFUL_CSV))
            utils.save_constructive_comments(df, os.path.join(output_dir, config.OUTPUT_CONSTRUCTIVE_CSV), threshold=config.CONSTRUCTIVE_THRESHOLD)
            visualization.tabel_statistik_per_klaster(df) # Fungsi ini sudah menyimpan ke path yang benar
            visualization.contoh_komentar_per_klaster(df, n=config.N_EXAMPLE_COMMENTS) # Fungsi ini juga
            
            visualization.visualisasi_semua(df, tfidf_matrix)
            visualization.plot_silhouette_scores(silhouette_scores, best_k)
            
            print(f"\n-> Hasil analisis lengkap (CSV) telah disimpan di '{os.path.join(output_dir, config.OUTPUT_CSV)}'.")
            print(f"-> Komentar bermakna (CSV) telah disimpan di '{os.path.join(output_dir, config.OUTPUT_MEANINGFUL_CSV)}'.")
            print(f"-> Saran konstruktif (CSV) telah disimpan di '{os.path.join(output_dir, config.OUTPUT_CONSTRUCTIVE_CSV)}'.")
            print(f"-> Statistik per klaster (CSV) telah disimpan di '{os.path.join(output_dir, config.OUTPUT_STATS_CSV)}'.")
            print(f"-> Contoh komentar per klaster (TXT) telah disimpan di '{os.path.join(output_dir, config.OUTPUT_COMMENTS_TXT)}'.")
            print(f"-> Semua visualisasi (PNG) telah disimpan di folder '{output_dir}/'.")
            
            print("\n" + "="*50)
            print("ANALISIS SELESAI")
            print("="*50)

        finally:
            sys.stdout = original_stdout

    print(f"\nLaporan analisis lengkap telah disimpan di: {log_file_path}")

if __name__ == "__main__":
    main()