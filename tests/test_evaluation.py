# tests/test_evaluation.py

import pytest
import pandas as pd
from modules.evaluation import evaluasi_manual

# Definisikan path ke file ground truth mock
MOCK_GT_PATH = 'tests/mock_data/ground_truth_mock.csv'

@pytest.fixture
def mock_preprocessing(monkeypatch):
    """
    Fixture untuk me-mock fungsi preprocessing.proses_teks.
    Ini mencegah ketergantungan pada modul preprocessing yang kompleks dan
    membuat pengujian lebih fokus dan cepat.
    """
    def mock_proses_teks(teks):
        # Dalam pengujian ini, kita asumsikan teks sudah "bersih"
        # dan sama dengan kolom 'teks_bersih' yang kita buat di mock df.
        # Contoh: "ini adalah komentar yang bagus" -> "ini adalah komentar yang bagus"
        return teks.lower()

    # Ganti fungsi asli dengan mock function
    monkeypatch.setattr('modules.preprocessing.proses_teks', mock_proses_teks)

def test_evaluasi_kasus_ideal(mock_preprocessing, capsys):
    """
    Tes 1: Skenario di mana prediksi model 100% cocok dengan ground truth.
    Harapkan precision, recall, f1-score menjadi 1.00.
    """
    # Data prediksi yang sempurna
    df_prediksi = pd.DataFrame({
        'teks_bersih': [
            'ini adalah komentar yang bagus',
            'ini adalah komentar yang jelek',
            'ini komentar biasa saja',
        ],
        'sentimen': ['positif', 'negatif', 'netral'],
        'makna': ['bermakna', 'bermakna', 'tidak bermakna']
    })
    
    laporan = evaluasi_manual(df_prediksi, MOCK_GT_PATH)
    
    assert "Evaluasi Sentimen" in laporan
    assert "Evaluasi Makna" in laporan
    
    # Periksa laporan baris per baris untuk menghindari masalah spasi
    laporan_lines = laporan.split('\n')
    weighted_avg_lines = [line for line in laporan_lines if 'weighted avg' in line]
    
    # Harus ada dua baris 'weighted avg' (satu untuk sentimen, satu untuk makna)
    assert len(weighted_avg_lines) == 2
    # Dan keduanya harus menunjukkan skor 1.00
    for line in weighted_avg_lines:
        assert "1.00" in line

def test_evaluasi_kasus_campuran(mock_preprocessing):
    """
    Tes 2: Skenario realistis dengan beberapa prediksi benar dan salah.
    Fokus utama adalah memastikan fungsi berjalan tanpa error dan menghasilkan laporan.
    """
    # Data prediksi dengan beberapa kesalahan
    df_prediksi = pd.DataFrame({
        'teks_bersih': [
            'ini adalah komentar yang bagus', # Benar
            'ini adalah komentar yang jelek', # Salah sentimen
            'ini komentar biasa saja',       # Benar
            'ini komentar hebat',            # Salah makna
            'ini komentar buruk',            # Benar
        ],
        'sentimen': ['positif', 'positif', 'netral', 'positif', 'negatif'],
        'makna': ['bermakna', 'bermakna', 'tidak bermakna', 'tidak bermakna', 'bermakna']
    })
    
    laporan = evaluasi_manual(df_prediksi, MOCK_GT_PATH)
    
    assert isinstance(laporan, str)
    assert "Evaluasi Sentimen" in laporan
    assert "Evaluasi Makna" in laporan
    assert "precision" in laporan # Memastikan tabel laporan klasifikasi ada

def test_evaluasi_tidak_ada_data_cocok(mock_preprocessing):
    """
    Tes 3: Skenario di mana tidak ada teks yang cocok antara prediksi dan ground truth.
    Fungsi harus mengembalikan pesan yang sesuai.
    """
    df_prediksi = pd.DataFrame({
        'teks_bersih': ['teks ini sama sekali berbeda'],
        'sentimen': ['positif'],
        'makna': ['bermakna']
    })
    
    laporan = evaluasi_manual(df_prediksi, MOCK_GT_PATH)
    
    assert "Tidak ada data yang cocok" in laporan

def test_evaluasi_dataframe_prediksi_kosong(mock_preprocessing):
    """
    Tes 4: Edge case dengan DataFrame prediksi yang kosong.
    Fungsi harus menangani ini dengan baik tanpa error.
    """
    df_prediksi = pd.DataFrame(columns=['teks_bersih', 'sentimen', 'makna'])
    
    laporan = evaluasi_manual(df_prediksi, MOCK_GT_PATH)
    
    assert "Tidak ada data yang cocok" in laporan

def test_evaluasi_dengan_satu_label_saja(mock_preprocessing):
    """
    Tes 5: Skenario di mana data hanya memiliki satu jenis label (misal, semua positif).
    Classification report harus tetap bisa dibuat.
    """
    df_prediksi = pd.DataFrame({
        'teks_bersih': [
            'ini adalah komentar yang bagus',
            'ini komentar hebat',
        ],
        'sentimen': ['positif', 'positif'],
        'makna': ['bermakna', 'bermakna']
    })
    
    laporan = evaluasi_manual(df_prediksi, MOCK_GT_PATH)
    
    assert "Evaluasi Sentimen" in laporan
    assert "positif       1.00      1.00      1.00" in laporan # Hanya ada kelas positif
    assert "negatif" not in laporan # Kelas lain tidak boleh muncul
