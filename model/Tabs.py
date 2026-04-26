import os
import customtkinter as ctk
from PIL import Image
from model.ImageModel import ImageModel
from model.ImageView import ImageView
from model.SateliteMap import SateliteMap
from model.NormalMap import NormalMap

class Tabs:
    def __init__(self, master, properties=None):

        self.miniMap = None
        self.properties = properties   # ⭐ ligação externa
        self.currentImage = None
        self.carouselButtons = []
        self.selectedButton = None


        # Center
        self.centerFrame = ctk.CTkFrame(master)
        self.centerFrame.grid(row=0, column=1, sticky='nswe')

        self.centerFrame.columnconfigure(0, weight=1)
        self.centerFrame.rowconfigure(1, weight=4)
        self.centerFrame.rowconfigure(2, weight=0)

        self.titleLabCenterFrame = ctk.CTkLabel(
            self.centerFrame,
            text='Image Preview',
            font=('Berlin Sans FB Demi', 32)
        )
        self.titleLabCenterFrame.grid(row=0, column=0, sticky='we', pady=(40, 10))

        self.createTabs(self.centerFrame)

        # ---------- Scroll Dos Botoes com mini imagens---------

        self.metaDataDetails = ctk.CTkFrame(self.centerFrame)
        self.metaDataDetails.grid(row=2, column=0, sticky='nswe', pady=5)

        self.metaDataDetails.columnconfigure(0, weight=1)
        self.metaDataDetails.rowconfigure(0, weight=1)
        # ---------- ScrollPane for images carousel ----------

        self.imageScrollPane = ctk.CTkScrollableFrame(
            self.metaDataDetails, fg_color="#141414",
            orientation="horizontal"
        )

        self.imageScrollPane.grid(row=0, column=0, sticky="nswe")

    def createTabs(self, frame):
        self.tab_font = ctk.CTkFont(
            family="Berlin Sans FB Demi",
            size=20,
            # weight="bold",  # normal | bold
            # slant="italic",  # italic
            # underline=True,
            # overstrike=False
        )

        self.tabview = ctk.CTkTabview(frame, fg_color="#141414",
                                      segmented_button_selected_color="#38c20e",
                                      # segmented_button_selected_border_color="#38c20e",
                                      segmented_button_selected_hover_color="#38c20e"
                                      )
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.tabview._segmented_button.configure(font=self.tab_font)


        # Criar abas
        self.tab_carousel = self.tabview.add("Image Preview")
        self.tab_satelite = self.tabview.add("Satelite Map")
        self.tab_normal = self.tabview.add("Normal Map")


        # Carregar conteúdo das abas

        # ⭐ GUARDA A INSTÂNCIA
        self.imageView = ImageView(self.tab_carousel)
        self.sateliteMap = SateliteMap(self.tab_satelite)
        self.normalMap = NormalMap(self.tab_normal)

        return self.tabview

    def onCarouselClick(self, path, clicked_button):

        # remover seleção anterior
        if self.selectedButton:
            self.selectedButton.configure(
                border_width=0,
                fg_color="#141414"
            )

        # aplicar seleção nova
        clicked_button.configure(
            border_width=2,
            border_color="#38c20e",
            fg_color="#020617"
        )

        self.selectedButton = clicked_button

        # guardar imagem actual
        self.currentImage = path

        # actualizar preview
        self.getImageView().setImage(path)

        # actualizar propriedades
        if self.properties:
            self.properties.updateImageProperties(path)

            image_model = ImageModel.from_image(path)

            self.getSatelliteMap().updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])
            self.getNormalMap().updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])

            if hasattr(self, "miniMap") and self.miniMap:
                self.miniMap.updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])

    def setMiniMap(self, mini_map):
        self.miniMap = mini_map

    def getImageView(self):
        return self.imageView

    def getSatelliteMap(self):
        return self.sateliteMap

    def getNormalMap(self):
        return self.normalMap

    def carouselButtonLoader(self, path):

        self.dataSource = {}

        # limpar UI antiga
        for widget in self.imageScrollPane.winfo_children():
            widget.destroy()

        self.image_cache = {}

        valid_extensions = ('.jpg', '.jpeg', '.png')

        files = [
            entry for entry in os.scandir(path)
            if entry.is_file() and entry.name.lower().endswith(valid_extensions)
        ]

        self.dataSource[0] = {'srcPath': path}

        for idx, entry in enumerate(files, start=1):

            self.dataSource[idx] = {
                'file': entry.name,
                'absolutePath': entry.path,
            }

            # -------- CACHE (evita recarregar imagem) --------
            if entry.path in self.image_cache:
                icon = self.image_cache[entry.path]
            else:
                img = Image.open(entry.path)
                img = img.resize((120, 120), Image.LANCZOS)  # força preenchimento total

                icon = ctk.CTkImage(light_image=img, size=(120, 120))
                self.image_cache[entry.path] = icon


            iconBtn = ctk.CTkButton(
                self.imageScrollPane,
                text="",
                image=icon,

                width=120,
                height=120,
                corner_radius=14,
                fg_color="#141414",  # dark glass
                hover_color="#1e293b",
                # command=lambda p=entry.path: self.onCarouselClick(p),

            )
            self.carouselButtons.append(iconBtn)
            iconBtn.pack(side="left", padx=8, pady=6)

            iconBtn.configure(
                command=lambda p=entry.path, b=iconBtn: self.onCarouselClick(p, b)
            )



