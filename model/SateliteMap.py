
import customtkinter as ctk


class SateliteMap:

    def __init__(self, master):

        self.master = master

        # self.master.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(master, text="User Name").grid(row=0, column=0, padx=10, pady=10)

        self.entry = ctk.CTkEntry(master)
        self.entry.grid(row=0, column=1, sticky="ew", padx=10)

        self.save_btn = ctk.CTkButton(
            master,
            text="Save User",
            command=self.save_user
        )
        self.save_btn.grid(row=1, column=1, pady=20)

    def save_user(self):
        print("User:", self.entry.get())


