
import os
import customtkinter as ctk
from PIL import Image
from utils.ImageAnalyzer import ImageAnalyzer as ia
from PIL import Image, ImageDraw

class CarouselWidgets:

    def __init__(self, on_change=None):

        self.index = 0
        self.pil_images = []
        self.image_paths = []
        self.size = (850, 550)
        self.details = {}

        # callback vindo da App
        self.on_change = on_change

    def createCarousel(self, frame, paths, size=(850, 550)):
        self.size = size
        self.index = 0
        self.pil_images = []

        # Layout responsivo
        frame.columnconfigure(0, weight=0)
        frame.rowconfigure(0, weight=0)

        # Carregar imagens
        for p in paths:
            if os.path.exists(p):
                img = Image.open(p).convert("RGBA").resize(self.size)
                self.pil_images.append(img)
                self.image_paths.append(p)
            else:
                print(f"⚠️ Imagem não encontrada: {p}")

        if not self.pil_images:
            print("❌ Nenhuma imagem válida encontrada!")
            return

        # Label principal (imagem)
        self.label = ctk.CTkLabel(frame, text="", width=850, height=550)
        self.label.grid(row=0, column=0, pady=10, padx=10)

        # Mostrar primeira imagem
        self.update_image()

        # 🔲 Overlay inferior (estilo moderno)
        self.overlay = ctk.CTkFrame(
            self.label,
            fg_color="#000000",  # semi-transparente
            corner_radius=5
        )
        self.overlay.place(relx=0.5, rely=0.9, anchor="center")

        # ⬅️ Botão anterior
        self.btn_prev = ctk.CTkButton(
            self.overlay,
            text="<",
            width=40,
            command=self.prev
        )
        self.btn_prev.pack(side="left", padx=5, pady=5)

        # 🔢 Contador
        self.counter = ctk.CTkLabel(
            self.overlay,
            text="",
            font=("Arial", 14)
        )
        self.counter.pack(side="left", padx=10)

        # ➡️ Botão próximo
        self.btn_next = ctk.CTkButton(
            self.overlay,
            text=">",
            width=40,
            command=self.next
        )
        self.btn_next.pack(side="left", padx=5, pady=5)

        # Atualizar contador inicial
        self.update_counter()

        return self.label

    def round_corners(self, img, radius=20):
        """Arredonda os cantos da imagem (Pillow)"""
        # img deve estar em RGBA
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=radius, fill=255)
        img.putalpha(mask)
        return img

    # 🔄 Atualiza imagem exibida
    def update_image(self):
        img = self.pil_images[self.index]

        # Aplicar border-radius
        img_rounded = self.round_corners(img.copy(), radius=30)

        self.tk_img = ctk.CTkImage(img_rounded, size=self.size)
        self.label.configure(image=self.tk_img)


    # 🔢 Atualiza contador
    def update_counter(self):

        self.counter.configure(
            text=f"{self.index + 1} / {len(self.pil_images)}"
        )

        path = self.image_paths[self.index]

        analyzer = ia(path)
        analyzer.extract_metadata()

        self.details = {
            'locationDetails': analyzer.get_location(),
            'cameraDetails': analyzer.get_camera_info()
        }

        # ⭐ DISPARAR EVENTO PARA APP
        if self.on_change:
            self.on_change(self.details)


    # 🔄 Animação suave (fade)
    def animate_transition(self, from_img, to_img, steps=10, delay=30):
        # Aplicar borda arredondada antes
        from_img_rounded = self.round_corners(from_img.copy(), radius=30)
        to_img_rounded = self.round_corners(to_img.copy(), radius=30)

        def step(i):
            if i > steps:
                return
            alpha = i / steps
            blended = Image.blend(from_img_rounded, to_img_rounded, alpha)
            tk_img = ctk.CTkImage(blended, size=self.size)
            self.label.configure(image=tk_img)
            self.label.image = tk_img
            self.label.after(delay, step, i + 1)

        step(0)

    # ➡️ Próxima imagem
    def next(self):
        if not self.pil_images:
            return

        old_index = self.index
        self.index = (self.index + 1) % len(self.pil_images)

        self.animate_transition(
            self.pil_images[old_index],
            self.pil_images[self.index]
        )

        self.update_counter()

    # ⬅️ Imagem anterior
    def prev(self):
        if not self.pil_images:
            return

        old_index = self.index
        self.index = (self.index - 1) % len(self.pil_images)

        self.animate_transition(
            self.pil_images[old_index],
            self.pil_images[self.index]
        )

        self.update_counter()