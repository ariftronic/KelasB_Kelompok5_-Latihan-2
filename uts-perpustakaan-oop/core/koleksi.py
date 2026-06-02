from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun

    @abstractmethod
    def tampilkan_info(self):
        pass