from model.utils import get_base_path

BASE_DIR = get_base_path()


from tkintermapview import TkinterMapView
from PIL import ImageGrab
from pathlib import Path

# Pasta Documents do utilizador
DOCUMENTS_DIR = Path.home() / "Documents"

# Pasta da aplicação
APP_DIR = DOCUMENTS_DIR / "JM-Image-Analyzer"
APP_DIR.mkdir(parents=True, exist_ok=True)

# Subpasta File Explore
SNAP_DIR = APP_DIR / "temp_snap"
SNAP_DIR.mkdir(parents=True, exist_ok=True)

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

        self._last_bbox = (0, 0, 314, 198)

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

        self.marker = self.map_widget.set_marker(lat, lon, marker_color_circle="#141414",
    marker_color_outside="#38c20e")

        # 🔥 marca mapa como pronto após render inicial
        # self.map_widget.after(1500, self._mark_map_ready)

    # --------------------------------------------------

    def _mark_map_ready(self):
        self.map_ready = True
        print("✔ Mapa pronto")

        self._auto_capture_fixed_area()

    # --------------------------------------------------

    def updatePosition(self, lat, lon):
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
        img.save(SNAP_DIR/"mapa.png")

        print("📸 Captura realizada:", bbox)