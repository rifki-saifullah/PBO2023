import tkinter as tk 
from tkinter import ttk

class balok:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Balok")
        self.component()

    def hitung_luas(self):
        panjang = float(self.entry_panjang.get())
        lebar = float(self.entry_lebar.get())
        tinggi = float(self.entry_tinggi.get())

        value = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

        self.entry_luas.delete(0, tk.END)
        self.entry_luas.insert(tk.END, value)

    def hitung_volume(self):
        panjang = float(self.entry_panjang.get())
        lebar = float(self.entry_lebar.get())
        tinggi = float(self.entry_tinggi.get())

        value = panjang * lebar * tinggi

        self.entry_volume.delete(0,tk.END)
        self.entry_volume.insert(tk.END,value)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

    def component(self):
        frame = ttk.Frame(self.root) 
        frame.pack(padx=20, pady=20)

        # Panjang
        label_panjang = ttk.Label(frame, text="Panjang") 
        label_panjang.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_panjang = ttk.Entry(frame)
        self.entry_panjang.grid(row=0, column=1)

        # Lebar
        label_lebar = ttk.Label(frame, text="Lebar")
        label_lebar.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_lebar = ttk.Entry(frame)
        self.entry_lebar.grid(row=1, column=1)

        # Tinggi
        label_tinggi = ttk.Label(frame, text="Tinggi")
        label_tinggi.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_tinggi = ttk.Entry(frame)
        self.entry_tinggi.grid(row=2, column=1)

        # Button
        hitung = ttk.Button(frame, text="Hitung", command=self.hitung)
        hitung.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Luas
        label_luas = ttk.Label(frame, text="Luas")
        label_luas.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_luas = ttk.Entry(frame)
        self.entry_luas.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        # Output volume
        label_volume = ttk.Label (frame, text="volume")
        label_volume.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_volume = ttk.Entry (frame)
        self.entry_volume.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = balok(root)
    root.mainloop()