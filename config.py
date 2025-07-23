# File utama
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

# Parameter logika
MAKNA_THRESHOLD = 4  # Minimum jumlah kata agar dianggap bermakna
