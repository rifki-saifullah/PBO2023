import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def submit():
    day = day_var.get()
    time = time_var.get()
    subject = subject_entry.get()

    if day and time and subject:
        schedule_listbox.insert(tk.END, f"{day} - {time}: {subject}")
        clear_entries()
    else:
        error_label.config(text="Semua kolom harus diisi!")

def save_schedule():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for schedule in schedule_listbox.get(0, tk.END):
                file.write(schedule + "\n")

def open_schedule():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            schedules = file.readlines()
            for schedule in schedules:
                schedule_listbox.insert(tk.END, schedule.strip())

def clear_entries():
    day_var.set("")
    time_var.set("")
    subject_entry.delete(0, tk.END)
    error_label.config(text="")

# Membuat jendela utama
root = tk.Tk()
root.title("Jadwal Mata Kuliah")

# Variabel StringVar untuk menyimpan input dari pengguna
day_var = tk.StringVar(root)
time_var = tk.StringVar(root)

# Label dan Entry untuk Hari
day_label = tk.Label(root, text="Hari:")
day_label.grid(row=0, column=0, padx=10, pady=10)
day_entry = ttk.Combobox(root, textvariable=day_var, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"])
day_entry.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk Waktu
time_label = tk.Label(root, text="Waktu:")
time_label.grid(row=1, column=0, padx=10, pady=10)
time_entry = ttk.Combobox(root, textvariable=time_var, values=["08:00-09:30", "10:00-11:30", "13:00-14:30", "15:00-16:30"])
time_entry.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk Mata Kuliah
subject_label = tk.Label(root, text="Mata Kuliah:")
subject_label.grid(row=2, column=0, padx=10, pady=10)
subject_entry = tk.Entry(root)
subject_entry.grid(row=2, column=1, padx=10, pady=10)

# Tombol Submit
submit_button = tk.Button(root, text="Tambah Jadwal", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk pesan kesalahan
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

# Listbox untuk menampilkan jadwal
schedule_listbox = tk.Listbox(root, width=50, height=10)
schedule_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Tombol Save
save_button = tk.Button(root, text="Simpan Jadwal", command=save_schedule)
save_button.grid(row=6, column=0, pady=10)

# Tombol Open
open_button = tk.Button(root, text="Buka Jadwal", command=open_schedule)
open_button.grid(row=6, column=1, pady=10)

# Menjalankan loop utama Tkinter
root.mainloop()
