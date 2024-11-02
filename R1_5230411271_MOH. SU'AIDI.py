class Produk:
    def __init__(self, kode, nama, jenis):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis


class Snack(Produk):
    def __init__(self, kode, nama, harga, jenis="Snack"):
        super().__init__(kode, nama, jenis)
        self.harga = harga

    def add(self, kode, nama, harga, jenis="Snack"):
        return Snack(kode, nama, harga, jenis)

    def remove(self, kode):
        global list_snack
        for snack in list_snack:
            if snack.kode == kode:
                list_snack.remove(snack)
                print(f"Snack dengan kode {kode} berhasil dihapus!\n")
                return
        print("Kode snack tidak ditemukan!\n")


class Makanan(Produk):
    def __init__(self, kode, nama, harga, jenis="Makanan"):
        super().__init__(kode, nama, jenis)
        self.harga = harga

    def add(self, kode, nama, harga, jenis="Makanan"):
        return Makanan(kode, nama, harga, jenis)

    def remove(self, kode):
        global list_makanan
        for makanan in list_makanan:
            if makanan.kode == kode:
                list_makanan.remove(makanan)
                print(f"Makanan dengan kode {kode} berhasil dihapus!\n")
                return
        print("Kode makanan tidak ditemukan!\n")


class Minuman(Produk):
    def __init__(self, kode, nama, harga, jenis="Minuman"):
        super().__init__(kode, nama, jenis)
        self.harga = harga

    def add(self, kode, nama, harga, jenis="Minuman"):
        return Minuman(kode, nama, harga, jenis)

    def remove(self, kode):
        global list_minuman
        for minuman in list_minuman:
            if minuman.kode == kode:
                list_minuman.remove(minuman)
                print(f"Minuman dengan kode {kode} berhasil dihapus!\n")
                return
        print("Kode minuman tidak ditemukan!\n")


class Pegawai:
    def __init__(self, nik, nama, alamat):
        self._nik = nik
        self.nama = nama
        self.alamat = alamat

    def add(self, nik, nama, alamat):
        return Pegawai(nik, nama, alamat)

    def remove(self, nik):
        global list_pegawai
        for pegawai in list_pegawai:
            if pegawai._nik == nik:
                list_pegawai.remove(pegawai)
                print(f"Pegawai dengan NIK {nik} berhasil dihapus!\n")
                return
        print("NIK pegawai tidak ditemukan!\n")


class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

    def add(self, no_transaksi, detail_transaksi):
        return Transaksi(no_transaksi, detail_transaksi)


class Struk:
    def __init__(
        self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga
    ):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

    def add(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        return Struk(
            no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga
        )


snack1 = Snack("SN001", "Kerupuk", 5000)
snack2 = snack1.add("SN002", "Kacang", 10000)
snack3 = snack1.add("SN003", "Permen", 2000)
snack4 = snack1.add("SN004", "Coklat", 3000)
snack5 = snack1.add("SN005", "Chiki", 4000)

makanan1 = Makanan("MA001", "Nasi Goreng", 15000)
makanan2 = makanan1.add("MA002", "Mie Goreng", 12000)
makanan3 = makanan1.add("MA003", "Nasi Uduk", 20000)
makanan4 = makanan1.add("MA004", "Nasi Kuning", 18000)
makanan5 = makanan1.add("MA005", "Nasi Rames", 25000)

minuman1 = Minuman("MI001", "Es Teh", 5000)
minuman2 = minuman1.add("MI002", "Es Jeruk", 6000)
minuman3 = minuman1.add("MI003", "Es Campur", 7000)
minuman4 = minuman1.add("MI004", "Es Teler", 8000)
minuman5 = minuman1.add("MI005", "Es Doger", 9000)

pegawai1 = Pegawai("111", "Budi", "Jakarta")
pegawai2 = pegawai1.add("222", "Andi", "Bandung")
pegawai3 = pegawai1.add("333", "Siti", "Bogor")
pegawai4 = pegawai1.add("444", "Rose", "Pekalongan")

list_snack = [snack1, snack2, snack3, snack4, snack5]
list_makanan = [makanan1, makanan2, makanan3, makanan4, makanan5]
list_minuman = [minuman1, minuman2, minuman3, minuman4, minuman5]
list_pegawai = [pegawai1, pegawai2, pegawai3, pegawai4]
list_transaksi = []


while True:
    print("==================== Aplikasi Kasir ====================")
    print("0. Keluar")
    print("1. Snack")
    print("2. Makanan")
    print("3. Minuman")
    print("4. Pegawai")
    print("5. Transaksi")
    menu = input("Pilih menu [0-5]: ")
    print("")

    if menu == "0":
        break

    elif menu == "1":
        print("=============== Snack ===============")
        print("0. Kembali")
        print("1. List Snack")
        print("2. Tambah Snack")
        print("3. Hapus Snack")
        menu_snack = input("Pilih Menu [0-3]: ")
        print("")

        if menu_snack == "0":
            print("")
        elif menu_snack == "1":
            print("=============== List Snack ===============")
            print("Kode - Nama - Harga\n")
            for snack in list_snack:
                print(
                    f"{snack.kode} - {snack.nama} - Rp. {'{:,.0f}'.format(snack.harga)}"
                )
            print("")
        elif menu_snack == "2":
            if list_snack:
                last_kode = list_snack[-1].kode
                new_kode = "SN" + str(int(last_kode[2:]) + 1).zfill(3)
            else:
                new_kode = "SN001"
            nama = input("Nama Snack: ")
            harga = int(input("Harga: "))
            snack = snack1.add(new_kode, nama, harga)
            list_snack.append(snack)
            print(f"{nama} berhasil ditambahkan!\n")
        elif menu_snack == "3":
            kode = input("Kode Snack: ")
            snack1.remove(kode)

    elif menu == "2":
        print("=============== Makanan ===============")
        print("0. Kembali")
        print("1. List Makanan")
        print("2. Tambah Makanan")
        print("3. Hapus Makanan")
        menu_makanan = input("Pilih Menu [0-3]: ")
        print("")

        if menu_makanan == "0":
            print("")
        elif menu_makanan == "1":
            print("=============== List Makanan ===============")
            print("Kode - Nama - Harga\n")
            for makanan in list_makanan:
                print(
                    f"{makanan.kode} - {makanan.nama} - Rp. {'{:,.0f}'.format(makanan.harga)}"
                )
            print("")
        elif menu_makanan == "2":
            if list_makanan:
                last_kode = list_makanan[-1].kode
                new_kode = "MA" + str(int(last_kode[2:]) + 1).zfill(3)
            else:
                new_kode = "MA001"
            nama = input("Nama Makanan: ")
            harga = int(input("Harga: "))
            makanan = makanan1.add(new_kode, nama, harga)
            list_makanan.append(makanan)
            print(f"{nama} berhasil ditambahkan!\n")
        elif menu_makanan == "3":
            kode = input("Kode Makanan: ")
            makanan1.remove(kode)

    elif menu == "3":
        print("=============== Minuman ===============")
        print("0. Kembali")
        print("1. List Minuman")
        print("2. Tambah Minuman")
        print("3. Hapus Minuman")
        menu_minuman = input("Pilih Menu [0-3]: ")
        print("")

        if menu_minuman == "0":
            print("")
        elif menu_minuman == "1":
            print("=============== List Minuman ===============")
            print("Kode - Nama - Harga\n")
            for minuman in list_minuman:
                print(
                    f"{minuman.kode} - {minuman.nama} - Rp. {'{:,.0f}'.format(minuman.harga)}"
                )
            print("")
        elif menu_minuman == "2":
            if list_minuman:
                last_kode = list_minuman[-1].kode
                new_kode = "MI" + str(int(last_kode[2:]) + 1).zfill(3)
            else:
                new_kode = "MI001"
            nama = input("Nama Minuman: ")
            harga = int(input("Harga: "))
            minuman = minuman1.add(new_kode, nama, harga)
            list_minuman.append(minuman)
            print(f"{nama} berhasil ditambahkan!\n")
        elif menu_minuman == "3":
            kode = input("Kode Minuman: ")
            minuman1.remove(kode)

    elif menu == "4":
        print("=============== Pegawai ===============")
        print("0. Kembali")
        print("1. List Pegawai")
        print("2. Tambah Pegawai")
        print("3. Hapus Pegawai")
        menu_pegawai = input("Pilih Menu [0-3]: ")
        print("")

        if menu_pegawai == "0":
            print("")
        elif menu_pegawai == "1":
            print("=============== List pegawai ===============")
            print("NIK - Nama - Harga\n")
            for pegawai in list_pegawai:
                print(f"{pegawai._nik} - {pegawai.nama} - {pegawai.alamat}")
            print("")
        elif menu_pegawai == "2":
            nik = input("NIK Pegawai: ")
            nama = input("Nama Pegawai: ")
            alamat = input("Alamat Pegawai: ")
            pegawai = pegawai1.add(nik, nama, alamat)
            list_pegawai.append(pegawai)
            print(f"{nama} berhasil ditambahkan!\n")
        elif menu_pegawai == "3":
            nik = input("NIK pegawai: ")
            pegawai1.remove(nik)

    elif menu == "5":
        print("=============== Transaksi ===============")
        keranjang = []
        nama_produk = []
        jumlah_produk = []

        nama_pegawai = input("Nama Pegawai: ")
        for pegawai in list_pegawai:
            if pegawai.nama == nama_pegawai:
                while True:
                    kode = input("Kode Produk Yang Ingin Dibeli: ")
                    jumlah = int(input("Jumlah Produk: "))
                    produk_ditemukan = False

                    if kode[0:2] == "SN":
                        for snack in list_snack:
                            if snack.kode == kode:
                                total_harga = snack.harga * jumlah
                                keranjang.append((snack.nama, jumlah, total_harga))
                                produk_ditemukan = True
                                break
                    elif kode[0:2] == "MA":
                        for makanan in list_makanan:
                            if makanan.kode == kode:
                                total_harga = makanan.harga * jumlah
                                keranjang.append((makanan.nama, jumlah, total_harga))
                                produk_ditemukan = True
                                break
                    elif kode[0:2] == "MI":
                        for minuman in list_minuman:
                            if minuman.kode == kode:
                                total_harga = minuman.harga * jumlah
                                keranjang.append((minuman.nama, jumlah, total_harga))
                                produk_ditemukan = True
                                break

                    if list_transaksi:
                        last_kode = list_transaksi[-1].no_transaksi
                        new_kode = "TR" + str(int(last_kode[2:]) + 1).zfill(3)
                    else:
                        new_kode = "TR001"

                    detail_transaksi = f"{kode} - {jumlah}"
                    transaksi = Transaksi(new_kode, detail_transaksi)
                    list_transaksi.append(transaksi)

                    if not produk_ditemukan:
                        print("Kode produk tidak ditemukan!\n")
                    else:
                        print("")

                    lanjut = input(
                        "Apakah Anda Ingin Melanjutkan Transaksi? (Y/N): "
                    ).upper()
                    if lanjut != "Y":
                        break

                struk = Struk(
                    new_kode, nama_pegawai, nama_produk, jumlah_produk, total_harga
                )

                print("\n=============== Struk ===============\n")
                print(f"No Transaksi: {new_kode}")
                print(f"Nama Pegawai: {nama_pegawai}\n")
                total_belanja = 0
                for item in keranjang:
                    total_belanja += item[2]
                    print(f"{item[0]} - {item[1]} - Rp. {'{:,.0f}'.format(item[2])}")
                print("")
                print(f"Total Belanja: Rp. {'{:,.0f}'.format(total_belanja)}\n")
                break

        else:
            print("Nama pegawai tidak ditemukan!\n")
