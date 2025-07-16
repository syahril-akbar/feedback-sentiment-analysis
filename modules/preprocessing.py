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
    # 1. Case Folding: Mengubah teks menjadi huruf kecil
    teks = teks.lower()

    # 2. Text Cleaning: Menghapus karakter selain huruf dan spasi
    teks = re.sub(r'[^a-z\s]', '', teks)

    # 3. Tokenizing: Memecah teks menjadi token (kata)
    tokens = teks.split()

    # 4. Stopword Removal: Menghapus kata-kata umum (stopword)
    tokens = [kata for kata in tokens if kata not in stopword_list]

    # 5. Stemming: Mengubah kata ke bentuk dasarnya
    hasil = " ".join([stemmer.stem(kata) for kata in tokens])
    
    return hasil

def tampilkan_langkah_preprocessing(teks):
    """
    Menampilkan output dari setiap langkah preprocessing untuk satu teks.
    """
    print(f"Teks Asli: '{teks}'")
    
    # 1. Case Folding
    teks_case_folded = teks.lower()
    print(f"  -> 1. Case Folding: '{teks_case_folded}'")

    # 2. Text Cleaning
    teks_cleaned = re.sub(r'[^a-z\s]', '', teks_case_folded)
    print(f"  -> 2. Text Cleaning: '{teks_cleaned}'")

    # 3. Tokenizing
    tokens = teks_cleaned.split()
    print(f"  -> 3. Tokenizing: {tokens}")

    # 4. Stopword Removal
    tokens_no_stopwords = [kata for kata in tokens if kata not in stopword_list]
    print(f"  -> 4. Stopword Removal: {tokens_no_stopwords}")

    # 5. Stemming
    tokens_stemmed = [stemmer.stem(kata) for kata in tokens_no_stopwords]
    print(f"  -> 5. Stemming: {tokens_stemmed}")

    hasil_akhir = " ".join(tokens_stemmed)
    print(f"  => Hasil Akhir: '{hasil_akhir}'")
    print("-" * 30)