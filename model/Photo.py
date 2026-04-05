import customtkinter as ctk

from ImageView import ImageView
from SateliteMap import SateliteMap
from NormalMap import NormalMap


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------
        # Window config
        # ----------------------
        self.title("CustomTkinter TabView Example")
        self.geometry("900x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ----------------------
        # TabView
        # ----------------------
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create Tabs
        self.tab_home = self.tabview.add("Home H")
        self.tab_users = self.tabview.add("Users")
        self.tab_settings = self.tabview.add("Settings")

        # Load tab classes
        ImageView(self.tab_home)
        SateliteMap(self.tab_users)
        NormalMap(self.tab_settings)


if __name__ == "__main__":
    app = App()
    app.mainloop()

