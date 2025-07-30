# HASIL DAN PEMBAHASAN

## C. Ekstraksi Fitur dan Pembobotan Kata Menggunakan TF-IDF

Setelah melalui serangkaian tahap pra-pemrosesan yang menghasilkan data teks yang bersih dan terstandardisasi, korpus data kritik dan saran masih berbentuk kualitatif. Algoritma *machine learning* seperti K-Means tidak dapat memproses data tekstual secara langsung; algoritma tersebut memerlukan input dalam format numerik. Oleh karena itu, diperlukan sebuah tahap fundamental yang disebut **ekstraksi fitur**, di mana data teks ditransformasikan menjadi representasi vektor numerik yang dapat diukur dan dianalisis secara matematis.

Dalam penelitian ini, metode yang diimplementasikan untuk ekstraksi fitur adalah **Term Frequency-Inverse Document Frequency (TF-IDF)**. Metode ini dipilih karena kemampuannya yang telah terbukti dalam mengkuantifikasi signifikansi sebuah term (kata atau frasa) dalam sebuah dokumen relatif terhadap posisinya di dalam keseluruhan koleksi dokumen (korpus).

### 1. Konsep Dasar TF-IDF

TF-IDF merupakan sebuah teknik statistik yang memberikan bobot pada setiap term. Bobot ini mencerminkan tingkat kepentingan term tersebut dalam sebuah dokumen spesifik serta keunikannya di seluruh korpus. Perhitungan bobot ini didasarkan pada dua komponen utama:

*   **_Term Frequency_ (TF):** Merepresentasikan frekuensi kemunculan sebuah term dalam satu dokumen (komentar). Logikanya adalah term yang muncul lebih sering dalam sebuah komentar memiliki kontribusi yang lebih besar terhadap makna atau topik utama dari komentar tersebut.
*   **_Inverse Document Frequency_ (IDF):** Mengukur tingkat kelangkaan atau keunikan sebuah term di seluruh korpus data. Term yang umum dan muncul di banyak dokumen (misalnya, "yang", "dan", "di", meskipun sebagian besar sudah dihapus oleh *stopword removal*) akan menerima bobot IDF yang rendah. Sebaliknya, term yang jarang muncul dan hanya terdapat pada beberapa dokumen spesifik akan menerima bobot IDF yang tinggi, menandakan bahwa term tersebut memiliki daya diskriminatif yang lebih kuat dan lebih informatif.

Skor akhir TF-IDF untuk sebuah term dihitung dengan mengalikan nilai TF dan IDF (TF × IDF). Hasil dari proses ini adalah setiap komentar diubah menjadi sebuah **vektor fitur**, di mana setiap dimensi vektor merepresentasikan sebuah term unik dari kosakata korpus, dan nilai pada dimensi tersebut adalah skor TF-IDF dari term yang bersangkutan.

### 2. Implementasi dan Konfigurasi Vektorisasi

Berdasarkan laporan analisis yang dihasilkan oleh sistem (`laporan_analisis.txt`), proses vektorisasi TF-IDF diimplementasikan menggunakan `TfidfVectorizer` dari pustaka Scikit-learn dengan konfigurasi parameter sebagai berikut:

*   **`min_df=2`**: Sebuah term (baik *unigram* maupun *bigram*) akan diabaikan jika frekuensi kemunculannya dalam keseluruhan dokumen (komentar) kurang dari 2. Parameter ini berfungsi sebagai filter untuk mengeliminasi term yang sangat langka, yang kemungkinan besar merupakan *noise*, kesalahan ketik (*typo*), atau istilah yang terlalu spesifik sehingga tidak signifikan secara statistik untuk analisis pengelompokan.
*   **`max_df=0.8`**: Sebuah term akan diabaikan jika muncul di lebih dari 80% dari total dokumen. Konfigurasi ini bertujuan untuk menyaring *stopword* kontekstual, yaitu term-term yang terlalu umum dalam konteks dataset ini sehingga tidak memiliki nilai informatif untuk membedakan antara satu klaster dengan klaster lainnya.
*   **`ngram_range=(1, 2)`**: Proses ekstraksi fitur tidak hanya mempertimbangkan term tunggal (*unigram*), tetapi juga pasangan term yang muncul secara berurutan (*bigram*). Penggunaan *bigram* sangat penting dalam analisis teks karena mampu menangkap frasa yang memiliki makna spesifik dan utuh, yang mungkin hilang jika hanya mengandalkan kata tunggal. Contoh *bigram* yang signifikan dari hasil analisis adalah "kurang dingin", "sangat baik", dan "uji kompetensi".

### 3. Hasil Vektorisasi

Implementasi dari proses vektorisasi dengan parameter di atas pada korpus data yang telah melalui pra-pemrosesan menghasilkan sebuah **matriks TF-IDF** dengan dimensi yang merepresentasikan jumlah dokumen (komentar) dan jumlah fitur unik. Berdasarkan laporan eksekusi program, proses ini berhasil mengidentifikasi **2089 fitur unik** dari keseluruhan korpus.

Dengan demikian, setiap komentar dalam dataset kini direpresentasikan sebagai sebuah vektor numerik dengan panjang 2089. Matriks TF-IDF yang dihasilkan ini bersifat *sparse* (mayoritas nilainya adalah nol), karena setiap komentar hanya mengandung sebagian kecil dari total fitur yang ada. Matriks numerik inilah yang menjadi input final dan fundamental untuk tahap analisis selanjutnya, yaitu **pengelompokan menggunakan algoritma K-Means**, yang akan dibahas pada sub-bab berikutnya.