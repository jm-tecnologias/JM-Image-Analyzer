
import customtkinter as ctk
from PIL import Image
import os
class Pallet:

    def __init__(self, master, centerFrame, on_image_selected):
        self.on_image_selected = on_image_selected
        self.selected_item = None
        self.dataSource = {}
        self.master = master
        # self.imageView = imageView
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

        # ---------- Scroll Dos Botoes com mini imagens---------

        self.metaDataDetails = ctk.CTkFrame(centerFrame)
        self.metaDataDetails.grid(row=2, column=0, sticky='nswe', pady=5)

        self.metaDataDetails.columnconfigure(0, weight=1)
        self.metaDataDetails.rowconfigure(0, weight=1)
        # ---------- ScrollPane for images carousel ----------

        self.imageScrollPane = ctk.CTkScrollableFrame(
            self.metaDataDetails,
            orientation="horizontal"
        )

        self.imageScrollPane.grid(row=0, column=0, sticky="nswe")

        self.loadImagesDir()

    def carouselButtonLoader(self, path):

        # ---------- limpar dados antigos ----------
        self.dataSource = {}

        for widget in self.imageScrollPane.winfo_children():
            widget.destroy()

        # ---------- guardar pasta raiz ----------
        self.dataSource[0] = {
            'srcPath': path,
            'type': 'root'
        }

        valid_extensions = ('.jpg', '.jpeg', '.png')

        # ---------- listar imagens ----------
        idx = 1

        for entry in os.scandir(path):

            if entry.is_file() and entry.name.lower().endswith(valid_extensions):
                # guardar no datasource
                self.dataSource[idx] = {
                    'file': entry.name,
                    'absolutePath': entry.path,
                    'type': 'image'
                }
                # ---------- carregar ícone ----------
                icon = ctk.CTkImage(
                    light_image=Image.open(entry.path),
                    size=(180, 180)  # tamanho do ícone
                )

                ctk.CTkButton(
                    self.imageScrollPane,
                    text="",
                    image=icon,
                    hover_color="#333",
                    fg_color="transparent",
                    command=lambda p=entry.path: self.previewImage(p)
                ).pack(side="left", padx=5)


    # def previewImage(self, path):
    #     self.on_image_selected(path)
    def previewImage(self, path):

        # dispara evento externo
        if self.on_image_selected:
            self.on_image_selected(path)


    def loadImagesDir(self):

        path = 'C:/Users/JM-Tecnologias/Downloads'

        # ---------- Loader ----------
        loader = ctk.CTkLabel(
            self.scrollPane,
            text="Loading...",
            font=('Berlin Sans FB Demi', 20)
        )
        loader.pack(pady=20)

        progress = ctk.CTkProgressBar(self.scrollPane, width=200)
        progress.pack(pady=10)
        progress.set(0)

        self.master.update()

        # ---------- limpar ----------
        self.dataSource = {}

        for widget in self.scrollPane.winfo_children():
            if widget not in (loader, progress):
                widget.destroy()

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

            progress.set(idx / total_folders)
            self.master.update()

        loader.destroy()
        progress.destroy()

    def on_click(self, event, widget, data):

        # reset item anterior
        if self.selected_item and self.selected_item.winfo_exists():
            self.selected_item.configure(fg_color="transparent")

        # destacar novo
        widget.configure(fg_color="#1f6aa5")

        self.selected_item = widget

        self.carouselButtonLoader(data.get('absolutePath'))

