import customtkinter as ctk
from PIL import Image

class SplashScreen(ctk.CTkToplevel):

    def __init__(self, master):
        super().__init__(master)

        self.overrideredirect(True)  # remove bordas
        self.geometry("500x300")

        # centralizar
        self.center_window()

        # imagem
        logo = ctk.CTkImage(
            light_image=Image.open("assets/logo.png"),
            size=(180, 180)
        )

        self.label_logo = ctk.CTkLabel(self, image=logo, text="")
        self.label_logo.pack(pady=30)

        self.label_text = ctk.CTkLabel(
            self,
            text="JM Image Analyzer",
            font=("Berlin Sans FB Demi", 22)
        )
        self.label_text.pack()

        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=20)
        self.progress.start()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.winfo_screenheight() // 2) - (300 // 2)
        self.geometry(f"+{x}+{y}")