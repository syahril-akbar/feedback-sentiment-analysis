# tests/test_sentiment_lexicon.py

import pytest
import pandas as pd
from modules.sentiment_lexicon import load_lexicon, klasifikasi_sentimen

# Definisikan path ke file leksikon mock
MOCK_POS_LEXICON_PATH = 'tests/mock_kamus/positif_mock.tsv'
MOCK_NEG_LEXICON_PATH = 'tests/mock_kamus/negatif_mock.tsv'

@pytest.fixture(scope="module")
def leksikon_mock():
    """
    Fixture untuk memuat leksikon dari file mock.
    Ini akan dijalankan sekali per modul tes.
    """
    lex_pos, lex_neg = load_lexicon(MOCK_POS_LEXICON_PATH, MOCK_NEG_LEXICON_PATH)
    return lex_pos, lex_neg

def test_load_lexicon():
    """
    Tes 1: Memastikan fungsi load_lexicon dapat memuat data dengan benar.
    - Memverifikasi bahwa outputnya adalah tuple dari dua set.
    - Memverifikasi bahwa kata-kata dari file mock ada di dalam set yang sesuai.
    """
    lex_pos, lex_neg = load_lexicon(MOCK_POS_LEXICON_PATH, MOCK_NEG_LEXICON_PATH)
    
    # Pastikan tipe data benar (set)
    assert isinstance(lex_pos, set)
    assert isinstance(lex_neg, set)
    
    # Pastikan beberapa kata kunci ada di dalam set
    assert 'senang' in lex_pos
    assert 'hebat' in lex_pos
    assert 'buruk' in lex_neg
    assert 'kecewa' in lex_neg
    
    # Pastikan kata yang tidak ada di file tidak ada di set
    assert 'netral' not in lex_pos
    assert 'netral' not in lex_neg

def test_klasifikasi_sentimen_positif(leksikon_mock):
    """
    Tes 2: Menguji klasifikasi untuk teks yang jelas-jelas positif.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = "pelayanannya hebat dan bagus"
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert isinstance(hasil, pd.Series)
    assert hasil['sentimen'] == 'positif'
    assert hasil['skor_sentimen'] == 2

def test_klasifikasi_sentimen_negatif(leksikon_mock):
    """
    Tes 3: Menguji klasifikasi untuk teks yang jelas-jelas negatif.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = "makanannya buruk dan pelayanannya lambat"
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert hasil['sentimen'] == 'negatif'
    assert hasil['skor_sentimen'] == -2

def test_klasifikasi_sentimen_netral_imbang(leksikon_mock):
    """
    Tes 4: Menguji klasifikasi untuk teks dengan sentimen seimbang (positif vs negatif).
    Hasilnya harus netral dengan skor 0.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = "ruangannya bagus tapi makanannya jelek"
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert hasil['sentimen'] == 'netral'
    assert hasil['skor_sentimen'] == 0

def test_klasifikasi_sentimen_netral_tanpa_kata_kunci(leksikon_mock):
    """
    Tes 5: Menguji klasifikasi untuk teks yang tidak mengandung kata dari leksikon.
    Hasilnya harus netral dengan skor 0.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = "meja itu berwarna coklat"
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert hasil['sentimen'] == 'netral'
    assert hasil['skor_sentimen'] == 0

def test_klasifikasi_sentimen_teks_kosong(leksikon_mock):
    """
    Tes 6: Menguji klasifikasi untuk string kosong.
    Ini adalah edge case untuk memastikan tidak ada error.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = ""
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert hasil['sentimen'] == 'netral'
    assert hasil['skor_sentimen'] == 0

def test_klasifikasi_sentimen_dengan_duplikat(leksikon_mock):
    """
    Tes 7: Menguji apakah kata yang sama dihitung beberapa kali.
    """
    lex_pos, lex_neg = leksikon_mock
    teks = "sangat bagus bagus bagus, tapi ada satu masalah"
    hasil = klasifikasi_sentimen(teks, lex_pos, lex_neg)
    
    assert hasil['sentimen'] == 'positif'
    assert hasil['skor_sentimen'] == 2 # (bagus: +1) + (bagus: +1) + (bagus: +1) - (masalah: -1) = 2
