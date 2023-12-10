import tkinter as tk
from tkinter import ttk
import math

class kerucut:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Kerucut")
        self.component()

    def hitung_luas_permukaan(self):
        jari_jari = float(self.entry_jari_jari.get())
        tinggi = float(self.entry_tinggi.get())

        garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)
        luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)

        self.entry_luas.delete(0, tk.END)
        self.entry_luas.insert(tk.END, luas_permukaan)

    def hitung_volume(self):
        jari_jari = float(self.entry_jari_jari.get())
        tinggi = float(self.entry_tinggi.get())

        volume = (1/3) * math.pi * jari_jari**2 * tinggi

        self.entry_volume.delete(0, tk.END)
        self.entry_volume.insert(tk.END, volume)

    def hitung(self):
        self.hitung_luas_permukaan()
        self.hitung_volume()

    def component(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Jari-jari
        label_jari_jari = ttk.Label(frame, text="Jari-jari")
        label_jari_jari.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_jari_jari = ttk.Entry(frame)
        self.entry_jari_jari.grid(row=0, column=1)

        # Tinggi
        label_tinggi = ttk.Label(frame, text="Tinggi")
        label_tinggi.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_tinggi = ttk.Entry(frame)
        self.entry_tinggi.grid(row=1, column=1)

        # Button
        hitung = ttk.Button(frame, text="Hitung", command=self.hitung)
        hitung.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Luas Permukaan
        label_luas = ttk.Label(frame, text="Luas Permukaan")
        label_luas.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_luas = ttk.Entry(frame)
        self.entry_luas.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Volume
        label_volume = ttk.Label(frame, text="Volume")
        label_volume.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_volume = ttk.Entry(frame)
        self.entry_volume.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = kerucut(root)
    root.mainloop()
