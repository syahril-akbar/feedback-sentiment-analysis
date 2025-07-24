import unittest
import sys
import os
import numpy as np
from scipy.sparse import spmatrix

# Tambahkan direktori root proyek ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.tfidf_vectorizer import ubah_ke_tfidf
import config

class TestTfidfVectorizer(unittest.TestCase):

    def setUp(self):
        """Menyiapkan data teks untuk pengujian."""
        self.teks_sampel = [
            "saran saya tingkatkan pelayanan",
            "kritik saya pelayanan kurang baik",
            "pelayanan sudah baik dan bagus",
            "saran saya perbaiki sistem yang ada",
            "sistem ini kurang bagus"
        ]
        # Mengatur parameter config untuk pengujian yang dapat diprediksi
        config.TFIDF_MIN_DF = 2
        config.TFIDF_MAX_DF = 0.85
        config.TFIDF_NGRAM_RANGE = (1, 1)

    def test_ubah_ke_tfidf_output(self):
        """
        Menguji tipe output dan bentuk dasar dari fungsi ubah_ke_tfidf.
        """
        matrix, feature_names, vectorizer = ubah_ke_tfidf(self.teks_sampel)

        # 1. Verifikasi tipe output
        self.assertIsInstance(matrix, spmatrix, "Output matrix seharusnya adalah sparse matrix dari SciPy.")
        self.assertIsInstance(feature_names, np.ndarray, "Nama fitur seharusnya adalah numpy array.")
        self.assertIsNotNone(vectorizer, "Vectorizer seharusnya tidak None.")

        # 2. Verifikasi dimensi matrix
        jumlah_dokumen = len(self.teks_sampel)
        jumlah_fitur = len(feature_names)
        self.assertEqual(matrix.shape, (jumlah_dokumen, jumlah_fitur), "Dimensi matrix tidak sesuai.")

    def test_tfidf_min_df(self):
        """
        Menguji fungsionalitas min_df. Kata harus muncul minimal di 'min_df' dokumen.
        """
        # Dengan min_df=2, kata 'pelayanan', 'saran', 'saya', 'bagus', 'kurang' harus ada.
        # Kata 'tingkatkan', 'kritik', 'baik', 'perbaiki', 'sistem' (muncul 1x) harusnya hilang.
        config.TFIDF_MIN_DF = 2
        config.TFIDF_NGRAM_RANGE = (1, 1)
        
        _, feature_names, _ = ubah_ke_tfidf(self.teks_sampel)
        
        expected_features = ['bagus', 'baik', 'kurang', 'pelayanan', 'saran', 'saya', 'sistem']
        # 'baik' dan 'dan' juga akan hilang karena hanya muncul sekali atau merupakan stopword (jika ada).
        # Dalam kasus ini, kita asumsikan teks sudah bersih.
        
        self.assertCountEqual(feature_names, expected_features, "Fitur yang dihasilkan tidak sesuai dengan aturan min_df.")

    def test_tfidf_ngram_range(self):
        """
        Menguji fungsionalitas ngram_range untuk menyertakan bigram.
        """
        config.TFIDF_MIN_DF = 2 # Reset ke nilai yang wajar untuk bigram
        config.TFIDF_NGRAM_RANGE = (1, 2)

        _, feature_names, _ = ubah_ke_tfidf(self.teks_sampel)

        # Bigram yang diharapkan muncul minimal 2 kali: 'saran saya'
        self.assertIn("saran saya", feature_names, "Bigram 'saran saya' seharusnya ada di dalam fitur.")
        
        # Unigram yang diharapkan
        self.assertIn("pelayanan", feature_names)
        
        # Bigram yang hanya muncul sekali seharusnya tidak ada jika min_df > 1
        config.TFIDF_MIN_DF = 2
        _, feature_names_min2, _ = ubah_ke_tfidf(self.teks_sampel)
        self.assertNotIn("kurang baik", feature_names_min2, "Bigram 'kurang baik' seharusnya tidak ada dengan min_df=2.")


if __name__ == '__main__':
    unittest.main()
