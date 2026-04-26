from tkintermapview import TkinterMapView

class NormalMap:

    def __init__(self, master, LAT_INICIAL=-25.9692, LON_INICIAL=32.5732):
        self.master = master
        self.map_widget = None
        self.master.pack_propagate(False)
        self.marker = None

        self.openStreetMapWidgets(master, LAT_INICIAL, LON_INICIAL)

    def openStreetMapWidgets(self, frame, LAT_INICIAL, LON_INICIAL):
        self.map_widget = TkinterMapView(frame, corner_radius=0)
        self.map_widget.pack(fill='both', expand=True)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)



        # 🌍 Usar mapa normal (OpenStreetMap)
        self.map_widget.set_tile_server(
            "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
        )

        self.map_widget.set_position(LAT_INICIAL, LON_INICIAL)
        self.map_widget.set_zoom(10)

        # 📌 Marcador
        # self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
        self.marker = self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL, marker_color_circle="#141414", marker_color_outside="#38c20e")


        return self.map_widget

    def updatePosition(self, lat, lon):
        # mover mapa
        self.map_widget.set_position(lat, lon)

        # remover marcador antigo
        if self.marker:
            self.marker.delete()

        # criar novo marcador
        self.marker = self.map_widget.set_marker(lat, lon)

    # def converter_gps(self, valor, ref=None):
    #
    #     graus, minutos, segundos = valor
    #
    #     decimal = graus + (minutos / 60.0) + (segundos / 3600.0)
    #
    #     if ref in ["S", "W"]:
    #         decimal = -decimal
    #
    #     return decimal
