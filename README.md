# Analisis Sentimen dan Topik pada Data Teks Menggunakan K-Means Clustering

Proyek ini adalah implementasi sistem untuk menganalisis data teks, khususnya untuk mengelompokkan topik-topik utama dan menganalisis sentimen yang terkandung di dalamnya. Sistem ini menggunakan **K-Means Clustering** untuk pengelompokan topik secara *unsupervised* dan **Analisis Sentimen berbasis Leksikon** untuk menentukan polaritas sentimen.

Salah satu keunggulan utama proyek ini adalah **fleksibilitasnya**. Semua parameter penting, mulai dari path file hingga bobot untuk skor, dapat dikonfigurasi melalui satu file pusat, yaitu `config.py`.

## 🚀 Fitur Utama

- **Preprocessing Teks Komprehensif**: Termasuk case folding, normalisasi (menggunakan kamus `kbba.txt`), penghapusan stopwords, dan stemming.
- **Vektorisasi TF-IDF**: Mengubah teks menjadi representasi numerik dengan parameter yang dapat disesuaikan (`min_df`, `max_df`, `ngram_range`).
- **Clustering K-Means dengan Penentuan `k` Otomatis**: Mengelompokkan data dan menentukan jumlah klaster optimal (`k`) secara otomatis menggunakan **Silhouette Score**.
- **Analisis Topik (Kata Kunci)**: Mengidentifikasi kata-kata kunci yang paling representatif dari setiap klaster untuk interpretasi topik.
- **Analisis Sentimen & Makna**: Mengklasifikasikan sentimen (positif, negatif, netral) dan mengidentifikasi komentar yang dianggap "bermakna".
- **Skor Konstruktif**: Memberikan skor pada komentar berdasarkan bobot yang dapat disesuaikan untuk kata-kata saran, kritik, dan pujian.
- **Visualisasi Data Komprehensif**:
    - Distribusi klaster, sentimen, dan makna.
    - Word cloud per klaster untuk visualisasi topik.
    - Grafik Silhouette Score untuk penentuan `k` optimal.
    - **Visualisasi PCA 2D** untuk melihat sebaran klaster.
    - **Heatmap Korelasi** untuk melihat hubungan antar fitur.
- **Struktur Direktori yang Jelas**: Memisahkan data, konfigurasi, dan logika aplikasi untuk kemudahan pemeliharaan.
- **Laporan Analisis Otomatis**: Menghasilkan file `.txt` yang merangkum seluruh proses dan hasil analisis, serta file `.csv` untuk hasil yang lebih detail.

## 📂 Struktur Direktori

```
.
├── config.py             # FILE KONFIGURASI UTAMA untuk semua parameter
├── data/                 # Berisi data input (kritik_saran.xlsx) dan data uji manual (data_uji_manual.csv)
├── download_nltk_data.py # Skrip untuk mengunduh data NLTK yang dibutuhkan
├── kamus/                # Berisi kamus untuk normalisasi dan leksikon sentimen
│   ├── lexicon/          # Leksikon untuk sentimen positif dan negatif
│   └── normalisasi/      # Kamus untuk normalisasi kata (slang, singkatan, dll.)
├── main.py               # Skrip utama untuk menjalankan seluruh alur kerja
├── modules/              # Kumpulan modul Python untuk setiap tahap analisis
│   ├── clustering.py     # Berisi fungsi untuk K-Means clustering dan penentuan k optimal.
│   ├── evaluation.py     # Modul untuk evaluasi model, khususnya perbandingan dengan ground truth.
│   ├── preprocessing.py  # Fungsi-fungsi untuk pra-pemrosesan teks (case folding, normalisasi, stemming, stopword removal).
│   ├── sentiment_lexicon.py # Implementasi analisis sentimen berbasis leksikon dan identifikasi komentar bermakna/konstruktif.
│   ├── tfidf_vectorizer.py # Fungsi untuk mengubah teks menjadi representasi TF-IDF.
│   ├── utils.py          # Fungsi utilitas seperti memuat data, menyimpan output, dan penulisan laporan.
│   └── visualization.py  # Fungsi untuk membuat berbagai visualisasi data dan hasil analisis.
├── output/               # Tempat menyimpan semua hasil analisis (CSV, gambar, laporan)
├── requirements.txt      # Daftar library Python yang dibutuhkan
└── tests/                # Berisi unit tests dan mock data untuk pengujian
```

## 🛠️ Instalasi dan Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/syahril-akbar/skripsi-kmeans-nlp-monev.git
cd skripsi-kmeans-nlp-monev
```

### 2. Buat dan Aktifkan Virtual Environment

Sangat disarankan untuk menggunakan *virtual environment* agar tidak mengganggu instalasi Python global.

```bash
# Membuat environment
python -m venv .venv

# Mengaktifkan environment (Windows)
.\.venv\Scripts\activate

# Mengaktifkan environment (macOS/Linux)
source .venv/bin/activate
```

### 3. Instal Dependensi

Instal semua library yang dibutuhkan dari file `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Unduh Data NLTK

Jalankan skrip berikut untuk mengunduh data `stopwords` dan `punkt` dari NLTK. Skrip ini juga menangani potensi masalah sertifikat SSL.

```bash
python download_nltk_data.py
```

### 5. Atur Konfigurasi

Buka file `config.py`. File ini berfungsi sebagai pusat kendali. Sesuaikan parameter di dalamnya sesuai kebutuhan, terutama `DATA_PATH` dan `GROUND_TRUTH_PATH`.

### 6. Jalankan Analisis Utama

```bash
python main.py
```

## 📊 Hasil Analisis

Setelah eksekusi selesai, semua hasil akan tersimpan di dalam direktori `output/`:

- **`laporan_analisis.txt`**: Laporan teks lengkap yang berisi semua output dari konsol.
- **`hasil_akhir.csv`**: File CSV utama yang berisi hasil analisis lengkap, termasuk kolom `top_keywords` untuk setiap data.
- **`komentar_bermakna.csv`**: CSV yang hanya berisi komentar-komentar yang dilabeli "Bermakna".
- **`saran_konstruktif.csv`**: CSV yang berisi saran-saran yang diurutkan berdasarkan skor konstruktif.
- **`statistik_per_klaster.csv`**: Ringkasan statistik untuk setiap klaster.
- **`contoh_komentar_per_klaster.txt`**: Contoh komentar dari setiap klaster untuk memudahkan interpretasi.
- **File Gambar (`.png`)**:
    - `distribusi_sentimen.png` & `distribusi_makna.png`: Grafik distribusi keseluruhan sentimen dan makna komentar.
    - `jumlah_komentar_per_klaster.png`: Diagram batang jumlah komentar untuk setiap klaster.
    - `distribusi_sentimen_per_klaster.png`: Grafik proporsi sentimen dalam setiap klaster.
    - `silhouette_scores.png`: Grafik untuk menentukan jumlah klaster (`k`) optimal.
    - `wordcloud_klaster_N.png`: Visualisasi kata-kata paling umum untuk setiap klaster.
    - `pca_clusters.png`: Visualisasi sebaran klaster dalam 2D.
    - `correlation_heatmap.png`: Heatmap korelasi antar fitur.

## 📚 Pustaka Utama

- **Pandas**: Untuk manipulasi dan analisis data.
- **NLTK**: Untuk pemrosesan bahasa alami (tokenisasi, stopwords).
- **Scikit-learn**: Untuk implementasi K-Means dan TF-IDF.
- **Matplotlib & Seaborn**: Untuk visualisasi data.
