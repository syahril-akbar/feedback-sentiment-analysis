import pandas as pd
import config

def load_lexicon(pos_path, neg_path):
    """
    Muat leksikon positif dan negatif dari file CSV InSet.
    """
    lex_pos = set(pd.read_csv(pos_path, delimiter='	', header=None, names=['word', 'weight'])['word'])
    lex_neg = set(pd.read_csv(neg_path, delimiter='	', header=None, names=['word', 'weight'])['word'])
    return lex_pos, lex_neg

import re

def klasifikasi_sentimen(teks, lex_pos, lex_neg):
    """
    Klasifikasi sentimen berdasarkan perhitungan skor kata positif dan negatif.
    Mengembalikan Series Pandas dengan 'label' dan 'skor'.
    """
    # Lakukan pembersihan dasar untuk menghapus tanda baca agar perbandingan kata lebih akurat
    teks_bersih = re.sub(r'[^a-z\s]', '', teks.lower())
    tokens = teks_bersih.split()
    
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
    """
    token = teks.split()
    if len(token) >= config.MAKNA_THRESHOLD:
        return "bermakna"
    if any(k in teks for k in config.MEANINGFUL_KEYWORDS):
        return "bermakna"
    return "tidak bermakna"

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

