from sklearn.metrics import classification_report
import pandas as pd
from . import preprocessing

def evaluasi_manual(df_prediksi, path_ground_truth):
    """
    Evaluasi hasil sistem menggunakan confusion matrix berdasarkan label manual (ground truth).
    Mengembalikan string laporan evaluasi.
    """
    df_gt = pd.read_csv(path_ground_truth)
    df_gt.columns = df_gt.columns.str.lower()
    df_gt = df_gt.rename(columns={"komentar": "kritik dan saran"})

    # Lakukan pra-pemrosesan pada ground truth agar formatnya sama dengan data prediksi
    df_gt["teks_bersih"] = df_gt["kritik dan saran"].apply(preprocessing.proses_teks)
    
    # Kolom yang relevan dari hasil prediksi
    df_prediksi_relevan = df_prediksi[["teks_bersih", "sentimen", "makna"]]

    # Gabungkan berdasarkan teks yang sudah dibersihkan
    df_eval = pd.merge(df_gt, df_prediksi_relevan, on="teks_bersih", how="inner")

    hasil = []

    if not df_eval.empty:
        # Hapus duplikat jika ada teks bersih yang sama setelah pra-pemrosesan
        df_eval = df_eval.drop_duplicates(subset=["teks_bersih"])

        # Pastikan kolom sentimen dan makna adalah string dan tangani NaN
        df_eval["sentimen_manual"] = df_eval["sentimen_manual"].astype(str).fillna("TIDAK DIKETAHUI")
        df_eval["sentimen"] = df_eval["sentimen"].astype(str).fillna("TIDAK DIKETAHUI")
        df_eval["makna_manual"] = df_eval["makna_manual"].astype(str).fillna("TIDAK DIKETAHUI")
        df_eval["makna"] = df_eval["makna"].astype(str).fillna("TIDAK DIKETAHUI")
        
        hasil.append("=== Evaluasi Sentimen ===\n")
        hasil.append(classification_report(df_eval["sentimen_manual"], df_eval["sentimen"], zero_division=0, labels=df_eval['sentimen_manual'].unique()))
        hasil.append("\n=== Evaluasi Makna ===\n")
        hasil.append(classification_report(df_eval["makna_manual"], df_eval["makna"], zero_division=0, labels=df_eval['makna_manual'].unique()))
    else:
        hasil.append("Tidak ada data yang cocok antara hasil prediksi dan data uji manual.\n")

    return "".join(hasil)
