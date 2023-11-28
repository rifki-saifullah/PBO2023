import tkinter as tk
from gtts import gTTS
from playsound import playsound

def convert_text_to_audio():
    text = entry.get()
    language = 'id'
    
    # Menggunakan gTTS untuk mengonversi teks ke audio
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Menyimpan audio ke file temporary
    tts.save("output.mp3")
    
    # Memutar audio
    playsound("output.mp3")

# Membuat GUI dengan Tkinter
app = tk.Tk()
app.title("Text to Audio")
app.geometry("500x200")

# Label dan Entry untuk input teks
label = tk.Label(app, text="Masukkan Teks:")
label.pack(pady=10)
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

# Tombol untuk mengonversi teks menjadi audio
convert_button = tk.Button(app, text="Convert to Audio", command=convert_text_to_audio)
convert_button.pack(pady=20)

# Menjalankan aplikasi Tkinter
app.mainloop()
