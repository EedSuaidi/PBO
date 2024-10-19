class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama
        self.__ktp = ktp
        self._limit_pinjaman = limit_pinjaman

    def get_ktp(self):
        return self.__ktp
    
    def display(self):
        print(f"{self.nama}     -     {self.__ktp}     -     Rp. {'{:,.0f}'.format(self._limit_pinjaman)}")

class Pinjaman(Debitur):
    def __init__(self, nama, ktp, limit_pinjaman, jumlah_pinjaman, suku_bunga, limit_waktu):
        super().__init__(nama, ktp, limit_pinjaman)
        self.jumlah_pinjaman = jumlah_pinjaman
        self.suku_bunga = suku_bunga
        self.limit_waktu = limit_waktu
        self.angsuran = (jumlah_pinjaman * suku_bunga / 100) + (jumlah_pinjaman * suku_bunga / 100 / limit_waktu)
    
    def display(self):
        print(f"{self.nama}     -     Rp. {'{:,.0f}'.format(self.jumlah_pinjaman)}     -     {self.suku_bunga}     -     {self.limit_waktu}     -     Rp. {'{:,.0f}'.format(self.angsuran)}")



goku = Debitur("Goku", "111", 50000000)
conan = Debitur("Conan", "222", 30000000)
boruto = Debitur("Boruto", "333", 20000000)
bowo = Debitur("Bowo", "444", 50000000)
thoriq = Debitur("Thoriq", "555", 50000000)
fufufafa = Debitur("Fufufafa", "666", 20000000)

list_debitur = [goku, conan, boruto, bowo, thoriq, fufufafa]
list_pinjaman = []



while True:
    print("=============== Aplikasi Pinjol ===============")
    print("0. Exit")
    print("1. Kelola Debitur")
    print("2. Kelola Pinjaman")
    menu = input("Pilih Menu [0-2] : ")
    print("")

    if menu == "0":
        break

    elif menu == "1":
        print("========== Kelola Debitur ==========")
        print("0. Kembali")
        print("1. Tampilkan Semua Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Debitur")
        submenu = input("Pilih Menu [0-3] : ")
        print("")

        if submenu == "0":
            print("")
        elif submenu == "1":
            print("========== Daftar Debitur ==========")
            print("Nama     -     No. KTP     -     Limit Pinjaman\n")
            for i in list_debitur:
                i.display()
            print("")
        elif submenu == "2":
            nama = input("Masukkan Nama Debitur Yang Ingin Dicari : ")
            print("")
            for i in list_debitur:
                if i.nama == nama:
                    print("========== Daftar Debitur ==========")
                    print("Nama     -     No. KTP     -     Limit Pinjaman\n")
                    i.display()
                    print("")
                    break
            else:
                print("Debitur Tidak Ditemukan!\n")
        elif submenu == "3":
            ktp = input("Masukkan No. KTP Debitur Baru : ")
            for i in list_debitur:
                if i.get_ktp() == ktp:
                    print("Debitur Sudah Ada!\n")
                    break
            else:
                nama = input("Masukkan Nama Debitur Baru : ")
                limit_pinjaman = int(input("Masukkan Limit Pinjaman Debitur Baru: "))
                debitur = Debitur(nama, ktp, limit_pinjaman)
                list_debitur.append(debitur)
                print(f"{nama} berhasil ditambahkan!\n")
                

    elif menu == "2":
        print("========== Kelola Pinjaman ==========")
        print("0. Kembali")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        submenu = input("Pilih Menu [0-2] : ")
        print("")

        if submenu == "0":
            print("")
        elif submenu == "1":
            nama = input("Masukkan Nama Debitur : ")
            for i in list_debitur:
                if i.nama == nama:
                    jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman : "))
                    if jumlah_pinjaman <= i._limit_pinjaman:
                        suku_bunga = int(input("Masukkan Suku Bunga (dalam persen) : "))
                        limit_waktu = int(input("Masukkan Limit Waktu (dalam Bulan) : "))
                        pinjaman = Pinjaman(nama, i.get_ktp(), i._limit_pinjaman, jumlah_pinjaman, suku_bunga, limit_waktu)
                        list_pinjaman.append(pinjaman)
                        print(f"Pinjaman Atas Nama {nama} berhasil ditambahkan!\n")
                        break
                    else:
                        print("Limit Pinjaman Debitur Tidak Cukup!\n")
                        break
            else:
                print(f"{nama} Belum Terdaftar!\n")
        elif submenu == "2":
            print("========== Daftar Pinjaman ==========")
            print("Nama Debitur     -     Pinjaman     -     Bunga     -     Bulan     -     Angsuran\n")
            for i in list_pinjaman:
                i.display()
                print("")
