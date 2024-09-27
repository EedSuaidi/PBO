def segitiga(a, t):
    return (a * t) / 2

def jajar_genjang(a, t):
    return a * t

def tabung(r, t):
    if r % 7 == 0:
        pi = 22/7
    else:
        pi = 3.14
    return pi * r * r * t

def bola(r):
    if r % 7 == 0:
        pi = 22/7
    else:
        pi = 3.14
    return (4/3) * pi * r * r * r



while True:
    print("========== Program Mencari Luas Bangun Datar & Volume Bangun Ruang ==========")
    print("===== Menu =====")
    print("1. Segitiga")
    print("2. Jajar Genjang")
    print("3. Tabung")
    print("4. Bola")

    menu = input("Pilih Menu : ")
    print("")

    if menu == "1":
        a = int(input("Masukkan Alas : "))
        t = int(input("Masukkan Tinggi : "))
        print("Luas Segitiga : ", segitiga(a, t), "\n")
    elif menu == "2":
        a = int(input("Masukkan Alas : "))
        t = int(input("Masukkan Tinggi : "))
        print("Luas Jajar Genjang : ", jajar_genjang(a, t), "\n")
    elif menu == "3":
        r = int(input("Masukkan Jari-Jari : "))
        t = int(input("Masukkan Tinggi : "))
        print("Volume Tabung : ", tabung(r, t), "\n")
    elif menu == "4":
        r = int(input("Masukkan Jari-Jari : "))
        print("Volume Bola : ", bola(r), "\n")
