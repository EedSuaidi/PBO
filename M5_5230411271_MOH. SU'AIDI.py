class Musik:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre


class Indonesian(Musik):
    def __init__(self, judul, penyanyi, genre="Indonesian"):
        super().__init__(judul, penyanyi, genre)

    def display(self):
        print(f"{self.judul}     |     {self.penyanyi}     |     {self.genre}")
    
    def add(self, judul, penyanyi, genre="Indonesian"):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def delete(self, judul):
        if judul in self.judul:
            self.judul.remove(judul)
        else:
            print("Judul tidak ditemukan")


class Javanese(Musik):
    def __init__(self, judul, penyanyi, genre="Javanese"):
        super().__init__(judul, penyanyi, genre)

    def display(self):
        print(f"{self.judul}     |     {self.penyanyi}     |     {self.genre}")
    
    def add(self, judul, penyanyi, genre="Javanese"):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre


class Korean(Musik):
    def __init__(self, judul, penyanyi, genre="Korean"):
        super().__init__(judul, penyanyi, genre)

    def display(self):
        print(f"{self.judul}     |     {self.penyanyi}     |     {self.genre}")
    
    def add(self, judul, penyanyi, genre="Korean"):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre



musikIndo1 = Indonesian("Laskar Pelangi", "Ari Lasso")
musikIndo2 = Indonesian("Satu Bulan", "Bernadya")
musikIndo3 = Indonesian("Sial", "Mahalini")
musikIndo4 = Indonesian("Tiba-Tiba Cinta Datang", "Maudy Ayunda")
musikIndo5 = Indonesian("Ganyang Fufufafa", "Rizieq")
musikJawa1 = Javanese("Sigar", "Denny Caknan")
musikJawa2 = Javanese("Sanes", "Guyon Waton")
musikJawa3 = Javanese("Kisinan", "Masdddho")
musikJawa4 = Javanese("LDR", "Denny Caknan")
musikJawa5 = Javanese("Mendung Tanpo Udan", "Ndarboy Genk")
musikKorea1 = Korean("Lovesick Girls", "Blackpink")
musikKorea2 = Korean("Likey", "Twice")
musikKorea3 = Korean("Solo", "Jennie")
musikKorea4 = Korean("APT.", "Rose")
musikKorea5 = Korean("Hard to Love", "Blackpink")

list_musik = [musikIndo1, musikIndo2, musikIndo3, musikIndo4, musikIndo5, musikJawa1, musikJawa2, musikJawa3, musikJawa4, musikJawa5, musikKorea1, musikKorea2, musikKorea3, musikKorea4, musikKorea5]
list_musik_indonesia = [musikIndo1, musikIndo2, musikIndo3, musikIndo4, musikIndo5]
list_musik_jawa = [musikJawa1, musikJawa2, musikJawa3, musikJawa4, musikJawa5]
list_musik_korea = [musikKorea1, musikKorea2, musikKorea3, musikKorea4, musikKorea5]


while True:
    print("=============== Music App ===============")
    print("0. Exit")
    print("1. Indonesian Song")
    print("2. Javanese Song")
    print("3. Korean Song")
    print("4. Tampilkan Semua Musik")
    print("5. Cari Musik")
    input1 = input("Pilih Menu [0-5] : ")
    print("")

    if input1 == "1":
        print("=============== Indonesian Song ===============")
        print("0. Kembali")
        print("1. Tampilkan Musik")
        print("2. Tambah Musik")
        print("3. Hapus Musik")
        input2 = input("Pilih Menu [0-3] : ")
        print("")

        if input2 == "1":
            if len(list_musik_indonesia) == 0:
                print("Tidak ada musik yang ditambahkan!")
            else:
                print("=============== Daftar Musik Indonesia ===============")
                print("Judul     |     Penyanyi     |     Genre\n")
                sorted_musik = sorted(list_musik_indonesia, key=lambda musik: musik.judul)
                for i in sorted_musik:
                    i.display()
                print("")

        elif input2 == "2":
            judul = input("Masukkan judul: ")
            penyanyi = input("Masukkan penyanyi: ")
            musikIndo = Indonesian(judul, penyanyi)
            list_musik.append(musikIndo)
            list_musik_indonesia.append(musikIndo)
            print("")
        
        elif input2 == "3":
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            
            for i in list_musik_indonesia:
                if i.judul == judul:
                    for j in list_musik:
                        if j.judul == judul:
                            list_musik.remove(j)
                    list_musik_indonesia.remove(i)
                    print("Musik berhasil dihapus!\n")
                    break
            else:
                print("Musik tidak ditemukan!\n")

        elif input2 == "0":
            print("")


    elif input1 == "2":
        print("=============== Javanese Song ===============")
        print("0. Exit")
        print("1. Tampilkan Musik")
        print("2. Tambah Musik")
        print("3. Hapus Musik")
        input2 = input("Pilih Menu [0-3] : ")
        print("")

        if input2 == "1":
            if len(list_musik_jawa) == 0:
                print("Tidak ada musik yang ditambahkan!")
            else:
                print("=============== Daftar Musik Jawa ===============")
                print("Judul     |     Penyanyi     |     Genre\n")
                sorted_musik = sorted(list_musik_jawa, key=lambda musik: musik.judul)
                for i in sorted_musik:
                    i.display()
                print("")

        elif input2 == "2":
            judul = input("Masukkan judul: ")
            penyanyi = input("Masukkan penyanyi: ")
            musikJawa = Javanese(judul, penyanyi)
            list_musik.append(musikJawa)
            list_musik_jawa.append(musikJawa)
            print("")
        
        elif input2 == "3":
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            for i in list_musik_jawa:
                if i.judul == judul:
                    for j in list_musik:
                        if j.judul == judul:
                            list_musik.remove(j)
                    list_musik_jawa.remove(i)
                    print("Musik berhasil dihapus!\n")   
                    break  
            else:
                print("Musik tidak ditemukan!")
        
        elif input2 == "0":
            print("")


    elif input1 == "3":
        print("=============== Javanese Song ===============")
        print("0. Exit")
        print("1. Tampilkan Musik")
        print("2. Tambah Musik")
        print("3. Hapus Musik")
        input2 = input("Pilih Menu [0-3] : ")
        print("")

        if input2 == "1":
            if len(list_musik_korea) == 0:
                print("Tidak ada musik yang ditambahkan!")
            else:
                print("=============== Daftar Musik Korea ===============")
                print("Judul     |     Penyanyi     |     Genre\n")
                sorted_musik = sorted(list_musik_korea, key=lambda musik: musik.judul)
                for i in sorted_musik:
                    i.display()
                print("")

        elif input2 == "2":
            judul = input("Masukkan judul: ")
            penyanyi = input("Masukkan penyanyi: ")
            musikKorea = Korean(judul, penyanyi)
            list_musik.append(musikKorea)
            list_musik_korea.append(musikKorea)
            print("")
        
        elif input2 == "3":
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            for i in list_musik_korea:
                if i.judul == judul:
                    for j in list_musik:
                        if j.judul == judul:
                            list_musik.remove(j)
                    list_musik_korea.remove(i)
                    print("Musik berhasil dihapus!\n")
                    break
            else:
                print("Musik tidak ditemukan!\n")
        
        elif input2 == "0":
            print("")

        
    elif input1 == "4":
        print("=============== Daftar Musik ===============")
        print("Judul     |     Penyanyi     |     Genre\n")
        sorted_musik = sorted(list_musik, key=lambda musik: musik.judul)

        for i in sorted_musik:
            i.display()
        print("")


    elif input1 == "5":
        print("=============== Cari Musik ===============")
        penyanyi = input("Masukkan penyanyi yang ingin dicari: ")
        print("")
        for i in list_musik:
            if i.penyanyi == penyanyi:
                i.display()
                print("")
        print("---------------------------------------------\n")

    
    elif input1 == "0":
        break
            