# HASIL DAN PEMBAHASAN

## H. Pembahasan Hasil Penelitian

Sub-bab ini menyajikan pembahasan dan sintesis holistik terhadap keseluruhan hasil penelitian. Analisis yang disajikan bertujuan untuk menginterpretasi temuan-temuan kunci secara mendalam, menghubungkannya dengan kerangka metodologis yang telah diterapkan, serta merefleksikan implikasi teoretis dan praktis dari penelitian ini. Pembahasan ini disusun untuk memberikan pemahaman yang koheren mengenai bagaimana integrasi dari berbagai teknik Pemrosesan Bahasa Alami (NLP) dan *unsupervised learning* berhasil mentransformasi data umpan balik kualitatif menjadi wawasan yang terstruktur dan dapat ditindaklanjuti.

### 1. Sintesis Metodologi dan Temuan Kunci

Penelitian ini mengimplementasikan sebuah alur kerja analitis yang sistematis, dimulai dari pengolahan data mentah hingga ekstraksi wawasan strategis. Setiap tahapan memberikan kontribusi fundamental terhadap hasil akhir.

#### a. Transformasi Data Melalui Pra-pemrosesan dan Vektorisasi TF-IDF

Tahap pra-pemrosesan, sebagaimana dirinci pada Sub-bab 4.B, terbukti krusial dalam menangani heterogenitas dan *noise* pada data tekstual mentah. Implementasi serangkaian teknik seperti *case folding*, normalisasi kata menggunakan kamus eksternal (`kbba.txt`), dan *stemming* dengan algoritma Sastrawi berhasil menyeragamkan korpus data. Proses ini secara efektif mereduksi variasi leksikal dan morfologis yang tidak signifikan, sehingga memungkinkan representasi fitur yang lebih konsisten.

Selanjutnya, penerapan metode **TF-IDF** (Sub-bab 4.C) dengan konfigurasi parameter `min_df=2`, `max_df=0.8`, dan `ngram_range=(1, 2)` berhasil mentransformasikan korpus teks menjadi sebuah matriks vektor numerik berdimensi 2089. Penggunaan *n-gram* (khususnya *bigram*) terbukti sangat efektif dalam menangkap frasa-frasa kontekstual yang memiliki makna spesifik, seperti "kurang dingin", "uji kompetensi", dan "sangat baik", yang tidak akan tertangkap jika hanya menggunakan *unigram*. Matriks TF-IDF ini menjadi fondasi matematis untuk seluruh analisis hilir, termasuk *clustering* dan klasifikasi.

#### b. Identifikasi Pola Tematik Melalui Clustering K-Means

Penentuan jumlah klaster (K) yang optimal merupakan langkah kritis dalam analisis *clustering*. Dengan menggunakan **Metode Silhouette**, nilai K=9 diidentifikasi sebagai pilihan yang paling optimal secara kuantitatif dalam rentang yang diuji, meskipun menghasilkan skor yang relatif rendah (0.029). Skor ini, sebagaimana divalidasi oleh visualisasi PCA (Gambar 4.4), mengindikasikan adanya tumpang tindih yang signifikan antar klaster. Fenomena ini lazim terjadi pada data tekstual berdimensi tinggi, di mana batas-batas semantik antar topik seringkali bersifat kabur dan tidak kaku.

Meskipun demikian, analisis kualitatif terhadap *centroid* dan kata kunci pada setiap klaster (Sub-bab 4.D) menunjukkan bahwa algoritma K-Means berhasil mempartisi data ke dalam **sembilan kelompok tematik yang koheren dan dapat diinterpretasikan secara substantif**. Klaster-klaster yang terbentuk secara efektif memisahkan berbagai domain umpan balik, mulai dari isu yang sangat spesifik seperti **suhu AC (Klaster 6)** dan **konsumsi (Klaster 5)**, hingga topik yang lebih umum seperti **apresiasi terhadap materi (Klaster 3 dan 8)** dan **keluhan fasilitas umum (Klaster 4 dan 7)**. Keberhasilan ini menunjukkan bahwa K-Means, meskipun merupakan algoritma sederhana, mampu mengekstraksi struktur tematik yang tersembunyi dari data umpan balik yang kompleks.

### 2. Implikasi Strategis dari Analisis Sentimen dan Makna Lintas-Klaster

Integrasi hasil *clustering* dengan analisis sentimen dan klasifikasi makna (Sub-bab 4.E) menghasilkan wawasan yang paling signifikan dari penelitian ini. Analisis ini tidak hanya mengidentifikasi "apa" yang dibicarakan, tetapi juga "bagaimana" persepsi peserta terhadap topik tersebut.

-   **Identifikasi Titik Kritis dan Area Keunggulan:** Analisis sentimen lintas-klaster secara gamblang memetakan area-area yang memerlukan perhatian prioritas. **Klaster 6 (AC)**, **Klaster 5 (Konsumsi)**, dan **Klaster 4 (Fasilitas & Penyelenggaraan)** secara konsisten menunjukkan proporsi sentimen negatif yang tertinggi. Temuan ini memberikan bukti empiris yang kuat bagi manajemen untuk mengalokasikan sumber daya pada perbaikan aspek-aspek tersebut. Sebaliknya, **Klaster 2 (Uji Kompetensi)** dan **Klaster 8 (Kemudahan Pemahaman Materi)** menunjukkan dominasi sentimen positif dan netral-informatif, yang mengindikasikan bahwa aspek kurikulum dan pengajaran merupakan kekuatan utama dari program pelatihan ini.

-   **Validasi Kualitas Umpan Balik:** Hasil klasifikasi makna yang menunjukkan bahwa **90.31%** dari seluruh komentar bersifat "bermakna" merupakan temuan yang signifikan. Hal ini memvalidasi bahwa data umpan balik yang dikumpulkan memiliki nilai informasional yang tinggi. Lebih lanjut, analisis saran konstruktif (Sub-bab 4.F) berhasil mengidentifikasi komentar-komentar yang paling elaboratif dan dapat ditindaklanjuti, yang mayoritas terkonsentrasi pada klaster-klaster terkait fasilitas. Ini menunjukkan bahwa peserta tidak hanya mengeluh, tetapi juga aktif memberikan usulan solusi yang spesifik.

-   **Keandalan Model Analitis:** Kinerja sistem yang dievaluasi pada Sub-bab 4.G menunjukkan tingkat keandalan yang tinggi. Model **klasifikasi sentimen mencapai akurasi 99%**, membuktikan efektivitas pendekatan berbasis leksikon yang dikustomisasi. Sementara itu, model **klasifikasi makna mencapai akurasi 88%** dengan **Recall 99% untuk kelas "Bermakna"**. Desain ini secara sengaja memprioritaskan identifikasi semua umpan balik yang berpotensi penting, sejalan dengan tujuan utama sistem untuk tidak melewatkan informasi krusial.

### 3. Keterbatasan Penelitian dan Arah Pengembangan Selanjutnya

Meskipun penelitian ini berhasil mencapai tujuannya, terdapat beberapa keterbatasan yang perlu diakui dan dapat menjadi landasan untuk penelitian di masa depan:

1.  **Ketergantungan pada Pendekatan Statis:** Analisis sentimen dan makna yang berbasis pada leksikon dan aturan heuristik bersifat statis. Model ini mungkin tidak dapat menangkap nuansa bahasa yang lebih kompleks seperti sarkasme, ironi, atau konteks kalimat yang ambigu. Penelitian selanjutnya dapat mengeksplorasi penggunaan model *machine learning* atau *deep learning* (misalnya, LSTM, GRU, atau arsitektur berbasis Transformer seperti BERT) yang dilatih secara spesifik pada data Monev untuk meningkatkan pemahaman kontekstual.

2.  **Optimalitas Algoritma Clustering:** Seperti yang ditunjukkan oleh Silhouette Score yang rendah dan visualisasi PCA, K-Means menghasilkan klaster dengan tingkat tumpang tindih yang cukup tinggi. Algoritma *clustering* alternatif seperti **DBSCAN**, yang dapat mengidentifikasi klaster dengan bentuk yang lebih arbitrer dan menangani *noise*, atau pendekatan berbasis *topic modeling* seperti **Latent Dirichlet Allocation (LDA)**, dapat dieksplorasi untuk menghasilkan pengelompokan yang lebih tajam dan terdefinisi dengan baik.

3.  **Generalisasi Model:** Sistem yang dibangun, terutama kamus normalisasi dan leksikon sentimen yang dikustomisasi, dirancang secara spesifik untuk konteks data umpan balik dari BBPSDMP Kominfo Makassar. Penerapannya pada domain atau institusi lain kemungkinan besar akan memerlukan proses adaptasi dan kustomisasi ulang untuk memastikan relevansi dan akurasi.

### 4. Kesimpulan Umum

Secara keseluruhan, penelitian ini berhasil mendemonstrasikan kelayakan dan nilai praktis dari penerapan alur kerja analitik berbasis NLP dan K-Means untuk menganalisis data umpan balik kualitatif. Sistem yang dikembangkan mampu secara otomatis mentransformasi ribuan komentar tidak terstruktur menjadi wawasan yang terorganisir, terkuantifikasi, dan dapat ditindaklanjuti. Dengan mengidentifikasi tema-tema utama, mengukur sentimen publik terhadap setiap tema, dan menyaring saran-saran yang paling konstruktif, sistem ini menyediakan sebuah instrumen evaluasi berbasis data yang kuat. Luaran dari penelitian ini tidak hanya menjawab permasalahan teknis dalam analisis teks, tetapi juga memberikan kontribusi praktis yang nyata dalam mendukung siklus peningkatan kualitas layanan publik secara berkelanjutan dan efisien.