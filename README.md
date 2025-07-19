# Analisis Clustering dan Sentimen pada Data Teks Kritikan dan Saran

Proyek ini merupakan implementasi sistem untuk menganalisis data teks berupa kritikan dan saran. Tujuannya adalah untuk mengelompokkan (clustering) topik-topik utama yang dibicarakan, menganalisis sentimen (positif/negatif), serta mengidentifikasi masukan yang bermakna dan konstruktif.

Metode yang digunakan adalah **K-Means Clustering** untuk pengelompokan topik secara *unsupervised* dan **Sentiment Analysis berbasis Lexicon** untuk menentukan polaritas sentimen.

## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:
- Mengimplementasikan algoritma K-Means untuk mengelompokkan data teks kritikan dan saran secara otomatis.
- Menganalisis sentimen (positif, negatif, netral) dari setiap masukan menggunakan pendekatan berbasis lexicon.
- Mengidentifikasi komentar yang dianggap "bermakna" berdasarkan jumlah kata.
- Memberikan skor "konstruktif" pada setiap masukan untuk menyoroti saran yang paling relevan.
- Mengidentifikasi topik-topik utama yang muncul dari kritikan dan saran melalui analisis klaster.
- Menyediakan visualisasi dan laporan yang mudah dipahami untuk membantu interpretasi hasil analisis.

## 🚀 Fitur Utama

- **Preprocessing Teks**: Membersihkan dan mempersiapkan data teks (case folding, tokenizing, stopword removal, stemming).
- **Pembobotan TF-IDF**: Mengubah teks menjadi representasi numerik.
- **K-Means Clustering**: Mengelompokkan data ke dalam beberapa klaster (topik) dan menentukan jumlah klaster optimal menggunakan *Silhouette Score*.
- **Analisis Topik (Kata Kunci)**: Mengidentifikasi kata-kata kunci yang paling representatif dari setiap klaster.
- **Analisis Sentimen**: Mengklasifikasikan setiap masukan sebagai positif, negatif, atau netral.
- **Analisis Makna & Konstruktif**: Memberikan label "Bermakna" atau "Tidak Bermakna" dan menghitung skor konstruktif untuk setiap masukan.
- **Evaluasi Model**: Membandingkan hasil sentimen dan makna dengan data uji manual untuk mengukur performa.
- **Visualisasi Data**: Menghasilkan grafik dan tabel (distribusi klaster, sentimen, word cloud, dll).
- **Laporan Otomatis**: Menghasilkan file laporan `.txt` yang merangkum seluruh proses dan hasil analisis.

## 📂 Struktur Direktori

```
skripsi-kmeans-nlp-monev/
├── data/                 # Berisi data input (kritik_saran.xlsx) dan data uji
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
git clone https://github.com/syahril-akbar/skripsi-kmeans-nlp-monev.git
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

Jalankan skrip berikut untuk mengunduh data `stopwords` dan `punkt` dari NLTK.

```bash
python download_nltk_data.py
```

### 5. Siapkan Data
Letakkan file data Anda (misalnya `kritik_saran.xlsx`) di dalam direktori `data/`. Pastikan path file sudah benar di `config.py`.

### 6. Jalankan Analisis Utama

```bash
python main.py
```

## 📊 Hasil Analisis

Setelah eksekusi `main.py` selesai, semua hasil akan tersimpan di dalam direktori `output/`:

- **`laporan_akhir.txt`**: Laporan teks lengkap yang berisi semua output dari konsol, termasuk kata kunci per klaster, skor evaluasi, dan ringkasan lainnya.
- **`hasil_akhir.csv`**: File CSV utama yang berisi hasil analisis lengkap untuk setiap baris data (teks asli, teks bersih, klaster, sentimen, makna, skor konstruktif).
- **`komentar_bermakna.csv`**: CSV yang hanya berisi komentar-komentar yang dilabeli "Bermakna".
- **`saran_konstruktif.csv`**: CSV yang berisi saran-saran yang diurutkan berdasarkan skor konstruktif tertinggi.
- **`statistik_per_klaster.csv`**: Ringkasan statistik untuk setiap klaster.
- **`contoh_komentar_per_klaster.txt`**: Contoh komentar dari setiap klaster untuk memudahkan interpretasi.
- **File Gambar (`.png`)**:
    - **`distribusi_sentimen.png`**: Diagram distribusi sentimen.
    - **`jumlah_komentar_per_klaster.png`**: Diagram batang jumlah komentar per klaster.
    - **`silhouette_scores.png`**: Grafik skor Silhouette untuk penentuan `k` optimal.
    - **`word_cloud_klaster_N.png`**: Word cloud untuk setiap klaster.