import tkinter as tk
from tkinter import ttk 
from function.include import *

def new_window(_class):
	new = tk.Toplevel()
	new.transient()
	new.grab_set()
	_class(new)

# Window
window = tk.Tk()
window.title("Multiform")
window.geometry("300x200")

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

nama = ttk.Label(frame, text="Rifki Saifullah")
nama.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

nim = ttk.Label(frame, text="220511145")
nim.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

kelas = ttk.Label(frame, text="R5")
kelas.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

# Bar Menu
menu = tk.Menu(window)
window.config(menu=menu)

# Menu Calculator
menu_calculator = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Kalkulator Bangun Ruang", menu=menu_calculator)
menu_calculator.add_command(label="Balok", command=lambda: new_window(balok))
menu_calculator.add_command(label="Bola", command=lambda: new_window(bola))
menu_calculator.add_command(label="Kerucut", command=lambda: new_window(kerucut))
menu_calculator.add_command(label="Kubus", command=lambda: new_window(kubus))
menu_calculator.add_command(label="Limas Segiempat", command=lambda: new_window(limas_segiempat))
menu_calculator.add_command(label="Limas Segitiga", command=lambda: new_window(limas_segitiga))
menu_calculator.add_command(label="Prisma Segitiga", command=lambda: new_window(prisma_segitiga))
menu_calculator.add_command(label="Tabung", command=lambda: new_window(tabung))

window.mainloop()
