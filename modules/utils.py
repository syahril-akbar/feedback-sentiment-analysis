import pandas as pd
import os

def load_data(path):
    """
    Muat data dari file Excel (.xlsx) dan ubah nama kolom ke huruf kecil.
    Memastikan kolom 'kritik dan saran' dibaca sebagai string.
    """
    df = pd.read_excel(path)
    df.columns = df.columns.str.lower()
    # Konversi paksa kolom 'kritik dan saran' ke tipe data string untuk menghindari galat
    if 'kritik dan saran' in df.columns:
        df['kritik dan saran'] = df['kritik dan saran'].astype(str)
    return df

def save_output(df, output_path):
    """
    Simpan hasil akhir analisis ke dalam satu file CSV.
    """
    # Buat direktori jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Pilih kolom yang akan disimpan
    output_columns = [
        "kritik dan saran",
        "teks_bersih",
        "klaster",
        "sentimen",
        "skor_sentimen", # Tambahkan kolom skor_sentimen
        "makna",
        "skor_konstruktif"
    ]
    
    # Pastikan semua kolom ada di dataframe sebelum menyimpan dan mengurutkannya
    save_df = df[[col for col in output_columns if col in df.columns]]

    save_df.to_csv(output_path, index=False)

def save_meaningful_comments(df, output_path):
    """
    Simpan kritik dan saran yang bermakna ke dalam satu kolom di file CSV.
    """
    # Buat direktori jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Filter komentar yang bermakna dan pilih kolom yang relevan
    meaningful_df = df[df["makna"] == "bermakna"][["kritik dan saran", "klaster", "sentimen", "makna"]]
    
    # Ubah nama kolom untuk output
    output_df = meaningful_df.rename(columns={"kritik dan saran": "komentar bermakna"})

    # Simpan ke CSV
    output_df.to_csv(output_path, index=False)

def save_constructive_comments(df, output_path, threshold=2):
    """
    Simpan kritik dan saran yang dianggap konstruktif ke dalam satu kolom di file CSV.
    """
    # Buat direktori jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Filter komentar yang skor konstruktifnya di atas ambang batas dan pilih kolom yang relevan
    constructive_df = df[df["skor_konstruktif"] >= threshold][["kritik dan saran", "klaster", "sentimen", "skor_konstruktif"]]
    
    # Ubah nama kolom untuk output
    output_df = constructive_df.rename(columns={"kritik dan saran": "saran konstruktif"})

    # Simpan ke CSV
    output_df.to_csv(output_path, index=False)
