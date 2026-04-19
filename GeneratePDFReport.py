from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from model.ClickableImage import ClickableImage




class GeneratePDFReport:

    def __init__(self, image_model):
        self.imageModel = image_model

        self.doc = SimpleDocTemplate(
            "relatorio.pdf",
            pagesize=A4
        )

        self.elementos = []
        self.styles = getSampleStyleSheet()

    # ---------------------------------------------------
    # BACKGROUND
    # ---------------------------------------------------
    def background(self, canvas, doc):

        canvas.saveState()

        width, height = A4

        canvas.drawImage(
            "assets/bg1.jpg",
            0,
            0,
            width=width,
            height=height
        )

        canvas.restoreState()

    # ---------------------------------------------------
    # BUILD PDF
    # ---------------------------------------------------
    def buildPDFSchema(self):
        titulo_style = ParagraphStyle(
            name="TituloCustom",
            parent=self.styles["Title"],  # herda o Title
            fontName="Courier-Bold",
            fontSize=24,
            # textColor=colors.darkgreen,
            alignment=1  # CENTER
        )

        titulo = Paragraph(
            "JM-Image Analyzer Report",
            titulo_style
        )

        self.elementos.append(titulo)
        self.elementos.append(Spacer(1, 5))

        self.createHeader()

        mapa = Image(f"{self.imageModel.absolutePath}", width=515, height=250)
        self.elementos.append(mapa)

        self.elementos.append(Spacer(0, 0))
        print()

        self.createTable()

        self.doc.build(
            self.elementos,
            onFirstPage=self.background,
            onLaterPages=self.background
        )

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------
    def createHeader(self):

        header_data = [
            [f"Created at:{'2026-04-19'}", f"ImageID: {self.imageModel.fileName}", f"Analyst: {'jm-tecnologias.co.mz'}"]
        ]

        header_table = Table(
            header_data,
            colWidths=[170, 170, 170]
        )

        header_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))

        self.elementos.append(header_table)
        self.elementos.append(Spacer(1, 5))

    # ---------------------------------------------------
    # MAIN TABLES
    # ---------------------------------------------------
    def createTable(self):

        # ---------------- Device Info ----------------
        t1 = Table([
            ["Device Information"],
            [f"Camera: {self.imageModel.make}"],
            [f"Lens: {self.imageModel.model}"],
            [f"Software: {self.imageModel.software}"]
        ], colWidths=[295])

        # ---------------- Capture Metadata ----------------
        t2 = Table([
            ["Image Specifications"],
            [f"Exposure Time: {self.imageModel.ExposureTime}"],
            [f"ShutterSpeedValue: {self.imageModel.ShutterSpeedValue}"],
            [f"ISO Speed Ratings: {self.imageModel.ISOSpeedRatings}"],
            [f"Focal Length: {self.imageModel.FocalLength}"],
            [f"Focal Length In 35 mm Film: {self.imageModel.FocalLengthIn35mmFilm}"]
        ], colWidths=[295])

        # ---------------- Time Info ----------------
        t3 = Table([
            ["Time Information"],
            [f"Captured Date: {datetime.strptime(self.imageModel.DateTimeOriginal, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
            [f"Digitized Date: {datetime.strptime(self.imageModel.DateTimeDigitized, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
            [f"Offset Time: {self.imageModel.OffsetTime}"]
        ], colWidths=[210])

        self.styleSection(t1)
        self.styleSection(t2)
        self.styleSection(t3)

        # layout correto (mesmo nº colunas)
        layout = Table(
            [
                [t1, t3],
                [t2, ""]
            ],
            colWidths=[310, 215]
        )

        layout.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))

        self.elementos.append(layout)
        self.elementos.append(Spacer(0, 0))

        # ---------------------------------------------------
        # GEO SECTION
        # ---------------------------------------------------

        geo_title = Table(
            [["Geographic Information"]],
            colWidths=[515]
        )

        geo_title.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))

        geo_content = Table([
            ["Pin Point Position"],
            [f"Latitude: {self.imageModel.gpsInfo.latitude}"],
            [f"Longitude: {self.imageModel.gpsInfo.longitude}"],
            [f"Altitude: {self.imageModel.gpsInfo.altitude}"]
        ], colWidths=[190])

        geo_content.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ]))

        map_url = f"https://www.google.com/maps?q={self.imageModel.gpsInfo.latitude},{self.imageModel.gpsInfo.longitude}"

        mapa_img = ClickableImage(
            "mapa.png",
            width=315,
            height=100,
            url=map_url
        )

        geo_map = Table([[mapa_img]], colWidths=[315])

        # ✅ TORNAR CÉLULA CLICÁVEL
        geo_map.setStyle(TableStyle([
            ("LINK", (0, 0), (0, 0), map_url),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))

        layout_geo = Table([
            [geo_title, ""],
            [geo_content, geo_map]
        ], colWidths=[200, 320])

        layout_geo.setStyle(TableStyle([
            ("SPAN", (0, 0), (1, 0)),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))

        self.elementos.append(layout_geo)

    # ---------------------------------------------------
    # STYLE HELPER (REUTILIZÁVEL)
    # ---------------------------------------------------
    def styleSection(self, table):

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("SPAN", (0, 0), (-1, 0)),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("FONTSIZE", (0, 1), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ]))

    # ---------------------------------------------------
    # PUBLIC RUN
    # ---------------------------------------------------
    def runBuild(self):

        self.buildPDFSchema()
        print('Codex')

