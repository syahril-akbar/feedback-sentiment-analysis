import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

# Inisialisasi stemmer dan stopword
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stopword_list = set(stopwords.words("indonesian"))
# Hapus beberapa stopword yang mungkin relevan untuk analisis sentimen
stopword_list.remove('baik')
stopword_list.remove('tidak')
stopword_list.remove('kurang')
stopword_list.remove('lebih')
stopword_list.remove('sangat')

def proses_teks(teks):
    """
    Bersihkan dan normalisasi teks: lowercase, hapus karakter khusus, normalisasi spasi, stopword, dan stemming.
    """
    # 1. Case Folding: Mengubah teks menjadi huruf kecil
    teks = teks.lower()

    # 2. Text Cleaning: Menghapus karakter selain huruf dan spasi
    teks = re.sub(r'[^a-z\s]', '', teks)

    # 3. Normalisasi Spasi: Menghapus spasi berlebih
    teks = re.sub(r'\s+', ' ', teks).strip()

    # 4. Tokenizing: Memecah teks menjadi token (kata)
    tokens = teks.split()

    # 5. Stopword Removal: Menghapus kata-kata umum (stopword)
    tokens = [kata for kata in tokens if kata not in stopword_list]

    # 6. Stemming: Mengubah kata ke bentuk dasarnya
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

    # 3. Normalisasi Spasi
    teks_normalized = re.sub(r'\s+', ' ', teks_cleaned).strip()
    print(f"  -> 3. Normalisasi Spasi: '{teks_normalized}'")

    # 4. Tokenizing
    tokens = teks_normalized.split()
    print(f"  -> 4. Tokenizing: {tokens}")

    # 5. Stopword Removal
    tokens_no_stopwords = [kata for kata in tokens if kata not in stopword_list]
    print(f"  -> 5. Stopword Removal: {tokens_no_stopwords}")

    # 6. Stemming
    tokens_stemmed = [stemmer.stem(kata) for kata in tokens_no_stopwords]
    print(f"  -> 6. Stemming: {tokens_stemmed}")

    hasil_akhir = " ".join(tokens_stemmed)
    print(f"  => Hasil Akhir: '{hasil_akhir}'")
    print("-" * 30)