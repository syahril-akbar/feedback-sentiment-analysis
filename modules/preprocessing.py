import pandas as pd
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
import config

# --- Kamus Normalisasi ---
def load_normalization_dict(path=config.NORMALIZATION_DICT):
    """Memuat kamus normalisasi dari file TXT (tab-separated)."""
    try:
        df = pd.read_csv(path, sep='	', header=None, names=['slang', 'formal'])
        df.dropna(inplace=True)
        # Mengatasi duplikat jika ada, ambil yang pertama
        df = df.drop_duplicates(subset=['slang'])
        return pd.Series(df.formal.values, index=df.slang).to_dict()
    except FileNotFoundError:
        print(f"Peringatan: File kamus normalisasi tidak ditemukan di '{path}'. Normalisasi slang tidak akan dilakukan.")
        return {}
    except Exception as e:
        print(f"Terjadi error saat memuat kamus normalisasi: {e}")
        return {}

# --- Inisialisasi Stopwords dan Stemmer ---

# 1. Daftar stopword dasar dari NLTK
stopword_list_nltk = set(stopwords.words("indonesian"))

# 2. Daftar stopword tambahan yang spesifik untuk konteks ini
# Kata-kata ini sering muncul tapi tidak memberikan makna topik yang jelas
custom_stopwords = {
    'lebih', 'baik', 'sangat', 'kurang', 'tidak', 'nya', 'sih', 'ya', 'biar',
    'moga', 'semoga', 'saran', 'kasih', 'terima', 'terimakasih', 'mohon',
    'tolong', 'agar', 'buat', 'untuk', 'supaya', 'tetap', 'perlu', 'adain',
    'diadain', 'diadakan', 'atas', 'bawah', 'depan', 'belakang', 'pada',
    'juga', 'lagi', 'masih', 'udah', 'sudah', 'aja', 'saja', 'ok', 'oke',
    'lumayan', 'cukup', 'selalu', 'paling', 'agak'
}

# 3. Gabungkan kedua daftar stopword
stopword_list = stopword_list_nltk.union(custom_stopwords)

# 4. Hapus beberapa stopword yang mungkin relevan (jika didefinisikan di config)
for word in config.STOPWORDS_TO_KEEP:
    if word in stopword_list:
        stopword_list.remove(word)

# 5. Inisialisasi komponen lain
normalization_dict = load_normalization_dict()
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def proses_teks(teks):
    """
    Bersihkan dan normalisasi teks: lowercase, hapus karakter khusus, normalisasi spasi, normalisasi slang, stopword, dan stemming.
    """
    # 1. Case Folding: Mengubah teks menjadi huruf kecil
    teks = teks.lower()

    # 2. Text Cleaning: Menghapus karakter selain huruf dan spasi
    teks = re.sub(r'[^a-z\s]', '', teks)

    # 3. Normalisasi Spasi: Menghapus spasi berlebih
    teks = re.sub(r'\s+', ' ', teks).strip()

    # 4. Tokenizing: Memecah teks menjadi token (kata)
    tokens = teks.split()

    # 5. Normalisasi Kata (Slang): Mengganti kata slang dengan kata baku
    tokens = [normalization_dict.get(kata, kata) for kata in tokens]

    # 6. Stopword Removal: Menghapus kata-kata umum (stopword)
    tokens = [kata for kata in tokens if kata not in stopword_list]

    # 7. Stemming: Mengubah kata ke bentuk dasarnya
    tokens = [stemmer.stem(kata) for kata in tokens]
    hasil = " ".join(tokens)
    
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
    teks_normalized_space = re.sub(r'\s+', ' ', teks_cleaned).strip()
    print(f"  -> 3. Normalisasi Spasi: '{teks_normalized_space}'")

    # 4. Tokenizing
    tokens = teks_normalized_space.split()
    print(f"  -> 4. Tokenizing: {tokens}")

    # 5. Normalisasi Kata (Slang)
    tokens_normalized_word = [normalization_dict.get(kata, kata) for kata in tokens]
    print(f"  -> 5. Normalisasi Kata (Slang): {tokens_normalized_word}")

    # 6. Stopword Removal
    tokens_no_stopwords = [kata for kata in tokens_normalized_word if kata not in stopword_list]
    print(f"  -> 6. Stopword Removal: {tokens_no_stopwords}")

    # 7. Stemming
    # Gabungkan dulu sebelum stemming untuk konteks yang lebih baik
    teks_sebelum_stem = " ".join(tokens_no_stopwords)
    tokens_stemmed = stemmer.stem(teks_sebelum_stem).split()
    print(f"  -> 7. Stemming: {tokens_stemmed}")

    hasil_akhir = " ".join(tokens_stemmed)
    print(f"  => Hasil Akhir: '{hasil_akhir}'")
    print("-" * 30)
