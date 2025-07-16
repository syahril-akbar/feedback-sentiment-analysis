import sys
import os
from modules import preprocessing, tfidf_vectorizer, clustering, sentiment_lexicon, evaluation, utils, visualization
import config

def main():
    # Konfigurasi output
    log_dir = "output"
    log_file_path = os.path.join(log_dir, "laporan_akhir.txt")
    os.makedirs(log_dir, exist_ok=True)

    # Redirect stdout to log file
    with open(log_file_path, "w", encoding="utf-8") as f:
        old_stdout = sys.stdout
        sys.stdout = f

        print("="*50)
        print("ANALISIS CLUSTERING DAN SENTIMEN KRITIK & SARAN")
        print("="*50 + "\n")

        # [1] Load & Preprocess
        df = utils.load_data(config.DATA_PATH)
        df["teks_bersih"] = df["kritik dan saran"].apply(preprocessing.proses_teks)
        
        print("--- TAHAP 1: PREPROCESSING TEKS ---")
        print("Menampilkan 3 contoh hasil preprocessing:\n")
        for i in range(3):
            preprocessing.tampilkan_langkah_preprocessing(df["kritik dan saran"].iloc[i])
        
        # [2] TF-IDF Vectorization
        tfidf_matrix, feature_names, vectorizer = tfidf_vectorizer.ubah_ke_tfidf(df["teks_bersih"])
        print("\n--- TAHAP 2: TF-IDF VECTORIZATION ---")
        print(f"Teks telah diubah menjadi matriks TF-IDF dengan {tfidf_matrix.shape[1]} fitur unik.\n")

        # [3] K-Means Clustering
        df["klaster"], best_k = clustering.kmeans_clustering(tfidf_matrix)
        print("--- TAHAP 3: CLUSTERING K-MEANS ---")
        print(f"Clustering selesai dengan k={best_k} (nilai k terbaik).")
        clustering.analisis_klaster(df, tfidf_matrix, vectorizer, feature_names)
        
        print("\nContoh Komentar per Klaster:")
        visualization.contoh_komentar_per_klaster(df, n=2)

        # [4] Sentiment & Meaning Analysis
        lex_pos, lex_neg = sentiment_lexicon.load_lexicon(config.LEXICON_POS, config.LEXICON_NEG)
        df["sentimen"] = df["teks_bersih"].apply(lambda teks: sentiment_lexicon.klasifikasi_sentimen(teks, lex_pos, lex_neg))
        df["makna"] = df["teks_bersih"].apply(sentiment_lexicon.cek_komentar_bermakna)

        print("\n--- TAHAP 4: ANALISIS SENTIMEN & MAKNA ---")
        visualization.tampilkan_analisis_sentimen_dan_makna(df)

        # [5] Evaluation
        print("\n--- TAHAP 5: EVALUASI MODEL ---")
        print("Evaluasi performa klasifikasi Sentimen dan Makna berdasarkan data uji manual:")
        evaluation.evaluasi_manual(df, config.GROUND_TRUTH_PATH)

        # [6] Save Results & Visualizations
        utils.save_output(df, config.OUTPUT_KLASTER, config.OUTPUT_SENTIMEN)
        visualization.visualisasi_semua(df)
        visualization.tabel_statistik_per_klaster(df)
        
        print("\n--- TAHAP 6: PENYIMPANAN HASIL ---")
        print(f"-> Hasil analisis (CSV) telah disimpan di '{config.OUTPUT_KLASTER}' dan '{config.OUTPUT_SENTIMEN}'.")
        print("-> Visualisasi (PNG) telah disimpan di folder 'output/'.")
        print(f"-> Statistik per klaster (CSV) telah disimpan di 'output/statistik_per_klaster.csv'.")
        
        print("\n" + "="*50)
        print("ANALISIS SELESAI")
        print("="*50)

        # Restore stdout
        sys.stdout = old_stdout

    print(f"\nLaporan analisis lengkap telah disimpan di: {log_file_path}")

if __name__ == "__main__":
    main()