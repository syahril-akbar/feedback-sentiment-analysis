# Analisis Clustering dan Sentimen pada Data Teks Kritikan dan Saran

Proyek ini merupakan implementasi sistem untuk menganalisis data teks berupa kritikan dan saran. Tujuannya adalah untuk mengelompokkan (clustering) topik-topik utama yang dibicarakan, menganalisis sentimen (positif/negatif), serta mengidentifikasi masukan yang bermakna dan konstruktif.

Metode yang digunakan adalah **K-Means Clustering** untuk pengelompokan topik secara *unsupervised* dan **Sentiment Analysis berbasis Lexicon** untuk menentukan polaritas sentimen. Proyek ini dirancang agar **sangat fleksibel**, di mana semua parameter penting dapat dikonfigurasi dari satu file pusat (`config.py`).

## 🎯 Tujuan Proyek

- Mengimplementasikan algoritma K-Means untuk mengelompokkan data teks.
- Menganalisis sentimen (positif, negatif, netral) dari setiap masukan.
- Mengidentifikasi komentar yang dianggap "bermakna" dan memberikan skor "konstruktif".
- Mengidentifikasi topik-topik utama melalui analisis klaster.
- Menyediakan visualisasi dan laporan yang mudah dipahami untuk membantu interpretasi hasil.

## 🚀 Fitur Utama

- **Preprocessing Teks**: Membersihkan dan mempersiapkan data teks (case folding, tokenizing, stopword removal, stemming).
- **Pembobotan TF-IDF**: Mengubah teks menjadi representasi numerik dengan parameter yang dapat disesuaikan (`min_df`, `max_df`, `ngram_range`).
- **K-Means Clustering**: Mengelompokkan data dan menentukan jumlah klaster optimal (`k`) secara otomatis menggunakan *Silhouette Score*.
- **Analisis Topik (Kata Kunci)**: Mengidentifikasi kata-kata kunci yang paling representatif dari setiap klaster.
- **Analisis Sentimen & Makna**: Mengklasifikasikan sentimen, makna, dan skor konstruktif untuk setiap masukan.
- **Evaluasi Model**: Membandingkan hasil sentimen dan makna dengan data uji manual.
- **Visualisasi Data Komprehensif**:
    - Distribusi klaster, sentimen, dan makna.
    - Word cloud per klaster.
    - Grafik Silhouette Score untuk penentuan `k`.
    - **Visualisasi PCA 2D** untuk melihat sebaran klaster.
    - **Heatmap Korelasi** untuk melihat hubungan antar fitur.
- **Konfigurasi Terpusat**: Semua parameter penting (TF-IDF, K-Means, bobot skor, path file, dll.) dapat dengan mudah diubah dari satu file `config.py` tanpa menyentuh kode logika.
- **Laporan Otomatis**: Menghasilkan file laporan `.txt` yang merangkum seluruh proses dan hasil analisis.

## 📂 Struktur Direktori

```
skripsi-kmeans-nlp-monev/
├── data/                 # Berisi data input (kritik_saran.xlsx) dan data uji
├── lexicon/              # Berisi lexicon sentimen positif dan negatif
├── modules/              # Kumpulan modul Python untuk setiap tahap analisis
├── output/               # Tempat menyimpan semua hasil analisis (CSV, gambar, laporan)
├── .gitignore
├── config.py             # FILE KONFIGURASI UTAMA untuk semua parameter
├── main.py               # Skrip utama untuk menjalankan seluruh alur kerja
├── requirements.txt      # Daftar library Python yang dibutuhkan
├── download_nltk_data.py # Skrip untuk mengunduh data NLTK yang dibutuhkan
└── README.md
```

## 🛠️ Instalasi dan Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/syahril-akbar/skripsi-kmeans-nlp-monev.git
cd skripsi-kmeans-nlp-monev
```

### 2. Buat Virtual Environment

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

### 5. Siapkan Data
Letakkan file data (misalnya `kritik_saran.xlsx`) di dalam direktori `data/`. Pastikan path file sudah benar di `config.py`.

### 6. Atur Konfigurasi (Penting!)
Buka file `config.py`. File ini berfungsi sebagai pusat kendali. Sesuaikan parameter di dalamnya sesuai kebutuhan eksperimen. Beberapa parameter kunci yang bisa diubah:
- **Parameter Pra-pemrosesan**: `TFIDF_MIN_DF`, `TFIDF_MAX_DF`, `TFIDF_NGRAM_RANGE`.
- **Parameter Clustering**: `K_RANGE` untuk menentukan rentang pencarian klaster.
- **Parameter Logika**: `CONSTRUCTIVE_THRESHOLD`, `MAKNA_THRESHOLD`, dan semua bobot skor.
- **Path File**: Pastikan semua path input dan output sudah benar.

### 7. Jalankan Analisis Utama

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