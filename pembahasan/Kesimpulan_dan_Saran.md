# KESIMPULAN DAN SARAN

Bab ini menyajikan kesimpulan yang ditarik dari keseluruhan hasil analisis dan pembahasan yang telah diuraikan pada bab-bab sebelumnya. Selain itu, bab ini juga merumuskan sejumlah saran yang ditujukan bagi pihak penyelenggara (BBPSDMP Kominfo Makassar) untuk perbaikan di masa mendatang, serta bagi peneliti selanjutnya yang tertarik untuk mengembangkan penelitian di bidang serupa.

## A. Kesimpulan

Berdasarkan hasil analisis data dan pembahasan yang telah dilakukan, dapat ditarik beberapa kesimpulan utama sebagai berikut:

1.  **Implementasi Pra-pemrosesan dan Ekstraksi Fitur yang Efektif:** Rangkaian teknik pra-pemrosesan yang mencakup *case folding*, pembersihan teks, normalisasi kata, tokenisasi, pembuangan *stopwords*, dan *stemming* berhasil mentransformasi data umpan balik mentah yang tidak terstruktur menjadi format yang bersih dan terstandarisasi. Representasi teks menggunakan pembobotan **TF-IDF** dengan parameter `min_df=2`, `max_df=0.8`, dan `ngram_range=(1, 2)` terbukti efektif dalam mengkuantifikasi signifikansi kata dan frasa, menghasilkan **2089 fitur** yang menjadi dasar analisis kuantitatif selanjutnya.

2.  **Identifikasi Topik Utama Melalui Clustering K-Means:** Algoritma K-Means, dengan jumlah klaster optimal **K=9** yang ditentukan melalui metode *Silhouette Score*, berhasil mengelompokkan 2.601 komentar ke dalam sembilan klaster tematik yang dapat diinterpretasikan secara kualitatif. Meskipun terdapat tumpang tindih antar klaster, pengelompokan ini secara efektif memisahkan berbagai domain umpan balik, seperti **keluhan fasilitas (Klaster 4, 6, 7)**, **apresiasi terhadap materi dan pengajar (Klaster 1, 2, 3, 8)**, dan **umpan balik terkait konsumsi (Klaster 5)**.

3.  **Analisis Sentimen dan Makna Memberikan Wawasan Mendalam:** Pemanfaatan teknik NLP untuk analisis sentimen dan klasifikasi makna berhasil memberikan dimensi pemahaman yang lebih kaya.
    *   **Analisis Sentimen** menunjukkan bahwa umpan balik peserta bersifat seimbang, dengan proporsi sentimen **positif (37.18%)**, **netral (34.87%)**, dan **negatif (27.95%)**. Kinerja model sentimen berbasis leksikon terbukti sangat andal dengan **akurasi 99%**.
    *   **Klasifikasi Makna** mengungkapkan bahwa mayoritas umpan balik (**90.31%**) bersifat **"bermakna"**, yang mengindikasikan tingginya kualitas dan substansi masukan dari peserta. Model klasifikasi makna mencapai **akurasi 88%** dengan **Recall 99%** untuk kelas "bermakna", memastikan bahwa hampir semua umpan balik penting berhasil ditangkap oleh sistem.

4.  **Identifikasi Area Prioritas untuk Peningkatan Layanan:** Integrasi hasil *clustering* dan analisis sentimen secara gamblang mengidentifikasi titik-titik kritis yang memerlukan perhatian. Aspek **fasilitas**, khususnya terkait **konektivitas internet, ketersediaan colokan listrik, dan suhu AC**, menjadi area dengan keluhan paling dominan dan sentimen negatif tertinggi. Sebaliknya, aspek **materi, metode pengajaran, dan pelaksanaan uji kompetensi** merupakan kekuatan utama program yang perlu dipertahankan.

## B. Saran

Berdasarkan kesimpulan yang telah diuraikan, berikut adalah beberapa saran yang dapat diajukan:

### 1. Saran untuk Pihak Penyelenggara (BBPSDMP Kominfo Makassar)

*   **Prioritas Perbaikan Fasilitas:** Mengingat tingginya volume keluhan dan sentimen negatif terkait fasilitas, disarankan untuk memprioritaskan investasi pada:
    *   Peningkatan infrastruktur jaringan dengan menyediakan **akses WiFi yang stabil** bagi peserta.
    *   Penambahan **jumlah colokan listrik** di setiap ruang pelatihan.
    *   Optimalisasi **sistem pendingin ruangan (AC)** untuk menjaga kenyamanan termal.
*   **Peningkatan Kualitas Konsumsi:** Melakukan evaluasi terhadap vendor penyedia konsumsi untuk memastikan kualitas, rasa, dan ketepatan waktu penyajian makanan dan minuman.
*   **Mempertahankan Kualitas Pengajaran:** Terus mendukung dan mengembangkan kualitas para pengajar dan instruktur, karena aspek ini secara konsisten menerima apresiasi tertinggi dari peserta.
*   **Pemanfaatan Sistem untuk Evaluasi Berkelanjutan:** Mengadopsi sistem analisis umpan balik ini sebagai alat bantu standar dalam siklus evaluasi program. Luaran seperti `saran_konstruktif.csv` dan `statistik_per_klaster.csv` dapat digunakan sebagai dasar yang objektif untuk pengambilan keputusan berbasis data.

### 2. Saran untuk Penelitian Selanjutnya

*   **Eksplorasi Model Machine Learning dan Deep Learning:** Untuk mengatasi keterbatasan pendekatan berbasis leksikon dan heuristik, penelitian selanjutnya dapat mengeksplorasi penggunaan model *machine learning* (seperti SVM atau Naive Bayes) atau *deep learning* (seperti LSTM atau arsitektur Transformer seperti BERT) yang dilatih secara spesifik pada data Monev untuk meningkatkan pemahaman kontekstual.
*   **Penggunaan Algoritma Clustering Alternatif:** Mengingat skor Silhouette yang relatif rendah, penelitian di masa depan dapat menguji algoritma *clustering* lain seperti **DBSCAN** atau pendekatan *topic modeling* seperti **Latent Dirichlet Allocation (LDA)** untuk melihat apakah metode tersebut dapat menghasilkan pengelompokan yang lebih tajam dan terpisah dengan lebih baik.
*   **Generalisasi Model:** Membangun model yang dapat digeneralisasi untuk domain atau dataset yang berbeda dengan melakukan pelatihan pada korpus data yang lebih beragam dan mengembangkan kamus normalisasi serta leksikon sentimen yang lebih komprehensif.
