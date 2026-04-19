from pydantic import BaseModel, Field, ConfigDict


class GPSInfo(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    latitude: float = Field(alias="Latitude")
    longitude: float = Field(alias="Longitude")
    altitude: float = Field(alias="Altitude")


class ImageModel(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    make: str = Field(alias="Make")
    model: str = Field(alias="Model")
    software: str = Field(alias="Software")

    gpsInfo: GPSInfo = Field(alias="GPSInfo")

    ExposureTime: float
    ShutterSpeedValue: float
    ISOSpeedRatings: float
    FocalLength: float
    FocalLengthIn35mmFilm: float
    DateTimeOriginal: str
    DateTimeDigitized: str
    OffsetTime: str
    absolutePath: str
    fileName: str

