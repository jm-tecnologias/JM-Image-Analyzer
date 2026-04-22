import os

import customtkinter as ctk
from PIL import Image

from model.ImageView import ImageView
from model.MineSateliteMap import MiniSateliteMap
from model.Pallet import Pallet
from model.SateliteMap import SateliteMap
from model.NormalMap import NormalMap

class Tabs:
    def __init__(self, master, properties=None):

        self.miniMap = None
        self.properties = properties   # ⭐ ligação externa
        self.currentImage = None


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
            self.metaDataDetails,
            orientation="horizontal"
        )

        self.imageScrollPane.grid(row=0, column=0, sticky="nswe")

        # ctk.CTkButton(self.imageScrollPane, text="Botao de teste").pack(side="left", padx=5)


    def createTabs(self, frame):
        self.tabview = ctk.CTkTabview(frame)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        # Criar abas
        self.tab_carousel = self.tabview.add("Carousel")
        self.tab_satelite = self.tabview.add("Satelite Map")
        self.tab_normal = self.tabview.add("Normal Map")


        # Carregar conteúdo das abas

        # ⭐ GUARDA A INSTÂNCIA
        self.imageView = ImageView(self.tab_carousel)
        self.sateliteMap = SateliteMap(self.tab_satelite)
        self.normalMap = NormalMap(self.tab_normal)


        return self.tabview

    def onCarouselClick(self, path):

        # guardar imagem actual
        self.currentImage = path

        # actualizar preview
        self.getImageView().setImage(path)

        # actualizar propriedades
        if self.properties:
            self.properties.updateImageProperties(path)
            gps = self.properties.metaDataSouce.get("GPSInfo")

            if gps:
                lat_ref = gps.get(1)
                lat = gps.get(2)
                lon_ref = gps.get(3)
                lon = gps.get(4)

                self.getSatelliteMap().updatePosition(
                    lat, lon, lat_ref, lon_ref
                )

                self.getNormalMap().updatePosition(
                    lat, lon, lat_ref, lon_ref
                )

                if hasattr(self, "miniMap") and self.miniMap:
                    self.miniMap.updatePosition(lat, lon, lat_ref, lon_ref)

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
                img.thumbnail((180, 180))  # mais rápido
                icon = ctk.CTkImage(light_image=img, size=(180, 180))
                self.image_cache[entry.path] = icon

            btn = ctk.CTkButton(
                self.imageScrollPane,
                text="",
                image=icon,
                hover_color="#333",
                fg_color="transparent",
                command=lambda p=entry.path: self.onCarouselClick(p)
            )

            btn.pack(side="left", padx=5)

