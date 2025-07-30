# HASIL DAN PEMBAHASAN

## D. Pengelompokan Data Teks Menggunakan Algoritma K-Means

Tahap pengelompokan atau *clustering* merupakan fase sentral dalam penelitian ini, yang bertujuan untuk mengekstraksi dan mengidentifikasi pola-pola tematik yang terkandung dalam data kritik dan saran peserta. Dengan menerapkan algoritma K-Means pada representasi numerik data teks (vektor TF-IDF), penelitian ini berupaya mengelompokkan komentar-komentar yang memiliki kemiripan semantik secara objektif. Proses ini memungkinkan penemuan topik-topik utama yang menjadi perhatian peserta, tanpa memerlukan intervensi manual dalam penentuan kategori.

Algoritma K-Means bekerja secara iteratif untuk mempartisi himpunan data ke dalam sejumlah K klaster yang telah ditentukan sebelumnya. Setiap data point (dalam hal ini, setiap komentar yang telah ditransformasikan menjadi vektor TF-IDF) dialokasikan ke klaster yang memiliki *centroid* (pusat klaster) terdekat, yang diukur berdasarkan jarak Euclidean. Posisi *centroid* kemudian diperbarui secara iteratif berdasarkan rata-rata dari seluruh data point dalam klaster tersebut. Proses ini berlanjut hingga posisi *centroid* tidak lagi mengalami perubahan signifikan (konvergen), yang mengindikasikan bahwa konfigurasi klaster yang paling stabil telah tercapai.

### 1. Penentuan Jumlah Klaster Optimal (K) Menggunakan Metode Silhouette

Penentuan jumlah klaster (K) yang optimal adalah langkah fundamental sebelum eksekusi algoritma K-Means. Pemilihan nilai K yang tidak tepat dapat menghasilkan pengelompokan yang tidak representatif dan menyesatkan. Untuk mengatasi hal ini, penelitian ini mengadopsi **Metode Silhouette** sebagai metrik evaluasi kuantitatif untuk menentukan nilai K yang paling sesuai untuk struktur data yang ada.

Metode Silhouette mengukur seberapa baik sebuah objek data ditempatkan dalam klasternya. Skor ini dihitung berdasarkan dua metrik:
1.  **Kohesi (a):** Rata-rata jarak antara sebuah objek dengan semua objek lain dalam klaster yang sama. Nilai yang rendah menunjukkan kohesi yang baik.
2.  **Separasi (b):** Rata-rata jarak antara sebuah objek dengan semua objek dalam klaster tetangga terdekat. Nilai yang tinggi menunjukkan separasi yang baik.

*Silhouette Score* untuk satu sampel dihitung dengan formula `(b - a) / max(a, b)`. Skor ini berkisar antara -1 hingga 1, di mana nilai yang mendekati 1 mengindikasikan bahwa objek tersebut sangat cocok dengan klasternya dan terpisah dengan baik dari klaster lain. Nilai yang mendekati 0 menunjukkan adanya tumpang tindih antar klaster, sementara nilai negatif menandakan kemungkinan objek tersebut salah diklasifikasikan.

Dalam analisis ini, sistem melakukan evaluasi *Silhouette Score* untuk rentang K dari 2 hingga 10. Hasil evaluasi tersebut divisualisasikan pada Gambar 4.2.

![Silhouette Scores](..\output\silhouette_scores.png)
**Gambar 4.2:** Grafik Silhouette Score untuk Penentuan K Optimal

Berdasarkan grafik pada Gambar 4.2, nilai **K = 9** menghasilkan *Silhouette Score* tertinggi, yaitu **0.029**. Meskipun skor ini relatif rendah dan tidak mendekati 1, hal ini merupakan fenomena yang lazim dalam analisis data teks. Sifat data tekstual yang kaya akan variasi linguistik, sinonim, dan konteks yang tumpang tindih secara inheren menyulitkan pencapaian separasi klaster yang sempurna. Dengan demikian, K=9 dipilih sebagai jumlah klaster terbaik secara kuantitatif dalam rentang yang diuji untuk analisis lebih lanjut.

### 2. Distribusi Data pada Setiap Klaster

Setelah menetapkan K=9, algoritma K-Means diaplikasikan pada keseluruhan data vektor TF-IDF. Hasilnya, setiap komentar (dokumen) dialokasikan ke salah satu dari sembilan klaster yang terbentuk. Distribusi ini memberikan gambaran awal mengenai volume dan dominasi topik-topik yang ada dalam umpan balik.

![Jumlah Komentar per Klaster](..\output\jumlah_komentar_per_klaster.png)
**Gambar 4.3:** Visualisasi Distribusi Jumlah Komentar per Klaster

Data kuantitatif dari distribusi tersebut dirangkum dalam Tabel 4.3. Terlihat bahwa sebaran komentar antar klaster sangat tidak merata. **Klaster 7** menjadi klaster yang paling dominan dengan menampung **1328 komentar (49.85%)**, mengindikasikan adanya sebuah tema yang sangat umum dan sering dibicarakan oleh peserta. Sebaliknya, **Klaster 0** merupakan yang terkecil dengan hanya **20 komentar (0.75%)**. Varians yang signifikan dalam ukuran klaster ini menunjukkan bahwa beberapa topik bersifat sangat spesifik (niche), sementara topik lainnya bersifat lebih general dan menjadi perhatian mayoritas peserta.

**Tabel 4.3:** Distribusi Jumlah Komentar per Klaster

| Klaster | Jumlah Komentar | Persentase (%) |
|:-------:|:---------------:|:--------------:|
| 0       | 20              | 0.75%          |
| 1       | 296             | 11.11%         |
| 2       | 161             | 6.04%          |
| 3       | 145             | 5.44%          |
| 4       | 250             | 9.38%          |
| 5       | 225             | 8.45%          |
| 6       | 74              | 2.78%          |
| 7       | 1328            | 49.85%         |
| 8       | 102             | 3.83%          |
| **Total** | **2601**        | **100%**       |

*Catatan: Total data yang berhasil diklusterisasi adalah 2601, sesuai dengan laporan analisis program.*

### 3. Analisis dan Interpretasi Tematik Klaster

Untuk memahami makna substantif dari setiap klaster, dilakukan analisis kualitatif terhadap kata kunci (*keywords*) yang paling representatif. Kata kunci ini merupakan istilah-istilah dengan bobot TF-IDF tertinggi yang secara efektif merangkum inti topik dari setiap klaster. Analisis ini diperkaya dengan merujuk pada contoh-contoh komentar aktual dari setiap klaster untuk validasi dan pendalaman interpretasi.

#### **Klaster 0: Permintaan Penggantian Item Spesifik**
- **Kata Kunci Utama:** `ganti`, `menu`, `buah ganti`, `kursi`, `menu ganti`.
- **Analisis:** Klaster ini secara spesifik menghimpun komentar yang berisi permintaan atau saran untuk **mengganti** item-item tertentu. Contohnya, *"Ganti kursinya"* dan *"Saran saya kursinya diganti, pakai kursi yang ada gabus"*, menunjukkan ketidakpuasan terhadap fasilitas kursi. Selain itu, permintaan seperti *"agar membantu mengurangi penggunaan kantong plastik boleh di ganti dengan paper bag"* juga masuk dalam kategori ini, menyoroti saran penggantian untuk alasan lingkungan.
- ![Word Cloud Klaster 0](..\output\wordcloud_klaster_0.png)

#### **Klaster 1: Umpan Balik Terhadap Materi dan Harapan Peningkatan**
- **Kata Kunci Utama:** `materi`, `lebih`, `baik`, `lebih baik`, `ajar`.
- **Analisis:** Klaster ini berfokus pada evaluasi terhadap **materi ajar dan proses pembelajaran**. Komentar di dalamnya mencakup harapan umum seperti *"Semoga kedepannya lebih baik lagi"* dan saran yang lebih spesifik terkait penyampaian materi, misalnya *"lebih bagus jika menampilkan slide materi menggunakan proyektor"*. Tema ini mencerminkan keinginan peserta untuk peningkatan kualitas dan efektivitas penyampaian materi di masa depan.
- ![Word Cloud Klaster 1](..\output\wordcloud_klaster_1.png)

#### **Klaster 2: Evaluasi Terkait Uji Kompetensi**
- **Kata Kunci Utama:** `uji`, `kompetensi`, `uji kompetensi`, `baik`, `assessor`.
- **Analisis:** Klaster ini secara eksklusif berisi umpan balik yang berkaitan dengan **pelaksanaan uji kompetensi**. Topik yang dibahas meliputi kesesuaian materi pelatihan dengan soal ujian (*"Baiknya materi bersambung dengan tes yang akan diujikan"*) dan apresiasi terhadap penguji (*"para pengajar dan penguji sudah sangat baik dalam menjelaskan dan menguji peserta"*). Klaster ini sangat penting untuk mengevaluasi relevansi kurikulum pelatihan terhadap standar sertifikasi.
- ![Word Cloud Klaster 2](..\output\wordcloud_klaster_2.png)

#### **Klaster 3: Apresiasi dan Kepuasan Secara Umum**
- **Kata Kunci Utama:** `sangat`, `sangat baik`, `baik`, `ajar`, `materi`.
- **Analisis:** Berbeda dengan klaster lain yang lebih spesifik, klaster ini menghimpun ekspresi **kepuasan dan apresiasi secara umum**. Komentar seperti *"Sejauh ini sudah sangat baik"* dan *"Alhmdulillah pelatihan sangat menyenangkan dengan mentor mentor yg handal"* menunjukkan sentimen positif yang kuat terhadap keseluruhan pengalaman pelatihan, baik dari segi fasilitas maupun kualitas pengajar.
- ![Word Cloud Klaster 3](..\output\wordcloud_klaster_3.png)

#### **Klaster 4: Umpan Balik Terkait Fasilitas dan Penyelenggaraan Pelatihan**
- **Kata Kunci Utama:** `latih`, `fasilitas`, `ruang`, `fasilitas latih`, `wifi`.
- **Analisis:** Klaster ini menjadi wadah untuk komentar mengenai **fasilitas umum dan logistik penyelenggaraan pelatihan**. Topik yang dominan adalah permintaan penyediaan akses internet (WiFi) seperti *"di sediakan wifi bagi peserta"*, serta saran terkait lokasi dan jangkauan pelatihan seperti *"Semoga Pelatihan Ini Terus di Adakan"* dan *"memperbanyak pelatihan seperti dan jika bisa ke beberapa daerah juga"*.
- ![Word Cloud Klaster 4](..\output\wordcloud_klaster_4.png)

#### **Klaster 5: Umpan Balik Terkait Konsumsi (Makanan dan Minuman)**
- **Kata Kunci Utama:** `makan`, `saji`, `enak`, `tidak`, `basi`.
- **Analisis:** Klaster ini sangat spesifik membahas tentang **konsumsi** yang disediakan selama pelatihan. Isinya beragam, mulai dari keluhan tentang kualitas makanan (*"Makanannya basi"*, *"Makanan ada yang terlalu asin"*) hingga saran perbaikan seperti *"Tingkatkan rasa makanannya"* dan *"pengantaran makanan pada saat istirahat mkan siang kadang telat"*.
- ![Word Cloud Klaster 5](..\output\wordcloud_klaster_5.png)

#### **Klaster 6: Evaluasi Suhu Ruangan (AC)**
- **Kata Kunci Utama:** `dingin`, `ac`, `ac dingin`, `kurang dingin`, `ac kurang`.
- **Analisis:** Klaster ini secara khusus mengelompokkan semua komentar yang berhubungan dengan **suhu pendingin ruangan (AC)**. Terdapat dua kutub opini: keluhan bahwa ruangan terlalu panas (*"acnya kurang dingin"*) dan keluhan bahwa ruangan terlalu dingin (*"ruangan nya nyaman, bersih tapi ac nya dingin sekali"*). Ini menunjukkan perlunya penyesuaian suhu yang lebih optimal.
- ![Word Cloud Klaster 6](..\output\wordcloud_klaster_6.png)

#### **Klaster 7: Umpan Balik Umum Terkait Kekurangan Fasilitas dan Lain-lain**
- **Kata Kunci Utama:** `kurang`, `tidak`, `ruang`, `tahan`, `lebih`.
- **Analisis:** Sebagai klaster terbesar, klaster ini berfungsi sebagai penampung umpan balik yang sangat beragam, namun sering kali mengandung kata kunci bernada kekurangan seperti "kurang" dan "tidak". Topiknya mencakup berbagai aspek, mulai dari fasilitas fisik seperti pencahayaan (*"Pencahayaan ruangan kurang"*), meja dan kursi (*"Meja tidak sesuai untuk kebetuhan desain"*), hingga ketersediaan jaringan dan colokan listrik. Besarnya klaster ini menandakan banyaknya area perbaikan minor yang bersifat heterogen.
- ![Word Cloud Klaster 7](..\output\wordcloud_klaster_7.png)

#### **Klaster 8: Apresiasi Terhadap Kemudahan Pemahaman Materi**
- **Kata Kunci Utama:** `mudah`, `mudah paham`, `paham`, `materi`, `materi mudah`.
- **Analisis:** Klaster ini mirip dengan Klaster 3 namun lebih spesifik pada aspek **kemudahan pemahaman materi**. Komentar seperti *"Penyampaian materi yang sangat mudah untuk dimengerti"* dan *"Materi yang telah disampaikan pengajar mudah dipahami"* secara eksplisit memberikan pujian kepada pengajar atas kemampuan mereka dalam menyederhanakan dan menjelaskan materi secara efektif.
- ![Word Cloud Klaster 8](..\output\wordcloud_klaster_8.png)

### 4. Visualisasi Sebaran Klaster Menggunakan PCA (Principal Component Analysis)

Untuk mendapatkan intuisi visual mengenai hubungan dan separasi antar klaster, teknik reduksi dimensi *Principal Component Analysis* (PCA) diaplikasikan. PCA mentransformasikan data dari ruang fitur TF-IDF yang berdimensi tinggi (2089 dimensi) ke dalam ruang dua dimensi (2D), yang memungkinkan untuk visualisasi dalam bentuk plot sebar.

![Visualisasi PCA Clusters](..\output\pca_clusters.png)
**Gambar 4.4:** Visualisasi Sebaran Klaster dalam Ruang 2D Hasil Reduksi PCA

Plot PCA pada Gambar 4.4 merepresentasikan setiap komentar sebagai sebuah titik, di mana warna titik menandakan keanggotaan klasternya. Visualisasi ini secara empiris mengkonfirmasi hasil *Silhouette Score* yang rendah. Terlihat adanya **tumpang tindih (overlap) yang signifikan** antar klaster, terutama pada klaster-klaster besar yang bersifat umum seperti Klaster 1, 4, dan 7. Hal ini mengindikasikan bahwa banyak komentar yang memiliki kemiripan leksikal meskipun membahas nuansa topik yang sedikit berbeda.

Meskipun demikian, beberapa pola dapat teridentifikasi. Klaster-klaster yang lebih spesifik, seperti **Klaster 6 (AC)** dan **Klaster 0 (Ganti)**, tampak membentuk sub-grup yang sedikit lebih terkonsentrasi, meskipun masih terintegrasi dalam awan data yang besar. Visualisasi ini menegaskan kompleksitas data umpan balik tekstual dan menunjukkan bahwa meskipun tema-tema utama dapat diidentifikasi, batas antar tema seringkali tidak kaku dan saling berkaitan.