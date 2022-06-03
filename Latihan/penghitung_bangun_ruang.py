from abc import ABC, abstractmethod

class PenghitungBangunRuang:
    def __init__(self, rusuk: float):
        self.__rusuk = rusuk
        
    @abstractmethod
    def hitung_luas(self):
        pass
    
    @abstractmethod
    def hitung_keliling(self):
        pass
    
    @abstractmethod
    def hitung_volume(self):
        pass