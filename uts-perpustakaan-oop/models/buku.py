from core.koleksi import Koleksi

# [OOP] Inheritance: Buku mewarisi sifat dari Koleksi
# [SOLID] Liskov Substitution Principle (LSP): Objek Buku bisa menggantikan Koleksi tanpa error
class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.jenis = "Buku"
        self.pengarang = pengarang
        self.penerbit = penerbit

    # [OOP] Polymorphism: Implementasi spesifik untuk Buku
    def tampilkan_info(self):
        return f"Jenis\t\t: {self.jenis}\nKode Koleksi\t: {self.kode}\nJudul\t\t: {self.judul}\nThn Terbit\t: {self.tahun}\nPengarang\t: {self.pengarang}\nPenerbit\t: {self.penerbit}\n"
