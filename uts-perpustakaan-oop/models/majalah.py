from core.koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun)
        self.jenis = "Majalah"
        self.penerbit = penerbit
        self.edisi = edisi

    def tampilkan_info(self):
        return f"Jenis\t\t: {self.jenis}\nKode Koleksi\t: {self.kode}\nJudul\t\t: {self.judul}\nTahun Terbit\t: {self.tahun}\nPenerbit\t: {self.penerbit}\nEdisi\t\t: {self.edisi}\n"
