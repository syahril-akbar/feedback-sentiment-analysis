from sklearn.feature_extraction.text import TfidfVectorizer

def ubah_ke_tfidf(teks_bersih):
    """
    Konversi teks bersih ke dalam representasi fitur numerik TF-IDF.
    """
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(teks_bersih)
    return matrix, vectorizer.get_feature_names_out()
