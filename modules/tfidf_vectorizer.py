from sklearn.feature_extraction.text import TfidfVectorizer
import config

def ubah_ke_tfidf(teks_bersih):
    """
    Konversi teks bersih ke dalam representasi fitur numerik TF-IDF
    menggunakan parameter dari file config.
    """
    vectorizer = TfidfVectorizer(
        min_df=config.TFIDF_MIN_DF,
        max_df=config.TFIDF_MAX_DF,
        ngram_range=config.TFIDF_NGRAM_RANGE
    )
    matrix = vectorizer.fit_transform(teks_bersih)
    feature_names = vectorizer.get_feature_names_out()
    
    print(f"TF-IDF Vectorizer menggunakan min_df={config.TFIDF_MIN_DF}, max_df={config.TFIDF_MAX_DF}, ngram_range={config.TFIDF_NGRAM_RANGE}.")
    
    return matrix, feature_names, vectorizer