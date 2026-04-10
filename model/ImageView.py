import os

import customtkinter as ctk
from PIL import Image

from utils.CarouselWidgets import CarouselWidgets

import customtkinter as ctk
from PIL import Image


class ImageView:

    def __init__(self, master):

        self.master = master
        self.master.pack_propagate(False)

        self.image_label = ctk.CTkLabel(
            self.master,
            text=""
        )
        self.image_label.pack(fill='both', expand=True)

        self.current_pil = None
        self.setImage('assets/logo.png')

    # ------------------------------
    # SET IMAGE COM TRANSIÇÃO
    # ------------------------------
    def setImage(self, path):
        new_image = Image.open(path).convert("RGBA").resize((890, 850))

        if self.current_pil is None:
            self.current_pil = new_image
            self._update_label(new_image)
            return

        # converter a imagem antiga também
        old_image = self.current_pil.convert("RGBA")

        self._fade_transition(old_image, new_image)
    # ------------------------------
    # ANIMAÇÃO FADE
    # ------------------------------
    def _fade_transition(self, old_img, new_img, step=0):
        alpha = step / 10
        blended = Image.blend(old_img, new_img, alpha)
        self._update_label(blended)
        if step < 10:
            self.master.after(30, lambda: self._fade_transition(old_img, new_img, step + 1))
        else:
            self.current_pil = new_img

    # ------------------------------
    # UPDATE LABEL
    # ------------------------------
    def _update_label(self, pil_image):

        self.my_image = ctk.CTkImage(
            light_image=pil_image,
            size=(890, 850)
        )

        self.image_label.configure(image=self.my_image)


#
# import customtkinter as ctk
# from PIL import Image
#
# class ImageView:
#     def __init__(self, master):
#         self.master = master
#         self.master.pack_propagate(False)
#
#         # ------------------- Label da imagem -------------------
#         self.image_label = ctk.CTkLabel(master, text="", bg_color='red')
#         self.image_label.grid(row=1, column=0, sticky='nswe', pady=10)
#
#         # ------------------- Estado interno -------------------
#         self.current_pil = None
#         self.setImage("assets/logo.png")
#
#     # ------------------- SET IMAGE -------------------
#     def setImage(self, path):
#         new_image = Image.open(path).convert("RGBA").resize((850, 550))
#
#         if self.current_pil is None:
#             self.current_pil = new_image
#             self._update_label(new_image)
#             return
#
#         old_image = self.current_pil.convert("RGBA")
#         self._fade_transition(old_image, new_image)
#
#     # ------------------- FADE TRANSITION -------------------
#     def _fade_transition(self, old_img, new_img, step=0):
#         alpha = step / 10
#         blended = Image.blend(old_img, new_img, alpha)
#         self._update_label(blended)
#         if step < 10:
#             self.master.after(30, lambda: self._fade_transition(old_img, new_img, step + 1))
#         else:
#             self.current_pil = new_img
#
#     # ------------------- UPDATE LABEL -------------------
#     def _update_label(self, pil_image):
#         self.my_image = ctk.CTkImage(light_image=pil_image, size=(850, 550))
#         self.image_label.configure(image=self.my_image)