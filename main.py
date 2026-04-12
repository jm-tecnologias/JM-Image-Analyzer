import customtkinter as ctk
from model.Tabs import Tabs
from model.Pallet import Pallet
from model.Properties import Properties

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


        # criar primeiro
        self.tabs = Tabs(self.main_frame)

        # depois usar
        self.pallet = Pallet(
            self.main_frame,
            self.tabs.centerFrame,
            on_image_selected=self.onImageSelected
        )

        self.properties = Properties(self.main_frame)

    def onImageSelected(self, path):

        self.tabs.getImageView().setImage(path)

        self.properties.updateImageProperties(path)

        gps = self.properties.metaDataSouce.get("GPSInfo")

        if gps:
            lat_ref = gps.get(1)
            lat = gps.get(2)
            lon_ref = gps.get(3)
            lon = gps.get(4)

            self.tabs.getSatelliteMap().updatePosition(
                lat, lon, lat_ref, lon_ref
            )

            self.tabs.getNormalMap().updatePosition(
                lat, lon, lat_ref, lon_ref
            )




    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()




