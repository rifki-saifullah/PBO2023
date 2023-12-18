import tkinter as tk
from tkinter import ttk

class Rumus:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Suhu")
        self.component()

    # Celsius
    def celcius_to_fahrenheit(self):
        celcius = float(self.entry_input.get())
        value = (9 / 5 * celcius) + 32
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def celcius_to_reamur(self):
        celcius = float(self.entry_input.get())
        value = 4 / 5 * celcius
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def celcius_to_kelvin(self):
        celcius = float(self.entry_input.get())
        value = celcius + 273
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    # Fahrenheit
    def fahrenheit_to_celcius(self):
        fahrenheit = float(self.entry_input.get())
        value = 5 / 9 * (fahrenheit - 32)
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def fahrenheit_to_reamur(self):
        fahrenheit = float(self.entry_input.get())
        value = 4 / 9 * (fahrenheit - 32)
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def fahrenheit_to_kelvin(self):
        fahrenheit = float(self.entry_input.get())
        value = 5 / 9 * (fahrenheit - 32) + 273
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def hitung(self):
        if self.combobox_from.get() == "Celcius":
            if self.combobox_to.get() == "Fahrenheit":
                self.celcius_to_fahrenheit()
            elif self.combobox_to.get() == "Reamur":
                self.celcius_to_reamur()
            elif self.combobox_to.get() == "Kelvin":
                self.celcius_to_kelvin()
        elif self.combobox_from.get() == "Fahrenheit":
            if self.combobox_to.get() == "Celcius":
                self.fahrenheit_to_celcius()
            elif self.combobox_to.get() == "Reamur":
                self.fahrenheit_to_reamur()
            elif self.combobox_to.get() == "Kelvin":
                self.fahrenheit_to_kelvin()

    def component(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Input
        label_input = ttk.Label(frame, text="Masukkan Nilai : ")
        label_input.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_input = ttk.Entry(frame)
        self.entry_input.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Combobox From
        label_from = ttk.Label(frame, text="From")
        label_from.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.combobox_from = ttk.Combobox(frame, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
        self.combobox_from.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Combobox To
        label_to = ttk.Label(frame, text="To")
        label_to.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.combobox_to = ttk.Combobox(frame, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
        self.combobox_to.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Button
        hitung = ttk.Button(frame, text="Hitung", command=self.hitung)
        hitung.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        # Output
        label_output = ttk.Label(frame, text="Output")
        label_output.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.entry_output = ttk.Entry(frame)
        self.entry_output.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = Rumus(root)
    root.mainloop()
