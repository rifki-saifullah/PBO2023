import tkinter as tk 
from tkinter import ttk
import math

class prisma_segitiga:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Prisma Segitiga")
        self.component()

    def hitung_luas(self):
        alas = float(self.entry_alas.get())
        tinggi_alas = float(self.entry_tinggi_alas.get())
        tinggi_prisma = float(self.entry_tinggi_prisma.get())

        luas = alas * tinggi_alas + 3 * (alas * tinggi_prisma)
        
        self.entry_luas.delete(0, tk.END)
        self.entry_luas.insert(tk.END, luas)

    def hitung_volume(self):
        alas = float(self.entry_alas.get())
        tinggi_alas = float(self.entry_tinggi_alas.get())
        tinggi_prisma = float(self.entry_tinggi_prisma.get())

        volume = (1/2) * alas * tinggi_alas * tinggi_prisma
        
        self.entry_volume.delete(0, tk.END)
        self.entry_volume.insert(tk.END, volume)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

    def component(self):
        frame = ttk.Frame(self.root) 
        frame.pack(padx=20, pady=20)

        # Alas Segitiga
        label_alas = ttk.Label(frame, text="Alas Segitiga") 
        label_alas.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_alas = ttk.Entry(frame)
        self.entry_alas.grid(row=0, column=1)

        # Tinggi Alas Segitiga
        label_tinggi_alas = ttk.Label(frame, text="Tinggi Alas Segitiga")
        label_tinggi_alas.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_tinggi_alas = ttk.Entry(frame)
        self.entry_tinggi_alas.grid(row=1, column=1)

        # Tinggi Prisma
        label_tinggi_prisma = ttk.Label(frame, text="Tinggi Prisma")
        label_tinggi_prisma.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_tinggi_prisma = ttk.Entry(frame)
        self.entry_tinggi_prisma.grid(row=2, column=1)

        # Button
        hitung = ttk.Button(frame, text="Hitung", command=self.hitung)
        hitung.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Luas
        label_luas = ttk.Label(frame, text="Luas")
        label_luas.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_luas = ttk.Entry(frame)
        self.entry_luas.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Volume
        label_volume = ttk.Label(frame, text="Volume")
        label_volume.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_volume = ttk.Entry(frame)
        self.entry_volume.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = prisma_segitiga(root)
    root.mainloop()
