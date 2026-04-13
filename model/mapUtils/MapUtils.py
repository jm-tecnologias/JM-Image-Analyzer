class MapUtils:


    def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):

        # --- Converter se vier em DMS (tuple) ---
        if isinstance(lat, tuple):
            lat = self.converter_gps(lat)

        if isinstance(lon, tuple):
            lon = self.converter_gps(lon)

        # --- Aplicar hemisfério ---
        if lat_ref == "S":
            lat = -abs(lat)

        if lon_ref == "W":
            lon = -abs(lon)

        print("FINAL S:", lat, lon)

        self.map_widget.set_position(lat, lon)
        self.map_widget.set_marker(lat, lon)

    def converter_gps(self, valor, ref=None):

        graus, minutos, segundos = valor

        decimal = graus + (minutos / 60.0) + (segundos / 3600.0)

        if ref in ["S", "W"]:
            decimal = -decimal

        return decimal