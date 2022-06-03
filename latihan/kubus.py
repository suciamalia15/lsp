from penghitung_bangun_ruang import PenghitungBangunRuang

class Kubus(PenghitungBangunRuang):
    def __init__(self, rusak: float):
        super().__init__(rusak)

    def hitung_luas(self):
        print("Luas kubus", (self.get_rusak() ** 2) * 6)

    def hitung_keliling(self):
        print("Keliling kubus", self.get_rusak() * 12)

    def hitung_volume(self):
        print("Volume kubus", self.get_rusak() ** 3)
        