import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemutar Video")
        self.master.geometry("400x270")

        self.video_path = None
        self.video_clip = None

        # Membuat elemen-elemen GUI
        self.label = tk.Label(self.master, text="Pemutar Video")
        self.label.pack(pady=10)

        self.btn_open = tk.Button(self.master, text="Pilih Video", command=self.open_file)
        self.btn_open.pack(pady=20)

        self.btn_play = tk.Button(self.master, text="Mainkan", state=tk.DISABLED, command=self.play_video)
        self.btn_play.pack(pady=10)

        self.btn_close = tk.Button(self.master, text="Tutup", command=self.close_app)
        self.btn_close.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.video_path = file_path
            self.video_clip = VideoFileClip(file_path)
            self.btn_play.config(state=tk.NORMAL)
            self.label.config(text=f"Pemutar Video - {file_path}")

    def play_video(self):
        if self.video_clip:
            self.video_clip.preview()

    def close_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
