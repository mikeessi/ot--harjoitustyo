import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_oikea_maara_rahaa_kassassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_oikea_maara_edullisia_lounaita_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_oikea_maara_maukkaita_lounaita_myyty(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_lisaa_saldon_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_lisaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_vaihtoraha_palautetaan_oikein(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(340)
        self.assertEqual(vastaus, 100)

    def test_syo_edullisesti_kateisella_ei_tarpeeksi_rahaa(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vastaus, 100)

    def test_syo_maukkaasti_kateisella_lisaa_saldon_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_lisaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_vaihtoraha_palautetaan_oikein(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vastaus, 100)

    def test_syo_maukkaasti_kateisella_ei_tarpeeksi_rahaa(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vastaus, 100)

    def test_syo_edullisesti_kortilla_saldo_pienenee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
    
    def test_syo_edullisesti_kortilla_onnistunut_palauttaa_oikein(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)

    def test_syo_edullisesti_kortilla_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_oikea_saldo(self):
        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 40)
    
    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_lounaat_oikein(self):
        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 4)

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_palauttaa_oikein(self):
        for i in range(5):
            vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, False)
    
    def test_syo_edullisesti_kortilla_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_saldo_pienenee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_syo_maukkaasti_kortilla_onnistunut_palauttaa_oikein(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)

    def test_syo_maukkaasti_kortilla_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_oikea_saldo(self):
        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)
    
    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_lounaat_oikein(self):
        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_palauttaa_oikein(self):
        for i in range(3):
            vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, False)
    
    def test_syo_maukkaasti_kortilla_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_onnistunut_kortin_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_lataa_rahaa_kortille_onnistunut_kassan_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        vastaus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(vastaus, None)