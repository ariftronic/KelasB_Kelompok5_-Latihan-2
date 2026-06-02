from managers.manajemen import ManajemenPerpustakaan
from models.buku import Buku
from models.majalah import Majalah
from models.jurnal import Jurnal
from models.dvd_dokumenter import DVDDokumenter

# [SOLID] Single Responsibility Principle (SRP): 
# Class ini khusus mengurus tampilan terminal (UI) dan interaksi user (input/output).
class MenuUI:
    def __init__(self):
        self.manajemen = ManajemenPerpustakaan()

    def jalankan(self):
        while True:
            print("\n====================")
            print("MENU PROGRAM")
            print("--------------------")
            print("1. Tambah data koleksi")
            print("2. Hapus data koleksi")
            print("3. Tampil semua data koleksi")
            print("4. Keluar")
            
            pilihan = input("\nNomor yang dipilih: ")

            if pilihan == '1':
                self.menu_tambah()
            elif pilihan == '2':
                self.menu_hapus()
            elif pilihan == '3':
                self.menu_tampil()
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid.")

    def menu_tambah(self):
        print("\nJENIS KOLEKSI YANG AKAN DITAMBAH")
        print("1. Buku")
        print("2. Majalah")
        print("3. Jurnal")
        print("4. DVD Film Dokumenter")
        
        jenis = input("\nNomor yang dipilih: ")
        
        kode = input("Masukkan Kode Koleksi\t: ")
        judul = input("Masukkan Judul\t\t: ")
        tahun = input("Masukkan Tahun Terbit\t: ")

        if jenis == '1':
            pengarang = input("Masukkan Pengarang\t: ")
            penerbit = input("Masukkan Penerbit\t: ")
            koleksi = Buku(kode, judul, tahun, pengarang, penerbit)
        elif jenis == '2':
            penerbit = input("Masukkan Penerbit\t: ")
            edisi = input("Masukkan Edisi\t\t: ")
            koleksi = Majalah(kode, judul, tahun, penerbit, edisi)
        elif jenis == '3':
            penerbit = input("Masukkan Penerbit\t: ")
            bidang = input("Masukkan Bidang Studi\t: ")
            impact = input("Masukkan Impact Factor\t: ")
            koleksi = Jurnal(kode, judul, tahun, penerbit, bidang, impact)
        elif jenis == '4':
            bidang = input("Masukkan Bidang Ilmu\t: ")
            durasi = input("Masukkan Durasi (menit)\t: ")
            koleksi = DVDDokumenter(kode, judul, tahun, bidang, durasi)
        else:
            print("Pilihan tidak valid.")
            return

        self.manajemen.tambah_koleksi(koleksi)
        print("----------------------------------------")
        print("Tambah Koleksi Sukses")
        input("Tekan [ENTER] untuk kembali ke menu program")

    def menu_hapus(self):
        print("\nHAPUS DATA KOLEKSI")
        kode = input("Masukkan Kode Koleksi\t: ")
        if self.manajemen.hapus_koleksi(kode):
            print("----------------------------------------")
            print("Hapus data koleksi sukses")
        else:
            print("----------------------------------------")
            print("Data tidak ditemukan")
        input("Tekan [ENTER] untuk kembali ke menu program")

    def menu_tampil(self):
        print("\nDATA KOLEKSI\n")
        koleksi_list = self.manajemen.get_semua_koleksi()
        if not koleksi_list:
            print("Belum ada data.")
        else:
            for i, koleksi in enumerate(koleksi_list, 1):
                print(f"Koleksi {i}:")
                print(koleksi.tampilkan_info())
        input("Tekan [ENTER] untuk kembali ke menu program")
