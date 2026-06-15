import customtkinter as ctk
from PIL import Image, ImageTk

from model.Tabs import Tabs
from model.Pallet import Pallet
from model.Properties import Properties

from model.utils import get_base_path

BASE_DIR = get_base_path()

# "#C9AB6A" dourado
# "#1B2A63" azul

class App:
    def __init__(self):
        # ICON
        self.dataSource = {}
        self.selected_item = None
        self.imageView = None

        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        self.root = ctk.CTk()
        self.root.overrideredirect(True)
        # self.root.bind("<FocusIn>", self.on_focus)

        title_bar = ctk.CTkFrame(self.root, height=60, fg_color="#1B2A63")
        title_bar.pack(fill="x")

        # Frame esquerdo (logo + título)
        info_frame = ctk.CTkFrame(title_bar, fg_color="transparent")
        info_frame.pack(side="left")

        logo = ctk.CTkImage(
            light_image=Image.open(BASE_DIR / "assets/logotipo.png"),
            dark_image=Image.open(BASE_DIR / "assets/logotipo.png"),
            size=(72, 64)
        )

        # Logo
        logo_label = ctk.CTkLabel(
            info_frame,
            text="",
            image=logo
        )
        logo_label.pack(padx=10)

        self.is_maximized = False
        self.normal_geometry = self.root.geometry()

        btn_fechar = ctk.CTkButton(
            title_bar,
            text="X",
            width=80,
            corner_radius=0,
            fg_color="transparent",
            font=("Montserrat SemiBold", 18, "bold"),
            command=self.root.destroy
        )

        btn_fechar.pack(
            side="right",
            fill="y"  # ocupa toda altura vertical
        )

        btn_max = ctk.CTkButton(
            title_bar,
            text="⬜",
            width=80,
            corner_radius=0,
            fg_color="transparent",
            font=("Montserrat SemiBold", 18, "bold"),
            command=self.toggle_maximize
        )
        btn_max.pack(
            side="right",
            fill="y"  # ocupa toda altura vertical
        )


        # Eventos de arrasto
        title_bar.bind("<Button-1>", self.iniciar_arrasto)
        title_bar.bind("<B1-Motion>", self.arrastar_janela)
        title_bar.bind("<Double-Button-1>", lambda e: self.toggle_maximize())

        # windows size
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f'{width}x{height}')

        # main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Column Configuration
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=5)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.properties = Properties(self.main_frame)
        self.tabs = Tabs(self.main_frame, self.properties)
        self.pallet = Pallet(self.main_frame, on_folder_selected=self.onFolderSelected)

        footer_bar = ctk.CTkFrame(self.root, height=40, fg_color="#1B2A63")
        footer_bar.pack(fill="x")

        # Alteração 1: Removemos o side="left" e usamos pack padrão para centralizar o frame no rodapé
        info_frame2 = ctk.CTkFrame(footer_bar, fg_color="transparent")
        info_frame2.pack(expand=True)  # expand=True faz o frame buscar o centro do espaço disponível

        logo2 = ctk.CTkImage(
            light_image=Image.open(BASE_DIR / "assets/logotipo2.png"),
            dark_image=Image.open(BASE_DIR / "assets/logotipo2.png"),
            size=(128, 32)
        )

        # Logo
        logo_label2 = ctk.CTkLabel(
            info_frame2,
            text="",
            image=logo2
        )
        # Alteração 2: side="left" coloca a logo na esquerda dentro do frame interno
        logo_label2.pack(side="left", padx=(10, 5))

        title2 = ctk.CTkLabel(
            info_frame2,
            text="JM Vision Intelligence System | Precision Imagery | Confident Decisions",
            text_color="#C9AB6A",
            font=("Montserrat SemiBold", 18, "bold")
        )
        # Alteração 3: side="left" coloca o texto logo após a logo, na mesma linha
        title2.pack(side="left", padx=(5, 10))

        self.tabs.setMiniMap(self.pallet.getMiniMap())

        # self.root.bind("<Map>", self.on_restore)

    def iniciar_arrasto(self, event):
        self.x = event.x
        self.y = event.y

    def arrastar_janela(self, event):
        pos_x = self.root.winfo_x() + event.x - self.x
        pos_y = self.root.winfo_y() + event.y - self.y

        self.root.geometry(f"+{pos_x}+{pos_y}")

    def toggle_maximize(self):
        if not self.is_maximized:
            self.normal_geometry = self.root.geometry()

            self.root.geometry(
                f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0"
            )

            self.is_maximized = True
        else:
            self.root.geometry(self.normal_geometry)
            self.is_maximized = False

    def minimize(self):
        self.root.overrideredirect(False)
        self.root.iconify()

    def restore(self):
        self.root.deiconify()
        self.root.after(10, lambda: self.root.overrideredirect(True))

    def onFolderSelected(self, path):
        self.properties.set_path_to_bacth(path)
        self.tabs.carouselButtonLoader(path)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
