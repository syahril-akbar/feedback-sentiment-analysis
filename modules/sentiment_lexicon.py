import pandas as pd
import config
import re

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
    tokens = teks.lower().split()
    
    skor = sum(1 for kata in tokens if kata in lex_pos) - sum(1 for kata in tokens if kata in lex_neg)
    
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
    Aturan baru:
    1. Harus lebih panjang dari MAKNA_THRESHOLD.
    2. Tidak boleh HANYA berisi kata-kata pujian umum.
    3. Atau mengandung kata kunci eksplisit (saran/kritik).
    """
    tokens = teks.lower().split()
    
    # Aturan 1: Cek panjang minimum
    if len(tokens) < config.MAKNA_THRESHOLD:
        return "tidak bermakna"
        
    # Aturan 2: Cek apakah hanya berisi kata pujian
    # Buat set dari token untuk perbandingan yang efisien
    token_set = set(tokens)
    pujian_set = set(config.KATA_PUJIAN)
    
    # Jika semua token dalam komentar ada di dalam daftar kata pujian
    if token_set.issubset(pujian_set):
        return "tidak bermakna"

    # Aturan 3: Cek kata kunci eksplisit (opsional, tapi menjaga logika lama)
    if any(k in tokens for k in config.MEANINGFUL_KEYWORDS):
        return "bermakna"
        
    # Jika lolos dari aturan 1 dan 2, anggap bermakna
    return "bermakna"

def analisis_konstruktif(teks):
    """
    Menghitung skor konstruktif untuk sebuah komentar menggunakan bobot dari config.
    Semakin tinggi skor, semakin besar kemungkinan komentar tersebut berisi kritik/saran yang konstruktif.
    """
    skor = 0
    tokens = teks.lower().split()
    
    # [1] Skor berdasarkan panjang komentar
    if len(tokens) > 15:
        skor += config.SCORE_LEN_LONG
    elif len(tokens) > 5:
        skor += config.SCORE_LEN_MEDIUM

    # [2] Skor berdasarkan kata kunci pemicu dari config
    found_saran = False
    found_kritik = False

    for token in tokens:
        if token in config.KATA_SARAN:
            skor += config.SCORE_SUGGESTION_WORD
            found_saran = True
        elif token in config.KATA_KRITIK:
            skor += config.SCORE_CRITICISM_WORD
            found_kritik = True
        elif token in config.KATA_PUJIAN:
            skor += config.SCORE_PRAISE_WORD

    # [3] Bonus untuk kombinasi kritik dan saran
    if found_saran and found_kritik:
        skor += config.SCORE_COMBO_BONUS

    # Pastikan skor tidak negatif
    return max(0, skor)

