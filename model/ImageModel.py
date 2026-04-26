# import os
#
# from PIL import Image
# from PIL.ExifTags import TAGS
# from pydantic import BaseModel, Field, ConfigDict
#
#
# class GPSInfo(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     latitude: float = Field(alias="Latitude")
#     longitude: float = Field(alias="Longitude")
#     altitude: float = Field(alias="Altitude")
#
#
# class ImageModel(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     make: str = Field(alias="Make")
#     model: str = Field(alias="Model")
#     software: str = Field(alias="Software")
#
#     gpsInfo: GPSInfo = Field(alias="GPSInfo")
#
#     ExposureTime: float
#     ShutterSpeedValue: float
#     ISOSpeedRatings: float
#     FocalLength: float
#     FocalLengthIn35mmFilm: float
#     DateTimeOriginal: str
#     DateTimeDigitized: str
#     OffsetTime: str
#     absolutePath: str
#     fileName: str
#
#     def getData(self, path):
#
#         img = Image.open(path)
#         metadata = {}
#         gps_model = None
#
#         exifData = img._getexif()
#
#         if exifData:
#             for tag_id, value in exifData.items():
#                 tag = TAGS.get(tag_id, tag_id)
#
#                 # if tag == "GPSInfo":
#                 #     gps_model = cls._extract_gps(value)
#                 # else:
#                 metadata[tag] = value
#
#         # cria e retorna o objeto já preenchido
#         return metadata
#
#
# img_model = ImageModel()
# img_model = ImageModel(**dados)
# print(img_model.getData('photo.png'))

import os
from PIL import Image
from PIL.ExifTags import TAGS
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

def converter_gps(valor, ref=None):
    graus, minutos, segundos = valor

    decimal = graus + (minutos / 60.0) + (segundos / 3600.0)

    if ref in ["S", "W"]:
        decimal = -decimal

    return decimal
def parse_gps_info(gps_raw: dict):
    if not gps_raw:
        return None

    lat_ref = gps_raw.get(1)
    lat = gps_raw.get(2)
    lon_ref = gps_raw.get(3)
    lon = gps_raw.get(4)

    lat = converter_gps(lat)
    lon = converter_gps(lon)


    # Hemisfério
    if lat_ref == "S":
        lat = -abs(lat)

    if lon_ref == "W":
        lon = -abs(lon)


    alt = gps_raw.get(6)
    altitude = alt

    return {
        "latitude": lat,
        "longitude": lon,
        "altitude": altitude
    }

class GPSInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    latitude: Optional[float] = Field(None, alias="Latitude")
    longitude: Optional[float] = Field(None, alias="Longitude")
    altitude: Optional[float] = Field(None, alias="Altitude")


class ImageModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    make: Optional[str] = Field(None, alias="Make")
    model: Optional[str] = Field(None, alias="Model")
    software: Optional[str] = Field(None, alias="Software")

    gpsInfo: Optional[GPSInfo] = Field(None, alias="GPSInfo")

    ExposureTime: Optional[float] = None
    ShutterSpeedValue: Optional[float] = None
    ISOSpeedRatings: Optional[float] = None
    FocalLength: Optional[float] = None
    FocalLengthIn35mmFilm: Optional[float] = None

    DateTimeOriginal: Optional[str] = None
    DateTimeDigitized: Optional[str] = None
    OffsetTime: Optional[str] = None

    absolutePath: str
    fileName: str

    # ✅ FACTORY METHOD
    @classmethod
    def from_image(self, path):

        img = Image.open(path)
        metadata = {}

        exifData = img._getexif()

        if exifData:
            for tag_id, value in exifData.items():
                tag = TAGS.get(tag_id, tag_id)

                if tag == "GPSInfo":
                    gps_data = parse_gps_info(value)
                    if gps_data:
                        metadata["GPSInfo"] = {
                            "Latitude": gps_data["latitude"],
                            "Longitude": gps_data["longitude"],
                            "Altitude": gps_data["altitude"],
                        }
                else:
                    metadata[tag] = value

        metadata["absolutePath"] = os.path.abspath(path)
        metadata["fileName"] = os.path.basename(path)

        return metadata


# img_model = ImageModel.from_image("photo.jpg")
#
# print(img_model)
