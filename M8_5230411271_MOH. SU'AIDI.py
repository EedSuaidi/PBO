import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


class MahasiswaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pendataan Mahasiswa")
        self.root.geometry("600x600")

        self.widget_create()

    def widget_create(self):
        # Title Label
        title_lable = tk.Label(
            text="Aplikasi Pendataan Mahasiswa", font=("Times New Roman", 20, "bold")
        )
        title_lable.pack(pady=10)

        # Nama
        nama_label = tk.Label(text="Nama : ")
        nama_label.pack()
        self.nama_entry = tk.Entry(self.root, width=30)
        self.nama_entry.pack(pady=5)

        # NPM
        npm_label = tk.Label(text="NPM : ")
        npm_label.pack()
        self.npm_entry = tk.Entry(self.root, width=30)
        self.npm_entry.pack(pady=5)

        # Program Studi
        prodi_label = tk.Label(text="Program Studi : ")
        prodi_label.pack()
        prodi_option = [
            "Informatika",
            "Sistem Informasi",
            "Teknik Komputer",
            "Sains Data",
            "Informatika Medis",
        ]
        self.prodi_var = ""
        self.prodi_entry = ttk.Combobox(
            self.root, values=prodi_option, textvariable=self.prodi_var, width=30
        )
        self.prodi_entry.pack(pady=5)

        # IPK
        ipk_label = tk.Label(text="IPK : ")
        ipk_label.pack()
        self.ipk_entry = tk.Entry(self.root, width=30)
        self.ipk_entry.pack(pady=5)

        # Tombol Tambah
        add_button = tk.Button(self.root, text="Tambah Data", command=self.add_data)
        add_button.pack(pady=5)

        # Daftar Mahasiswa
        daftar_label = tk.Label(text="Daftar Mahasiswa : ")
        daftar_label.pack()
        self.daftar_table = ttk.Treeview(
            self.root,
            columns=("Nama", "NPM", "Program Studi", "IPK", "Kategori"),
            show="headings",
        )
        self.daftar_table.heading("Nama", text="Nama")
        self.daftar_table.heading("NPM", text="NPM")
        self.daftar_table.heading("Program Studi", text="Program Studi")
        self.daftar_table.heading("IPK", text="IPK")
        self.daftar_table.heading("Kategori", text="Kategori")
        self.daftar_table.pack(pady=5)

        # Tombol Ekspor Data
        export_button = tk.Button(
            self.root, text="Ekspor Data", command=self.export_to_excel
        )
        export_button.pack(pady=10)

        # Tombol Hapus
        hapus_button = tk.Button(self.root, text="Hapus Data", command=self.hapus_data)
        hapus_button.pack(pady=10)

    def add_data(self):
        nama = self.nama_entry.get()
        npm = self.npm_entry.get()
        prodi = self.prodi_entry.get()

        if self.ipk_entry.get().isdigit() or self.ipk_entry.get().count(".") == 1:
            ipk = float(self.ipk_entry.get())
        else:
            messagebox.showerror("Error", "IPK Harus Berupa Angka!")
            return

        if ipk > 4:
            messagebox.showerror("Error", "IPK Tidak Valid!")
            return
        elif ipk == 4:
            kategori = "Jenius"
        elif ipk >= 3:
            kategori = "Pintar"
        elif ipk >= 2:
            kategori = "Cukup"
        elif ipk >= 1:
            kategori = "Kurang"
        else:
            kategori = "Bodoh"

        if not (nama and prodi and npm and ipk):
            messagebox.showerror("Error", "Semua Kolom Harus Diisi!")
        elif not npm.isdigit():
            messagebox.showerror("Error", "NPM Harus Berupa Angka!")
        else:
            self.daftar_table.insert(
                "", "end", values=(nama, npm, prodi, ipk, kategori)
            )

    def hapus_data(self):
        confirm = messagebox.askquestion(
            "Konfirmasi", "Apakah anda yakin ingin menghapus semua data?"
        )
        if confirm == "yes":
            for item in self.daftar_table.get_children():
                self.daftar_table.delete(item)

    def export_to_excel(self):
        data = []
        for row in self.daftar_table.get_children():
            data.append(self.daftar_table.item(row)["values"])

        df = pd.DataFrame(
            data, columns=["Nama", "NPM", "Program Studi", "IPK", "Kategori"]
        )
        df.to_excel("data_mahasiswa.xlsx", index=False)
        messagebox.showinfo("Sukses", "Data berhasil diexport ke data_mahasiswa.xlsx")


if __name__ == "__main__":
    root = tk.Tk()
    app = MahasiswaApp(root)
    root.mainloop()
