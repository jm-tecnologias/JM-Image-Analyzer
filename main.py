
import customtkinter as ctk
from model.Tabs import Tabs
from model.Pallet import Pallet
from model.Properties import Properties

from model.utils import get_base_path

BASE_DIR = get_base_path()

class App:
    def __init__(self):
        # ICON
        self.dataSource = {}
        self.selected_item = None
        self.imageView = None

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        self.root = ctk.CTk()
        self.root.title('JM-Image Analyzer')
        self.root.iconbitmap(BASE_DIR / "assets/icon.ico")

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

        self.tabs.setMiniMap(self.pallet.getMiniMap())

    def onFolderSelected(self, path):
        self.tabs.carouselButtonLoader(path)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
