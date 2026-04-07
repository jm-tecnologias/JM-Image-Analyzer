import customtkinter as ctk
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

        row = 0

        # ---------- Device Details ----------
        ctk.CTkLabel(
            self.detais,
            text='Device Detalis',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=40)
        row += 1

        deviceMaker = ctk.CTkLabel(
            self.detais,
            text='Camera: GoPro',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        deviceMaker.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        deviceModel = ctk.CTkLabel(
            self.detais,
            text='Model: GoPro Max',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        deviceModel.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        deviceSoftware = ctk.CTkLabel(
            self.detais,
            text='Software: Adobe Lightroom',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        deviceSoftware.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        # ---------- GPS Details ----------
        ctk.CTkLabel(
            self.detais,
            text='GPS Detalis',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=40)
        row += 1

        gpsLatitude = ctk.CTkLabel(
            self.detais,
            text='Latitude: -25.4342423',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        gpsLatitude.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        gpsLongitude = ctk.CTkLabel(
            self.detais,
            text='Longitude: 35.3424234',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        gpsLongitude.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        gpsAltitude = ctk.CTkLabel(
            self.detais,
            text='Altitude: 523,45',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        gpsAltitude.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        # ---------- Image Specifications ----------
        ctk.CTkLabel(
            self.detais,
            text='Image Specifications',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=40)
        row += 1

        ExposureTime = ctk.CTkLabel(
            self.detais,
            text='ExposureTime: 145',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        ExposureTime.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        ShutterSpeedValue = ctk.CTkLabel(
            self.detais,
            text='ShutterSpeedValue: 120',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        ShutterSpeedValue.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        IOSSpeeddRatings = ctk.CTkLabel(
            self.detais,
            text='IOS Speedd Ratings: 100',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        IOSSpeeddRatings.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        FocalLength = ctk.CTkLabel(
            self.detais,
            text='Focal Length: 523,45',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        FocalLength.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        FocalLengthIn35mmFilm = ctk.CTkLabel(
            self.detais,
            text='Focal LengthIn 35mm Film: 523,45',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        FocalLengthIn35mmFilm.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        # ---------- Date Specifications ----------
        ctk.CTkLabel(
            self.detais,
            text='Date Specifications',
            font=('Berlin Sans FB Demi', 32),
            anchor='w'
        ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=40)
        row += 1

        DateTimeOrigin = ctk.CTkLabel(
            self.detais,
            text='DateTimeOrigin: GoPro',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        DateTimeOrigin.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        DateTimeDigitized = ctk.CTkLabel(
            self.detais,
            text='DateTimeDigitized: GoPro Max',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        DateTimeDigitized.grid(row=row, column=0, sticky='we', padx=40)
        row += 1

        OffatTime = ctk.CTkLabel(
            self.detais,
            text='OffatTime: Adobe Lightroom',
            font=('Comic Sans MS', 18),
            anchor='w'
        )
        OffatTime.grid(row=row, column=0, sticky='we', padx=40)

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