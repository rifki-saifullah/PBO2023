import tkinter as tk
from tkinter import ttk

class Rumus:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Kalkulator Suhu")
        self.component()

    # Temperature conversion methods
    def celcius_to_fahrenheit(self):
        celcius = float(self.entry_input.get())
        value = (9 / 5 * celcius) + 32
        self.update_output(value)

    def celcius_to_reamur(self):
        celcius = float(self.entry_input.get())
        value = 4 / 5 * celcius
        self.update_output(value)

    def celcius_to_kelvin(self):
        celcius = float(self.entry_input.get())
        value = celcius + 273
        self.update_output(value)

    def fahrenheit_to_celcius(self):
        fahrenheit = float(self.entry_input.get())
        value = 5 / 9 * (fahrenheit - 32)
        self.update_output(value)

    def fahrenheit_to_reamur(self):
        fahrenheit = float(self.entry_input.get())
        value = 4 / 9 * (fahrenheit - 32)
        self.update_output(value)

    def fahrenheit_to_kelvin(self):
        fahrenheit = float(self.entry_input.get())
        value = 5 / 9 * (fahrenheit - 32) + 273
        self.update_output(value)

    def reamur_to_celcius(self):
        reamur = float(self.entry_input.get())
        value = (5 / 4) * reamur
        self.update_output(value)

    def reamur_to_fahrenheit(self):
        reamur = float(self.entry_input.get())
        value = (9 / 4) * reamur + 32
        self.update_output(value)

    def reamur_to_kelvin(self):
        reamur = float(self.entry_input.get())
        value = (5 / 4) * reamur + 273.15
        self.update_output(value)

    def kelvin_to_celcius(self):
        kelvin = float(self.entry_input.get())
        value = kelvin - 273.15
        self.update_output(value)

    def kelvin_to_fahrenheit(self):
        kelvin = float(self.entry_input.get())
        value = (9 / 5) * (kelvin - 273) + 32
        self.update_output(value)

    def kelvin_to_reamur(self):
        kelvin = float(self.entry_input.get())
        value = (4 / 5) * (kelvin - 273)
        self.update_output(value)

    def hitung(self):
        conversion_from = self.combobox_from.get()
        conversion_to = self.combobox_to.get()

        if conversion_from == "Celcius":
            self.handle_celcius_conversion(conversion_to)
        elif conversion_from == "Fahrenheit":
            self.handle_fahrenheit_conversion(conversion_to)
        elif conversion_from == "Reamur":
            self.handle_reamur_conversion(conversion_to)
        elif conversion_from == "Kelvin":
            self.handle_kelvin_conversion(conversion_to)

    def handle_celcius_conversion(self, conversion_to):
        if conversion_to == "Fahrenheit":
            self.celcius_to_fahrenheit()
        elif conversion_to == "Reamur":
            self.celcius_to_reamur()
        elif conversion_to == "Kelvin":
            self.celcius_to_kelvin()

    def handle_fahrenheit_conversion(self, conversion_to):
        if conversion_to == "Celcius":
            self.fahrenheit_to_celcius()
        elif conversion_to == "Reamur":
            self.fahrenheit_to_reamur()
        elif conversion_to == "Kelvin":
            self.fahrenheit_to_kelvin()

    def handle_reamur_conversion(self, conversion_to):
        if conversion_to == "Celcius":
            self.reamur_to_celcius()
        elif conversion_to == "Fahrenheit":
            self.reamur_to_fahrenheit()
        elif conversion_to == "Kelvin":
            self.reamur_to_kelvin()

    def handle_kelvin_conversion(self, conversion_to):
        if conversion_to == "Celcius":
            self.kelvin_to_celcius()
        elif conversion_to == "Fahrenheit":
            self.kelvin_to_fahrenheit()
        elif conversion_to == "Reamur":
            self.kelvin_to_reamur()

    def update_output(self, value):
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(tk.END, value)

    def component(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Input
        ttk.Label(frame, text="Masukkan Nilai : ").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_input = ttk.Entry(frame)
        self.entry_input.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Combobox From
        ttk.Label(frame, text="From").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.combobox_from = ttk.Combobox(frame, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
        self.combobox_from.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Combobox To
        ttk.Label(frame, text="To").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.combobox_to = ttk.Combobox(frame, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
        self.combobox_to.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Button
        ttk.Button(frame, text="Hitung", command=self.hitung).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        # Output
        ttk.Label(frame, text="Output").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_output = ttk.Entry(frame)
        self.entry_output.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = Rumus(root)
    root.mainloop()
