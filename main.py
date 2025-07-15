from modules import preprocessing, tfidf_vectorizer, clustering, sentiment_lexicon, evaluation, utils, visualization
import config

def main():
    # [1] Load data utama dari kritik_saran.xlsx
    df = utils.load_data(config.DATA_PATH)

    # [2] Lakukan preprocessing teks
    df["teks_bersih"] = df["komentar"].apply(preprocessing.proses_teks)

    # [3] Konversi teks ke TF-IDF
    tfidf_matrix, feature_names = tfidf_vectorizer.ubah_ke_tfidf(df["teks_bersih"])

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

    # [9] Visualisasi hasil
    visualization.visualisasi_semua(df)

if __name__ == "__main__":
    main()
