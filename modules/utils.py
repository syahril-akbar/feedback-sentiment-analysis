import pandas as pd

def load_data(path):
    """
    Load data dari file Excel (.xlsx) dan ubah nama kolom ke lowercase.
    """
    df = pd.read_excel(path)
    df.columns = df.columns.str.lower()
    return df

def save_output(df, path_klaster, path_sentimen):
    """
    Simpan hasil klaster dan sentimen ke file CSV terpisah.
    """
    df[["komentar", "klaster"]].to_csv(path_klaster, index=False)
    df[["komentar", "sentimen", "makna"]].to_csv(path_sentimen, index=False)
