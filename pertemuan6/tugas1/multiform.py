import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("700x300")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_tab("Balok", self.calculate_balok)
        self.create_tab("Bola", self.calculate_bola)
        self.create_tab("Kerucut", self.calculate_kerucut)
        self.create_tab("Kubus", self.calculate_kubus)
        self.create_tab("Limas Segiempat", self.calculate_limas_segiempat)
        self.create_tab("Limas Segitiga", self.calculate_limas_segitiga)
        self.create_tab("Prisma Segitiga", self.calculate_prisma_segitiga)
        self.create_tab("Tabung", self.calculate_tabung)

    def create_tab(self, title, callback):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=title)

        callback(tab)

    def calculate_balok(self, tab):
        label_panjang = tk.Label(tab, text="Panjang:")
        entry_panjang = tk.Entry(tab)
        label_panjang.grid(row=0, column=0, padx=10, pady=10)
        entry_panjang.grid(row=0, column=1, padx=10, pady=10)

        label_lebar = tk.Label(tab, text="Lebar:")
        entry_lebar = tk.Entry(tab)
        label_lebar.grid(row=1, column=0, padx=10, pady=10)
        entry_lebar.grid(row=1, column=1, padx=10, pady=10)

        label_tinggi = tk.Label(tab, text="Tinggi:")
        entry_tinggi = tk.Entry(tab)
        label_tinggi.grid(row=2, column=0, padx=10, pady=10)
        entry_tinggi.grid(row=2, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=3, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_balok(entry_panjang.get(), entry_lebar.get(), entry_tinggi.get(), result_label))
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_result_balok(self, panjang, lebar, tinggi, result_label):
        try:
            panjang = float(panjang)
            lebar = float(lebar)
            tinggi = float(tinggi)

            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            volume = panjang * lebar * tinggi

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_bola(self, tab):
        label_jari = tk.Label(tab, text="Jari-jari:")
        entry_jari = tk.Entry(tab)
        label_jari.grid(row=0, column=0, padx=10, pady=10)
        entry_jari.grid(row=0, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=1, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_bola(entry_jari.get(), result_label))
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_result_bola(self, jari, result_label):
        try:
            jari = float(jari)

            luas = 4 * 3.14 * (jari ** 2)
            volume = (4 / 3) * 3.14 * (jari ** 3)

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_kerucut(self, tab):
        label_jari_kerucut = tk.Label(tab, text="Jari-jari:")
        entry_jari_kerucut = tk.Entry(tab)
        label_jari_kerucut.grid(row=0, column=0, padx=10, pady=10)
        entry_jari_kerucut.grid(row=0, column=1, padx=10, pady=10)

        label_tinggi_kerucut = tk.Label(tab, text="Tinggi:")
        entry_tinggi_kerucut = tk.Entry(tab)
        label_tinggi_kerucut.grid(row=1, column=0, padx=10, pady=10)
        entry_tinggi_kerucut.grid(row=1, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=2, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_kerucut(entry_jari_kerucut.get(), entry_tinggi_kerucut.get(), result_label))
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_result_kerucut(self, jari, tinggi, result_label):
        try:
            jari = float(jari)
            tinggi = float(tinggi)

            luas = math.pi * jari * (jari + math.sqrt(jari**2 + tinggi**2))
            volume = (1 / 3) * math.pi * (jari**2) * tinggi

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_kubus(self, tab):
        label_sisi_kubus = tk.Label(tab, text="Sisi:")
        entry_sisi_kubus = tk.Entry(tab)
        label_sisi_kubus.grid(row=0, column=0, padx=10, pady=10)
        entry_sisi_kubus.grid(row=0, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=1, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_kubus(entry_sisi_kubus.get(), result_label))
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_result_kubus(self, sisi, result_label):
        try:
            sisi = float(sisi)

            luas = 6 * (sisi**2)
            volume = sisi**3

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_limas_segiempat(self, tab):
        label_sisi_limas_segiempat = tk.Label(tab, text="Sisi Alas:")
        entry_sisi_limas_segiempat = tk.Entry(tab)
        label_sisi_limas_segiempat.grid(row=0, column=0, padx=10, pady=10)
        entry_sisi_limas_segiempat.grid(row=0, column=1, padx=10, pady=10)

        label_tinggi_limas_segiempat = tk.Label(tab, text="Tinggi:")
        entry_tinggi_limas_segiempat = tk.Entry(tab)
        label_tinggi_limas_segiempat.grid(row=1, column=0, padx=10, pady=10)
        entry_tinggi_limas_segiempat.grid(row=1, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=2, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_limas_segiempat(entry_sisi_limas_segiempat.get(), entry_tinggi_limas_segiempat.get(), result_label))
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_result_limas_segiempat(self, sisi_alas, tinggi, result_label):
        try:
            sisi_alas = float(sisi_alas)
            tinggi = float(tinggi)

            luas = sisi_alas**2 + 4 * (sisi_alas * tinggi) / 2
            volume = (1 / 3) * (sisi_alas**2) * tinggi

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_limas_segitiga(self, tab):
        label_sisi_limas_segitiga = tk.Label(tab, text="Sisi Alas:")
        entry_sisi_limas_segitiga = tk.Entry(tab)
        label_sisi_limas_segitiga.grid(row=0, column=0, padx=10, pady=10)
        entry_sisi_limas_segitiga.grid(row=0, column=1, padx=10, pady=10)

        label_tinggi_limas_segitiga = tk.Label(tab, text="Tinggi:")
        entry_tinggi_limas_segitiga = tk.Entry(tab)
        label_tinggi_limas_segitiga.grid(row=1, column=0, padx=10, pady=10)
        entry_tinggi_limas_segitiga.grid(row=1, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=2, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_limas_segitiga(entry_sisi_limas_segitiga.get(), entry_tinggi_limas_segitiga.get(), result_label))
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_result_limas_segitiga(self, sisi_alas, tinggi, result_label):
        try:
            sisi_alas = float(sisi_alas)
            tinggi = float(tinggi)

            luas = sisi_alas * (sisi_alas + math.sqrt(3) * tinggi**2)
            volume = (1 / 3) * (sisi_alas**2) * tinggi

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_prisma_segitiga(self, tab):
        label_sisi_alas_prisma = tk.Label(tab, text="Sisi Alas:")
        entry_sisi_alas_prisma = tk.Entry(tab)
        label_sisi_alas_prisma.grid(row=0, column=0, padx=10, pady=10)
        entry_sisi_alas_prisma.grid(row=0, column=1, padx=10, pady=10)

        label_tinggi_prisma = tk.Label(tab, text="Tinggi:")
        entry_tinggi_prisma = tk.Entry(tab)
        label_tinggi_prisma.grid(row=1, column=0, padx=10, pady=10)
        entry_tinggi_prisma.grid(row=1, column=1, padx=10, pady=10)

        label_tinggi_segitiga_prisma = tk.Label(tab, text="Tinggi Segitiga Alas:")
        entry_tinggi_segitiga_prisma = tk.Entry(tab)
        label_tinggi_segitiga_prisma.grid(row=2, column=0, padx=10, pady=10)
        entry_tinggi_segitiga_prisma.grid(row=2, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=3, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_prisma_segitiga(entry_sisi_alas_prisma.get(), entry_tinggi_prisma.get(), entry_tinggi_segitiga_prisma.get(), result_label))
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_result_prisma_segitiga(self, sisi_alas, tinggi_prisma, tinggi_segitiga, result_label):
        try:
            sisi_alas = float(sisi_alas)
            tinggi_prisma = float(tinggi_prisma)
            tinggi_segitiga = float(tinggi_segitiga)

            luas = sisi_alas * (tinggi_prisma + tinggi_segitiga)
            volume = (1 / 2) * sisi_alas * tinggi_prisma * tinggi_segitiga

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

    def calculate_tabung(self, tab):
        label_jari_tabung = tk.Label(tab, text="Jari-jari:")
        entry_jari_tabung = tk.Entry(tab)
        label_jari_tabung.grid(row=0, column=0, padx=10, pady=10)
        entry_jari_tabung.grid(row=0, column=1, padx=10, pady=10)

        label_tinggi_tabung = tk.Label(tab, text="Tinggi:")
        entry_tinggi_tabung = tk.Entry(tab)
        label_tinggi_tabung.grid(row=1, column=0, padx=10, pady=10)
        entry_tinggi_tabung.grid(row=1, column=1, padx=10, pady=10)

        result_label = tk.Label(tab, text="")
        result_label.grid(row=2, column=0, columnspan=2, pady=10)

        calculate_button = tk.Button(tab, text="Hitung", command=lambda: self.calculate_result_tabung(entry_jari_tabung.get(), entry_tinggi_tabung.get(), result_label))
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_result_tabung(self, jari, tinggi, result_label):
        try:
            jari = float(jari)
            tinggi = float(tinggi)

            luas = 2 * math.pi * jari * (jari + tinggi)
            volume = math.pi * (jari**2) * tinggi

            result_text = f"Luas: {luas:.2f}, Volume: {volume:.2f}"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()