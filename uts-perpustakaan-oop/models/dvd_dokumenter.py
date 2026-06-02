from core.koleksi import Koleksi

class DVDDokumenter(Koleksi):
    def __init__(self, kode, judul, tahun, bidang_ilmu, durasi):
        super().__init__(kode, judul, tahun)
        self.jenis = "DVD Film Dokumenter"
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def tampilkan_info(self):
        return f"Jenis\t\t: {self.jenis}\nKode Koleksi\t: {self.kode}\nJudul\t\t: {self.judul}\nTahun\t\t: {self.tahun}\nBidang Ilmu\t: {self.bidang_ilmu}\nDurasi\t\t: {self.durasi} menit\n"