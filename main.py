from mahasiswa import ManajemenNilai
from menu import tampil_menu

def main():
    mn = ManajemenNilai()

    while True:
        tampil_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nama = input("Masukkan nama mahasiswa: ")
            nilai = float(input("Masukkan nilai: "))
            mn.tambah_mahasiswa(nama, nilai)
            print("Data mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            mn.tampilkan_mahasiswa()

        elif pilihan == "3":
            rata = mn.rata_rata()
            print(f"Rata-rata nilai mahasiswa: {rata:.2f}")

        elif pilihan == "4":
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()