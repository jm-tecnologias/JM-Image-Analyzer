import customtkinter as ctk

from model.GeneratePDFReport import GeneratePDFReport
from model.ImageModel import ImageModel
import os

import platform
import tkinter as tk
from tkinter import filedialog

from model.utils import get_base_path

BASE_DIR = get_base_path()

from pathlib import Path

# Pasta Documents do utilizador
DOCUMENTS_DIR = Path.home() / "Documents"

# Pasta da aplicação
APP_DIR = DOCUMENTS_DIR / "JM-Image-Analyzer"
APP_DIR.mkdir(parents=True, exist_ok=True)

# Subpasta File Explore
REPORT_FILE_DIR = APP_DIR / "Report Files"
REPORT_FILE_DIR.mkdir(parents=True, exist_ok=True)


class Properties:
    def __init__(self, master):
        # self.metaDataSouce = None
        self.master = master
        self.master.pack_propagate(False)
        self.imageModel = None

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
        self.detais = ctk.CTkFrame(self.detaisFrame, fg_color="#141414")
        self.detais.grid(row=1, column=0, sticky='nswe', padx=20, pady=(26, 0))

        self.detais.grid_columnconfigure(0, weight=1)
        # self.detais.grid_propagate(False)

        row = 0

        # ---------- Device Details ----------
        ctk.CTkLabel(
            self.detais,
            text='🎥 Device Detalis',
            text_color="#38c20e",
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
        self.deviceMaker.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        self.deviceModel = ctk.CTkLabel(
            self.detais,
            text='Model: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
        )
        self.deviceModel.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        ctk.CTkLabel(
            self.detais,
            text='Software:',
            font=('Comic Sans MS', 14),
            anchor='w'
            # wraplength=353,
            # bg_color='red'
        ).grid(row=row, column=0, sticky='we', padx=(20, 0))
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
            text='🧭 GPS Details',
            text_color="#38c20e",
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
        self.gpsLatitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        self.gpsLongitude = ctk.CTkLabel(
            self.detais,
            text='Longitude: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # bg_color='red'
        )
        self.gpsLongitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        self.gpsAltitude = ctk.CTkLabel(
            self.detais,
            text='Altitude: N/A',
            font=('Comic Sans MS', 14),
            anchor='w'
            # bg_color='red'
        )
        self.gpsAltitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
        row += 1

        # ---------- Image Specifications ----------
        ctk.CTkLabel(
            self.detais,
            text='📸 Image Specifications',
            text_color="#38c20e",
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
            text='📅 Date Specifications',
            text_color="#38c20e",
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


        self.buttonFrameDetails = ctk.CTkFrame(self.detaisFrame, fg_color="#141414")
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
            fg_color="#141414"
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
        export_btn = ctk.CTkButton(
            buttons_frame,
            text="📤 Export Report ",
            height=44,
            corner_radius=12,
            fg_color="#141414",  # dark glass
            hover_color="#1e293b",
            border_width=1,
            border_color="#38c20e",  # cor neon JM
            text_color="#38c20e",
            font=("Berlin Sans FB Demi", 16),
            command=self.exportDadaToPDF
        )

        export_btn.grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="we"
        )

        ctk.CTkButton(
            buttons_frame,
            text="⚡Batch Analysis",
            height=44,
            corner_radius=12,
            fg_color="#141414",  # dark glass
            hover_color="#1e293b",
            border_width=1,
            border_color="#38c20e",  # cor neon JM
            text_color="#38c20e",
            font=("Berlin Sans FB Demi", 16),
        ).grid(row=0, column=1, padx=5, pady=5, sticky="we")

        # -------- SEGUNDA LINHA --------
        ctk.CTkButton(
            buttons_frame,
            text="📂 Open Reports",
            height=44,
            corner_radius=12,
            fg_color="#141414",  # dark glass
            hover_color="#1e293b",
            border_width=1,
            border_color="#38c20e",  # cor neon JM
            text_color="#38c20e",
            font=("Berlin Sans FB Demi", 16),
            command=lambda: self.selecionar_e_abrir_pdf()
        ).grid(row=1, column=0, padx=5, pady=5, sticky="we")

        ctk.CTkButton(
            buttons_frame,
            text="➕ More Actions",
            height=44,
            corner_radius=12,
            fg_color="#141414",  # dark glass
            hover_color="#1e293b",
            border_width=1,
            border_color="#38c20e",  # cor neon JM
            text_color="#38c20e",
            font=("Berlin Sans FB Demi", 16),
        ).grid(row=1, column=1, padx=5, pady=5, sticky="we")

    def exportDadaToPDF(self):
        # print(self.imageModel)
        pdf = GeneratePDFReport(self.imageModel)
        pdf.runBuild()

    def abrir_pdf(self,caminho_pdf):
        sistema = platform.system()

        if sistema == "Windows":
            os.startfile(caminho_pdf)
        elif sistema == "Darwin":
            os.system(f"open '{caminho_pdf}'")
        else:
            os.system(f"xdg-open '{caminho_pdf}'")

    def selecionar_e_abrir_pdf(self):
        root = tk.Tk()
        root.withdraw()

        caminho = filedialog.askopenfilename(
            title="Selecionar PDF",
            initialdir=REPORT_FILE_DIR,  # 👈 pasta padrão
            filetypes=[("Ficheiros PDF", "*.pdf")]
        )

        if caminho:
            self.abrir_pdf(caminho)


    def updateImageProperties(self, path):
        self.imageModel = ImageModel.model_validate(ImageModel.from_image(path))

        # -------- DEVICE ----------
        self.deviceMaker.configure(text=f"Camera: {self.imageModel.make}")
        self.deviceModel.configure(text=f"Model: {self.imageModel.model}")
        self.deviceSoftware.configure(text=f"{self.imageModel.software}")

        # -------- GPS ----------
        if self.imageModel.gpsInfo is not None:
            self.gpsLatitude.configure(text=f"Latitude: {self.imageModel.gpsInfo.latitude:.4f}" if self.imageModel.gpsInfo.latitude is not None else "Latitude: N/A")
            self.gpsLongitude.configure(text=f"Longitude: {self.imageModel.gpsInfo.longitude:.4f}" if self.imageModel.gpsInfo.longitude is not None else "Longitude: N/A")
            self.gpsAltitude.configure(text=f"Altitude: {self.imageModel.gpsInfo.altitude}" if self.imageModel.gpsInfo.altitude is not None else "Altitude: N/A")
        else:
            self.gpsLatitude.configure(text=f"Latitude: N/A")
            self.gpsLongitude.configure(text=f"Longitude: N/A")
            self.gpsAltitude.configure(text=f"Altitude: N/A")

            # ---------- Image Specifications ----------
        self.ExposureTime.configure(text=f"Exposure Time: {self.imageModel.ExposureTime}")
        self.ShutterSpeedValue.configure(text=f"Shutter Speed Value: {self.imageModel.ShutterSpeedValue}")
        self.IOSSpeeddRatings.configure(text=f"IOS Speed Ratings: {self.imageModel.ISOSpeedRatings}")
        self.FocalLength.configure(text=f"Focal Length: {self.imageModel.FocalLength}")
        self.FocalLengthIn35mmFilm.configure(
            text=f"Focal Length In 35mm Film: {self.imageModel.FocalLengthIn35mmFilm}")
        # ---------- Date Specifications ----------
        self.DateTimeOriginal.configure(text=f"Date/Time Original: {self.imageModel.DateTimeOriginal}")
        self.DateTimeDigitized.configure(text=f"Date/Time Digitized: {self.imageModel.DateTimeDigitized}")
        self.OffsetTime.configure(text=f"OffsetTime: {self.imageModel.OffsetTime}")
        return self.imageModel

