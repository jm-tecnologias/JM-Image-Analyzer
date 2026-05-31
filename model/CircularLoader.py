# import customtkinter as ctk
# import threading
# import time
#
# app = ctk.CTk()
#
# progress = ctk.CTkProgressBar(app)
# progress.pack(pady=20)
# progress.start()
#
# def tarefa_pesada():
#     time.sleep(5)   # simula processamento
#     progress.stop()
#
# threading.Thread(target=tarefa_pesada).start()
#
# app.mainloop()


import customtkinter as ctk
import math


class CircularLoader(ctk.CTkCanvas):

    def __init__(self, master, size=120, dots=8, **kwargs):
        mode = ctk.get_appearance_mode()

        bg_color = "gray14" if mode == "Dark" else "gray92"

        super().__init__(
            master,
            width=size,
            height=size,
            bg=bg_color,
            highlightthickness=0
        )

        self.size = size
        self.dots = dots
        self.radius = size // 3
        self.angle = 0
        self.items = []

        self.create_dots()
        self.animate()

    # ----------------------------
    # Criar pontos do círculo
    # ----------------------------
    def create_dots(self):

        center = self.size // 2

        for i in range(self.dots):
            angle = 2 * math.pi * i / self.dots

            x = center + self.radius * math.cos(angle)
            y = center + self.radius * math.sin(angle)

            dot = self.create_oval(
                x - 5, y - 5, x + 5, y + 5,
                fill="#17b5c3",
                outline=""
            )

            self.items.append(dot)

    # ----------------------------
    # Animação
    # ----------------------------
    def animate(self):

        self.angle += 1

        for i, dot in enumerate(self.items):
            brightness = (i + self.angle) % self.dots
            alpha = 0.2 + (brightness / self.dots)

            color = f"#{int(23 * alpha):02x}{int(181 * alpha):02x}{int(195 * alpha):02x}"
            self.itemconfig(dot, fill=color)

        self.after(80, self.animate)


# ----------------------------
# APP
# ----------------------------
app = ctk.CTk()
app.geometry("400x300")

loader = CircularLoader(app)
loader.pack(expand=True)

app.mainloop()
