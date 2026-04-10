import customtkinter as ctk
from PIL import Image
from PIL.ExifTags import TAGS

class Properties:
    def __init__(self, master):
        self.master = master
        self.master.pack_propagate(False)

        # ______________________ Ponto de teste_______________________
        # Right
        self.detaisFrame = ctk.CTkFrame(master)
        self.detaisFrame.grid(row=0, column=2, sticky='nswe')


        # coluna única expansível
        self.detaisFrame.columnconfigure(0, weight=1)
        #
        # ⭐ Header / Content /
        self.detaisFrame.rowconfigure(0, weight=0)  # title
        self.detaisFrame.rowconfigure(1, weight=1)  # scroll area
        # self.detaisFrame.grid_propagate(False)


        # ---------- Title ----------
        ctk.CTkLabel(
            self.detaisFrame,
            text='Selected Image Details',
            font=('Berlin Sans FB Demi', 32)
        ).grid(row=0, column=0, sticky='we', pady=(40, 10))

        self.detaisFrame.grid_columnconfigure(0, weight=1)

        # ---------- Details Frame ----------
        self.detais = ctk.CTkFrame(self.detaisFrame)
        self.detais.grid(row=1, column=0, sticky='nswe', padx=20, pady=(26, 0))

        self.detais.grid_columnconfigure(0, weight=1)
        # self.detais.grid_propagate(False)


        row = 0

        # ---------- Device Details ----------
        ctk.CTkLabel(
            self.detais,
            text='Device Detalis',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
        row += 1

        self.deviceMaker = ctk.CTkLabel(
            self.detais,
            text='Camera: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'

        )
        self.deviceMaker.grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        self.deviceModel = ctk.CTkLabel(
            self.detais,
            text='Model: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.deviceModel.grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        ctk.CTkLabel(
            self.detais,
            text='Software:',
            font=('Comic Sans MS', 14),
            anchor='w'
            # wraplength=353,
            # bg_color='red'
        ).grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        self.deviceSoftware = ctk.CTkLabel(
            self.detais,
            text='N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # wraplength=353,
            # bg_color='red'
        )
        self.deviceSoftware.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        # ---------- GPS Details ----------
        ctk.CTkLabel(
            self.detais,
            text='GPS Detalis',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
            # bg_color='red'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
        row += 1

        self.gpsLatitude = ctk.CTkLabel(
            self.detais,
            text='Latitude: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # bg_color='red'
        )
        self.gpsLatitude.grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        self.gpsLongitude = ctk.CTkLabel(
            self.detais,
            text='Longitude: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # bg_color='red'
        )
        self.gpsLongitude.grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        self.gpsAltitude = ctk.CTkLabel(
            self.detais,
            text='Altitude: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # bg_color='red'
        )
        self.gpsAltitude.grid(row=row, column=0, sticky='we', padx=(20,0))
        row += 1

        # ---------- Image Specifications ----------
        ctk.CTkLabel(
            self.detais,
            text='Image Specifications',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
        row += 1

        self.ExposureTime = ctk.CTkLabel(
            self.detais,
            text='Exposure Time: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.ExposureTime.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.ShutterSpeedValue = ctk.CTkLabel(
            self.detais,
            text='Shutter Speed Value: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.ShutterSpeedValue.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.IOSSpeeddRatings = ctk.CTkLabel(
            self.detais,
            text='IOS Speedd Ratings: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.IOSSpeeddRatings.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.FocalLength = ctk.CTkLabel(
            self.detais,
            text='Focal Length: 523,45',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.FocalLength.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.FocalLengthIn35mmFilm = ctk.CTkLabel(
            self.detais,
            text='Focal LengthIn 35mm Film: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.FocalLengthIn35mmFilm.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        # ---------- Date Specifications ----------
        ctk.CTkLabel(
            self.detais,
            text='Date Specifications',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
        row += 1

        self.DateTimeOriginal = ctk.CTkLabel(
            self.detais,
            text='Date&Time Original: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.DateTimeOriginal.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.DateTimeDigitized = ctk.CTkLabel(
            self.detais,
            text='DateTimeDigitized: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.DateTimeDigitized.grid(row=row, column=0, sticky='we', padx=20)
        row += 1

        self.OffsetTime = ctk.CTkLabel(
            self.detais,
            text='OffsetTime: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.OffsetTime.grid(row=row, column=0, sticky='we', padx=20)

        # ---------- BUTTON FRAME DETAILS ----------

        self.buttonFrameDetails = ctk.CTkFrame(self.detaisFrame)
        self.buttonFrameDetails.grid(
            row=2,
            column=0,
            sticky='we',
            padx=20,
            pady=(5, 10)
        )

        self.buttonFrameDetails.grid_columnconfigure(0, weight=1)

        # ---------- Title ----------
        ctk.CTkLabel(
            self.buttonFrameDetails,
            text='Actions',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=0, column=0, sticky='we', padx=40, pady=(10, 5))

        # ---------- Buttons Frame ----------
        buttons_frame = ctk.CTkFrame(
            self.buttonFrameDetails,
            fg_color="transparent"
        )

        buttons_frame.grid(
            row=1,
            column=0,
            sticky='we',

        )

        # configurar colunas
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)

        # -------- PRIMEIRA LINHA --------
        ctk.CTkButton(
            buttons_frame,
            text="Export",
            fg_color="transparent",
            height=40
        ).grid(row=0, column=0, padx=5, pady=5, sticky="we")

        ctk.CTkButton(
            buttons_frame,
            text="Action 1",
            fg_color="transparent",
            height=40
        ).grid(row=0, column=1, padx=5, pady=5, sticky="we")

        # -------- SEGUNDA LINHA --------
        ctk.CTkButton(
            buttons_frame,
            text="Action 3",
            fg_color="transparent",
            height=40
        ).grid(row=1, column=0, padx=5, pady=5, sticky="we")

        ctk.CTkButton(
            buttons_frame,
            text="Action 4",
            fg_color="transparent",
            height=40
        ).grid(row=1, column=1, padx=5, pady=5, sticky="we")

    def getImageData(self, path = None):
        self.metaDataSouce = {}

        img = Image.open(path)

        exifData = img._getexif()
        if exifData:
            for tag_id, value in exifData.items():
                tag = TAGS.get(tag_id, tag_id)

                self.metaDataSouce[tag] = value

        return self.metaDataSouce

    def updateImageProperties(self, path):

        data = self.getImageData(path)

        # -------- DEVICE ----------
        self.deviceMaker.configure(text=f"Camera: {data.get('Make', 'N/A')}")
        self.deviceModel.configure(text=f"Model: {data.get('Model', 'N/A')}")
        self.deviceSoftware.configure(text=f"{data.get('Software', 'N/A')}")
        # -------- GPS ----------
        gps = data.get('GPSInfo')

        if gps:
            self.gpsLatitude.configure(text=f"Latitude: {gps.get(2, 'N/A')}")

            self.gpsLongitude.configure(text=f"Longitude: {gps.get(4, 'N/A')}")

            self.gpsAltitude.configure(text=f"Altitude: {gps.get(6, 'N/A')}")
            # ---------- Image Specifications ----------
        self.ExposureTime.configure(text=f"Exposure Time: {data.get('ExposureTime','N/A')}")
        self.ShutterSpeedValue.configure(text=f"Shutter Speed Value: {data.get('ShutterSpeedValue','N/A')}")
        self.IOSSpeeddRatings.configure(text=f"IOS Speed Ratings: {data.get('ISOSpeedRatings','N/A')}")
        self.FocalLength.configure(text=f"Focal Length: {data.get('FocalLength','N/A')}")
        self.FocalLengthIn35mmFilm.configure(text=f"Focal Length In 35mm Film: {data.get('FocalLengthIn35mmFilm','N/A')}")
            # ---------- Date Specifications ----------
        self.DateTimeOriginal.configure(text=f"Date/Time Original: {data.get('DateTimeOriginal','N/A')}")
        self.DateTimeDigitized.configure(text=f"Date/Time Digitized: {data.get('DateTimeDigitized','N/A')}")
        self.OffsetTime.configure(text=f"OffsetTime: {data.get('OffsetTime','N/A')}")