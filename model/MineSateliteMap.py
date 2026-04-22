# from tkintermapview import TkinterMapView
from pathlib import Path
# import tkinter as tk
# from PIL import ImageGrab
#
BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# class MiniSateliteMap:
#
#     def __init__(self, master,
#                  LAT_INICIAL=-25.9692,
#                  LON_INICIAL=32.5732):
#
#         self.master = master
#         self.master.pack_propagate(False)
#
#         self.map_widget = None
#         self.marker = None
#
#         # -----------------------------
#         # ATRIBUTOS DA MÁSCARA
#         # -----------------------------
#         self.mask_canvas = None
#         self.rect = None
#
#         self.start_x = None
#         self.start_y = None
#
#         self._last_bbox = None
#
#         # -----------------------------
#         self._create_map(master, LAT_INICIAL, LON_INICIAL)
#
#     # --------------------------------------------------
#     # MAP SETUP
#     # --------------------------------------------------
#
#     def _create_map(self, frame, lat, lon):
#
#         self.map_widget = TkinterMapView(frame, corner_radius=0)
#         self.map_widget.pack(fill="both", expand=True)
#
#         self.map_widget.set_tile_server(
#             "https://mt0.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
#         )
#
#         self.map_widget.set_position(lat, lon)
#         self.map_widget.set_zoom(15)
#
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#         # --------------------------------------------------
#         # SELECTION START
#         # --------------------------------------------------
#
#     def _auto_capture_fixed_area(self):
#
#         x1, y1, x2, y2 = 0, 0, 364, 198
#
#         root_x = self.map_widget.winfo_rootx()
#         root_y = self.map_widget.winfo_rooty()
#
#         bbox = (
#             root_x + x1,
#             root_y + y1,
#             root_x + x2,
#             root_y + y2
#         )
#
#         img = ImageGrab.grab(bbox=bbox)
#         img.save("mini_map_capture.png")
#
#         print("Captura automática feita:", bbox)
#
#
#     # --------------------------------------------------
#     # UPDATE POSITION
#     # --------------------------------------------------
#
#     def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):
#
#         if isinstance(lat, tuple):
#             lat = self._converter_gps(lat)
#
#         if isinstance(lon, tuple):
#             lon = self._converter_gps(lon)
#
#         if lat_ref == "S":
#             lat = -abs(lat)
#
#         if lon_ref == "W":
#             lon = -abs(lon)
#
#         print("FINAL:", lat, lon)
#
#         self.map_widget.set_position(lat, lon)
#
#         if self.marker:
#             self.marker.delete()
#
#         self.marker = self.map_widget.set_marker(lat, lon)
#         self.map_widget.after(10000, self._auto_capture_fixed_area)
#
#     # --------------------------------------------------
#     # GPS CONVERTER
#     # --------------------------------------------------
#
#     def _converter_gps(self, valor):
#
#         graus, minutos, segundos = valor
#         return graus + minutos / 60 + segundos / 3600

from tkintermapview import TkinterMapView
from PIL import ImageGrab


# class MiniSateliteMap:
#
#     def __init__(self, master,
#                  LAT_INICIAL=-25.9692,
#                  LON_INICIAL=32.5732):
#
#         self.master = master
#         self.master.pack_propagate(False)
#
#         self.map_widget = None
#         self.marker = None
#
#         # estado do mapa
#         self.map_loaded = False
#
#         # -----------------------------
#         # ATRIBUTOS DA CAPTURA
#         # -----------------------------
#         self._last_bbox = (0, 0, 364, 198)
#
#         # cria mapa
#         self._create_map(master, LAT_INICIAL, LON_INICIAL)
#
#     # --------------------------------------------------
#     # MAP SETUP
#     # --------------------------------------------------
#
#     def _create_map(self, frame, lat, lon):
#
#         self.map_widget = TkinterMapView(frame, corner_radius=0)
#         self.map_widget.pack(fill="both", expand=True)
#
#         self.map_widget.set_tile_server(
#             # "https://mt0.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
#             # "https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
#             # "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
#         )
#
#         self.map_widget.set_position(lat, lon)
#         self.map_widget.set_zoom(15)
#
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#         # espera inicialização real do mapa
#         # self.map_widget.after(2000, self._mark_map_ready)
#
#     # --------------------------------------------------
#     # UPDATE POSITION
#     # --------------------------------------------------
#
#     def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):
#
#         if isinstance(lat, tuple):
#             lat = self._converter_gps(lat)
#
#         if isinstance(lon, tuple):
#             lon = self._converter_gps(lon)
#
#         if lat_ref == "S":
#             lat = -abs(lat)
#
#         if lon_ref == "W":
#             lon = -abs(lon)
#
#         print("FINAL:", lat, lon)
#
#         self.map_widget.set_position(lat, lon)
#
#         if self.marker:
#             self.marker.delete()
#
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#         # opcional: re-capturar após mover mapa
#         if self.marker:
#             self.map_widget.after(1000, self._auto_capture_fixed_area)
#
#     # --------------------------------------------------
#     # GPS CONVERTER
#     # --------------------------------------------------
#
#     def _converter_gps(self, valor):
#         graus, minutos, segundos = valor
#         return graus + minutos / 60 + segundos / 3600

from tkintermapview import TkinterMapView
from PIL import ImageGrab


class MiniSateliteMap:

    def __init__(self, master,
                 LAT_INICIAL=-25.9692,
                 LON_INICIAL=32.5732):

        self.master = master
        self.master.pack_propagate(False)

        self.map_widget = None
        self.marker = None

        self._job = None
        self.map_ready = False

        self._last_bbox = (0, 0, 364, 198)

        self._create_map(master, LAT_INICIAL, LON_INICIAL)

    # --------------------------------------------------

    def _create_map(self, frame, lat, lon):

        self.map_widget = TkinterMapView(frame, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)

        # 🔥 MAPA LEVE
        self.map_widget.set_tile_server(
            "https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
        )

        self.map_widget.set_position(lat, lon)
        self.map_widget.set_zoom(12)

        self.marker = self.map_widget.set_marker(lat, lon)

        # 🔥 marca mapa como pronto após render inicial
        # self.map_widget.after(1500, self._mark_map_ready)

    # --------------------------------------------------

    def _mark_map_ready(self):
        self.map_ready = True
        print("✔ Mapa pronto")

        self._auto_capture_fixed_area()

    # --------------------------------------------------

    def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):

        if isinstance(lat, tuple):
            lat = self._converter_gps(lat)

        if isinstance(lon, tuple):
            lon = self._converter_gps(lon)

        if lat_ref == "S":
            lat = -abs(lat)

        if lon_ref == "W":
            lon = -abs(lon)

        # 🔥 debounce
        if self._job:
            self.map_widget.after_cancel(self._job)

        self._job = self.map_widget.after(
            300,
            lambda: self._update_map(lat, lon)
        )

    # --------------------------------------------------

    def _update_map(self, lat, lon):

        self.map_widget.set_position(lat, lon)

        # 🔥 marker leve (sem recriar)
        if self.marker:
            self.marker.set_position(lat, lon)
        else:
            self.marker = self.map_widget.set_marker(lat, lon)
        self.map_widget.after(3000, self._mark_map_ready)


    # --------------------------------------------------

    def _auto_capture_fixed_area(self):

        if not self.map_ready:
            return

        x1, y1, x2, y2 = self._last_bbox

        root_x = self.map_widget.winfo_rootx()
        root_y = self.map_widget.winfo_rooty()

        bbox = (
            root_x + x1,
            root_y + y1,
            root_x + x2,
            root_y + y2
        )

        img = ImageGrab.grab(bbox=bbox)
        img.save(BASE_DIR/"assets/snap/mapa.png")

        print("📸 Captura realizada:", bbox)

    # --------------------------------------------------

    def _converter_gps(self, valor):
        graus, minutos, segundos = valor
        return graus + minutos / 60 + segundos / 3600