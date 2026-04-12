import customtkinter as ctk
from model.ImageView import ImageView
from model.SateliteMap import SateliteMap
from model.NormalMap import NormalMap

class Tabs:
    def __init__(self, master):

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

    def getImageView(self):
        return self.imageView

    def getSatelliteMap(self):
        return self.sateliteMap

    def getNormalMap(self):
        return self.normalMap


