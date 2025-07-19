import pandas as pd
import config

def load_lexicon(pos_path, neg_path):
    """
    Muat leksikon positif dan negatif dari file CSV InSet.
    """
    lex_pos = set(pd.read_csv(pos_path, delimiter='	', header=None, names=['word', 'weight'])['word'])
    lex_neg = set(pd.read_csv(neg_path, delimiter='	', header=None, names=['word', 'weight'])['word'])
    return lex_pos, lex_neg

def klasifikasi_sentimen(teks, lex_pos, lex_neg):
    """
    Klasifikasi sentimen berdasarkan perhitungan skor kata positif dan negatif.
    Mengembalikan Series Pandas dengan 'label' dan 'skor'.
    """
    skor = sum(1 for kata in teks.split() if kata in lex_pos) - sum(1 for kata in teks.split() if kata in lex_neg)
    if skor > 0:
        label = "positif"
    elif skor < 0:
        label = "negatif"
    else:
        label = "netral"
    return pd.Series([label, skor], index=['sentimen', 'skor_sentimen'])

def cek_komentar_bermakna(teks):
    """
    Klasifikasi apakah komentar termasuk 'bermakna' atau 'tidak bermakna'.
    """
    token = teks.split()
    if len(token) >= config.MAKNA_THRESHOLD:
        return "bermakna"
    if any(k in teks for k in ["saran", "kritik", "perbaikan"]):
        return "bermakna"
    return "tidak bermakna"

def analisis_konstruktif(teks):
    """
    Menghitung skor konstruktif untuk sebuah komentar.
    Semakin tinggi skor, semakin besar kemungkinan komentar tersebut berisi kritik/saran yang konstruktif.
    """
    skor = 0
    tokens = teks.lower().split()
    
    # [1] Skor berdasarkan panjang komentar
    if len(tokens) > 15:
        skor += 3
    elif len(tokens) > 5:
        skor += 1

    # [2] Skor berdasarkan kata kunci pemicu
    kata_saran = ["saran", "sebaiknya", "mungkin bisa", "tolong", "mohon", "tingkatkan", "perbaiki", "perlu"]
    kata_kritik_spesifik = ["kurang", "tidak", "lambat", "sulit", "membingungkan", "masalah", "buruk", "jelek"]
    kata_positif_umum = ["terima kasih", "mantap", "bagus", "keren", "baik", "puas"]

    found_saran = False
    found_kritik = False

    for token in tokens:
        if token in kata_saran:
            skor += 2
            found_saran = True
        elif token in kata_kritik_spesifik:
            skor += 1
            found_kritik = True
        elif token in kata_positif_umum:
            skor -= 1 # Mengurangi skor untuk komentar yang hanya berisi pujian umum

    # [3] Bonus untuk kombinasi kritik dan saran
    if found_saran and found_kritik:
        skor += 2

    # Pastikan skor tidak negatif
    return max(0, skor)

