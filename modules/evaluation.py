from sklearn.metrics import classification_report
import pandas as pd

def evaluasi_manual(df_prediksi, path_ground_truth):
    """
    Evaluasi hasil sistem menggunakan confusion matrix berdasarkan label manual (ground truth).
    """
    df_gt = pd.read_excel(path_ground_truth)
    df_gt.columns = df_gt.columns.str.lower()
    df_gt = df_gt.rename(columns={"komentar": "kritik dan saran"})
    df_eval = pd.merge(df_gt, df_prediksi, on="kritik dan saran", how="inner")

    hasil = []
    hasil.append("=== Evaluasi Sentimen ===\n")
    hasil.append(classification_report(df_eval["sentimen_manual"], df_eval["sentimen"]))
    hasil.append("\n=== Evaluasi Makna ===\n")
    hasil.append(classification_report(df_eval["makna_manual"], df_eval["makna"]))

    # Cetak dan simpan ke file
    print("".join(hasil))
    with open("output/laporan_akhir.txt", "w") as f:
        f.writelines(hasil)
