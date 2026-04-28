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
        self.zoom_step = 0.02
        self.min_zoom = 0.1
        self.max_zoom = 10.0

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

    def _render_zoom(self):
        # self.zoom_factor =1

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
#         self.image_label = ctk.CTkLabel(master, text="")
#         self.image_label.place(relx=0.5, rely=0.5, anchor="center")
#
#         # -----------------------------
#         # IMAGE
#         # -----------------------------
#         self.original_pil = None
#         self.current_pil = None
#
#         # -----------------------------
#         # ZOOM SYSTEM (PRO)
#         # -----------------------------
#         self.zoom_factor = 1.0
#         self.target_zoom = 1.0
#         self.zoom_step = 1.15
#
#         self.min_zoom = 0.05
#         self.max_zoom = 20.0
#
#         self.zoom_animation_running = False
#
#         # -----------------------------
#         # POSITION
#         # -----------------------------
#         self.offset_x = 0
#         self.offset_y = 0
#
#         # mouse anchor (zoom focus)
#         self.zoom_anchor_x = 0
#         self.zoom_anchor_y = 0
#
#         # pan
#         self.start_x = 0
#         self.start_y = 0
#
#         # -----------------------------
#         # EVENTS
#         # -----------------------------
#         self.image_label.bind("<MouseWheel>", self._zoom)
#         self.image_label.bind("<Button-4>", self._zoom)
#         self.image_label.bind("<Button-5>", self._zoom)
#
#         self.image_label.bind("<ButtonPress-1>", self._start_pan)
#         self.image_label.bind("<B1-Motion>", self._pan_move)
#
#         self.setImage("assets/logo.png")
#
#     # =====================================================
#     # SET IMAGE
#     # =====================================================
#     def setImage(self, path):
#
#         self.original_pil = Image.open(path).convert("RGBA")
#
#         self.zoom_factor = 0.2
#         self.target_zoom = self.zoom_factor
#
#         self.offset_x = 0
#         self.offset_y = 0
#
#         self._render()
#
#     # =====================================================
#     # ZOOM EVENT (CURSOR FOCUSED)
#     # =====================================================
#     def _zoom(self, event):
#
#         # posição do cursor RELATIVA ao widget
#         self.zoom_anchor_x = event.x
#         self.zoom_anchor_y = event.y
#
#         old_zoom = self.target_zoom
#
#         if event.delta > 0 or event.num == 4:
#             self.target_zoom *= self.zoom_step
#         else:
#             self.target_zoom /= self.zoom_step
#
#         self.target_zoom = max(
#             self.min_zoom,
#             min(self.max_zoom, self.target_zoom)
#         )
#
#         # -------- MAGIC FORMULA --------
#         scale = self.target_zoom / old_zoom
#
#         self.offset_x = (
#             self.zoom_anchor_x -
#             scale * (self.zoom_anchor_x - self.offset_x)
#         )
#
#         self.offset_y = (
#             self.zoom_anchor_y -
#             scale * (self.zoom_anchor_y - self.offset_y)
#         )
#
#         if not self.zoom_animation_running:
#             self._animate_zoom()
#
#     # =====================================================
#     # SMOOTH ZOOM ANIMATION
#     # =====================================================
#     def _animate_zoom(self):
#
#         self.zoom_animation_running = True
#
#         diff = self.target_zoom - self.zoom_factor
#         self.zoom_factor += diff * 0.18  # easing
#
#         self._render()
#
#         if abs(diff) > 0.001:
#             self.master.after(16, self._animate_zoom)
#         else:
#             self.zoom_factor = self.target_zoom
#             self.zoom_animation_running = False
#
#     # =====================================================
#     # RENDER
#     # =====================================================
#     def _render(self):
#
#         if not self.original_pil:
#             return
#
#         w, h = self.original_pil.size
#
#         new_size = (
#             int(w * self.zoom_factor),
#             int(h * self.zoom_factor)
#         )
#
#         self.current_pil = self.original_pil.resize(
#             new_size,
#             Image.LANCZOS
#         )
#
#         self._update_label(self.current_pil)
#
#         self.image_label.place(
#             relx=0.5,
#             rely=0.5,
#             anchor="center",
#             x=self.offset_x,
#             y=self.offset_y
#         )
#
#     # =====================================================
#     # UPDATE IMAGE
#     # =====================================================
#     def _update_label(self, pil_image):
#
#         self.tk_image = ctk.CTkImage(
#             light_image=pil_image,
#             size=pil_image.size
#         )
#
#         self.image_label.configure(image=self.tk_image)
#
#     # =====================================================
#     # PAN START
#     # =====================================================
#     def _start_pan(self, event):
#
#         self.start_x = event.x_root
#         self.start_y = event.y_root
#
#     # =====================================================
#     # PAN MOVE
#     # =====================================================
#     def _pan_move(self, event):
#
#         dx = event.x_root - self.start_x
#         dy = event.y_root - self.start_y
#
#         self.offset_x += dx
#         self.offset_y += dy
#
#         self.start_x = event.x_root
#         self.start_y = event.y_root
#
#         self.image_label.place(
#             relx=0.5,
#             rely=0.5,
#             anchor="center",
#             x=self.offset_x,
#             y=self.offset_y
#         )