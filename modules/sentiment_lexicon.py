import pandas as pd
import config

def load_lexicon(pos_path, neg_path):
    """
    Load lexicon positif dan negatif dari file CSV InSet.
    """
    lex_pos = set(pd.read_csv(pos_path)["word"])
    lex_neg = set(pd.read_csv(neg_path)["word"])
    return lex_pos, lex_neg

def klasifikasi_sentimen(teks, lex_pos, lex_neg):
    """
    Klasifikasi sentimen berdasarkan perhitungan skor kata positif dan negatif.
    """
    skor = sum(1 for kata in teks.split() if kata in lex_pos) - sum(1 for kata in teks.split() if kata in lex_neg)
    if skor > 0:
        return "positif"
    elif skor < 0:
        return "negatif"
    return "netral"

def cek_komentar_bermakna(teks):
    """
    Klasifikasi apakah komentar termasuk 'bermakna' atau tidak.
    """
    token = teks.split()
    if len(token) >= config.MAKNA_THRESHOLD:
        return "bermakna"
    if any(k in teks for k in ["saran", "kritik", "perbaikan"]):
        return "bermakna"
    return "tidak bermakna"
