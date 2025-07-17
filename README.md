# Analisis Clustering dan Sentimen pada Data Teks Kritikan dan Saran

Proyek ini merupakan implementasi sistem untuk menganalisis data teks berupa kritikan dan saran. Tujuannya adalah untuk mengelompokkan (clustering) topik-topik utama yang dibicarakan dan menganalisis sentimen (positif/negatif) dari setiap masukan.

Metode yang digunakan adalah **K-Means Clustering** untuk pengelompokan topik secara *unsupervised* dan **Sentiment Analysis berbasis Lexicon** untuk menentukan polaritas sentimen.

## 🚀 Fitur Utama

- **Preprocessing Teks**: Membersihkan dan mempersiapkan data teks (case folding, tokenizing, stopword removal, stemming).
- **Pembobotan TF-IDF**: Mengubah teks menjadi representasi numerik yang dapat diolah oleh model machine learning.
- **K-Means Clustering**: Mengelompokkan data secara otomatis ke dalam beberapa klaster (topik) dan menentukan jumlah klaster optimal menggunakan *Silhouette Score*.
- **Analisis Topik (Kata Kunci)**: Mengidentifikasi kata-kata kunci yang paling representatif dari setiap klaster menggunakan analisis *centroid*.
- **Analisis Sentimen**: Mengklasifikasikan setiap masukan sebagai positif, negatif, atau netral berdasarkan lexicon Bahasa Indonesia.
- **Evaluasi Model**: Membandingkan hasil sentimen dan klasifikasi bermakna dengan data uji manual untuk mengukur performa.
- **Visualisasi Data**: Menghasilkan grafik dan tabel untuk mempermudah interpretasi hasil, seperti distribusi klaster, sentimen, dan word cloud.
- **Laporan Otomatis**: Menghasilkan file laporan `.txt` yang merangkum seluruh proses dan hasil analisis.

## 📂 Struktur Direktori

```
skripsi-kmeans-nlp-monev/
├── data/                 # Berisi data mentah (kritik_saran.xlsx) dan data uji
├── lexicon/              # Berisi lexicon sentimen positif dan negatif
├── modules/              # Kumpulan modul Python untuk setiap tahap analisis
├── output/               # Tempat menyimpan semua hasil analisis (CSV, gambar, laporan)
├── .gitignore
├── config.py             # File konfigurasi untuk path dan parameter
├── main.py               # Skrip utama untuk menjalankan seluruh alur kerja
├── requirements.txt      # Daftar library Python yang dibutuhkan
└── download_nltk_data.py # Skrip untuk mengunduh data NLTK
```

## 🛠️ Instalasi dan Penggunaan

Berikut adalah langkah-langkah untuk menyiapkan dan menjalankan proyek ini.

### 1. Clone Repository

```bash
git https://github.com/syahril-akbar/skripsi-kmeans-nlp-monev.git
cd skripsi-kmeans-nlp-monev
```

### 2. Buat Virtual Environment

Sangat disarankan untuk menggunakan *virtual environment* agar tidak mengganggu instalasi Python global Anda.

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

Jalankan skrip berikut untuk mengunduh data `stopwords` dan `punkt` dari NLTK yang diperlukan untuk preprocessing.

```bash
python download_nltk_data.py
```

### 5. Jalankan Analisis

Untuk menjalankan seluruh pipeline analisis, cukup eksekusi file `main.py`.

```bash
python main.py
```

## 📊 Hasil Analisis

Setelah eksekusi selesai, semua hasil akan tersimpan di dalam direktori `output/`:

- **`laporan_akhir.txt`**: Laporan teks lengkap yang berisi semua output dari konsol, termasuk kata kunci per klaster, skor evaluasi, dan ringkasan lainnya.
- **`hasil_akhir.csv`**: File CSV utama yang berisi hasil analisis lengkap untuk setiap baris data, mencakup kritik dan saran asli, teks bersih, label klaster, sentimen, dan penanda makna.
- **`komentar_bermakna.csv`**: File CSV yang hanya berisi daftar kritik dan saran asli yang telah diidentifikasi sebagai "bermakna" oleh sistem.
- **`statistik_per_klaster.csv`**: Ringkasan statistik untuk setiap klaster.
- **File Gambar (`.png`)**: Berbagai visualisasi seperti diagram lingkaran untuk distribusi sentimen, diagram batang untuk distribusi klaster, dan word cloud untuk setiap klaster.