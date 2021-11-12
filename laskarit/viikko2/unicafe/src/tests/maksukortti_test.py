import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_lisaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_rahan_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_rahan_onnistunut_ottaminen_palauttaa_truen(self):
        vastaus = self.maksukortti.ota_rahaa(5)
        self.assertEqual(vastaus, True)

    def test_rahaa_ei_voi_nostaa_yli_saldon(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_rahan_epaonnistunut_ottaminen_palauttaa_falsen(self):
        vastaus = self.maksukortti.ota_rahaa(20)
        self.assertEqual(vastaus, False)