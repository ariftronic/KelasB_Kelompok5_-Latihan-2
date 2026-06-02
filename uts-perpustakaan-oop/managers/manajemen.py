# [SOLID] Single Responsibility Principle (SRP): 
# Class ini HANYA mengurus penyimpanan data dan logika bisnis (CRUD). Tidak ada fungsi print() atau input() di sini.
class ManajemenPerpustakaan:
    def __init__(self):
        self.daftar_koleksi = []

    def tambah_koleksi(self, koleksi):
        self.daftar_koleksi.append(koleksi)
        return True

    def hapus_koleksi(self, kode):
        for koleksi in self.daftar_koleksi:
            if koleksi.kode == kode:
                self.daftar_koleksi.remove(koleksi)
                return True
        return False

    def get_semua_koleksi(self):
        return self.daftar_koleksi