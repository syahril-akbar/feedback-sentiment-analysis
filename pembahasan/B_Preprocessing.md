# HASIL DAN PEMBAHASAN

## B. Tahap Pra-pemrosesan Teks (Preprocessing)

Tahap pra-pemrosesan data teks merupakan fase fundamental dalam metodologi penelitian ini. Tujuan utamanya adalah untuk mentransformasi data tekstual mentah yang bersifat tidak terstruktur—diambil dari kolom `kritik dan saran`—menjadi format yang bersih, seragam, dan terstruktur. Kualitas data pada tahap ini secara langsung mengimplikasikan validitas dan akurasi dari proses-proses hilir, termasuk ekstraksi fitur dengan TF-IDF, analisis sentimen, dan *clustering*. Implementasi tahap ini secara efektif mereduksi *noise* (derau) dan menyingkirkan elemen-elemen linguistik yang tidak relevan, sehingga memungkinkan model untuk fokus pada fitur-fitur yang paling signifikan.

Keseluruhan alur kerja pra-pemrosesan diimplementasikan dalam modul `modules/preprocessing.py` dan dieksekusi secara sekuensial untuk setiap dokumen dalam korpus.

### 1. Rincian Tahapan Pra-pemrosesan

Proses pengolahan teks mentah menjadi teks bersih melibatkan serangkaian tahapan komputasi linguistik yang sistematis. Setiap tahapan dirancang untuk menangani aspek spesifik dari variasi dan inkonsistensi data.

#### a. Case Folding
Tahap pertama adalah *case folding*, di mana seluruh karakter dalam teks dikonversi menjadi format huruf kecil (*lowercase*). Proses ini esensial untuk unifikasi leksikal, memastikan bahwa kata yang sama namun ditulis dengan kapitalisasi berbeda (misalnya, "Fasilitas", "fasilitas", dan "FASILITAS") akan diperlakukan sebagai satu *token* yang identik oleh sistem.

#### b. Text Cleaning
Pada tahap ini, dilakukan pembersihan karakter-karakter non-alfabetik menggunakan ekspresi reguler (regex). Implementasi `re.sub(r'[^a-z\s]', '', teks)` secara spesifik menargetkan dan menghapus semua karakter yang bukan merupakan huruf (a-z) atau spasi, seperti tanda baca (koma, titik, tanda seru), angka, dan simbol lainnya. Hal ini bertujuan untuk mengeliminasi derau yang tidak memberikan kontribusi semantik pada analisis.

#### c. Normalisasi Kata dan Spasi
Normalisasi dilakukan dalam dua bentuk:
1.  **Normalisasi Spasi**: Spasi berlebih yang mungkin muncul setelah proses *cleaning* dihilangkan. Setiap rangkaian spasi ganda atau lebih dikonversi menjadi spasi tunggal.
2.  **Normalisasi Kata (Slang)**: Teks yang mengandung kata-kata tidak baku atau singkatan (slang) dinormalisasi ke dalam bentuk Bahasa Indonesia baku. Proses ini memanfaatkan kamus normalisasi eksternal yang tersimpan di `kamus/normalisasi/kbba.txt`. Sebagai contoh, *token* seperti "tdk" akan dikonversi menjadi "tidak", dan "jg" menjadi "juga".

#### d. Tokenizing
Setelah teks bersih dan ternormalisasi, proses *tokenizing* memecah kalimat menjadi unit-unit leksikal individual yang disebut *token*. Proses ini mengubah struktur data dari string menjadi sebuah daftar (list) *token*, yang memungkinkan analisis pada level kata.

#### e. Stopword Removal
Tahap ini bertujuan untuk menyaring dan menghapus *stopwords* atau kata henti—kata-kata umum dengan frekuensi tinggi namun memiliki signifikansi semantik yang rendah (misalnya, "yang", "di", "dan"). Proses ini diimplementasikan dengan strategi hibrida:
-   **Basis**: Menggunakan daftar *stopwords* standar untuk Bahasa Indonesia dari pustaka NLTK.
-   **Kustomisasi**: Daftar basis diperluas dengan kata-kata khusus yang didefinisikan dalam `config.py` (`CUSTOM_STOPWORDS`), seperti "kak", "terimakasih", dan "saran", yang sering muncul dalam konteks data namun tidak informatif untuk pemodelan topik.
-   **Pengecualian**: Beberapa kata yang secara default termasuk *stopwords* namun krusial untuk analisis sentimen, seperti "tidak", "kurang", dan "lebih", secara eksplisit dipertahankan (`STOPWORDS_TO_KEEP`).

#### f. Stemming
Tahap akhir adalah *stemming*, yaitu proses reduksi kata-kata ke bentuk dasarnya (*root word*) dengan menghilangkan afiks (imbuhan). Proses ini diimplementasikan menggunakan pustaka Sastrawi, sebuah *stemmer* yang dirancang khusus untuk Bahasa Indonesia. Sebagai contoh, kata "pelatihannya" akan direduksi menjadi "latih", dan "menyampaikan" menjadi "sampai". Tujuan utama *stemming* adalah untuk mengurangi dimensi ruang fitur dengan mengelompokkan variasi morfologis dari sebuah kata menjadi satu representasi tunggal.

### 2. Ilustrasi Proses Transformasi Teks

Untuk memberikan gambaran empiris mengenai dampak dari setiap tahapan, Tabel 4.1 berikut menyajikan ilustrasi alur transformasi untuk beberapa data aktual. Tabel ini mendemonstrasikan bagaimana teks mentah dari kolom `kritik dan saran` secara bertahap dibersihkan dan distandarisasi, mulai dari teks asli hingga menjadi `teks_bersih` yang siap untuk dianalisis lebih lanjut. Setiap kolom merepresentasikan output dari satu langkah spesifik dalam pipeline pra-pemrosesan.

| Contoh | Teks Asli | Case Folding | Text Cleaning | Normalisasi | Tokenizing | Stopword Removal | Stemming | Hasil Akhir |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `'acnya kurang dingin'` | `'acnya kurang dingin'` | `'acnya kurang dingin'` | `'acnya kurang dingin'` | `['acnya', 'kurang', 'dingin']` | `['acnya', 'kurang', 'dingin']` | `['ac', 'kurang', 'dingin']` | `'ac kurang dingin'` |
| **2** | `'Untuk anak JGD kursi nya kekecilan, susah mouse bergerak selebihnya bagus. Terimakasih'` | `'untuk anak jgd kursi nya kekecilan, susah mouse bergerak selebihnya bagus. terimakasih'` | `'untuk anak jgd kursi nya kekecilan susah mouse bergerak selebihnya bagus terimakasih'` | `'untuk anak jgd kursi nya kekecilan susah mouse bergerak selebihnya bagus terimakasih'` | `['untuk', 'anak', 'jgd', 'kursi', 'nya', 'kekecilan', 'susah', 'mouse', 'bergerak', 'selebihnya', 'bagus', 'terimakasih']` | `['anak', 'jgd', 'kursi', 'kekecilan', 'susah', 'mouse', 'bergerak', 'selebihnya', 'bagus']` | `['anak', 'jgd', 'kursi', 'kecil', 'susah', 'mouse', 'gerak', 'lebih', 'bagus']` | `'anak jgd kursi kecil susah mouse gerak lebih bagus'` |
| **3** | `'Materi yg disampaikan sangat bermanfaat, tapi penyampaiannya terlalu cepat.'` | `'materi yg disampaikan sangat bermanfaat, tapi penyampaiannya terlalu cepat.'` | `'materi yg disampaikan sangat bermanfaat tapi penyampaiannya terlalu cepat'` | `'materi yang disampaikan sangat bermanfaat tapi penyampaiannya terlalu cepat'` | `['materi', 'yang', 'disampaikan', 'sangat', 'bermanfaat', 'tapi', 'penyampaiannya', 'terlalu', 'cepat']` | `['materi', 'disampaikan', 'bermanfaat', 'penyampaiannya', 'cepat']` | `['materi', 'sampai', 'manfaat', 'sampai', 'cepat']` | `'materi sampai manfaat sampai cepat'` |
| **4** | `'Saran saya, mungkin bisa ditambah sesi tanya jawab di akhir pelatihan. Overall sudah oke'` | `'saran saya, mungkin bisa ditambah sesi tanya jawab di akhir pelatihan. overall sudah oke'` | `'saran saya mungkin bisa ditambah sesi tanya jawab di akhir pelatihan overall sudah oke'` | `'saran saya mungkin bisa ditambah sesi tanya jawab di akhir pelatihan overall sudah baik'` | `['saran', 'saya', 'mungkin', 'bisa', 'ditambah', 'sesi', 'tanya', 'jawab', 'di', 'akhir', 'pelatihan', 'overall', 'sudah', 'baik']` | `['ditambah', 'sesi', 'tanya', 'jawab', 'akhir', 'pelatihan', 'overall', 'baik']` | `['tambah', 'sesi', 'tanya', 'jawab', 'akhir', 'latih', 'overall', 'baik']` | `'tambah sesi tanya jawab akhir latih overall baik'` |
| **5** | `'Good job! Pertahankan kualitasnya. Gak ada komplain apa2.'` | `'good job! pertahankan kualitasnya. gak ada komplain apa2.'` | `'good job pertahankan kualitasnya gak ada komplain apa'` | `'good job pertahankan kualitasnya tidak ada komplain apa'` | `['good', 'job', 'pertahankan', 'kualitasnya', 'tidak', 'ada', 'komplain', 'apa']` | `['good', 'job', 'pertahankan', 'kualitasnya', 'tidak', 'komplain']` | `['good', 'job', 'tahan', 'kualitas', 'tidak', 'komplain']` | `'good job tahan kualitas tidak komplain'` |

Hasil dari keseluruhan proses ini adalah sebuah kolom baru, `teks_bersih`, dalam file `output/hasil_akhir.csv`. Kolom ini berisi representasi teks yang telah terstandarisasi dan siap untuk dianalisis pada tahap ekstraksi fitur TF-IDF.