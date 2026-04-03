from PIL import Image
from PIL.ExifTags import TAGS
from utils.Utils import extrair_gps


class ImageAnalyzer:

    def __init__(self, caminho):
        self.caminho = caminho
        self.imagem = Image.open(caminho)
        self.exif_data = self.imagem._getexif()
        self.dados = {}

    def extract_metadata(self):
        """Extrai metadados relevantes"""
        if not self.exif_data:
            return None

        gps_info = None

        for tag_id, valor in self.exif_data.items():
            tag = TAGS.get(tag_id, tag_id)

            if tag in [
                "DateTimeOriginal",
                "DateTime",
                "FocalLength",
                "FNumber",
                "ExposureTime",
                "ISOSpeedRatings"
            ]:
                self.dados[tag] = valor

            elif tag == "GPSInfo":
                gps_info = valor

        if gps_info:
            gps = extrair_gps(gps_info)
            self.dados.update(gps)

        return self.dados

    def get_location(self):
        """Retorna apenas localização"""
        return {
            "latitude": self.dados.get("latitude"),
            "longitude": self.dados.get("longitude"),
            "altitude": self.dados.get("altitude")
        }

    def get_camera_info(self):
        """Retorna informações detalhadas da câmera"""

        return {
            # 📷 Identificação
            "make": self.dados.get("Make"),
            "model": self.dados.get("Model"),
            "software": self.dados.get("Software"),

            # 🔍 Óptica
            "focal_length": self.dados.get("FocalLength"),
            "focal_length_35mm": self.dados.get("FocalLengthIn35mmFilm"),
            "max_aperture": self.dados.get("MaxApertureValue"),

            # 📸 Exposição
            "f_number": self.dados.get("FNumber"),
            "exposure_time": self.dados.get("ExposureTime"),
            "exposure_program": self.dados.get("ExposureProgram"),
            "exposure_mode": self.dados.get("ExposureMode"),
            "exposure_bias": self.dados.get("ExposureBiasValue"),

            # 🌡️ Sensibilidade
            "iso": self.dados.get("ISOSpeedRatings"),
            "gain_control": self.dados.get("GainControl"),

            # 💡 Luz
            "white_balance": self.dados.get("WhiteBalance"),
            "light_source": self.dados.get("LightSource"),
            "flash": self.dados.get("Flash"),

            # 🎨 Qualidade da imagem
            "contrast": self.dados.get("Contrast"),
            "saturation": self.dados.get("Saturation"),
            "sharpness": self.dados.get("Sharpness"),

            # 📏 Distância e zoom
            "subject_distance": self.dados.get("SubjectDistance"),
            "digital_zoom": self.dados.get("DigitalZoomRatio"),

            # 🎥 Captura
            "scene_capture_type": self.dados.get("SceneCaptureType"),
            "metering_mode": self.dados.get("MeteringMode")
        }

    def get_datetime(self):
        """Retorna data/hora"""
        return self.dados.get("DateTimeOriginal") or self.dados.get("DateTime")

    def summary(self):
        """Resumo completo formatado"""
        if not self.dados:
            self.extract_metadata()

        return {
            "datetime": self.get_datetime(),
            "location": self.get_location()
            # "camera": self.get_camera_info()
        }

    @classmethod
    def ImageAnalyzer(cls, img):
        pass