from PIL.ExifTags import GPSTAGS

def converter_gps(valor):
    """Converte coordenadas GPS para decimal"""
    graus, minutos, segundos = valor
    return graus + (minutos / 60.0) + (segundos / 3600.0)


def extrair_gps(info_gps):
    """Extrai e converte dados GPS"""
    gps_data = {}

    for key in info_gps:
        nome = GPSTAGS.get(key, key)
        gps_data[nome] = info_gps[key]

    try:
        lat = converter_gps(gps_data["GPSLatitude"])
        if gps_data["GPSLatitudeRef"] == "S":
            lat = -lat

        lon = converter_gps(gps_data["GPSLongitude"])
        if gps_data["GPSLongitudeRef"] == "W":
            lon = -lon

        alt = gps_data.get("GPSAltitude", None)

        return {
            "latitude": lat,
            "longitude": lon,
            "altitude": alt
        }

    except KeyError:
        return {
            "latitude": None,
            "longitude": None,
            "altitude": None
        }