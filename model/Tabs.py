import os
import customtkinter as ctk
from PIL import Image
import threading
from model.ImageModel import ImageModel
from model.ImageView import ImageView
from model.SateliteMap import SateliteMap

import cv2
from PIL import Image
from model.NormalMap import NormalMap

class Tabs:
    def __init__(self, master, properties=None):

        self.dataSource = None
        self.miniMap = None
        self.properties = properties   # ⭐ ligação externa
        self.currentImage = None
        self.carouselButtons = []
        self.selectedButton = None
        self.image_cache = {}


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
        # self.tab_normal = self.tabview.add("Normal Map")

        # ⭐ GUARDA A INSTÂNCIA
        self.imageView = ImageView(self.tab_carousel)
        self.sateliteMap = SateliteMap(self.tab_satelite)
        # self.normalMap = NormalMap(self.tab_normal)

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
            print(image_model)

            if 'GPSInfo' in image_model:
                self.getSatelliteMap().updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])
                # self.getNormalMap().updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])

                if hasattr(self, "miniMap") and self.miniMap:
                    self.miniMap.updatePosition(image_model['GPSInfo']['Latitude'], image_model['GPSInfo']['Longitude'])

    def setMiniMap(self, mini_map):
        self.miniMap = mini_map

    def getImageView(self):
        return self.imageView

    def getSatelliteMap(self):
        return self.sateliteMap

    # def getNormalMap(self):
    #     return self.normalMap

    def _add_button(self, path, icon):

        iconBtn = ctk.CTkButton(
            self.imageScrollPane,
            text="",
            image=icon,
            width=120,
            height=120,
            corner_radius=14,
            fg_color="#141414",
            hover_color="#1e293b",
        )

        self.carouselButtons.append(iconBtn)

        iconBtn.pack(side="left", padx=8, pady=6)

        iconBtn.configure(
            command=lambda p=path, b=iconBtn:
            self.onCarouselClick(p, b)
        )

    def load_thumbnail_opencv(self, path, size=(120,120)):

        # leitura ULTRA rápida
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        if img is None:
            return None

        # converter BGR → RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # resize rápido (MUITO mais leve que PIL)
        img = cv2.resize(
            img,
            size,
            interpolation=cv2.INTER_AREA
        )

        # numpy → PIL
        pil_image = Image.fromarray(img)

        return pil_image

    def _load_thumbnails_background(self, files):

        for idx, entry in enumerate(files, start=1):

            self.dataSource[idx] = {
                'file': entry.name,
                'absolutePath': entry.path,
            }

            if entry.path in self.image_cache:
                icon = self.image_cache[entry.path]
            else:
                img = self.load_thumbnail_opencv(entry.path, (120, 120))

                if img is None:
                    continue

                icon = ctk.CTkImage(light_image=img, size=(120, 120))
                self.image_cache[entry.path] = icon

            # atualizar UI com segurança
            self.imageScrollPane.after(
                0,
                lambda p=entry.path, ic=icon: self._add_button(p, ic)
            )

    def carouselButtonLoader(self, path):

        self.dataSource = {}

        for widget in self.imageScrollPane.winfo_children():
            widget.destroy()

        self.selectedButton = None
        self.carouselButtons.clear()

        valid_extensions = ('.jpg', '.jpeg', '.png')

        files = [
            entry for entry in os.scandir(path)
            if entry.is_file() and entry.name.lower().endswith(valid_extensions)
        ]

        self.dataSource[0] = {'srcPath': path}

        # THREAD BACKGROUND
        threading.Thread(
            target=self._load_thumbnails_background,
            args=(files,),
            daemon=True
        ).start()




