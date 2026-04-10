import customtkinter as ctk
from model.ImageView import ImageView
from model.Pallet import Pallet
from model.Properties import Properties
from model.SateliteMap import SateliteMap
from model.NormalMap import NormalMap

class App:
    def __init__(self):
        self.dataSource = {}
        self.selected_item = None
        self.imageView = None

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        self.root = ctk.CTk()
        self.root.title('JM-Image Analyzer')

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


        # Center
        self.centerFrame = ctk.CTkFrame(self.main_frame)
        self.centerFrame.grid(row=0, column=1, sticky='nswe')

        self.centerFrame.columnconfigure(0, weight=1)
        self.centerFrame.rowconfigure(1, weight=4)
        self.centerFrame.rowconfigure(2, weight=0)

        # ---------- Title ----------
        self.titleLabCenterFrame = ctk.CTkLabel(
            self.centerFrame,
            text='Image Preview',
            font=('Berlin Sans FB Demi', 32)
        )
        self.titleLabCenterFrame.grid(row=0, column=0, sticky='we', pady=(40, 10))

        # Chama TODA a interface da classe Properties
        self.properties = Properties(self.main_frame)
        self.createTabs()
        self.pallet = Pallet(
            self.main_frame,
            self.centerFrame,
            on_image_selected=self.onImageSelected
        )

    def onImageSelected(self, path):
        # 1️⃣ Preview
        self.imageView.setImage(path)

        # 2️⃣ Properties
        self.properties.updateImageProperties(path)


    def createTabs(self):
        # Criar TabView dentro do right_frame
        self.tabview = ctk.CTkTabview(self.centerFrame)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        # Criar abas
        self.tab_carousel = self.tabview.add("Carousel")
        self.tab_satelite = self.tabview.add("Satelite Map")
        self.tab_normal = self.tabview.add("Normal Map")

        # Carregar conteúdo das abas

        # ⭐ GUARDA A INSTÂNCIA
        self.imageView = ImageView(self.tab_carousel)
        SateliteMap(self.tab_satelite)
        NormalMap(self.tab_normal)



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()




