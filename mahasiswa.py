class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

class ManajemenNilai:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, nama, nilai):
        mhs = Mahasiswa(nama, nilai)
        self.data_mahasiswa.append(mhs)

    def tampilkan_mahasiswa(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            for mhs in self.data_mahasiswa:
                print(f"Nama: {mhs.nama}, Nilai: {mhs.nilai}")

    def rata_rata(self):
        if not self.data_mahasiswa:
            return 0
        total = sum(mhs.nilai for mhs in self.data_mahasiswa)
        return total / len(self.data_mahasiswa)
