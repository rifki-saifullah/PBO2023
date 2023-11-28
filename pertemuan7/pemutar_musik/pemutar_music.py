import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemutar Audio")
        self.master.geometry("300x300")

        self.audio_path = None
        self.paused = False

        # Membuat elemen-elemen GUI
        self.label = tk.Label(self.master, text="Pemutar Audio")
        self.label.pack(pady=10)

        self.btn_open = tk.Button(self.master, text="Pilih Audio", command=self.open_file)
        self.btn_open.pack(pady=20)

        self.btn_play_pause = tk.Button(self.master, text="Mainkan", state=tk.DISABLED, command=self.play_pause_audio)
        self.btn_play_pause.pack(pady=10)

        self.btn_exit = tk.Button(self.master, text="Keluar", command=self.master.destroy)
        self.btn_exit.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.audio_path = file_path
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            self.btn_play_pause.config(state=tk.NORMAL)
            self.label.config(text=f"Pemutar Audio - {file_path}")

    def play_pause_audio(self):
        if self.audio_path:
            if not self.paused:
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            self.paused = not self.paused

def main():
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
