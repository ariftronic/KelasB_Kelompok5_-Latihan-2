from core.koleksi import Koleksi

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        super().__init__(kode, judul, tahun)
        self.jenis = "Jurnal"
        self.penerbit = penerbit
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampilkan_info(self):
        return f"Jenis\t\t: {self.jenis}\nKode Koleksi\t: {self.kode}\nJudul\t\t: {self.judul}\nThn Terbit\t: {self.tahun}\nPenerbit\t: {self.penerbit}\nImpact Factor\t: {self.impact_factor}\nBidang Studi\t: {self.bidang_studi}\n"