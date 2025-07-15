import sys
import os
from modules import preprocessing, tfidf_vectorizer, clustering, sentiment_lexicon, evaluation, utils, visualization
from sklearn.metrics import silhouette_score
import config

def main():
    # Define log file path
    log_dir = "output"
    log_file_path = os.path.join(log_dir, "laporan_akhir.txt")

    # Ensure the output directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Redirect stdout to log file
    with open(log_file_path, "w") as f:
        old_stdout = sys.stdout
        sys.stdout = f

        # [1] Load data utama dari kritik_saran.xlsx
        df = utils.load_data(config.DATA_PATH)

        # [2] Lakukan preprocessing teks
        df["teks_bersih"] = df["kritik dan saran"].apply(preprocessing.proses_teks)

        # [3] Konversi teks ke TF-IDF
        tfidf_matrix, feature_names, vectorizer = tfidf_vectorizer.ubah_ke_tfidf(df["teks_bersih"])

        # [4] Lakukan clustering K-Means dengan pencarian k terbaik
        df["klaster"], best_k = clustering.kmeans_clustering(tfidf_matrix)

        # [5] Analisis sentimen menggunakan lexicon InSet
        lex_pos, lex_neg = sentiment_lexicon.load_lexicon(config.LEXICON_POS, config.LEXICON_NEG)
        df["sentimen"] = df["teks_bersih"].apply(lambda teks: sentiment_lexicon.klasifikasi_sentimen(teks, lex_pos, lex_neg))

        # [6] Klasifikasi komentar bermakna atau tidak bermakna
        df["makna"] = df["teks_bersih"].apply(sentiment_lexicon.cek_komentar_bermakna)

        # [7] Simpan hasil clustering dan sentimen ke output/
        utils.save_output(df, config.OUTPUT_KLASTER, config.OUTPUT_SENTIMEN)

        # [8] Evaluasi terhadap data uji manual (ground truth)
        evaluation.evaluasi_manual(df, config.GROUND_TRUTH_PATH)

        # [9] Visualisasi dan laporan deskriptif
        visualization.visualisasi_semua(df)
        visualization.tabel_statistik_per_klaster(df)
        visualization.contoh_komentar_per_klaster(df, n=3)

        # Additional analysis based on teknik analisis data

        # 1. Analisis Preprocessing Teks
        print("\n--- Analisis Preprocessing Teks ---")
        print("Menampilkan beberapa contoh komentar sebelum dan sesudah preprocessing:")
        for i in range(5): # Display 5 examples
            print(f"\nContoh {i+1}:")
            print(f"  Sebelum: {df['kritik dan saran'].iloc[i]}")
            print(f"  Sesudah: {df['teks_bersih'].iloc[i]}")

        # 2. Analisis Hasil Clustering K-Means
        print("\n--- Analisis Hasil Clustering K-Means ---")

        # a. Melaporkan nilai Silhouette Score
        silhouette_avg = silhouette_score(tfidf_matrix, df['klaster'])
        print(f"Nilai Silhouette Score: {silhouette_avg:.3f}")

        # b. Mengidentifikasi dan menampilkan kata-kata kunci utama per klaster
        print("\nKata Kunci Utama per Klaster (berdasarkan TF-IDF):")
        feature_names = vectorizer.get_feature_names_out()
        for cluster_id in sorted(df['klaster'].unique()):
            cluster_comments = df[df['klaster'] == cluster_id]['teks_bersih']
            if not cluster_comments.empty:
                # Create a temporary TF-IDF matrix for the current cluster
                cluster_tfidf_matrix = vectorizer.transform(cluster_comments)
                # Sum TF-IDF scores for each term in the cluster
                sum_tfidf = cluster_tfidf_matrix.sum(axis=0)
                # Get feature names and their summed TF-IDF scores
                tfidf_scores = [(feature_names[i], sum_tfidf[0, i]) for i in range(len(feature_names))]
                # Sort by score in descending order and get top 5
                sorted_tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
                top_keywords = [word for word, score in sorted_tfidf_scores[:5]]
                print(f"  Klaster {cluster_id}: {', '.join(top_keywords)}")

        # c. Disajikan satu atau dua contoh komentar dari tiap klaster sebagai ilustrasi.
        print("\nContoh Komentar dari Tiap Klaster:")
        for cluster_id in sorted(df['klaster'].unique()):
            cluster_comments = df[df['klaster'] == cluster_id]['kritik dan saran'] # Use original text for examples
            print(f"  Klaster {cluster_id}:")
            if not cluster_comments.empty:
                for i, comment in enumerate(cluster_comments.head(2)):
                    print(f"    - {comment}")
            else:
                print("    (Tidak ada komentar dalam klaster ini)")

        # 3. Analisis Hasil Analisis Sentimen dan Makna Komentar
        print("\n--- Analisis Hasil Analisis Sentimen dan Makna Komentar ---")

        # a. Menampilkan distribusi jumlah (atau persentase) komentar berdasarkan kategori sentimen dan makna
        print("\nDistribusi Sentimen:")
        sentiment_distribution = df['sentimen'].value_counts(normalize=True) * 100
        print(sentiment_distribution.to_string(float_format="%.2f%%"))

        # b. Melaporkan hasil Akurasi dan F1-Score dari klasifikasi sentimen dan makna
        print("\nDistribusi Makna:")
        meaning_distribution = df['makna'].value_counts(normalize=True) * 100
        print(meaning_distribution.to_string(float_format="%.2f%%"))

        # b. Melaporkan hasil Akurasi dan F1-Score dari klasifikasi sentimen dan makna
        print("\nEvaluasi Klasifikasi Sentimen dan Makna (menggunakan data uji manual):")
        evaluation.evaluasi_manual(df, 'data/data_uji_manual.xlsx')

        # 4. Pembahasan dan Kesimpulan Awal
        print("\n--- Pembahasan dan Kesimpulan Awal ---")
        print("Analisis data telah selesai. Hasil-hasil di atas dapat digunakan untuk pembahasan dan penarikan kesimpulan awal.")
        print("\nRingkasan implementasi dan hasil utama:")
        print("  - Tahapan preprocessing telah mengubah teks mentah menjadi format yang siap dianalisis.")
        print("  - Pengelompokan K-Means membantu mengidentifikasi tema-tema utama dalam kritik dan saran, seperti yang ditunjukkan oleh kata kunci dan contoh komentar per klaster.")
        print("  - Analisis sentimen dan makna memberikan wawasan tentang polaritas dan relevansi komentar, dengan evaluasi akurasi dan F1-Score.")
        print("\nPotensi manfaat bagi BBPSDMP Kominfo Makassar:")
        print("  - Memahami isu-isu utama dari kritik dan saran melalui klasterisasi.")
        print("  - Mengidentifikasi komentar yang paling relevan dan substantif melalui analisis makna.")
        print("  - Memantau sentimen umum terhadap program atau layanan.")

        # Restore stdout
        sys.stdout = old_stdout

    print(f"Analisis selesai. Output terminal telah disimpan ke: {log_file_path}")

if __name__ == "__main__":
    main()feat: Implement comprehensive data analysis and refactor logging

This commit introduces a complete data analysis pipeline within `main.py` and refactors the logging mechanism to centralize all output.

Key changes include:
- `main.py`:
    - All console output is now redirected to `output/laporan_akhir.txt`, providing a single, comprehensive analysis report.
    - Integrated detailed analysis steps as per `teknik_analisis_data.txt`, including:
        - Text preprocessing examples (before and after).
        - K-Means clustering analysis: Silhouette Score, top TF-IDF keywords per cluster, and example comments for each cluster.
        - Sentiment and meaning distribution analysis.
        - Evaluation of sentiment and meaning classification using manual test data.
    - Re-enabled visualization calls to ensure all relevant plots and reports are generated.
- `modules/evaluation.py`: Modified `evaluasi_manual` to print its report to stdout instead of writing directly to `laporan_akhir.txt`, allowing `main.py`'s logging redirection to capture it.
- `modules/tfidf_vectorizer.py`: Updated `ubah_ke_tfidf` to return the `TfidfVectorizer` object, enabling keyword extraction in `main.py`.

This refactoring centralizes reporting and enhances the analytical capabilities of the main script.
