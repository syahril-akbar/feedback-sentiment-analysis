import nltk
import ssl

def download_nltk_data():
    """
    Downloads the 'stopwords' and 'punkt' corpora from NLTK.
    It also handles SSL certificate verification issues.
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    try:
        print("Downloading NLTK 'stopwords' corpus...")
        nltk.download('stopwords')
        print("Successfully downloaded 'stopwords'.")

        print("\nDownloading NLTK 'punkt' tokenizer...")
        nltk.download('punkt')
        print("Successfully downloaded 'punkt'.")

        print("\nNLTK data download process complete.")

    except Exception as e:
        print(f"An error occurred during download: {e}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    download_nltk_data()
