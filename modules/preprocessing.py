import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

# Inisialisasi stemmer dan stopword
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stopword_list = set(stopwords.words("indonesian"))

def proses_teks(teks):
    """
    Bersihkan dan normalisasi teks: lowercase, hapus karakter khusus, stopword, dan stemming.
    """
    teks = teks.lower()
    teks = re.sub(r'[^a-z\s]', '', teks)
    tokens = teks.split()
    tokens = [kata for kata in tokens if kata not in stopword_list]
    hasil = " ".join([stemmer.stem(kata) for kata in tokens])
    return hasil
