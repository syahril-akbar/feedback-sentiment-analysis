# --- File & Path ---
DATA_PATH = "data/kritik_saran.xlsx"
GROUND_TRUTH_PATH = "data/data_uji_manual.csv"

# File kamus
LEXICON_POS = "kamus/lexicon/InSet_positif.tsv"
LEXICON_NEG = "kamus/lexicon/InSet_negatif.tsv"
NORMALIZATION_DICT = "kamus/normalisasi/kbba.txt"

# Output
OUTPUT_PATH = "output/hasil_akhir.csv"
OUTPUT_MEANINGFUL_PATH = "output/komentar_bermakna.csv"
OUTPUT_CONSTRUCTIVE_PATH = "output/saran_konstruktif.csv"

# --- Parameter Global ---
RANDOM_SEED = 42  # Seed untuk proses acak agar hasil bisa direproduksi

# --- Parameter Pra-pemrosesan & Vektorisasi ---
STOPWORDS_TO_KEEP = ['baik', 'tidak', 'kurang', 'lebih', 'sangat'] # Kata yang dikecualikan dari daftar stopword
TFIDF_MIN_DF = 3          # Abaikan kata yang muncul di kurang dari X dokumen
TFIDF_MAX_DF = 0.85       # Abaikan kata yang muncul di lebih dari X% dokumen
TFIDF_NGRAM_RANGE = (1, 2)  # Rentang N-gram (1,1=unigram, 1,2=unigram+bigram)

# --- Parameter Clustering ---
K_RANGE = (2, 10)    # Rentang nilai K untuk diuji dalam clustering
N_TOP_WORDS = 10     # Jumlah kata kunci teratas per klaster

# --- Parameter Analisis & Logika ---
MAKNA_THRESHOLD = 2         # Minimum jumlah kata agar dianggap bermakna
MEANINGFUL_KEYWORDS = ["saran", "kritik", "perbaikan"] # Kata kunci pemicu status "bermakna"
CONSTRUCTIVE_THRESHOLD = 3  # Minimum skor agar dianggap saran konstruktif
N_EXAMPLE_COMMENTS = 10      # Jumlah contoh komentar per klaster untuk disimpan
N_PREPROCESSING_EXAMPLES = 10 # Jumlah contoh preprocessing yang ditampilkan di log

# --- Bobot Skor untuk Analisis Konstruktif ---
SCORE_LEN_LONG = 2          # Bonus skor untuk komentar panjang (> 15 kata)
SCORE_LEN_MEDIUM = 1        # Bonus skor untuk komentar sedang (> 5 kata)
SCORE_SUGGESTION_WORD = 2   # Bonus skor untuk kata kunci saran
SCORE_CRITICISM_WORD = 1    # Bonus skor untuk kata kunci kritik
SCORE_PRAISE_WORD = -1      # Penalti skor untuk kata kunci pujian
SCORE_COMBO_BONUS = 2       # Bonus skor untuk kombinasi saran & kritik

# --- Daftar Kata Kunci untuk Analisis Skor Konstruktif ---
KATA_SARAN = ["saran", "sebaiknya", "mungkin", "bisa", "tolong", "mohon", "tingkatkan", "perbaiki", "perlu", "tambah", "diperluas"]
KATA_KRITIK = ["kurang", "tidak", "lambat", "sulit", "membingungkan", "masalah", "buruk", "jelek", "kotor", "panas", "basi"]
KATA_PUJIAN = ["terima kasih", "mantap", "bagus", "keren", "baik", "puas", "enak", "nyaman", "bersih"]

# --- Parameter Visualisasi ---
VIZ_DPI = 300
VIZ_FIGSIZE_WIDE = (12, 7)
VIZ_FIGSIZE_SQUARE = (8, 8)
VIZ_PALETTE_SENTIMEN = ["#66b3ff", "#ff9999", "#99ff99"]
VIZ_PALETTE_MAKNA = ["#ffcc99", "#c2c2f0"]
VIZ_PALETTE_KLASTER = "Set2"
VIZ_PALETTE_STACKED = "viridis"