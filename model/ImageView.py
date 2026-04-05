import os

import customtkinter as ctk
from PIL import Image

from utils.CarouselWidgets import CarouselWidgets


class ImageView:

    def __init__(self, master):

        self.master = master

        # 🔥 impedir resize automático
        self.master.pack_propagate(False)

        self.my_image = ctk.CTkImage(
            light_image=Image.open("assets/ico.png"),
            dark_image=Image.open("assets/ico2.png"),
            size=(850, 550)
        )

        self.image_label = ctk.CTkLabel(
            master,
            image=self.my_image,
            text=""
        )

        self.image_label.pack(pady=40)

    def loadCarousel(self, dataSource, frame):
        paths = ['assets/photo.jpg']
        if len(dataSource) > 0:
            paths = []

        for item in dataSource.values():

            path = item.get('absolutePath')

            if path and os.path.isfile(path):
                paths.append(path)

        # CALLBACK REGISTADO
        self.carousel = CarouselWidgets(
            on_change=self.update_image_details)

        self.carousel.createCarousel(
            frame,
            paths
        )

    def update_image_details(self, details=None):

        print("NOVOS DETALHES RECEBIDOS:")
        print(details)
        print(details['locationDetails']['latitude'])
        print(details['locationDetails']['longitude'])
        print(details['locationDetails']['altitude'])



