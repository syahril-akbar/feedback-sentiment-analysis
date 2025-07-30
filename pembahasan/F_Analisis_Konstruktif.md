# HASIL DAN PEMBAHASAN

## F. Analisis Saran Konstruktif

Setelah melakukan analisis sentimen dan klasifikasi makna, tahap analisis ini difokuskan untuk mengidentifikasi dan mengevaluasi umpan balik yang paling bernilai bagi penyelenggara, yaitu **saran yang konstruktif**. Tujuan utama dari analisis ini adalah untuk menyaring komentar-komentar yang tidak hanya mengidentifikasi masalah, tetapi juga memberikan usulan perbaikan, ide, atau elaborasi yang jelas. Dengan demikian, sistem dapat secara otomatis memprioritaskan masukan yang paling dapat ditindaklanjuti (*actionable*).

### 1. Metodologi Penilaian Skor Konstruktif

Untuk mengkuantifikasi tingkat kekonstruktifan sebuah komentar, sebuah model skoring heuristik diterapkan. Model ini memberikan **skor konstruktif** pada setiap komentar berdasarkan kombinasi beberapa faktor, antara lain:

1.  **Kehadiran Kata Kunci Pemicu Saran:** Identifikasi kata-kata yang secara eksplisit menunjukkan niat untuk memberi masukan, seperti "saran", "kritik", "sebaiknya", "kalau bisa", "mohon", dan "harapan".
2.  **Elaborasi dan Spesifisitas:** Panjang komentar dan jumlah poin-poin berbeda yang diangkat dalam satu komentar. Komentar yang lebih panjang dan merinci beberapa aspek diasumsikan memiliki tingkat elaborasi yang lebih tinggi.
3.  **Identifikasi Masalah dan Solusi:** Sistem memberikan bobot lebih tinggi pada komentar yang tidak hanya menyebutkan masalah, tetapi juga secara implisit atau eksplisit mengusulkan solusi.

Skor yang dihasilkan merepresentasikan tingkat kekonstruktifan, di mana skor yang lebih tinggi menandakan bahwa komentar tersebut lebih spesifik, elaboratif, dan berpotensi tinggi untuk ditindaklanjuti oleh pihak penyelenggara.

### 2. Identifikasi dan Analisis Komentar Paling Konstruktif

Dari keseluruhan dataset, sistem berhasil mengidentifikasi sejumlah komentar yang memiliki skor konstruktif yang tinggi. Komentar-komentar ini kemudian diekstraksi ke dalam sebuah file terpisah (`saran_konstruktif.csv`) untuk memudahkan analisis mendalam. Tabel 4.8 menyajikan beberapa contoh representatif dari komentar dengan skor konstruktif tertinggi.

**Tabel 4.8:** Contoh Komentar dengan Skor Konstruktif Tertinggi

| Klaster | Sentimen | Skor | Contoh Komentar (Teks Asli) |
|:---:|:---|:---:|:---| 
| 7 | Negatif | 8 | "Tolong min, nextnya klo bisa ruangannya disediakan wifi. Klo pun gabisa wifi, paling tidak jaringan seluler cukup baik untuk hotspot. Agar pada saat penguploadan tugas dsb lebih cepat. Dan juga susunan kursi yang tidak begitu sempit" |
| 4 | Positif | 7 | "Saran saya ruangan yang digunakan itu sebaiknya yang dingin dikarenakan peserta pasti sangat kepanasan apalagi di hadapkan dengan Computer atau Laptop. Dan Colokan Kabel sebaiknya di perbanyak dan di sediakan tanpa perlu peserta membawa dari rumah. Dan Fasilitas Jaringan atau Wifi sebaiknya juga di berikan karena saat pelatihan tentunya peserta pasti sering berinteraksi dengan Internet untuk keperluan pelatihan dll." |
| 7 | Negatif | 6 | "Kritik nya posisi nya tdk menghadapi ke layar proyektor sarannya posisi kursi dan meja menghadap proyektor" |
| 4 | Negatif | 6 | "Untuk ruangan yang digunakan pada OKM Kelas A, Kipas angin tidak semuanya berfungsi, sehingga peserta pelatihan ada yang kepanasan. Sarannya, kedepannya mungkin ruangan yang akan digunakan pada saat pelatihan harus di cek dengan baik sebelum kegiatan dilaksanakan guna untuk kenyamanan peserta." |
| 7 | Netral | 5 | "Jaringan tidak memadai hari pertama jaringan kabel LAN nya berfungsi, namun pada hari ke 2 dan seterusnya, jaringan LAN nya sudah tidak berfungsi lagi, mohon untuk menyiapkan jaringannya juga, karena daerahnya yg kurang memadai jika jaringan seluler" |
| 7 | Negatif | 5 | "Berikan fasilitas yang memadai. Jaringan WIFI sangat buruk, ac terkasang tidak dingin, tidak disediakan colokan listrik, akses menuju lt atas sangat susah (tangga)." |

#### Analisis Kualitatif Terhadap Saran Konstruktif:

-   **Spesifisitas Masalah:** Komentar dengan skor tertinggi cenderung sangat spesifik. Contohnya, komentar dengan skor 8 tidak hanya meminta "WiFi", tetapi juga memberikan alternatif ("jaringan seluler cukup baik") dan justifikasi yang jelas ("agar penguploadan tugas lebih cepat"). Demikian pula, komentar dengan skor 6 secara presisi mengidentifikasi masalah tata letak kursi terhadap proyektor dan langsung memberikan solusinya.

-   **Multi-Aspek dalam Satu Umpan Balik:** Banyak dari saran dengan skor tinggi mencakup beberapa poin dalam satu komentar. Komentar dengan skor 7, misalnya, secara komprehensif membahas tiga isu utama: suhu ruangan (AC), ketersediaan colokan, dan akses internet (WiFi). Ini menunjukkan tingkat pemikiran yang mendalam dari peserta.

-   **Sentimen Tidak Selalu Negatif:** Sebuah temuan penting adalah bahwa saran konstruktif tidak selalu berasal dari komentar ber-sentimen negatif. Komentar dengan skor 7 dari Klaster 4 memiliki sentimen positif secara keseluruhan, namun tetap memberikan serangkaian saran perbaikan yang sangat detail. Hal ini membuktikan bahwa peserta yang puas pun dapat memberikan masukan berharga untuk peningkatan di masa depan.

-   **Korelasi dengan Klaster:** Mayoritas saran konstruktif dengan skor tertinggi berasal dari **Klaster 7 (Fasilitas Umum & Kekurangan)** dan **Klaster 4 (Fasilitas & Penyelenggaraan Pelatihan)**. Ini mengindikasikan bahwa aspek infrastruktur dan logistik merupakan area yang paling banyak mendapatkan perhatian dan saran perbaikan dari peserta. Isu-isu seperti konektivitas internet, ketersediaan colokan listrik, tata letak ruangan, dan kenyamanan termal (AC) menjadi perhatian utama.

Dengan demikian, penerapan modul analisis konstruktif ini terbukti efektif dalam menyaring dan memprioritaskan umpan balik. Sistem ini mampu mengidentifikasi saran-saran yang paling substantif dan dapat ditindaklanjuti, yang memungkinkan evaluator untuk fokus pada area perbaikan yang paling berdampak berdasarkan masukan riil dari peserta.