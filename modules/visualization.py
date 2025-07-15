import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Buat folder output jika belum ada
def pastikan_output_folder(path="output"):
    if not os.path.exists(path):
        os.makedirs(path)

def plot_distribusi_sentimen(df, path="output/distribusi_sentimen.png"):
    """
    Pie chart distribusi polaritas sentimen.
    """
    pastikan_output_folder()
    plt.figure(figsize=(6, 6))
    df["sentimen"].value_counts().plot.pie(
        autopct="%1.1f%%", startangle=90,
        colors=["#66b3ff", "#ff9999", "#99ff99"],
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title("Distribusi Sentimen")
    plt.ylabel("")
    plt.savefig(path)
    plt.close()

def plot_distribusi_makna(df, path="output/distribusi_makna.png"):
    """
    Pie chart komentar bermakna vs tidak bermakna.
    """
    pastikan_output_folder()
    plt.figure(figsize=(6, 6))
    df["makna"].value_counts().plot.pie(
        autopct="%1.1f%%", startangle=90,
        colors=["#ffcc99", "#c2c2f0"],
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title("Distribusi Komentar Bermakna")
    plt.ylabel("")
    plt.savefig(path)
    plt.close()

def plot_klaster_count(df, path="output/jumlah_komentar_per_klaster.png"):
    """
    Bar chart jumlah komentar tiap klaster.
    """
    pastikan_output_folder()
    plt.figure(figsize=(8, 5))
    sns.countplot(x="klaster", hue="klaster", data=df, palette="Set2", legend=False)
    plt.title("Jumlah Komentar per Klaster")
    plt.xlabel("Klaster")
    plt.ylabel("Jumlah")
    plt.savefig(path)
    plt.close()

def visualisasi_semua(df):
    """
    Jalankan semua fungsi visualisasi dan simpan hasilnya.
    """
    plot_distribusi_sentimen(df)
    plot_distribusi_makna(df)
    plot_klaster_count(df)
    print("[OK] Visualisasi berhasil disimpan di folder output/")

def tabel_statistik_per_klaster(df, path="output/statistik_per_klaster.csv"):
    """
    Buat tabel jumlah data per klaster dan distribusi sentimen & makna di dalamnya.
    """
    summary = df.groupby("klaster").agg({
        "kritik dan saran": "count",
        "sentimen": lambda x: x.value_counts().to_dict(),
        "makna": lambda x: x.value_counts().to_dict()
    }).rename(columns={"komentar": "jumlah_komentar"})

    summary.to_csv(path)
    print(f"[OK] Statistik per klaster disimpan di: {path}")
    return summary


def contoh_komentar_per_klaster(df, n=3, path="output/contoh_komentar_per_klaster.txt"):
    """
    Simpan beberapa contoh komentar dari masing-masing klaster.
    """
    with open(path, "w", encoding="utf-8") as f:
        for label in sorted(df["klaster"].unique()):
            f.write(f"--- Klaster {label} ---\n")
            contoh = df[df["klaster"] == label]["kritik dan saran"].head(n).tolist()
            for i, kalimat in enumerate(contoh, 1):
                f.write(f"{i}. {kalimat}\n")
            f.write("\n")
    print(f"[OK] Contoh komentar disimpan di: {path}")
