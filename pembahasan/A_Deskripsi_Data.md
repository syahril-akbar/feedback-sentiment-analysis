# HASIL DAN PEMBAHASAN

## A. Deskripsi Data Penelitian

Bab ini menyajikan hasil dan pembahasan dari analisis yang telah dilaksanakan. Paparan diawali dengan deskripsi data penelitian, yang merupakan tahap fundamental untuk mendefinisikan objek studi dan memberikan konteks bagi keseluruhan analisis.

Objek penelitian ini adalah korpus data sekunder berjenis tekstual yang bersumber dari kegiatan Monitoring dan Evaluasi (Monev) oleh Balai Besar Pengembangan Sumber Daya Manusia dan Penelitian (BBPSDMP) Kominfo Makassar. Data ini terdiri atas umpan balik kualitatif yang diberikan oleh peserta pelatihan sebagai respons terhadap program yang diselenggarakan. Tujuan utama dari pemanfaatan data ini adalah untuk mengekstraksi wawasan otentik yang dapat mendukung pengambilan keputusan berbasis data guna meningkatkan kualitas layanan di masa mendatang.

### 1. Karakteristik Dataset Penelitian

Dataset yang dianalisis dalam penelitian ini merupakan himpunan data tekstual yang diekstraksi dari file `kritik_saran.xlsx`. Sesuai dengan ruang lingkup yang ditetapkan, data ini mencakup respons dari peserta program *Vocational School Graduate Academy* (VSGA) yang berasal dari berbagai wilayah di Indonesia.

Berdasarkan analisis yang dijalankan oleh program, total data yang berhasil diolah adalah **2.601 _record_** individual. Setiap _record_ merepresentasikan satu unit umpan balik unik dari peserta. Struktur data mentah yang menjadi fokus analisis disajikan pada Tabel 4.1.

**Tabel 4.1: Struktur Data Mentah yang Dianalisis**

| Nama Kolom         | Tipe Data | Deskripsi                                                              |
|--------------------|-----------|------------------------------------------------------------------------|
| `kritik dan saran` | Teks      | Konten tekstual asli dari umpan balik yang diberikan peserta.          |

Variabel sentral dalam analisis ini adalah kolom `kritik dan saran`, yang berisi data linguistik tidak terstruktur (*unstructured linguistic data*) dalam Bahasa Indonesia. Data ini menunjukkan tingkat variabilitas yang tinggi dan mencakup beberapa tantangan komputasional, di antaranya:
*   **Variasi Leksikal:** Penggunaan kosakata yang beragam, mulai dari gaya bahasa formal hingga non-formal (bahasa gaul).
*   **Inkonsistensi Ortografis:** Adanya singkatan (contoh: "yg", "tdk"), kesalahan ketik (*typographical errors*), dan penggunaan tanda baca yang tidak standar.
*   **Komentar Bernilai Informasional Rendah:** Sebagaimana diidentifikasi dalam latar belakang masalah, terdapat proporsi data yang signifikan yang bersifat umum dan hanya merupakan formalitas (contoh: "bagus", "mantap"), sehingga tidak memberikan masukan yang substantif.

Karakteristik data yang kompleks dan tidak terstruktur ini memvalidasi urgensi penerapan metode Pemrosesan Bahasa Alami (*Natural Language Processing* - NLP). Korpus data mentah ini berfungsi sebagai input fundamental untuk keseluruhan alur kerja penelitian, yang meliputi tahap pra-pemrosesan, ekstraksi fitur dengan TF-IDF, pengelompokan topik dengan K-Means, dan analisis sentimen.


