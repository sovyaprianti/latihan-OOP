class ViewMahasiswa:
    @staticmethod
    def tampilkan_mahasiswa(mahasiswa):
        print(f"NIM: {mahasiswa.nim}, Nama: {mahasiswa.nama}, Jurusan: {mahasiswa.jurusan}")

    @staticmethod
    def tampilkan_semua_mahasiswa(data_mahasiswa):
        if not data_mahasiswa:
            print("Data mahasiswa kosong.")
        else:
            for mahasiswa in data_mahasiswa:
                ViewMahasiswa.tampilkan_mahasiswa(mahasiswa)