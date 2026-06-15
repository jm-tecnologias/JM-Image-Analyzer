# from datetime import datetime
# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     Table,
#     TableStyle,
#     Image
# )
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from model.ClickableImage import ClickableImage
# from pathlib import Path
#
# from model.utils import get_base_path
#
# BASE_DIR = get_base_path()
#
# # Pasta Documents do utilizador
# DOCUMENTS_DIR = Path.home() / "Documents"
#
# # Pasta da aplicação
# APP_DIR = DOCUMENTS_DIR / "JM-Image-Analyzer"
# APP_DIR.mkdir(parents=True, exist_ok=True)
#
# # Subpasta File Explore
# SNAP_DIR = APP_DIR / "temp_snap"
# REPORT_FILE_DIR = APP_DIR / "Report Files"
#
# class GeneratePDFReport:
#
#     def __init__(self, image_model):
#         self.imageModel = image_model
#
#         self.doc = SimpleDocTemplate(
#             str(REPORT_FILE_DIR / f"JM Report-{self.imageModel.fileName}.pdf"),
#             pagesize=A4
#         )
#
#         self.elementos = []
#         self.styles = getSampleStyleSheet()
#
#     # ---------------------------------------------------
#     # BACKGROUND
#     # ---------------------------------------------------
#     def background(self, canvas, doc):
#         canvas.saveState()
#
#         width, height = A4
#         canvas.drawImage(
#             str(BASE_DIR / "assets/bg1.jpg"),
#             0,
#             0,
#             width=width,
#             height=height
#         )
#
#         canvas.restoreState()
#
#     # ---------------------------------------------------
#     # BUILD PDF
#     # ---------------------------------------------------
#     def buildPDFSchema(self):
#         page_width = self.doc.width
#
#         titulo_style = ParagraphStyle(
#             name="TituloCustom",
#             parent=self.styles["Title"],
#             fontName="Courier-Bold",
#             fontSize=24,
#             alignment=1
#         )
#
#         titulo = Paragraph(
#             "JM-Image Analyzer Report",
#             titulo_style
#         )
#
#         self.elementos.append(titulo)
#         self.elementos.append(Spacer(1, 5))
#
#         self.createHeader(page_width)
#
#         mapa = Image(
#             f"{self.imageModel.absolutePath}",
#             width=page_width,
#             height=240
#         )
#
#         self.elementos.append(mapa)
#         self.elementos.append(Spacer(1, 5))
#
#         self.createTable(page_width)
#
#         self.doc.build(
#             self.elementos,
#             onFirstPage=self.background,
#             onLaterPages=self.background
#         )
#
#     # ---------------------------------------------------
#     # HEADER
#     # ---------------------------------------------------
#     def createHeader(self, page_width):
#         header_data = [[
#             f"ImageID: {self.imageModel.fileName}",
#             "Analyst: jm-tecnologias.co.mz"
#         ]]
#         print(page_width)
#         header_table = Table(
#             header_data,
#             colWidths=[page_width / 2] * 2
#             # colWidths=[170, 281.27559]
#         )
#
#         header_table.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, -1), colors.green),
#             ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
#             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#             ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
#             ("FONTSIZE", (0, 0), (-1, -1), 10),
#             ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#             ("LEFTPADDING", (0, 0), (-1, -1), 0),
#             ("RIGHTPADDING", (0, 0), (-1, -1), 0),
#         ]))
#
#         self.elementos.append(header_table)
#         self.elementos.append(Spacer(1, 5))
#
#     # ---------------------------------------------------
#     # MAIN TABLES
#     # ---------------------------------------------------
#     def createTable(self, page_width):
#         left_col = page_width * 0.60
#         right_col = page_width * 0.40
#
#         # ---------------- Device Info ----------------
#         t1 = Table([
#             ["Device Information"],
#             [f"Camera: {self.imageModel.make}"],
#             [f"Lens: {self.imageModel.model}"],
#             [f"Software: {self.imageModel.software}"]
#         ], colWidths=[left_col])
#
#         # ---------------- Image Specs ----------------
#         t2 = Table([
#             ["Image Specifications"],
#             [f"Exposure Time: {self.imageModel.ExposureTime}"],
#             [f"ShutterSpeedValue: {self.imageModel.ShutterSpeedValue}"],
#             [f"ISO Speed Ratings: {self.imageModel.ISOSpeedRatings}"],
#             [f"Focal Length: {self.imageModel.FocalLength}"],
#             [f"Focal Length In 35 mm Film: {self.imageModel.FocalLengthIn35mmFilm}"]
#         ], colWidths=[left_col])
#
#         # ---------------- Time Info ----------------
#         t3 = Table([
#             ["Time Information"],
#             [
#                 f"Captured Date: {datetime.strptime(self.imageModel.DateTimeOriginal, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
#             [
#                 f"Digitized Date: {datetime.strptime(self.imageModel.DateTimeDigitized, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
#             [f"Offset Time: {self.imageModel.OffsetTime}"]
#         ], colWidths=[right_col])
#
#         self.styleSection(t1)
#         self.styleSection(t2)
#         self.styleSection(t3)
#
#         layout = Table(
#             [
#                 [t1, t3],
#                 [t2, ""]
#             ],
#             colWidths=[left_col, right_col]
#         )
#
#         layout.setStyle(TableStyle([
#             ("VALIGN", (0, 0), (-1, -1), "TOP"),
#             ("LEFTPADDING", (0, 0), (-1, -1), 0),
#             ("RIGHTPADDING", (0, 0), (-1, -1), 0),
#         ]))
#
#         self.elementos.append(layout)
#         self.elementos.append(Spacer(1, 1))
#
#         # ---------------------------------------------------
#         # GEO SECTION
#         # ---------------------------------------------------
#         geo_title = Table(
#             [["Geographic Information"]],
#             colWidths=[page_width]
#         )
#
#         geo_title.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, -1), colors.green),
#             ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
#             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#             ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
#             ("FONTSIZE", (0, 0), (-1, -1), 14),
#             ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ]))
#
#         data = datetime.now().date()
#         createdAt = Table(
#             [[f"Created at: {data}"]],
#             colWidths=[page_width]
#         )
#
#         createdAt.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, -1), colors.green),
#             ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
#             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#             ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
#             ("FONTSIZE", (0, 0), (-1, -1), 10),
#         ]))
#
#         geo_left = page_width * 0.38
#         geo_right = page_width * 0.62
#
#         geo_content = Table([
#             ["Pin Point Position"],
#             [f"Latitude: {self.imageModel.gpsInfo.latitude:.4f}"],
#             [f"Longitude: {self.imageModel.gpsInfo.longitude:.4f}"],
#             [f"Altitude: {self.imageModel.gpsInfo.altitude}"]
#         ], colWidths=[geo_left])
#
#         geo_content.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
#             ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
#             ("FONTSIZE", (0, 0), (-1, -1), 10),
#             ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
#         ]))
#
#         map_url = f"https://www.google.com/maps?q={self.imageModel.gpsInfo.latitude},{self.imageModel.gpsInfo.longitude}"
#
#         mapa_img = ClickableImage(
#
#             SNAP_DIR / "mapa.png",
#             width=geo_right,
#             height=100,
#             url=map_url
#         )
#
#         geo_map = Table([[mapa_img]], colWidths=[geo_right])
#
#         geo_map.setStyle(TableStyle([
#             ("LINK", (0, 0), (0, 0), map_url),
#             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#         ]))
#
#         layout_geo = Table([
#             [geo_title, ""],
#             [geo_content, geo_map],
#             [createdAt, ""]
#         ], colWidths=[geo_left, geo_right])
#
#         layout_geo.setStyle(TableStyle([
#             ("SPAN", (0, 0), (1, 0)),
#             ("VALIGN", (0, 0), (-1, -1), "TOP"),
#             ("SPAN", (0, 0), (1, 0)),
#         ]))
#
#         self.elementos.append(layout_geo)
#
#     # ---------------------------------------------------
#     # STYLE HELPER
#     # ---------------------------------------------------
#     def styleSection(self, table):
#         table.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, 0), colors.green),
#             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#             ("SPAN", (0, 0), (-1, 0)),
#             ("ALIGN", (0, 0), (-1, 0), "CENTER"),
#             ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
#             ("FONTSIZE", (0, 0), (-1, 0), 14),
#             ("FONTSIZE", (0, 1), (-1, -1), 10),
#             ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
#             ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
#         ]))
#
#     # ---------------------------------------------------
#     # PUBLIC RUN
#     # ---------------------------------------------------
#     def runBuild(self):
#         self.buildPDFSchema()
#         print("PDF Generated ✔")


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


class GeneratePDFReport:

    def __init__(self, image_model):

        self.imageModel = image_model

        self.file = REPORT_FILE_DIR / f"JM-REPORT-{image_model.fileName}.pdf"

        self.c = canvas.Canvas(str(self.file), pagesize=A4)

        self.W, self.H = A4

    # ==================================================
    # COLORS (AI STYLE)
    # ==================================================
    NEON_GREEN = colors.HexColor("#C9AB6A")
    # DARK_BG = colors.HexColor("#071018")
    CARD_BG = colors.HexColor("#1B2A63")

    # ==================================================
    # BACKGROUND
    # ==================================================
    def drawBackground(self):
        # self.c.setFillColor(self.DARK_BG)
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
            self.imageModel.absolutePath,
            x,
            y,
            width=w,
            height=h,
            preserveAspectRatio=True
        )

        # HUD grid
        # c.setStrokeColor(colors.HexColor("#113A2F"))
        #
        # for i in range(10):
        #     c.line(x, y + i * 28, x + w, y + i * 28)
        #
        # for i in range(15):
        #     c.line(x + i * 40, y, x + i * 40, y + h)

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
                f"{self.imageModel.make}",
                f"Lens",
                f"{self.imageModel.model}",
                f"Software",
                f"{self.imageModel.software}"
            ]
        )

        captured = datetime.strptime(
            self.imageModel.DateTimeOriginal,
            "%Y:%m:%d %H:%M:%S"
        )

        self.drawCard(
            right, y, 145, 120,
            "TIME INFORMATION",
            [
                f"Captured Date",
                f"{datetime.strptime(self.imageModel.DateTimeOriginal, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}",
                f"Digitized Date",
                f"{datetime.strptime(self.imageModel.DateTimeDigitized, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}",
                f"Offset Time"
                f"{self.imageModel.OffsetTime}"
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
                f"Exposure Time:        {self.imageModel.ExposureTime}",
                f"Shutter Speed:        {self.imageModel.ShutterSpeedValue}",
                f"ISO:                  {self.imageModel.ISOSpeedRatings}",
                f"Focal Length:         {self.imageModel.FocalLength}",
                f"Focal Length (35mm):  {self.imageModel.FocalLengthIn35mmFilm}",
                f"Film:                 {self.imageModel.FocalLength}",
                f"White Balance:        {self.imageModel.WhiteBalance}",
                f"Dynamic Range:        N/A",
            ]
        )

        gps = self.imageModel.gpsInfo

        self.drawCard(
            250, y, 295, 150,
            "GEO INTELLIGENCE",
            [
                f"Latitude: {gps.latitude:.4f}",
                f"Longitude: {gps.longitude:.4f}",
                f"Altitude: {gps.altitude} m",
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

        self.drawBackground()
        self.drawHeader()
        self.drawImagePanel()
        self.drawAnalysis()
        self.drawTelemetry()
        self.drawFooter()

        self.c.save()

        print("✅ AI REPORT GENERATED")