# HASIL DAN PEMBAHASAN

## E. Analisis Sentimen dan Klasifikasi Makna

Setelah proses pengelompokan berhasil mengidentifikasi tema-tema utama dari data umpan balik, tahap analisis selanjutnya adalah mengukur polaritas sentimen dan nilai informasional (makna) dari setiap komentar. Analisis ini merupakan komponen krusial untuk menjawab rumusan masalah penelitian, yaitu bagaimana sistem dapat secara otomatis membedakan antara umpan balik yang substantif dan yang bersifat formalitas, serta mengukur kecenderungan opini publik terhadap topik-topik yang telah diidentifikasi.

Untuk mencapai tujuan ini, dua pendekatan komputasional diterapkan:
1.  **Analisis Sentimen Berbasis Leksikon:** Setiap komentar dievaluasi untuk menentukan polaritas emosionalnya (positif, negatif, atau netral). Metode ini bekerja dengan menghitung skor sentimen kumulatif berdasarkan leksikon sentimen berbahasa Indonesia yang telah teruji (InSet), yang berisi daftar kata dengan bobot polaritasnya masing-masing.
2.  **Klasifikasi Makna Berbasis Heuristik:** Setiap komentar diklasifikasikan sebagai "bermakna" atau "tidak bermakna". Klasifikasi ini tidak hanya mengandalkan sentimen, tetapi juga pada kriteria heuristik seperti panjang teks dan keberadaan kata-kata kunci yang mengindikasikan saran atau kritik yang elaboratif. Tujuannya adalah untuk menyaring komentar yang paling informatif dan berpotensi untuk ditindaklanjuti.

### 1. Distribusi Sentimen dan Makna pada Keseluruhan Data

Analisis awal dilakukan pada keseluruhan dataset untuk memperoleh gambaran umum mengenai persepsi dan kualitas umpan balik dari para peserta.

#### a. Analisis Sentimen Global
Distribusi sentimen secara keseluruhan mengindikasikan tendensi umum dari umpan balik yang diberikan. Hasil kuantitatif disajikan pada Tabel 4.5 dan divisualisasikan pada Gambar 4.5.

**Tabel 4.5:** Distribusi Sentimen Keseluruhan

| Kategori Sentimen | Jumlah Komentar | Persentase (%) |
|:------------------|:---------------:|:--------------:|
| Positif           | 971             | 37.18%         |
| Netral            | 910             | 34.87%         |
| Negatif           | 730             | 27.95%         |
| **Total**         | **2611**        | **100%**       |

![Distribusi Sentimen](..\output\distribusi_sentimen.png)
**Gambar 4.5:** Diagram Pie Distribusi Sentimen Keseluruhan

Hasil analisis menunjukkan bahwa sentimen **positif (37.18%)** merupakan polaritas yang paling dominan, namun tidak mayoritas secara absolut. Angka ini diikuti oleh sentimen **netral (34.87%)** dan **negatif (27.95%)** yang juga memiliki proporsi signifikan. Temuan ini mengindikasikan bahwa data umpan balik bersifat heterogen dan seimbang, mengandung tidak hanya apresiasi tetapi juga volume kritik dan pernyataan faktual yang substansial, yang sangat berharga untuk evaluasi.

#### b. Analisis Makna Global
Klasifikasi makna bertujuan untuk memisahkan komentar yang berisi informasi substantif dari yang bersifat umum atau formalitas. Hasilnya disajikan pada Tabel 4.6 dan Gambar 4.6.

**Tabel 4.6:** Distribusi Komentar Berdasarkan Kategori Makna

| Kategori Makna  | Jumlah Komentar | Persentase (%) |
|:----------------|:---------------:|:--------------:|
| Bermakna        | 2412            | 90.31%         |
| Tidak Bermakna  | 252             | 9.69%          |
| **Total**       | **2664**        | **100%**       |

![Distribusi Makna](..\output\distribusi_makna.png)
**Gambar 4.6:** Diagram Pie Distribusi Makna Komentar

Secara signifikan, analisis menunjukkan bahwa **90.31%** dari seluruh komentar diklasifikasikan sebagai **"bermakna"**. Angka ini membantah asumsi awal bahwa sebagian besar umpan balik mungkin bersifat sekadarnya. Sebaliknya, ini membuktikan bahwa mayoritas peserta meluangkan waktu untuk memberikan masukan yang cukup elaboratif, terlepas dari polaritas sentimennya. Hanya sebagian kecil (9.69%) yang merupakan komentar sangat singkat atau tidak informatif (misalnya, "baik", "terima kasih").

### 2. Analisis Sentimen dan Makna Lintas-Klaster

Analisis yang paling mendalam adalah dengan mengintegrasikan hasil *clustering* dengan analisis sentimen dan makna. Dengan membedah distribusi sentimen dan makna di dalam setiap klaster topik, kita dapat mengidentifikasi korelasi antara area pembahasan spesifik dengan persepsi peserta.

![Distribusi Sentimen per Klaster](..\output\distribusi_sentimen_per_klaster.png)
**Gambar 4.7:** Visualisasi Distribusi Sentimen per Klaster

![Distribusi Makna per Klaster](..\output\distribusi_makna_per_klaster.png)
**Gambar 4.8:** Visualisasi Distribusi Makna per Klaster

Data kuantitatif dari analisis lintas-klaster ini dirangkum dalam Tabel 4.7, yang menyajikan temuan-temuan kunci sebagai berikut:

**Tabel 4.7:** Analisis Sentimen dan Makna Lintas-Klaster

| Klaster | Interpretasi Tema | Sentimen Dominan | % Komentar Bermakna |
|:---:|:---|:---|:---:|
| 0 | Permintaan Penggantian | Netral (65.0%) | 100.0% |
| 1 | Umpan Balik Materi & Harapan | Positif (58.78%) | 96.96% |
| 2 | Evaluasi Uji Kompetensi | Positif (88.82%) | 99.38% |
| 3 | Apresiasi Umum | Positif (51.03%) | 100.0% |
| 4 | Fasilitas & Penyelenggaraan | Negatif (32.4%) | 98.8% |
| 5 | Konsumsi (Makanan/Minuman) | Negatif (38.67%) | 96.44% |
| 6 | Suhu Ruangan (AC) | Negatif (50.0%) | 86.49% |
| 7 | Fasilitas Umum & Kekurangan | Netral (37.88%) | 83.36% |
| 8 | Kemudahan Pemahaman Materi | Netral (74.51%) | 100.0% |

Dari data di atas, dapat ditarik beberapa kesimpulan strategis:

-   **Area Kritik Utama (Hotspots):**
    -   **Klaster 6 (Suhu Ruangan/AC):** Menjadi sumber ketidakpuasan paling signifikan dengan **50.0%** sentimen negatif. Ini menandakan masalah kenyamanan termal yang perlu menjadi prioritas perbaikan.
    -   **Klaster 5 (Konsumsi):** Juga menunjukkan tingkat sentimen negatif yang tinggi (**38.67%**), menyoroti isu-isu terkait kualitas dan penyajian makanan.
    -   **Klaster 4 (Fasilitas & Penyelenggaraan):** Meskipun tidak didominasi sentimen negatif, klaster ini memiliki persentase negatif yang cukup tinggi (**32.4%**), terutama didorong oleh keluhan terkait ketiadaan WiFi dan logistik lainnya.

-   **Area Apresiasi Tertinggi:**
    -   **Klaster 2 (Uji Kompetensi):** Secara luar biasa, klaster ini didominasi oleh sentimen **positif (88.82%)**. Ini merupakan indikator kuat bahwa peserta merasa puas dengan pelaksanaan, relevansi, dan profesionalisme pada tahap uji kompetensi.
    -   **Klaster 1 (Umpan Balik Materi):** Dengan **58.78%** sentimen positif, menunjukkan bahwa secara umum materi dan metode pengajaran diterima dengan baik oleh peserta.

-   **Komentar Netral yang Informatif:**
    -   **Klaster 8 (Kemudahan Pemahaman Materi):** Didominasi oleh sentimen **netral (74.51%)** namun memiliki **100%** komentar bermakna. Ini menunjukkan bahwa peserta cenderung memberikan umpan balik faktual mengenai pemahaman mereka (*"Materi mudah dipahami"*) tanpa muatan emosi yang kuat, yang merupakan data evaluasi yang sangat berharga.
    -   **Klaster 0 (Permintaan Penggantian):** Juga didominasi sentimen netral (**65.0%**) dengan **100%** komentar bermakna. Peserta secara langsung menyatakan permintaan (*"Ganti kursinya"*) yang bersifat solutif dan langsung ke tujuan.

-   **Tingkat Kebermanaan yang Tinggi:** Perlu dicatat bahwa hampir seluruh klaster menunjukkan persentase komentar "bermakna" di atas 83%. Ini memperkuat kesimpulan bahwa umpan balik yang diberikan sangat kaya akan informasi yang dapat ditindaklanjuti.

Secara keseluruhan, analisis sentimen dan makna yang dilapisi di atas hasil clustering berhasil memberikan pemahaman yang multidimensional. Sistem ini tidak hanya mengidentifikasi "apa" yang dibicarakan (topik), tetapi juga "bagaimana" peserta merasakannya (sentimen) dan "seberapa informatif" umpan balik tersebut (makna), sehingga menghasilkan wawasan yang komprehensif dan dapat diandalkan untuk evaluasi program.