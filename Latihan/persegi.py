from penghitung_bangun_datar import PenghitungBangunDatar

class Persegi(PenghitungBangunDatar):
    def __init__(self, sisi: float):
        super().__init__(sisi)
        
    def hitung_luas(self):
        print("luas persegi", self.get_sisi() ** 2)
        
    def hitung_keliling(self):
        print("keliling persegi", self.get_sisi() * 4)