import customtkinter as ctk


class NormalMap:

    def __init__(self, master):

        self.master = master

        self.switch = ctk.CTkSwitch(
            master,
            text="Dark Mode",
            command=self.toggle_mode
        )
        self.switch.grid(row=0, column=0, padx=20, pady=20)

    def toggle_mode(self):
        if self.switch.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")