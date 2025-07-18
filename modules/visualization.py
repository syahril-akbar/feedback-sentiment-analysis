import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from wordcloud import WordCloud

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

def plot_sentimen_per_klaster(df, path="output/distribusi_sentimen_per_klaster.png"):
    """
    Bar chart distribusi sentimen per klaster.
    """
    pastikan_output_folder()
    sentiment_counts = df.groupby('klaster')['sentimen'].value_counts(normalize=True).unstack().fillna(0)
    sentiment_counts.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='viridis')
    plt.title('Distribusi Sentimen per Klaster')
    plt.xlabel('Klaster')
    plt.ylabel('Proporsi')
    plt.xticks(rotation=0)
    plt.legend(title='Sentimen')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_makna_per_klaster(df, path="output/distribusi_makna_per_klaster.png"):
    """
    Bar chart distribusi makna per klaster.
    """
    pastikan_output_folder()
    makna_counts = df.groupby('klaster')['makna'].value_counts(normalize=True).unstack().fillna(0)
    makna_counts.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='Pastel1')
    plt.title('Distribusi Makna per Klaster')
    plt.xlabel('Klaster')
    plt.ylabel('Proporsi')
    plt.xticks(rotation=0)
    plt.legend(title='Makna')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def visualisasi_semua(df):
    """
    Jalankan semua fungsi visualisasi dan simpan hasilnya.
    """
    plot_distribusi_sentimen(df)
    plot_distribusi_makna(df)
    plot_klaster_count(df)
    plot_sentimen_per_klaster(df)
    plot_makna_per_klaster(df) # New call
    plot_wordcloud_per_klaster(df)

def tabel_statistik_per_klaster(df, path="output/statistik_per_klaster.csv"):
    """
    Buat tabel jumlah data per klaster dan distribusi sentimen & makna di dalamnya.
    """
    summary = df.groupby("klaster").agg(
        jumlah_komentar=("kritik dan saran", "count"),
        sentimen_positif=("sentimen", lambda x: (x == "positif").sum()),
        sentimen_negatif=("sentimen", lambda x: (x == "negatif").sum()),
        sentimen_netral=("sentimen", lambda x: (x == "netral").sum()),
        makna_bermakna=("makna", lambda x: (x == "bermakna").sum()),
        makna_tidak_bermakna=("makna", lambda x: (x == "tidak bermakna").sum())
    )

    # Hitung persentase
    summary["persentase_positif"] = (summary["sentimen_positif"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_negatif"] = (summary["sentimen_negatif"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_netral"] = (summary["sentimen_netral"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_bermakna"] = (summary["makna_bermakna"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_tidak_bermakna"] = (summary["makna_tidak_bermakna"] / summary["jumlah_komentar"] * 100).round(2)

    summary.to_csv(path)
    return summary

def plot_wordcloud_per_klaster(df, path_prefix="output/wordcloud_klaster_"):
    """
    Buat dan simpan word cloud untuk setiap klaster.
    """
    pastikan_output_folder()
    for label in sorted(df["klaster"].unique()):
        text = " ".join(df[df["klaster"] == label]["teks_bersih"].dropna())
        if text:
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Word Cloud Klaster {label}")
            plt.savefig(f"{path_prefix}{label}.png")
            plt.close()
        else:
            print(f"Tidak ada teks bersih untuk Klaster {label}. Word Cloud tidak dibuat.")

def contoh_komentar_per_klaster(df, n=3, path="output/contoh_komentar_per_klaster.txt"):
    """
    Simpan beberapa contoh komentar dari masing-masing klaster beserta sentimen dan maknanya.
    """
    pastikan_output_folder()
    with open(path, "w", encoding="utf-8") as f:
        for label in sorted(df["klaster"].unique()):
            f.write(f"--- Klaster {label} ---\n")
            # Ambil n contoh komentar beserta sentimen dan maknanya
            contoh_df = df[df["klaster"] == label][["kritik dan saran", "sentimen", "makna"]].head(n)
            for i, row in contoh_df.iterrows():
                f.write(f"{i+1}. Komentar: {row["kritik dan saran"]}\n")
                f.write(f"   Sentimen: {row["sentimen"]}\n")
                f.write(f"   Makna: {row["makna"]}\n")
            f.write("\n")

def tampilkan_analisis_sentimen_dan_makna(df):
    """
    Menampilkan hasil analisis sentimen dan makna ke konsol.
    """
    print("Distribusi Sentimen:")
    print((df['sentimen'].value_counts(normalize=True) * 100).to_string(float_format="%.2f%%"))
    
    print("\nDistribusi Makna Komentar:")
    print((df['makna'].value_counts(normalize=True) * 100).to_string(float_format="%.2f%%"))


def plot_silhouette_scores(silhouette_scores, best_k=None, path="output/silhouette_scores.png"):
    """
    Plot silhouette scores for different values of k, with an optional marker for the best k.
    """
    pastikan_output_folder()
    plt.figure(figsize=(8, 5))
    k_values = list(silhouette_scores.keys())
    scores = list(silhouette_scores.values())
    
    plt.plot(k_values, scores, 'bo-', markersize=8, lw=2)
    
    if best_k is not None and best_k in k_values:
        best_k_score = silhouette_scores[best_k]
        plt.plot(best_k, best_k_score, 'r*', markersize=15, label=f'Optimal k = {best_k}')
        plt.legend()

    plt.xlabel("Jumlah Klaster (k)")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Score untuk Menentukan k Optimal")
    plt.xticks(k_values)
    plt.grid(True)
    plt.savefig(path)
    plt.close()
