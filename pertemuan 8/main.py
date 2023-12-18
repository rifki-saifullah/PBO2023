import tkinter as tk
from tkinter import ttk 
from suhu.Rumus import *

def new_window(_class):
	new = tk.Toplevel()
	new.transient()
	new.grab_set()
	_class(new)

# Window
window = tk.Tk()
window.title("Rifki Saifullah R5")
window.geometry("300x400")

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

nama = ttk.Label(frame, text="Nama :")
nama.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

value_nama = ttk.Label(frame, text="Rifki Saifullah")
value_nama.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)

nim = ttk.Label(frame, text="NIM :")
nim.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

value_nim = ttk.Label(frame, text="220511145")
value_nim.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

kelas = ttk.Label(frame, text="Kelas :")
kelas.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

value_kelas = ttk.Label(frame, text="TIF22E")
value_kelas.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

fitur = ttk.Label(frame, text="Fitur :")
fitur.grid(row=3, column=0, sticky=tk.N, padx=10, pady=10)

fitur_suhu = ttk.Label(frame, text="- Konversi Suhu")
fitur_suhu.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)

# Bar Menu
menu = tk.Menu(window)
window.config(menu=menu)

# Menu Calculator
menu_calculator = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="App", menu=menu_calculator)
menu_calculator.add_command(label="Kalkulator Suhu", command=lambda: new_window(Rumus))

window.mainloop()