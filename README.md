# 📚 Sistem Manajemen Perpustakaan CLI

> **Tugas Latihan 2 / UTS — Object-Oriented Programming**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=for-the-badge)
![SOLID](https://img.shields.io/badge/Design-SOLID_Principles-success?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 📖 Tentang Proyek

**Sistem Manajemen Perpustakaan CLI** adalah program *Command Line Interface* (CLI) interaktif yang dikembangkan sebagai tugas UTS mata kuliah Object-Oriented Programming. Program ini dirancang untuk mengelola data koleksi perpustakaan secara menyeluruh, mencakup:

- 📕 **Buku**
- 📰 **Majalah**
- 📄 **Jurnal**
- 🎬 **DVD Film Dokumenter** *(fitur ekspansi)*

Proyek ini bukan sekadar program fungsional — seluruh arsitektur kode dibangun di atas fondasi **prinsip desain S-O-L-I-D** dan tiga pilar utama OOP (**Inheritance, Abstraction, Polymorphism**), sehingga menghasilkan sistem yang *scalable*, *maintainable*, dan mudah dikembangkan lebih lanjut.

---

## 👥 Anggota Kelompok 5 (Kelas B)

| No | Nama | Peran | Fokus Implementasi |
|:--:|------|-------|-------------------|
| 1 | **Arif** | 🏗️ System Architect & Repository Manager | Abstract Class & Dependency Inversion Principle (DIP) |
| 2 | **Awang** | 🧱 Data Modeler Core | Subclassing & Liskov Substitution Principle (LSP) |
| 3 | **Danang** | 🔧 Feature Expander | Penambahan Koleksi DVD & Open/Closed Principle (OCP) |
| 4 | **Afrizal** | ⚙️ Business Logic Manager | CRUD Logic & Single Responsibility Principle (SRP) |
| 5 | **Dika** | 🖥️ UI & CLI Integrator | Terminal Menu & Single Responsibility Principle (SRP) |

---

## ✨ Fitur Program

- ➕ **Tambah Koleksi** — Menambahkan item baru (Buku, Majalah, Jurnal, atau DVD) ke dalam perpustakaan
- 📋 **Tampilkan Semua Koleksi** — Menampilkan seluruh data koleksi yang tersimpan dalam format yang rapi
- 🔍 **Cari Koleksi** — Mencari item berdasarkan judul atau atribut tertentu
- ✏️ **Perbarui Koleksi** — Mengedit data koleksi yang sudah ada
- 🗑️ **Hapus Koleksi** — Menghapus item dari perpustakaan
- 🎬 **Manajemen DVD** — Pengelolaan khusus untuk koleksi DVD Film Dokumenter
- 🔄 **Menu Interaktif** — Navigasi berbasis menu terminal yang intuitif dan mudah digunakan

---

## 🧩 Penerapan Prinsip S-O-L-I-D

### **S — Single Responsibility Principle (SRP)**
> *"Setiap kelas hanya boleh memiliki satu alasan untuk berubah."*

Diterapkan melalui pemisahan tanggung jawab yang tegas antar modul:
- `models/` → hanya bertanggung jawab untuk mendefinisikan **struktur data** koleksi
- `managers/manajemen.py` → hanya menangani **logika bisnis** (CRUD)
- `ui/menu.py` → hanya bertanggung jawab pada **tampilan & interaksi** CLI dengan pengguna

---

### **O — Open/Closed Principle (OCP)**
> *"Kelas terbuka untuk ekstensi, tetapi tertutup untuk modifikasi."*

Diterapkan saat menambahkan **DVD Film Dokumenter** sebagai tipe koleksi baru. Fitur ini ditambahkan dengan membuat `models/dvd.py` yang mewarisi kelas abstrak `Koleksi` — **tanpa mengubah satu baris pun** kode yang sudah ada sebelumnya di `core/koleksi.py` atau `managers/manajemen.py`.

---

### **L — Liskov Substitution Principle (LSP)**
> *"Objek dari subclass harus dapat menggantikan objek dari superclass-nya."*

Setiap subclass (`Buku`, `Majalah`, `Jurnal`, `DVD`) mengimplementasikan method abstrak dari `Koleksi` secara penuh dan konsisten. Objek dari kelas-kelas turunan ini dapat digunakan secara saling tukar di dalam `ManajemenPerpustakaan` tanpa menyebabkan error atau perilaku yang tidak terduga.

---

### **I — Interface Segregation Principle (ISP)**
> *"Klien tidak boleh dipaksa bergantung pada method yang tidak mereka gunakan."*

Kelas abstrak `Koleksi` di `core/koleksi.py` hanya mendefinisikan **kontrak minimum** yang relevan dan wajib dimiliki oleh setiap jenis koleksi. Tidak ada satu kelas turunan pun yang terpaksa mengimplementasikan method yang tidak relevan untuk jenisnya.

---

### **D — Dependency Inversion Principle (DIP)**
> *"Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus bergantung pada abstraksi."*

`ManajemenPerpustakaan` (high-level module) tidak bergantung langsung pada `Buku`, `Majalah`, atau kelas konkret lainnya. Sebaliknya, ia hanya bergantung pada abstraksi `Koleksi`. Ini memungkinkan penambahan tipe koleksi baru tanpa mengubah logika di `manajemen.py`.

---

## 📁 Struktur Direktori
sistem-manajemen-perpustakaan/

│

├── 📄 main.py                  # Entry point utama program

│

├── 📂 core/

│   └── koleksi.py              # Abstract Class: Koleksi (base contract)

│

├── 📂 models/

│   ├── buku.py                 # Model: Buku (subclass Koleksi)

│   ├── majalah.py              # Model: Majalah (subclass Koleksi)

│   ├── jurnal.py               # Model: Jurnal (subclass Koleksi)

│   └── dvd.py                  # Model: DVD Dokumenter (subclass Koleksi)

│

├── 📂 managers/

│   └── manajemen.py            # Business Logic: CRUD Perpustakaan

│

├── 📂 ui/

│   └── menu.py                 # CLI Interface: Menu & Interaksi Pengguna

│

└── 📄 README.md

---

## 🚀 Cara Menjalankan Program

### Prasyarat
Pastikan **Python 3.10 atau lebih baru** sudah terinstal di komputer Anda.
```bash
python --version
```

### Langkah 1 — Clone Repository
```bash
git clone https://github.com/NAMA_USER/NAMA_REPO.git
```

### Langkah 2 — Masuk ke Direktori Proyek
```bash
cd NAMA_REPO
```

### Langkah 3 — Jalankan Program
```bash
python main.py
```

> 💡 **Catatan:** Tidak ada dependensi eksternal yang perlu diinstal. Program ini hanya menggunakan Python *standard library*.

---

<div align="center">

Dibuat oleh **Kelompok 5 — Kelas B**
Mata Kuliah Object-Oriented Programming

</div>
