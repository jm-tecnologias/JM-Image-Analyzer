import customtkinter as ctk
import tkinter.font as tkfont
from PIL import Image
import os
from utils.CarouselWidgets import CarouselWidgets
from model.ImageView import ImageView
from model.SateliteMap import SateliteMap
from model.NormalMap import NormalMap



class App:
    def __init__(self):
        self.dataSource = {}
        self.selected_item = None

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        self.root = ctk.CTk()
        self.root.title('JM-Image Analyzer')

        # windows size
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f'{width}x{height}')

        # main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Column Configuration
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=5)
        self.main_frame.columnconfigure(2, weight=2)
        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=1)


        # ________________________ Pallet Side ________________________

        self.palletFrame = ctk.CTkFrame(self.main_frame)
        self.palletFrame.grid(row=1, column=0, sticky='nswe')

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

        self.titleLab.grid(row=0, column=0, sticky='we', pady=(40,10))

        # ---------- ScrollPane for images ----------
        self.scrollPane = ctk.CTkScrollableFrame(self.palletFrame)
        self.scrollPane.grid(row=1, column=0, sticky='nswe', pady=(26,80), padx=20)



        # Center
        self.center_frame = ctk.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=1, sticky='nswe')

        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.rowconfigure(1, weight=4)
        self.center_frame.rowconfigure(2, weight=0)

        # ---------- Title ----------
        self.titleLabCenterFrame = ctk.CTkLabel(
            self.center_frame,
            text='Image Preview',
            font=('Berlin Sans FB Demi', 32)
        )



        self.titleLabCenterFrame.grid(row=0, column=0, sticky='we', pady=(40, 10))



        # ---------- MetaData Details ---------

        self.metaDataDetails = ctk.CTkFrame(self.center_frame)
        self.metaDataDetails.grid(row=2, column=0, sticky='nswe', padx=5, pady=5)

        self.metaDataDetails.columnconfigure(0, weight=1)
        self.metaDataDetails.rowconfigure(0, weight=1)

        # ---------- ScrollPane for images carousel ----------

        self.imageScrollPane = ctk.CTkScrollableFrame(
            self.metaDataDetails,
            orientation="horizontal"
        )

        self.imageScrollPane.grid(row=0, column=0, sticky="nswe")



        # Right
        self.detaisFrame = ctk.CTkFrame(self.main_frame)
        self.detaisFrame.grid(row=1, column=2, sticky='nswe')

        # coluna única expansível
        self.detaisFrame.columnconfigure(0, weight=1)
        #
        # ⭐ Header / Content /
        self.detaisFrame.rowconfigure(0, weight=0)  # title
        self.detaisFrame.rowconfigure(1, weight=1)  # scroll area

        # ---------- Title ----------
        ctk.CTkLabel(
            self.detaisFrame,
            text='Selected Image Details',
            font=('Berlin Sans FB Demi', 32)
        ).grid(row=0, column=0, sticky='we', pady=(40, 10))

        self.detais = ctk.CTkFrame(self.detaisFrame)
        self.detais.grid(row=1, column=0, sticky='nswe', padx=20, pady=26)

        ctk.CTkLabel(
            self.detais,
            text='Data',
            font=('Berlin Sans FB Demi', 32)
        ).pack( pady=(40, 10))


        ctk.CTkLabel(
            self.detais,
            text='Data',
            font=('Berlin Sans FB Demi', 32)
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self.detais,
            text='Data',
            font=('Berlin Sans FB Demi', 32)
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self.detais,
            text='Data',
            font=('Berlin Sans FB Demi', 32)
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self.detais,
            text='Actions',
            font=('Berlin Sans FB Demi', 32)
        ).pack(pady=(40, 10))

        ctk.CTkButton(
            self.detais,
            text="Export",
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack( padx=5)
        ctk.CTkButton(
            self.detais,
            text="Action 1",
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(padx=5)
        ctk.CTkButton(
            self.detais,
            text="Action 2",
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(padx=5)

        self.createTabs()
        self.loadImagesDir()

    def previewImage(self, path):
        self.imageView.setImage(path)

    def createTabs(self):

        # Criar TabView dentro do right_frame
        self.tabview = ctk.CTkTabview(self.center_frame)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        # Criar abas
        self.tab_carousel = self.tabview.add("Carousel")
        self.tab_satelite = self.tabview.add("Satelite Map")
        self.tab_normal = self.tabview.add("Normal Map")

        # Carregar conteúdo das abas

        # ⭐ GUARDA A INSTÂNCIA
        self.imageView = ImageView(self.tab_carousel)
        SateliteMap(self.tab_satelite)
        NormalMap(self.tab_normal)

    # Funcao para carregar botoes com um preview das imagens
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

        self.root.update()

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
            self.root.update()

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



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()