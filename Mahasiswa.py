class Mahasiswa:
    def _init_(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def _init_(self):
        self.data = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama_baru=None, jurusan_baru=None):
        for m in self.data:
            if m.nim == nim:
                if nama_baru:
                    m.nama = nama_baru
                if jurusan_baru:
                    m.jurusan = jurusan_baru
                return True
        return False

    def cari_mahasiswa(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None