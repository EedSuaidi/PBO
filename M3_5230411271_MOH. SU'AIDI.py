class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def display(self):
        print(f"{self.nama}     ->     Rp. {self.harga}")


list_makanan = []
list_minuman = []

makanan = Menu("Mie Goreng", 7000)
list_makanan.append(makanan)
makanan = Menu("Mie Rebus", 7000)
list_makanan.append(makanan)
makanan = Menu("Nasi Putih", 3000)
list_makanan.append(makanan)
makanan = Menu("Nasi Goreng", 10000)
list_makanan.append(makanan)
makanan = Menu("Nasi Kebuli", 15000)
list_makanan.append(makanan)

minuman = Menu("Es Teh", 3000)
list_minuman.append(minuman)
minuman = Menu("Teh Anget", 2000)
list_minuman.append(minuman)
minuman = Menu("Air Putih", 1000)
list_minuman.append(minuman)
minuman = Menu("Es Chocolatos", 5000)
list_minuman.append(minuman)
minuman = Menu("Es Beng-Beng", 5000)
list_minuman.append(minuman)



while True:
    print("========== Program Menu ==========")
    print("0. Exit")
    print("1. Daftar Menu Makanan")
    print("2. Daftar Menu Minuman")
    print("3. Tambah Menu")
    input1 = input("Pilih Menu [0-3] : ")
    print("")

    if input1 == "0":
        break

    elif input1 == "1":
        print("===== Daftar Menu Makanan =====")
        for i in list_makanan:
            i.display()
        print("")

    elif input1 == "2":
        print("===== Daftar Menu Minuman =====")
        for i in list_minuman:
            i.display()
        print("")

    elif input1 == "3":
        print("")
        print("===== Tambah Menu =====")
        print("0. Kembali")
        print("1. Tambah Menu Makanan")
        print("2. Tambah Menu Minuman")
        input2 = input("Pilih Menu [0-3] : ")
        print("")

        if input2 == "0":
            print("")
        elif input2 == "1":
            try:
                nama = input("Masukkan Nama Makanan : ")
                harga = int(input("Masukkan Harga Makanan : "))
            except ValueError:
                print("Makanan tidak valid!")
                print("")
                continue
            menu = Menu(nama, harga)
            list_makanan.append(menu)
            print("Menu Berhasil ditambahkan!\n")
        elif input2 == "2":
            try:
                nama = input("Masukkan Nama Minuman : ")
                harga = int(input("Masukkan Harga Minuman : "))
            except ValueError:
                print("Minuman tidak valid!")
                print("")
                continue
            menu = Menu(nama, harga)
            list_minuman.append(menu)
            print("Menu Berhasil ditambahkan!\n")
        else:
            print("Menu tidak valid!")

    else:
        print("Menu tidak valid!")
    
    
