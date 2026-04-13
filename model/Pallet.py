
import customtkinter as ctk
import os
class Pallet:

    def __init__(self, master, on_folder_selected):

        self.on_folder_selected = on_folder_selected

        self.selected_item = None
        self.dataSource = {}
        self.master = master
        # ________________________ Pallet Side ________________________

        self.palletFrame = ctk.CTkFrame(master)
        self.palletFrame.grid(row=0, column=0, sticky='nswe')

        # coluna única expansível
        self.palletFrame.columnconfigure(0, weight=1)

        # ⭐ Header / Content /
        self.palletFrame.rowconfigure(0, weight=0)  # title
        self.palletFrame.rowconfigure(1, weight=1)  # scroll area

        # ---------- Title ----------
        self.titleLab = ctk.CTkLabel(
            self.palletFrame,
            text='Media File Explore',
            font=('Berlin Sans FB Demi', 32)
        )

        self.titleLab.grid(row=0, column=0, sticky='we', pady=(40, 10))

        # ---------- ScrollPane for images ----------
        self.scrollPane = ctk.CTkScrollableFrame(self.palletFrame)
        self.scrollPane.grid(row=1, column=0, sticky='nswe', pady=(26, 80), padx=20)


        self.loadImagesDir()

    def loadImagesDir(self):

        path = 'C:/Users/JM-Tecnologias/Downloads'

        # ---------- limpar ----------
        self.dataSource = {}

        # guardar pasta raiz
        self.dataSource[0] = {
            "srcPath": path,
            "type": "root"
        }


        # ---------- LISTAR DIRECTORIAS ----------
        folders = []

        for entry in os.scandir(path):

            if entry.is_dir():
                folders.append(entry)

        total_folders = len(folders)

        # ---------- UI LOAD ----------
        for idx, entry in enumerate(folders, start=1):
            folder_name = entry.name
            folder_path = entry.path  # ⭐ caminho completo

            # ⭐ DATA SOURCE
            self.dataSource[idx] = {
                "name": folder_name,
                "absolutePath": folder_path,
                "type": "folder"
            }

            lab = ctk.CTkLabel(
                self.scrollPane,
                text=f"📁 {folder_name}",
                compound='left',
                font=('Comic Sans MS', 16),
                anchor='w'
            )

            lab.pack(fill='x', padx=8, pady=2)

            # ⭐ IMPORTANTÍSSIMO (bug clássico evitado)
            lab.bind(
                "<Button-1>",
                lambda e, widget=lab, data=self.dataSource[idx]:
                self.on_click(e, widget, data)
            )

    def on_click(self, event, widget, data):

        if self.selected_item and self.selected_item.winfo_exists():
            self.selected_item.configure(fg_color="transparent")

        widget.configure(fg_color="#1f6aa5")
        self.selected_item = widget

        path = data.get('absolutePath')

        # dispara evento externo
        if self.on_folder_selected:
            self.on_folder_selected(path)
