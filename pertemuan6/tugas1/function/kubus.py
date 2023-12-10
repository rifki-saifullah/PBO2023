import tkinter as tk
from tkinter import ttk

class kubus:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Kubus")
        self.component()

    def hitung_luas_dan_volume(self):
        sisi = float(self.entry_sisi.get())

        luas = 6 * sisi ** 2
        volume = sisi ** 3

        self.entry_luas.delete(0, tk.END)
        self.entry_luas.insert(tk.END, luas)

        self.entry_volume.delete(0, tk.END)
        self.entry_volume.insert(tk.END, volume)

    def hitung(self):
        self.hitung_luas_dan_volume()

    def component(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Sisi
        label_sisi = ttk.Label(frame, text="Sisi")
        label_sisi.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_sisi = ttk.Entry(frame)
        self.entry_sisi.grid(row=0, column=1)

        # Button
        hitung = ttk.Button(frame, text="Hitung", command=self.hitung)
        hitung.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Output Luas
        label_luas = ttk.Label(frame, text="Luas")
        label_luas.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_luas = ttk.Entry(frame)
        self.entry_luas.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Output volume
        label_volume = ttk.Label(frame, text="Volume")
        label_volume.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_volume = ttk.Entry(frame)
        self.entry_volume.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = kubus(root)
    root.mainloop()
