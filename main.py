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


        # ---------- Folder Details ----------
        # self.palletFolderDetails = ctk.CTkFrame(self.palletFrame)
        # self.palletFolderDetails.grid(row=2, column=0, sticky='we', padx=5, pady=5)


        # self.lab = ctk.CTkLabel(
        #     self.palletFolderDetails,
        #     text='Site Details',
        #     font=('Berlin Sans FB Demi', 24)
        # )
        # self.lab.pack(anchor='w', fill='x')

        # self.lab2 = ctk.CTkLabel(
        #     self.palletFolderDetails,
        #     text='Src:',
        #     font=('Comic Sans MS', 12),
        #     # wraplength=210, # px
        #     anchor='w'
        # )
        # self.lab2.pack(anchor='w', fill='x')
        #
        # self.lab3 = ctk.CTkLabel(
        #     self.palletFolderDetails,
        #     text='File Counter:',
        #     font=('Comic Sans MS', 12),
        #     anchor='w'
        # )
        # self.lab3.pack(anchor='w', fill='x')

        # self.lab4 = ctk.CTkLabel(
        #     self.palletFolderDetails,
        #     text='Folder Size:',
        #     font=('Comic Sans MS', 12),
        #     anchor='w'
        # )
        # self.lab4.pack(anchor='w', fill='x')
        #
        # self.lab5 = ctk.CTkLabel(
        #     self.palletFolderDetails,
        #     text='Created At:',
        #     font=('Comic Sans MS', 12),
        #     anchor='w'
        # )
        # self.lab5.pack(anchor='w', fill='x')





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



        #  Cria Carousel
        # self.loadCarousel()

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

        # _____________________ Group I _____________________


        self.icon = ctk.CTkImage(
            light_image=Image.open("assets/ico.png"),
            dark_image=Image.open("assets/ico2.png"),
            size=(180, 180)  # tamanho do ícone
        )

        ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=self.icon,
            fg_color="transparent",
            # hover_color="#1f6aa5",
        #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=self.icon,
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=self.icon,
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=self.icon,
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=self.icon,
            fg_color="transparent",
            # hover_color="#1f6aa5",
            #     # command=self.save_user
            # width=90,
            # height=90
        ).pack(side="left", padx=5)


        # Right
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.grid(row=1, column=2, sticky='nswe', padx = 2)

        self.createTabs()
        # Load File Function
        self.loadImageList()


    def createTabs(self):

        # Criar TabView dentro do right_frame
        self.tabview = ctk.CTkTabview(self.center_frame)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # # permitir expandir
        # self.center_frame.rowconfigure(0, weight=1)
        # self.center_frame.columnconfigure(0, weight=1)

        # Criar abas
        self.tab_carousel = self.tabview.add("Carousel")
        self.tab_satelite = self.tabview.add("Satelite Map")
        self.tab_normal = self.tabview.add("Normal Map")

        # Carregar conteúdo das abas
        ImageView(self.tab_carousel)
        SateliteMap(self.tab_satelite)
        NormalMap(self.tab_normal)


    def loadImageList(self):
        path = 'C:/Users/JM-Tecnologias/Downloads/metadata extraction project'

        # Mostrar loader
        loader = ctk.CTkLabel(self.scrollPane, text="Loading...", font=('Berlin Sans FB Demi', 20))
        loader.pack(pady=20)

        progress = ctk.CTkProgressBar(self.scrollPane, width=200)
        progress.pack(pady=10)
        progress.set(0)

        self.root.update()  # Forçar redraw para mostrar o loader antes de processar

        # Limpar dados antigos
        self.dataSource = {}
        for widget in self.scrollPane.winfo_children():
            if widget not in (loader, progress):
                widget.destroy()

        valid_extensions = ('.jpg', '.jpeg', '.png')
        self.dataSource[0] = {'srcPath': path}

        files = [f for f in os.listdir(path) if f.lower().endswith(valid_extensions)]
        total_files = len(files)

        self.icon = ctk.CTkImage(
            light_image=Image.open("assets/ico.png"),
            dark_image=Image.open("assets/ico2.png"),
            size=(48, 48)  # tamanho do ícone
        )

        # Carregar cada arquivo com update do progress
        for idx, file in enumerate(files, start=1):
            full_path = os.path.join(path, file)
            self.dataSource[idx] = {'absolutePath': full_path, 'file': file}



            lab = ctk.CTkLabel(
                self.scrollPane,
                text=f"➡ {file}",
                image=self.icon,
                compound='left',
                font=('Comic Sans MS', 16),
                anchor='w'
            )
            lab.pack(fill='x', padx=8, pady=2)

            lab.bind(
                "<Button-1>",
                lambda e, widget=lab, data=self.dataSource[idx]: self.on_click(e, widget, data)
            )

            progress.set(idx / total_files)  # Atualiza barra de progresso
            self.root.update()  # Redesenha a interface

        # Remover loader
        loader.destroy()
        progress.destroy()




        # self.loadCarousel()


    def ellipsis_path(self, widget, text, max_width):
        font = tkfont.Font(font=widget.cget("font"))

        # se couber, retorna normal
        if font.measure(text) <= max_width:
            return text

        left = 0
        right = len(text)

        while left < right:
            left_part = text[:left]
            right_part = text[len(text) - right:]
            candidate = f"{left_part}...{right_part}"

            if font.measure(candidate) <= max_width:
                return candidate

            if left <= right:
                right -= 1
            else:
                left += 1

        return "..."

    def on_click(self, event, widget, data):

        # reset item anterior
        if self.selected_item and self.selected_item.winfo_exists():
            self.selected_item.configure(fg_color="transparent")

        # destacar novo
        widget.configure(fg_color="#1f6aa5")

        self.selected_item = widget

        print(f"Selecionaste: {data.get('file')}")

    # def loadCarousel(self):
    #     paths = ['assets/photo.jpg']
    #     if len(self.dataSource) > 0:
    #         paths = []
    #
    #     for item in self.dataSource.values():
    #
    #         path = item.get('absolutePath')
    #
    #         if path and os.path.isfile(path):
    #             paths.append(path)
    #
    #     # ⭐ CALLBACK REGISTADO
    #     self.carousel = CarouselWidgets(
    #         on_change=self.update_image_details)
    #
    #     self.carousel.createCarousel(
    #         self.center_frame,
    #         paths
    #     )
    #
    # def update_image_details(self, details=None):
    #
    #     print("NOVOS DETALHES RECEBIDOS:")
    #     print(details)
    #     print(details['locationDetails']['latitude'])
    #     print(details['locationDetails']['longitude'])
    #     print(details['locationDetails']['altitude'])
    #



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()