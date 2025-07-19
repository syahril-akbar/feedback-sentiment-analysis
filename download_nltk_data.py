import nltk
import ssl

def download_nltk_data():
    """
    Mengunduh korpus 'stopwords' dan 'punkt' dari NLTK.
    Fungsi ini juga menangani masalah verifikasi sertifikat SSL.
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    try:
        print("Mengunduh korpus 'stopwords' NLTK...")
        nltk.download('stopwords')
        print("Berhasil mengunduh 'stopwords'.")

        print("\nMengunduh tokenizer 'punkt' NLTK...")
        nltk.download('punkt')
        print("Berhasil mengunduh 'punkt'.")

        print("\nProses pengunduhan data NLTK selesai.")

    except Exception as e:
        print(f"Terjadi kesalahan saat mengunduh: {e}")
        print("Silakan periksa koneksi internet Anda dan coba lagi.")

if __name__ == "__main__":
    download_nltk_data()
