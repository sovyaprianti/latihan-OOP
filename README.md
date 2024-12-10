# latihan-OOP
# Latihan-OOP

Program ini adalah aplikasi sederhana yang dijalankan di terminal atau konsol. Dengan aplikasi ini, Anda bisa mengelola data mahasiswa, seperti menambah data, mengubah data, menghapus data, mencari data berdasarkan NIM, dan menampilkan semua data mahasiswa.

Struktur Folder
Untuk menjalankan program ini, Anda perlu membuat beberapa folder dan file. Tujuannya agar program terorganisir dengan baik. Struktur foldernya seperti ini:
project_root/
├── data/
│   ├── _init_.py         # File ini wajib ada untuk membuat folder "data" jadi sebuah modul Python.
│   ├── mahasiswa.py        # Berisi logika data mahasiswa.
├── view/
│   ├── _init_.py         # File ini juga untuk menjadikan folder "view" modul Python.
│   ├── input_form.py       # Berisi form untuk memasukkan atau mengubah data mahasiswa.
│   ├── mahasiswa.py        # Berisi cara menampilkan data mahasiswa di konsol.
├── main.py                 # File utama untuk menjalankan program.

Cara Kerja Program
1. File main.py adalah pusat program. Ketika dijalankan, program akan menampilkan menu utama. Anda bisa memilih:
Tambah data mahasiswa.
Ubah data mahasiswa.
Hapus data mahasiswa.
Cari mahasiswa berdasarkan NIM.
Menampilkan semua data mahasiswa.
2. Folder data:
mahasiswa.py:
class Mahasiswa: Representasi seorang mahasiswa dengan atribut NIM, nama, dan prodi.
class DataMahasiswa: Tempat untuk menyimpan daftar mahasiswa, menambah, mengubah, menghapus, atau mencari data.
3. Folder view:
input_form.py: Mengelola masukan dari pengguna, seperti NIM, nama, atau prodi.
mahasiswa.py: Mengelola cara data mahasiswa ditampilkan di layar.

Penjelasan Setiap Bagian
1. mahasiswa.py di folder data
Berisi logika utama untuk data mahasiswa:
Class Mahasiswa:
Digunakan untuk membuat data mahasiswa baru dengan atribut seperti NIM, nama, dan prodi.
Class DataMahasiswa:
Digunakan untuk menyimpan dan memproses data mahasiswa, seperti menambah, menghapus, mengubah, atau mencari.
2. input_form.py di folder view
Berisi form sederhana yang meminta pengguna memasukkan data, misalnya:
Masukkan NIM mahasiswa.
Masukkan nama mahasiswa.
Masukkan prodi mahasiswa.
3. mahasiswa.py di folder view
Berisi logika untuk menampilkan data mahasiswa ke layar. Contohnya:
Menampilkan daftar semua mahasiswa.
Menampilkan detail seorang mahasiswa.
4. main.py
Berisi menu utama program. Pengguna bisa memilih tindakan (tambah data, ubah data, hapus data, dll.), dan program akan memproses pilihan tersebut.
Cara Menjalankan
1. Siapkan folder dan file seperti struktur di atas.
2. Buka terminal di folder utama proyek Anda.
3. Jalankan program dengan perintah:
python main.py
4. Anda akan melihat menu seperti ini:
Menu Utama:
  1. Tambah Mahasiswa
  2. Ubah Mahasiswa
  3. Hapus Mahasiswa
  4. Cari Mahasiswa
  5. Tampilkan Semua Mahasiswa
  6. Keluar
5. Pilih angka sesuai menu yang Anda inginkan, lalu ikuti petunjuk yang diberikan.

