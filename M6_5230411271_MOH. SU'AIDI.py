class Order:
    def __init__(self, id, name, details):
        self._id = id
        self.name = name
        self.details = details

    def setOrder(self):
        print("Berhasil memesan!")
    
    def displayOrder(self):
        print(f"ID Order: {self._id}")
        print(f"Name: {self.name}")
        print(f"Details: \n{self.details}")


class Delivery(Order):
    def __init__(self, id, name, details, information, date, address):
        super().__init__(id, name, details)
        self.information = information
        self.date = date
        self.address = address

    def processDelivery(self):
        print("Pesanan telah dikirim!")

    def displayDelivery(self):
        print(f"ID Order: {self._id}")
        print(f"Name: {self.name}")
        print(f"Details: \n{self.details}")
        print(f"Information: {self.information}")
        print(f"Date: {self.date}")
        print(f"Address: {self.address}")


order1 = Order(1, "Solaria", "1 Nasi Goreng\n1 Es Jeruk")
order2 = Order(2, "Gacoan", "2 Mie Gacoan\n2 Es Teh")
order3 = Order(3, "Mbah Rejo", "5 Steak Ayam\n2 Es Teh\n3 Air Putih")
order4 = Order(4, "Hara Chicken", "2 Ayam Geprek\n2 Es Milo")
order5 = Order(5, "Pizza Hut", "1 Splitza (Large)\n4 Coca-cola")

delivery1 = Delivery(order1._id, order1.name, order1.details, "Pesanan akan tiba dalam 5 menit", "26 Oktober 2024", "Jombor")
delivery2 = Delivery(order2._id, order2.name, order2.details, "Pesanan akan tiba dalam 30 menit", "29 Oktober 2024", "Mlati")
delivery3 = Delivery(order3._id, order3.name, order3.details, "Pesanan akan tiba dalam 10 menit", "31 Oktober 2024", "Tempel")
delivery4 = Delivery(order4._id, order4.name, order4.details, "Pesanan akan tiba dalam 15 menit", "3 November 2024", "Turi")
delivery5 = Delivery(order5._id, order5.name, order5.details, "Pesanan akan tiba dalam 30 menit", "7 November 2024", "Pakem")


list_order = [order1, order2, order3, order4, order5]
list_delivery = [delivery1, delivery2, delivery3, delivery4, delivery5]


while True:
    print("=============== UTY Food ===============")
    print("0. Exit")
    print("1. Kelola Order")
    print("2. Kelola Delivery")
    menu = input("Pilih Menu [0-2] : ")
    print("")

    if menu == "0":
        break

    elif menu == "1":
        print("=============== Kelola Order ===============")
        print("0. Kembali")
        print("1. Tampilkan Semua Order")
        print("2. Cari Order")
        submenu = input("Pilih Menu [0-2] : ")
        print("")

        if submenu == "0":
            print("")
        elif submenu == "1":
            print("=============== Daftar Order ===============")
            print("ID         Name\n")
            for i in list_order:
                print(f"{i._id}          {i.name}")
            print("")
        elif submenu == "2":
            id = int(input("Masukkan ID Order Yang Ingin Dicari : "))
            print("")
            for i in list_order:
                if i._id == id:
                    print("========== Detail Order ==========\n")
                    i.displayOrder()
                    print("")
                    break
            else:
                print("Order Tidak Ditemukan!\n")

    elif menu == "2":
        print("=============== Kelola Delivery ===============")
        print("0. Kembali")
        print("1. Tampilkan Semua Delivery")
        print("2. Cari Delivery")
        submenu = input("Pilih Menu [0-2] : ")
        print("")

        if submenu == "0":
            print("")
        elif submenu == "1":
            print("=============== Daftar Delivery ===============")
            print("ID         Name          Address\n")
            for i in list_delivery:
                print(f"{i._id}          {i.name}          {i.address}")
            print("")
        elif submenu == "2":
            id = int(input("Masukkan ID Delivery Yang Ingin Dicari : "))
            print("")
            for i in list_delivery:
                if i._id == id:
                    print("========== Daftar Delivery ==========\n")
                    i.displayDelivery()
                    print("")
                    break
            else:
                print("Delivery Tidak Ditemukan!\n")


