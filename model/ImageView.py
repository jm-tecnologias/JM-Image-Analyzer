#
# import customtkinter as ctk
# from PIL import Image
#
#
# class ImageView:
#
#     def __init__(self, master):
#
#         self.master = master
#         self.master.pack_propagate(False)
#
#         self.image_label = ctk.CTkLabel(
#             self.master,
#             text=""
#         )
#         self.image_label.pack(fill='both', expand=True)
#
#         self.current_pil = None
#         self.setImage('assets/logo.png')
#
#     # ------------------------------
#     # SET IMAGE COM TRANSIÇÃO
#     # ------------------------------
#     def setImage(self, path):
#         new_image = Image.open(path).convert("RGBA").resize((890, 850))
#
#         if self.current_pil is None:
#             self.current_pil = new_image
#             self._update_label(new_image)
#             return
#
#         # converter a imagem antiga também
#         old_image = self.current_pil.convert("RGBA")
#
#         self._fade_transition(old_image, new_image)
#     # ------------------------------
#     # ANIMAÇÃO FADE
#     # ------------------------------
#     def _fade_transition(self, old_img, new_img, step=0):
#         alpha = step / 10
#         blended = Image.blend(old_img, new_img, alpha)
#         self._update_label(blended)
#         if step < 10:
#             self.master.after(30, lambda: self._fade_transition(old_img, new_img, step + 1))
#         else:
#             self.current_pil = new_img
#
#     # ------------------------------
#     # UPDATE LABEL
#     # ------------------------------
#     def _update_label(self, pil_image):
#
#         self.my_image = ctk.CTkImage(
#             light_image=pil_image,
#             size=(890, 850)
#         )
#
#         self.image_label.configure(image=self.my_image)
#

import customtkinter as ctk
from PIL import Image


class ImageView:

    def __init__(self, master):

        self.master = master
        self.master.pack_propagate(False)

        self.image_label = ctk.CTkLabel(self.master, text="")
        # self.image_label.pack(fill="both", expand=True)
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

        # imagem original
        self.original_pil = None
        self.current_pil = None

        # zoom
        self.zoom_factor = 1
        self.zoom_step = 0.01
        self.min_zoom = 0.02
        self.max_zoom = 5.0

        # posição da imagem
        self.offset_x = 0
        self.offset_y = 0

        # posição do rato
        self.start_x = 0
        self.start_y = 0

        # eventos do rato
        self.image_label.bind("<MouseWheel>", self._zoom)   # Windows
        self.image_label.bind("<Button-4>", self._zoom)     # Linux scroll up
        self.image_label.bind("<Button-5>", self._zoom)     # Linux scroll down

        # PAN EVENTS
        self.image_label.bind("<ButtonPress-1>", self._start_pan)
        self.image_label.bind("<B1-Motion>", self._pan_move)

        self.setImage("assets/logo.png")

    # ------------------------------
    # SET IMAGE
    # ------------------------------
    def setImage(self, path):

        self.original_pil = Image.open(path).convert("RGBA")
        self.zoom_factor = 0.2

        self._render_zoom()

    # ------------------------------
    # ZOOM EVENT
    # ------------------------------
    def _zoom(self, event):

        if event.delta > 0 or event.num == 4:
            self.zoom_factor += self.zoom_step
        else:
            self.zoom_factor -= self.zoom_step

        # limitar zoom
        self.zoom_factor = max(self.min_zoom,
                               min(self.max_zoom, self.zoom_factor))

        self._render_zoom()

    # ------------------------------
    # RENDER IMAGE COM ZOOM
    # ------------------------------
    # def _render_zoom(self):
    #
    #     if self.original_pil is None:
    #         return
    #
    #     w, h = self.original_pil.size
    #
    #     new_size = (
    #         int(w * self.zoom_factor),
    #         int(h * self.zoom_factor)
    #     )
    #
    #     self.current_pil = self.original_pil.resize(
    #         new_size,
    #         Image.LANCZOS
    #     )
    #
    #     self._update_label(self.current_pil)

    def _render_zoom(self):

        if self.original_pil is None:
            return

        w, h = self.original_pil.size

        new_size = (
            int(w * self.zoom_factor),
            int(h * self.zoom_factor)
        )

        self.current_pil = self.original_pil.resize(
            new_size,
            Image.LANCZOS
        )

        self._update_label(self.current_pil)

        # manter posição atual
        self.image_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            x=self.offset_x,
            y=self.offset_y
        )


    # ------------------------------
    # UPDATE LABEL
    # ------------------------------
    def _update_label(self, pil_image):

        self.my_image = ctk.CTkImage(
            light_image=pil_image,
            size=pil_image.size
        )

        self.image_label.configure(image=self.my_image)

    def _start_pan(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root

    def _pan_move(self, event):

        dx = event.x_root - self.start_x
        dy = event.y_root - self.start_y

        self.offset_x += dx
        self.offset_y += dy

        self.start_x = event.x_root
        self.start_y = event.y_root

        self.image_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            x=self.offset_x,
            y=self.offset_y
        )