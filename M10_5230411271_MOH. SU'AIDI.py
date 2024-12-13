import mysql.connector

conn = mysql.connector.connect(
    user="root", password="", host="localhost", database="penjualan"
)

cur = conn.cursor()


# cur.execute(
#     """
# CREATE TABLE pegawai (
#     nik VARCHAR(20) PRIMARY KEY,
#     nama_pegawai VARCHAR(100),
#     alamat_pegawai VARCHAR(255)
# )
# """
# )

# cur.execute(
#     """
# CREATE TABLE transaksi (
#     no_transaksi VARCHAR(20) PRIMARY KEY,
#     detail_transaksi VARCHAR(255)
# )
# """
# )

# cur.execute(
#     """
# CREATE TABLE produk (
#     kode_produk VARCHAR(20) PRIMARY KEY,
#     nama_produk VARCHAR(100),
#     jenis_produk VARCHAR(100),
#     harga_produk INT
# )
# """
# )

# cur.execute(
#     """
# CREATE TABLE struk (
#     no_transaksi VARCHAR(20) PRIMARY KEY,
#     nik VARCHAR(50),
#     kode_produk VARCHAR(100),
#     jumlah_produk INT,
#     total_harga INT
# )
# """
# )


# cur.execute(
#     """
#         ALTER TABLE struk
#         ADD FOREIGN KEY (no_transaksi) REFERENCES transaksi(no_transaksi),
#         ADD FOREIGN KEY (nik) REFERENCES pegawai(nik),
#         ADD FOREIGN KEY (kode_produk) REFERENCES produk(kode_produk)
#     """
# )


while True:
    print("==================== Aplikasi Penjualan ====================")
    print("1. Menu Pegawai")
    print("2. Menu Produk")
    print("3. Menu Transaksi")
    print("4. Menu Struk")
    print("0. Keluar")
    menu1 = input("Pilih menu: ")
    print("")

    if menu1 == "1":
        print("==================== Menu Pegawai ====================")
        print("1. Lihat Pegawai")
        print("2. Tambah Pegawai")
        print("3. Edit Pegawai")
        print("4. Hapus Pegawai")
        print("0. Kembali")
        menu2 = input("Pilih menu: ")
        print("")

        if menu2 == "1":
            cur.execute("SELECT * FROM pegawai")
            data = cur.fetchall()
            for i in data:
                print(i)
            print("")

        elif menu2 == "2":
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            alamat = input("Masukkan Alamat: ")

            cur.execute(
                f"INSERT INTO pegawai (nik, nama_pegawai, alamat_pegawai) VALUES ('{nik}', '{nama}', '{alamat}')"
            )
            conn.commit()
            print("Pegawai berhasil ditambahkan!\n")

        elif menu2 == "3":
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            alamat = input("Masukkan Alamat: ")

            cur.execute(
                f"UPDATE pegawai SET nama_pegawai='{nama}', alamat_pegawai='{alamat}' WHERE nik='{nik}'"
            )
            conn.commit()
            print("Pegawai berhasil diubah!\n")

        elif menu2 == "4":
            nik = input("Masukkan NIK: ")

            cur.execute(f"DELETE FROM pegawai WHERE nik='{nik}'")
            conn.commit()
            print("Pegawai berhasil dihapus!\n")

    elif menu1 == "2":
        print("==================== Menu Produk ====================")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("0. Kembali")
        menu2 = input("Pilih menu: ")
        print("")

        if menu2 == "1":
            cur.execute("SELECT * FROM produk")
            data = cur.fetchall()
            for i in data:
                print(i)
            print("")

        elif menu2 == "2":
            kode = input("Masukkan Kode Produk: ")
            nama = input("Masukkan Nama Produk: ")
            jenis = input("Masukkan Jenis Produk: ")
            harga = input("Masukkan Harga Produk: ")

            cur.execute(
                f"INSERT INTO produk (kode_produk, nama_produk, jenis_produk, harga_produk) VALUES ('{kode}', '{nama}', '{jenis}', '{harga}')"
            )
            conn.commit()
            print("Produk berhasil ditambahkan!\n")

        elif menu2 == "3":
            kode = input("Masukkan Kode Produk: ")
            nama = input("Masukkan Nama Produk: ")
            jenis = input("Masukkan Jenis Produk: ")
            harga = input("Masukkan Harga Produk: ")

            cur.execute(
                f"UPDATE produk SET nama_produk='{nama}', jenis_produk='{jenis}', harga_produk='{harga}' WHERE kode_produk='{kode}'"
            )
            conn.commit()
            print("Produk berhasil diubah!\n")

        elif menu2 == "4":
            kode = input("Masukkan Kode Produk: ")

            cur.execute(f"DELETE FROM produk WHERE kode_produk='{kode}'")
            conn.commit()
            print("Produk berhasil dihapus!\n")

    elif menu1 == "3":
        print("==================== Menu Transaksi ====================")
        print("1. Lihat Transaksi")
        print("2. Tambah Transaksi")
        print("3. Edit Transaksi")
        print("4. Hapus Transaksi")
        print("0. Kembali")
        menu2 = input("Pilih menu: ")
        print("")

        if menu2 == "1":
            cur.execute("SELECT * FROM transaksi")
            data = cur.fetchall()
            for i in data:
                print(i)
            print("")

        elif menu2 == "2":
            no_transaksi = input("Masukkan No Transaksi: ")
            detail_transaksi = input("Masukkan Detail Transaksi: ")

            cur.execute(
                f"INSERT INTO transaksi (no_transaksi, detail_transaksi) VALUES ('{no_transaksi}', '{detail_transaksi}')"
            )
            conn.commit()
            print("Transaksi berhasil ditambahkan!\n")

        elif menu2 == "3":
            no_transaksi = input("Masukkan No Transaksi: ")
            detail_transaksi = input("Masukkan Detail Transaksi: ")

            cur.execute(
                f"UPDATE transaksi SET detail_transaksi='{detail_transaksi}' WHERE no_transaksi='{no_transaksi}'"
            )
            conn.commit()
            print("Transaksi berhasil diubah!\n")

        elif menu2 == "4":
            no_transaksi = input("Masukkan No Transaksi: ")

            cur.execute(f"DELETE FROM transaksi WHERE no_transaksi='{no_transaksi}'")
            conn.commit()
            print("Transaksi berhasil dihapus!\n")

    elif menu1 == "4":
        print("==================== Menu Struk ====================")
        print("1. Lihat Struk")
        print("2. Tambah Struk")
        print("3. Edit Struk")
        print("4. Hapus Struk")
        print("0. Kembali")
        menu2 = input("Pilih menu: ")
        print("")

        if menu2 == "1":
            cur.execute(
                """
                SELECT s.no_transaksi, p.nama_pegawai, pr.nama_produk, s.jumlah_produk, s.total_harga
                FROM struk s
                JOIN pegawai p ON s.nik = p.nik
                JOIN produk pr ON s.kode_produk = pr.kode_produk
            """
            )
            data = cur.fetchall()
            for i in data:
                print(i)
            print("")

        elif menu2 == "2":
            no_transaksi = input("Masukkan No Transaksi: ")
            nik = input("Masukkan NIK Pegawai: ")
            kode_produk = input("Masukkan Kode Produk: ")
            jumlah_produk = int(input("Masukkan Jumlah Produk: "))

            cur.execute(
                f"SELECT harga_produk FROM produk WHERE kode_produk='{kode_produk}'"
            )
            harga_produk = cur.fetchone()[0]
            total_harga = harga_produk * jumlah_produk

            cur.execute(
                f"INSERT INTO struk (no_transaksi, nik, kode_produk, jumlah_produk, total_harga) VALUES ('{no_transaksi}', '{nik}', '{kode_produk}', '{jumlah_produk}', '{total_harga}')"
            )
            conn.commit()
            print("Struk berhasil ditambahkan!\n")

        elif menu2 == "3":
            no_transaksi = input("Masukkan No Transaksi: ")
            nik = input("Masukkan NIK: ")
            kode_produk = input("Masukkan Kode Produk: ")
            jumlah_produk = int(input("Masukkan Jumlah Produk: "))

            cur.execute(
                f"SELECT harga_produk FROM produk WHERE kode_produk='{kode_produk}'"
            )
            harga_produk = cur.fetchone()[0]
            total_harga = harga_produk * jumlah_produk

            cur.execute(
                f"UPDATE struk SET nik='{nik}', kode_produk='{kode_produk}', jumlah_produk='{jumlah_produk}', total_harga='{total_harga}' WHERE no_transaksi='{no_transaksi}'"
            )
            conn.commit()
            print("Struk berhasil diubah!\n")

        elif menu2 == "4":
            no_transaksi = input("Masukkan No Transaksi: ")

            cur.execute(f"DELETE FROM struk WHERE no_transaksi='{no_transaksi}'")
            conn.commit()
            print("Struk berhasil dihapus!\n")

    elif menu1 == "0":
        break
