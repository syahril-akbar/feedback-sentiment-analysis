import unittest
import sys
import os
from io import StringIO

# Tambahkan direktori root proyek ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.preprocessing import proses_teks, tampilkan_langkah_preprocessing, load_normalization_dict

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        """Setup dijalankan sebelum setiap test."""
        # Pastikan kamus normalisasi dimuat untuk pengujian
        # Ini mungkin redudan jika modul sudah dimuat, tapi memastikan konsistensi
        self.normalization_dict = load_normalization_dict()
        # Jika kamus kosong, beberapa tes mungkin gagal. Kita bisa tambahkan mock jika perlu.
        if not self.normalization_dict:
            print("Peringatan: Kamus normalisasi kosong, tes normalisasi slang mungkin tidak akurat.")

    def test_proses_teks_lengkap(self):
        """
        Menguji seluruh alur fungsi proses_teks dengan kalimat kompleks.
        """
        teks_input = "Saya SANGAT tidak suka pElAyAnAn di toko ini, bgt jeleknya. Gak rekomen bgt!! 😠"
        hasil_yang_diharapkan = "sangat tidak suka layan toko banget jelek tidak rekomendasi banget"
        hasil_aktual = proses_teks(teks_input)
        self.assertEqual(hasil_aktual, hasil_yang_diharapkan)

    def test_proses_teks_tanpa_slang(self):
        """
        Menguji proses_teks dengan kalimat formal tanpa slang.
        """
        teks_input = "Pelayanan publik harus ditingkatkan kualitasnya."
        hasil_yang_diharapkan = "layan publik tingkat kualitas" # 'harus' dan 'ditingkatkan' menjadi stopword/stem
        hasil_aktual = proses_teks(teks_input)
        self.assertEqual(hasil_aktual, hasil_yang_diharapkan)

    def test_proses_teks_kosong(self):
        """
        Menguji proses_teks dengan string kosong.
        """
        teks_input = ""
        hasil_yang_diharapkan = ""
        hasil_aktual = proses_teks(teks_input)
        self.assertEqual(hasil_aktual, hasil_yang_diharapkan)

    def test_proses_teks_hanya_simbol(self):
        """
        Menguji proses_teks dengan string yang hanya berisi simbol dan angka.
        """
        teks_input = "12345 @#$%^&*()_+"
        hasil_yang_diharapkan = ""
        hasil_aktual = proses_teks(teks_input)
        self.assertEqual(hasil_aktual, hasil_yang_diharapkan)

    def test_tampilkan_langkah_preprocessing(self):
        """
        Menguji output dari fungsi tampilkan_langkah_preprocessing.
        Ini akan menangkap output print dan memverifikasinya.
        """
        teks_input = "Kualitasnya oke bgt."
        
        # Alihkan stdout untuk menangkap output print
        captured_output = StringIO()
        sys.stdout = captured_output
        
        tampilkan_langkah_preprocessing(teks_input)
        
        # Kembalikan stdout ke kondisi semula
        sys.stdout = sys.__stdout__
        
        # Dapatkan output sebagai string
        output_str = captured_output.getvalue()
        
        # Verifikasi beberapa bagian penting dari output
        self.assertIn("Teks Asli: 'Kualitasnya oke bgt.'", output_str)
        self.assertIn("-> 1. Case Folding: 'kualitasnya oke bgt.'", output_str)
        self.assertIn("-> 2. Text Cleaning: 'kualitasnya oke bgt'", output_str)
        self.assertIn("-> 4. Tokenizing: ['kualitasnya', 'oke', 'bgt']", output_str)
        # 'oke' mungkin tidak ada di kamus default, tapi 'bgt' seharusnya ada
        self.assertIn("-> 5. Normalisasi Kata (Slang): ['kualitasnya', 'oke', 'banget']", output_str)
        self.assertIn("-> 6. Stopword Removal: ['kualitasnya', 'oke', 'banget']", output_str) 
        self.assertIn("-> 7. Stemming: ['kualitas', 'oke', 'banget']", output_str) # asumsi stem dari 'kualitas' adalah 'kualitas'
        self.assertIn("=> Hasil Akhir: 'kualitas oke banget'", output_str)

if __name__ == '__main__':
    unittest.main()
