from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def main():
    data = DataMahasiswa()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_mahasiswa()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan.")
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data.hapus_mahasiswa(nim)
            print("Mahasiswa berhasil dihapus.")
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama_baru = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            jurusan_baru = input("Masukkan Jurusan baru (kosongkan jika tidak diubah): ")
            if data.ubah_mahasiswa(nim, nama_baru, jurusan_baru):
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mahasiswa = data.cari_mahasiswa(nim)
            if mahasiswa:
                ViewMahasiswa.tampilkan_mahasiswa(mahasiswa)
            else:
                print("Mahasiswa tidak ditemukan.")
        elif pilihan == "5":
            ViewMahasiswa.tampilkan_semua_mahasiswa(data.data)
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if _name_ == "_main_":
    main()