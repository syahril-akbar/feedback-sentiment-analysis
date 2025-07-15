import pandas as pd
import os

def load_data(path):
    """
    Load data dari file Excel (.xlsx) dan ubah nama kolom ke lowercase.
    """
    df = pd.read_excel(path, dtype=str)
    df.columns = df.columns.str.lower()
    return df

def save_output(df, path_klaster, path_sentimen):
    """
    Simpan hasil klaster dan sentimen ke file CSV terpisah.
    """
    # Membuat direktori jika belum ada
    os.makedirs(os.path.dirname(path_klaster), exist_ok=True)
    os.makedirs(os.path.dirname(path_sentimen), exist_ok=True)

    df[["kritik dan saran", "klaster"]].to_csv(path_klaster, index=False)
    df[["kritik dan saran", "sentimen", "makna"]].to_csv(path_sentimen, index=False)
