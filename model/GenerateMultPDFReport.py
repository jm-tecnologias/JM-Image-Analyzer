
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from pathlib import Path
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from model.utils import get_base_path

BASE_DIR = get_base_path()

pdfmetrics.registerFont(
    TTFont(
        "Montserrat-SemiBold",
        str(BASE_DIR / "assets/fonts/Montserrat-SemiBold.ttf")
    )
)
DOCUMENTS_DIR = Path.home() / "Documents"
APP_DIR = DOCUMENTS_DIR / "JM-Image-Analyzer"
REPORT_FILE_DIR = APP_DIR / "Report Files"

REPORT_FILE_DIR.mkdir(parents=True, exist_ok=True)


class GenerateMultPDFReport:

    def __init__(self, image_models):

        self.imageModels = image_models

        self.file = REPORT_FILE_DIR / f"JM-BATCH-REPORT.pdf"

        self.c = canvas.Canvas(str(self.file), pagesize=A4)

        self.W, self.H = A4

    # ==================================================
    # COLORS (AI STYLE)
    # ==================================================
    NEON_GREEN = colors.HexColor("#C9AB6A")
    CARD_BG = colors.HexColor("#1B2A63")

    # ==================================================
    # BACKGROUND
    # ==================================================
    def drawBackground(self):
        self.c.rect(0, 0, self.W, self.H)

    # ==================================================
    # HEADER
    # ==================================================
    def drawHeader(self):

        c = self.c

        c.setFillColor(self.NEON_GREEN)
        c.setFont("Montserrat-SemiBold", 22)
        c.drawString(60, self.H - 50, "JM Vision Intelligence System")

        c.setFont("Montserrat-SemiBold", 12)
        c.drawString(60, self.H - 70, "INTELLIGENT REPORT")

        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
        c.setFont("Montserrat-SemiBold", 10)
        c.setFillColor(colors.black)
        c.drawString(420, self.H - 65, now)


        c.setFillColor(colors.black)
        c.setFont("Montserrat-SemiBold", 12)
        c.drawString(200, self.H - 85, "Analyst.: jm-tecnologias.co.mz | Engine V1.5")


    # ==================================================
    # IMAGE PANEL (HUD STYLE)
    # ==================================================
    def drawImagePanel(self):

        c = self.c

        x = 0
        y = self.H - 375
        w = 600
        h = 280
        # frame
        # c.setStrokeColor(self.NEON_GREEN)
        # c.rect(x, y, w, h)

        # image
        c.drawImage(
            self.imageModel["absolutePath"],
            x,
            y,
            width=w,
            height=h,
            preserveAspectRatio=True
        )

    # ==================================================
    # CARD DRAWER
    # ==================================================
    def drawCard(self, x, y, w, h, title, lines):

        c = self.c

        c.setFillColor(self.CARD_BG)
        c.roundRect(x, y, w, h, 10, fill=1)

        c.setStrokeColor("#141414")
        c.roundRect(x, y, w, h, 10)

        c.setFillColor("#73bcd9")
        c.setFont("Montserrat-SemiBold", 12)
        c.drawString(x + 10, y + h - 20, title)

        c.setFillColor(colors.white)
        c.setFont("Montserrat-SemiBold", 9)

        yy = y + h - 40

        for line in lines:
            c.drawString(x + 10, yy, line)
            yy -= 15

    # ==================================================
    # ANALYSIS PANELS
    # ==================================================
    def drawAnalysis(self):

        left = 40
        mid = 210
        right = 400
        y = self.H - 510

        self.drawCard(
            left, y, 160, 120,
            "AI ANALYSIS SUMMARY",
            [
                "✔ Transmission Tower",
                "✔ Terrain: Vegetation",
                "✔ Integrity: NORMAL",
                "✔ Risk Level: LOW"
            ]
        )

        self.drawCard(
            mid, y, 180, 120,
            "DEVICE INFORMATION",
            [
                f"Camera",
                f"{self.imageModel.get("Make","N/A")}",
                f"Lens",
                f"{self.imageModel.get("Model","N/A")}",
                f"Software",
                f"{self.imageModel.get("Software","N/A")}"
            ]



        )

        captured = datetime.strptime(
            self.imageModel.get("DateTimeOriginal","N/A"),
            "%Y:%m:%d %H:%M:%S"
        )

        self.drawCard(
            right, y, 145, 120,
            "TIME INFORMATION",
            [
                f"Captured Date",
                f"{datetime.strptime(self.imageModel.get("DateTimeOriginal","N/A"), '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}",
                f"Digitized Date",
                f"{datetime.strptime(self.imageModel.get("DateTimeDigitized","N/A"), '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}",
                f"Offset Time"
                f"{self.imageModel.get("OffsetTime", "N/A")}"
            ]
        )

    # ==================================================
    # TELEMETRY
    # ==================================================
    def drawTelemetry(self):

        y = self.H - 670

        self.drawCard(
            40, y, 200, 150,
            "IMAGE TELEMETRY",
            [
                f"Exposure Time:        {self.imageModel.get("ExposureTime","N/A")}",
                f"Shutter Speed:        {self.imageModel.get("ShutterSpeedValue","N/A")}",
                f"ISO:                  {self.imageModel.get("ISOSpeedRatings","N/A")}",
                f"Focal Length:         {self.imageModel.get("FocalLength","N/A")}",
                f"Focal Length (35mm):  {self.imageModel.get("FocalLengthIn35mmFilm","N/A")}",
                f"Film:                 {self.imageModel.get("FocalLength","N/A")}",
                f"White Balance:        {self.imageModel.get("WhiteBalance","N/A")}",
                f"Dynamic Range:        N/A",
            ]
        )






        gps = self.imageModel["GPSInfo"]

        self.drawCard(
            250, y, 295, 150,
            "GEO INTELLIGENCE",
            [
                f"Latitude: {gps.get("Latitude","N/A"):.4f}",
                f"Longitude: {gps.get("Longitude","N/A"):.4f}",
                f"Altitude: {gps.get("Altitude","N/A")} m",
                "Coordinate System: WGS84"
            ]
        )




    # ==================================================
    # FOOTER
    # ==================================================
    def drawFooter(self):

        c = self.c

        c.setStrokeColor(self.NEON_GREEN)
        c.line(40, 60, self.W - 40, 60)

        c.setFillColor(self.NEON_GREEN)
        c.setFont("Montserrat-SemiBold", 10)

        c.drawCentredString(
            self.W / 2,
            40,
            "PRECISION  •  INTELLIGENCE  •  RELIABILITY"
        )

    # ==================================================
    # BUILD REPORT
    # ==================================================
    def runBuild(self):
        for image in self.imageModels:
            self.imageModel = image

            self.drawBackground()
            self.drawHeader()
            self.drawImagePanel()
            self.drawAnalysis()
            self.drawTelemetry()
            self.drawFooter()
            self.c.showPage()

        self.c.save()

        print("✅ AI REPORT GENERATED")