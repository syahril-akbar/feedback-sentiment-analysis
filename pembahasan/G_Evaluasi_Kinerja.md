# HASIL DAN PEMBAHASAN

## G. Evaluasi Kinerja Sistem

Tahap evaluasi kinerja merupakan langkah esensial untuk memvalidasi reliabilitas dan akurasi dari model-model klasifikasi yang telah dikembangkan. Pada tahap ini, dilakukan pengukuran kuantitatif terhadap kemampuan sistem dalam menjalankan dua tugas utamanya: **klasifikasi sentimen** dan **klasifikasi makna**. Evaluasi ini dilakukan dengan membandingkan hasil prediksi yang dihasilkan oleh sistem terhadap sebuah *dataset* uji (data uji manual) yang telah dilabeli oleh pakar sebagai *ground truth*. Dataset uji ini terdiri dari **191 komentar** yang dipilih untuk merepresentasikan distribusi data secara keseluruhan.

Metrik evaluasi standar dalam *machine learning* digunakan untuk mengukur performa, meliputi **Precision**, **Recall**, dan **F1-Score**. Metrik-metrik ini memberikan gambaran yang komprehensif mengenai keandalan model pada setiap kelas.

-   **Precision** mengukur tingkat ketepatan dari prediksi positif yang dibuat oleh model. (TP / (TP + FP))
-   **Recall** (atau Sensitivitas) mengukur kemampuan model untuk mengidentifikasi semua sampel positif yang relevan. (TP / (TP + FN))
-   **F1-Score** adalah rata-rata harmonik dari Precision dan Recall, memberikan skor tunggal yang menyeimbangkan kedua metrik tersebut. (2 * (Precision * Recall) / (Precision + Recall))

### 1. Evaluasi Kinerja Klasifikasi Sentimen

Evaluasi pertama bertujuan untuk mengukur performa model dalam mengklasifikasikan polaritas sentimen (positif, netral, negatif) dari setiap komentar. Hasil evaluasi disajikan dalam bentuk laporan klasifikasi pada Tabel 4.9.

**Tabel 4.9: Laporan Kinerja Klasifikasi Sentimen**

| Kategori Sentimen | Precision | Recall | F1-Score | Support |
|:------------------|:---------:|:------:|:--------:|:-------:|
| Positif           | 0.99      | 1.00   | 0.99     | 73      |
| Netral            | 1.00      | 0.96   | 0.98     | 57      |
| Negatif           | 0.98      | 1.00   | 0.99     | 61      |
| **Accuracy**      |           |        | **0.99** | **191** |
| **Macro Avg**     | **0.99**  | **0.99** | **0.99** | **191** |
| **Weighted Avg**  | **0.99**  | **0.99** | **0.99** | **191** |

Hasil evaluasi menunjukkan kinerja yang **sangat tinggi dan andal** dari model klasifikasi sentimen. Dengan nilai **akurasi keseluruhan mencapai 99%** dan F1-Score rata-rata (baik *macro* maupun *weighted*) sebesar **0.99**, dapat disimpulkan bahwa sistem mampu mengidentifikasi polaritas sentimen dengan tingkat kesalahan yang sangat minimal. Kinerja yang konsisten di ketiga kelas (positif, netral, dan negatif) membuktikan bahwa pendekatan berbasis leksikon yang diimplementasikan sangat efektif dan robust untuk dataset ini.

### 2. Evaluasi Kinerja Klasifikasi Makna

Evaluasi kedua berfokus pada kemampuan sistem untuk membedakan antara komentar yang **"bermakna"** (substantif dan informatif) dan yang **"tidak bermakna"** (terlalu singkat atau bersifat formalitas). Hasil evaluasi disajikan pada Tabel 4.10.

**Tabel 4.10: Laporan Kinerja Klasifikasi Makna**

| Kategori Makna  | Precision | Recall | F1-Score | Support |
|:----------------|:---------:|:------:|:--------:|:-------:|
| Bermakna        | 0.88      | 0.99   | 0.93     | 158     |
| Tidak Bermakna  | 0.92      | 0.36   | 0.52     | 33      |
| **Accuracy**      |           |        | **0.88** | **191** |
| **Macro Avg**     | **0.90**  | **0.68** | **0.73** | **191** |
| **Weighted Avg**  | **0.89**  | **0.88** | **0.86** | **191** |

Hasil evaluasi klasifikasi makna menunjukkan kinerja yang baik dengan **akurasi keseluruhan 88%**. Namun, analisis yang lebih mendalam pada metrik Precision dan Recall mengungkapkan karakteristik penting dari model ini:

-   **Untuk kelas "Bermakna"**: Model mencapai **Recall yang sangat tinggi (0.99)**. Ini berarti model berhasil mengidentifikasi 99% dari semua komentar yang seharusnya dianggap bermakna. Nilai Precision sebesar 0.88 menunjukkan bahwa dari semua yang diprediksi sebagai bermakna, 88% di antaranya adalah prediksi yang benar. Tingginya Recall pada kelas ini sangat krusial karena sejalan dengan tujuan penelitian, yaitu untuk **memastikan tidak ada umpan balik yang berpotensi penting yang terlewatkan** oleh sistem.

-   **Untuk kelas "Tidak Bermakna"**: Model menunjukkan **Precision yang tinggi (0.92)**, yang berarti ketika sistem memprediksi sebuah komentar sebagai "tidak bermakna", prediksi tersebut sangat dapat dipercaya. Namun, nilai **Recall-nya rendah (0.36)**, yang mengindikasikan bahwa model ini cenderung melewatkan sebagian besar komentar yang sebenarnya tidak bermakna dan salah mengklasifikasikannya sebagai "bermakna".

Kecenderungan ini merupakan sebuah *trade-off* yang dapat diterima. Sistem ini dirancang untuk lebih memilih terjadinya *false positive* (menganggap komentar tidak bermakna sebagai bermakna) daripada *false negative* (melewatkan komentar bermakna). Hal ini memastikan bahwa setiap masukan yang berpotensi mengandung kritik atau saran substantif akan tetap ditinjau, meskipun harus menyaring beberapa komentar yang kurang relevan.

Secara keseluruhan, hasil evaluasi kuantitatif ini memvalidasi bahwa arsitektur sistem yang diusulkan mampu menjalankan tugasnya dengan tingkat akurasi yang terukur dan dapat dipertanggungjawabkan secara ilmiah, serta selaras dengan tujuan praktis dari analisis umpan balik.