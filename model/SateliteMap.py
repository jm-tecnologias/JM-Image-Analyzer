from tkintermapview import TkinterMapView
import time
from PIL import ImageGrab


class SateliteMap:

    def __init__(self, master, LAT_INICIAL=-25.9692, LON_INICIAL=32.5732):
        self.master = master
        self.map_widget = None
        self.master.pack_propagate(False)
        self.marker = None

        self.seteliteMapWidgets(master, LAT_INICIAL, LON_INICIAL)

        # self.master.grid_columnconfigure(1, weight=1)

    def seteliteMapWidgets(self, frame, LAT_INICIAL, LON_INICIAL):
        self.map_widget = TkinterMapView(frame, corner_radius=0)
        # map_widget.pack(fill="both", expand=True)
        self.map_widget.pack(fill='both', expand=True)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)



        self.map_widget.set_tile_server(
            "https://mt0.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
        )

        self.map_widget.set_position(LAT_INICIAL, LON_INICIAL)
        self.map_widget.set_zoom(15)

        # Marcador
        # self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
        self.marker = self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)

        return self.map_widget

    def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):

        # Converter DMS
        if isinstance(lat, tuple):
            lat = self.converter_gps(lat)

        if isinstance(lon, tuple):
            lon = self.converter_gps(lon)

        # Hemisfério
        if lat_ref == "S":
            lat = -abs(lat)

        if lon_ref == "W":
            lon = -abs(lon)

        print("FINAL:", lat, lon)

        # mover mapa
        self.map_widget.set_position(lat, lon)

        # remover marcador antigo
        if self.marker:
            self.marker.delete()

        # criar novo marcador
        self.marker = self.map_widget.set_marker(lat, lon)
        if self.marker:
            # esperar mapa carregar
            self.master.after(10000, self.capture_map)

    def converter_gps(self, valor, ref=None):

        graus, minutos, segundos = valor

        decimal = graus + (minutos / 60.0) + (segundos / 3600.0)

        if ref in ["S", "W"]:
            decimal = -decimal

        return decimal

    def capture_map(self, file_name="mapa.png"):

        # garantir atualização gráfica
        self.master.update_idletasks()
        self.master.update()

        # posição absoluta do widget
        x = self.map_widget.winfo_rootx()
        y = self.map_widget.winfo_rooty()
        w = self.map_widget.winfo_width()
        h = self.map_widget.winfo_height()

        # pequena espera extra
        time.sleep(0.5)

        # screenshot
        image = ImageGrab.grab(bbox=(x, y, x + w, y + h))

        image.save(file_name)

        print("✅ Mapa capturado:", file_name)

        return file_name
