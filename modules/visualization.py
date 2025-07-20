import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from wordcloud import WordCloud
from sklearn.decomposition import PCA
import config

def pastikan_output_folder(path="output"):
    if not os.path.exists(path):
        os.makedirs(path)

def plot_distribusi_sentimen(df, path="output/distribusi_sentimen.png"):
    pastikan_output_folder()
    plt.figure(figsize=config.VIZ_FIGSIZE_SQUARE)
    ax = sns.countplot(y="sentimen", data=df, hue="sentimen", palette=config.VIZ_PALETTE_SENTIMEN, order=df['sentimen'].value_counts().index, legend=False)
    
    total = len(df['sentimen'])
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_width()/total)
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        ax.annotate(percentage, (x, y))

    plt.title("Distribusi Sentimen Komentar", fontsize=16)
    plt.xlabel("Jumlah Komentar", fontsize=12)
    plt.ylabel("Sentimen", fontsize=12)
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_distribusi_makna(df, path="output/distribusi_makna.png"):
    pastikan_output_folder()
    plt.figure(figsize=config.VIZ_FIGSIZE_SQUARE)
    df["makna"].value_counts().plot.pie(
        autopct="%1.1f%%", startangle=90,
        colors=config.VIZ_PALETTE_MAKNA,
        wedgeprops={'edgecolor': 'black'},
        textprops={'fontsize': 12}
    )
    plt.title("Distribusi Komentar Bermakna vs Tidak Bermakna", fontsize=16)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_klaster_count(df, path="output/jumlah_komentar_per_klaster.png"):
    pastikan_output_folder()
    plt.figure(figsize=config.VIZ_FIGSIZE_WIDE)
    sns.countplot(x="klaster", hue="klaster", data=df, palette=config.VIZ_PALETTE_KLASTER, legend=False)
    plt.title("Jumlah Komentar per Klaster", fontsize=16)
    plt.xlabel("Klaster", fontsize=12)
    plt.ylabel("Jumlah Komentar", fontsize=12)
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_sentimen_per_klaster(df, path="output/distribusi_sentimen_per_klaster.png"):
    pastikan_output_folder()
    sentiment_counts = df.groupby('klaster')['sentimen'].value_counts(normalize=True).unstack().fillna(0)
    sentiment_counts.plot(kind='bar', stacked=True, figsize=config.VIZ_FIGSIZE_WIDE, cmap=config.VIZ_PALETTE_STACKED)
    plt.title('Distribusi Sentimen per Klaster', fontsize=16)
    plt.xlabel('Klaster', fontsize=12)
    plt.ylabel('Proporsi', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Sentimen')
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_makna_per_klaster(df, path="output/distribusi_makna_per_klaster.png"):
    pastikan_output_folder()
    makna_counts = df.groupby('klaster')['makna'].value_counts(normalize=True).unstack().fillna(0)
    makna_counts.plot(kind='bar', stacked=True, figsize=config.VIZ_FIGSIZE_WIDE, cmap='Pastel1')
    plt.title('Distribusi Makna per Klaster', fontsize=16)
    plt.xlabel('Klaster', fontsize=12)
    plt.ylabel('Proporsi', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Makna')
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_wordcloud_per_klaster(df, path_prefix="output/wordcloud_klaster_"):
    pastikan_output_folder()
    for label in sorted(df["klaster"].unique()):
        text = " ".join(df[df["klaster"] == label]["teks_bersih"].dropna())
        if text:
            wordcloud = WordCloud(width=1200, height=600, background_color="white", collocations=False).generate(text)
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Word Cloud untuk Klaster {label}", fontsize=16)
            plt.tight_layout()
            plt.savefig(f"{path_prefix}{label}.png", dpi=config.VIZ_DPI)
            plt.close()

def plot_silhouette_scores(silhouette_scores, best_k=None, path="output/silhouette_scores.png"):
    pastikan_output_folder()
    plt.figure(figsize=config.VIZ_FIGSIZE_WIDE)
    k_values = list(silhouette_scores.keys())
    scores = list(silhouette_scores.values())
    
    plt.plot(k_values, scores, 'bo-', markersize=8, lw=2)
    
    if best_k is not None and best_k in k_values:
        best_k_score = silhouette_scores[best_k]
        plt.plot(best_k, best_k_score, 'r*', markersize=15, label=f'Optimal k = {best_k} (Score: {best_k_score:.3f})')
        plt.legend()

    plt.xlabel("Jumlah Klaster (k)", fontsize=12)
    plt.ylabel("Silhouette Score", fontsize=12)
    plt.title("Silhouette Score untuk Menentukan k Optimal", fontsize=16)
    plt.xticks(k_values)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_pca_clusters(tfidf_matrix, df, path="output/pca_clusters.png"):
    pastikan_output_folder()
    pca = PCA(n_components=2, random_state=42)
    tfidf_dense = tfidf_matrix.toarray()
    pca_result = pca.fit_transform(tfidf_dense)
    
    df_pca = pd.DataFrame({'pca_1': pca_result[:, 0], 'pca_2': pca_result[:, 1], 'klaster': df['klaster']})
    
    plt.figure(figsize=config.VIZ_FIGSIZE_SQUARE)
    sns.scatterplot(x="pca_1", y="pca_2", hue="klaster", palette=sns.color_palette("hsv", n_colors=df['klaster'].nunique()), data=df_pca, legend="full", alpha=0.7)
    
    plt.title("Visualisasi Klaster 2D dengan PCA", fontsize=16)
    plt.xlabel("Komponen Utama 1", fontsize=12)
    plt.ylabel("Komponen Utama 2", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def plot_correlation_heatmap(df, path="output/correlation_heatmap.png"):
    pastikan_output_folder()
    df_corr = df.copy()
    df_corr['sentimen_code'] = df_corr['sentimen'].astype('category').cat.codes
    df_corr['makna_code'] = df_corr['makna'].astype('category').cat.codes
    
    corr_data = df_corr[['klaster', 'sentimen_code', 'makna_code', 'skor_konstruktif']].rename(
        columns={'klaster': 'Klaster', 'sentimen_code': 'Sentimen', 'makna_code': 'Makna', 'skor_konstruktif': 'Skor Konstruktif'}
    )
    corr_matrix = corr_data.corr()
    
    plt.figure(figsize=config.VIZ_FIGSIZE_SQUARE)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    
    plt.title("Heatmap Korelasi antar Fitur", fontsize=16)
    plt.tight_layout()
    plt.savefig(path, dpi=config.VIZ_DPI)
    plt.close()

def visualisasi_semua(df, tfidf_matrix):
    print("\nMembuat dan menyimpan visualisasi...")
    plot_distribusi_sentimen(df)
    plot_distribusi_makna(df)
    plot_klaster_count(df)
    plot_sentimen_per_klaster(df)
    plot_makna_per_klaster(df)
    plot_wordcloud_per_klaster(df)
    plot_pca_clusters(tfidf_matrix, df)
    plot_correlation_heatmap(df)
    print("Visualisasi berhasil disimpan di folder 'output/'.")

def tabel_statistik_per_klaster(df, path="output/statistik_per_klaster.csv"):
    summary = df.groupby("klaster").agg(
        jumlah_komentar=("kritik dan saran", "count"),
        sentimen_positif=("sentimen", lambda x: (x == "positif").sum()),
        sentimen_negatif=("sentimen", lambda x: (x == "negatif").sum()),
        sentimen_netral=("sentimen", lambda x: (x == "netral").sum()),
        makna_bermakna=("makna", lambda x: (x == "bermakna").sum()),
        makna_tidak_bermakna=("makna", lambda x: (x == "tidak bermakna").sum())
    )
    summary["persentase_positif"] = (summary["sentimen_positif"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_negatif"] = (summary["sentimen_negatif"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_netral"] = (summary["sentimen_netral"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_bermakna"] = (summary["makna_bermakna"] / summary["jumlah_komentar"] * 100).round(2)
    summary["persentase_tidak_bermakna"] = (summary["makna_tidak_bermakna"] / summary["jumlah_komentar"] * 100).round(2)
    summary.to_csv(path)
    return summary

def contoh_komentar_per_klaster(df, n, path="output/contoh_komentar_per_klaster.txt"):
    pastikan_output_folder()
    with open(path, "w", encoding="utf-8") as f:
        f.write("="*50 + "\n")
        f.write("CONTOH KOMENTAR PER KLASTER\n")
        f.write("="*50 + "\n\n")
        for label in sorted(df["klaster"].unique()):
            f.write(f"--- Klaster {label} ---\n")
            contoh_df = df[df["klaster"] == label][["kritik dan saran", "sentimen", "makna"]].head(n)
            if contoh_df.empty:
                f.write("Tidak ada contoh komentar yang tersedia.\n")
            else:
                for i, row in contoh_df.iterrows():
                    f.write(f"  - Komentar: {row['kritik dan saran']}\n")
                    f.write(f"    (Sentimen: {row['sentimen']}, Makna: {row['makna']})\n")
            f.write("\n")

def tampilkan_analisis_sentimen_dan_makna(df):
    print("Distribusi Sentimen:")
    print((df['sentimen'].value_counts(normalize=True) * 100).to_string(float_format="%.2f%%"))
    
    print("\nDistribusi Makna Komentar:")
    print((df['makna'].value_counts(normalize=True) * 100).to_string(float_format="%.2f%%"))
