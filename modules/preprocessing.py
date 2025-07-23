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
        return pd.Series(df.formal.values, index=df.slang).to_dict()
    except FileNotFoundError:
        print(f"Peringatan: File kamus normalisasi tidak ditemukan di '{path}'. Normalisasi slang tidak akan dilakukan.")
        return {}
    except Exception as e:
        print(f"Terjadi error saat memuat kamus normalisasi: {e}")
        return {}

# Inisialisasi
normalization_dict = load_normalization_dict()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stopword_list = set(stopwords.words("indonesian"))
stopword_list.remove('baik')
stopword_list.remove('tidak')
stopword_list.remove('kurang')
stopword_list.remove('lebih')
stopword_list.remove('sangat')


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
    tokens_stemmed = [stemmer.stem(kata) for kata in tokens_no_stopwords]
    print(f"  -> 7. Stemming: {tokens_stemmed}")

    hasil_akhir = " ".join(tokens_stemmed)
    print(f"  => Hasil Akhir: '{hasil_akhir}'")
    print("-" * 30)