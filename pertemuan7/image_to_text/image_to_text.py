import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class ImageToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        self.image_path = None

        self.label = tk.Label(root, text="Pilih gambar:")
        self.label.pack(pady=10)

        self.btn_browse = tk.Button(root, text="Telusuri", command=self.browse_image)
        self.btn_browse.pack(pady=5)

        self.btn_convert = tk.Button(root, text="Konversi", command=self.convert_image_to_text)
        self.btn_convert.pack(pady=10)

        self.text_result = tk.Text(root, height=10, width=50)
        self.text_result.pack(padx=10, pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Pilih Gambar")
        if file_path:
            self.image_path = file_path
            self.show_image()

    def show_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        if hasattr(self, 'panel'):
            self.panel.destroy()

        self.panel = tk.Label(self.root, image=photo)
        self.panel.image = photo
        self.panel.pack(pady=10)

    def convert_image_to_text(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, text)
            print(text)
        else:
            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, "Pilih gambar terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverter(root)
    root.mainloop()
