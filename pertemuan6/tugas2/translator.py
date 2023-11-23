import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")
        self.master.geometry("400x500")

        self.label_text = tk.Label(self.master, text="Enter Text:")
        self.label_text.pack(pady=10)

        self.entry_text = tk.Entry(self.master, width=40)
        self.entry_text.pack(pady=10)

        self.label_source_lang = tk.Label(self.master, text="Source Language:")
        self.label_source_lang.pack(pady=5)

        self.source_lang_var = tk.StringVar()
        self.source_lang_var.set("auto")  # "auto" for automatic language detection

        self.source_lang_menu = ttk.Combobox(self.master, values=["auto", "en", "es", "fr", "de", "ja", "ko"])
        self.source_lang_menu.pack(pady=5)

        self.label_target_lang = tk.Label(self.master, text="Target Languages:")
        self.label_target_lang.pack(pady=5)

        self.target_lang_var = tk.StringVar()

        self.target_lang_menu = tk.Listbox(self.master, selectmode=tk.MULTIPLE, height=5)
        self.target_lang_menu.insert(6, "id")
        self.target_lang_menu.insert(1, "en")
        self.target_lang_menu.insert(2, "es")
        self.target_lang_menu.insert(3, "fr")
        self.target_lang_menu.insert(4, "de")
        self.target_lang_menu.insert(5, "ja")
        self.target_lang_menu.insert(6, "ko")
        self.target_lang_menu.pack(pady=5)

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def translate_text(self):
        text_to_translate = self.entry_text.get()
        source_lang = self.source_lang_var.get()
        target_langs = [self.target_lang_menu.get(idx) for idx in self.target_lang_menu.curselection()]

        if not text_to_translate or not target_langs:
            tk.messagebox.showwarning("Warning", "Please enter text and select target languages.")
            return

        translator = Translator()
        translations = []

        for target_lang in target_langs:
            translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
            translations.append(f"{target_lang.upper()}: {translation.text}")

        result_text = "\n".join(translations)
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()
    