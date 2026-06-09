# [SOLID] Single Responsibility Principle (SRP): 
# Class ini HANYA mengurus penyimpanan data dan logika bisnis (CRUD). Tidak ada fungsi print() atau input() di sini.
class ManajemenPerpustakaan:
    def __init__(self):
        self.daftar_koleksi = []

        self.tambah_service = TambahKoleksi()
        self.hapus_service = HapusKoleksi()
        self.lihat_service = LihatKoleksi()

    def tambah_koleksi(self, koleksi):
        return self.tambah_service.execute(
            self.daftar_koleksi,
            koleksi
        )

    def hapus_koleksi(self, kode):
        return self.hapus_service.execute(
            self.daftar_koleksi,
            kode
        )

    def get_semua_koleksi(self):
        return self.lihat_service.execute(
            self.daftar_koleksi
        )

class TambahKoleksi:
     def execute(self, daftar_koleksi, koleksi):
        daftar_koleksi.append(koleksi)
        return True

class HapusKoleksi:
    def execute(self, daftar_koleksi, kode):
        for koleksi in daftar_koleksi:
            if koleksi.kode == kode:
                daftar_koleksi.remove(koleksi)
                return True
        return False

class LihatKoleksi:
    def execute(self, daftar_koleksi):
        return daftar_koleksi