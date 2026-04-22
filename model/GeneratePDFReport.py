from datetime import datetime
from pathlib import Path
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

BASE_DIR = Path(__file__).resolve().parent.parent



class GeneratePDFReport:

    def __init__(self, image_model):
        self.imageModel = image_model

        self.doc = SimpleDocTemplate(
            str(BASE_DIR / f"assets/reports/JM Report-{self.imageModel.fileName}.pdf"),
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
        print(BASE_DIR)
        canvas.drawImage(
            str(BASE_DIR/"assets/bg1.jpg"),
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
        page_width = self.doc.width

        titulo_style = ParagraphStyle(
            name="TituloCustom",
            parent=self.styles["Title"],
            fontName="Courier-Bold",
            fontSize=24,
            alignment=1
        )

        titulo = Paragraph(
            "JM-Image Analyzer Report",
            titulo_style
        )

        self.elementos.append(titulo)
        self.elementos.append(Spacer(1, 5))

        self.createHeader(page_width)

        mapa = Image(
            f"{self.imageModel.absolutePath}",
            width=page_width,
            height=240
        )

        self.elementos.append(mapa)
        self.elementos.append(Spacer(1, 5))

        self.createTable(page_width)



        self.doc.build(
            self.elementos,
            onFirstPage=self.background,
            onLaterPages=self.background
        )

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------
    def createHeader(self, page_width):
        header_data = [[
            f"ImageID: {self.imageModel.fileName}",
            "Analyst: jm-tecnologias.co.mz"
        ]]
        print(page_width)
        header_table = Table(
            header_data,
            colWidths=[page_width / 2] * 2
            # colWidths=[170, 281.27559]
        )

        header_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))

        self.elementos.append(header_table)
        self.elementos.append(Spacer(1, 5))

    # ---------------------------------------------------
    # MAIN TABLES
    # ---------------------------------------------------
    def createTable(self, page_width):
        left_col = page_width * 0.60
        right_col = page_width * 0.40

        # ---------------- Device Info ----------------
        t1 = Table([
            ["Device Information"],
            [f"Camera: {self.imageModel.make}"],
            [f"Lens: {self.imageModel.model}"],
            [f"Software: {self.imageModel.software}"]
        ], colWidths=[left_col])

        # ---------------- Image Specs ----------------
        t2 = Table([
            ["Image Specifications"],
            [f"Exposure Time: {self.imageModel.ExposureTime}"],
            [f"ShutterSpeedValue: {self.imageModel.ShutterSpeedValue}"],
            [f"ISO Speed Ratings: {self.imageModel.ISOSpeedRatings}"],
            [f"Focal Length: {self.imageModel.FocalLength}"],
            [f"Focal Length In 35 mm Film: {self.imageModel.FocalLengthIn35mmFilm}"]
        ], colWidths=[left_col])

        # ---------------- Time Info ----------------
        t3 = Table([
            ["Time Information"],
            [f"Captured Date: {datetime.strptime(self.imageModel.DateTimeOriginal, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
            [f"Digitized Date: {datetime.strptime(self.imageModel.DateTimeDigitized, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')}"],
            [f"Offset Time: {self.imageModel.OffsetTime}"]
        ], colWidths=[right_col])

        self.styleSection(t1)
        self.styleSection(t2)
        self.styleSection(t3)

        layout = Table(
            [
                [t1, t3],
                [t2, ""]
            ],
            colWidths=[left_col, right_col]
        )

        layout.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))

        self.elementos.append(layout)
        self.elementos.append(Spacer(1, 1))

        # ---------------------------------------------------
        # GEO SECTION
        # ---------------------------------------------------
        geo_title = Table(
            [["Geographic Information"]],
            colWidths=[page_width]
        )

        geo_title.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))

        data = datetime.now().date()
        createdAt = Table(
            [[f"Created at: {data}"]],
            colWidths=[page_width]
        )

        createdAt.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
        ]))

        geo_left = page_width * 0.38
        geo_right = page_width * 0.62

        geo_content = Table([
            ["Pin Point Position"],
            [f"Latitude: {self.imageModel.gpsInfo.latitude}"],
            [f"Longitude: {self.imageModel.gpsInfo.longitude}"],
            [f"Altitude: {self.imageModel.gpsInfo.altitude}"]
        ], colWidths=[geo_left])

        geo_content.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ]))

        map_url = f"https://www.google.com/maps?q={self.imageModel.gpsInfo.latitude},{self.imageModel.gpsInfo.longitude}"

        mapa_img = ClickableImage(

            BASE_DIR/"assets/snap/mapa.png",
            width=geo_right,
            height=100,
            url=map_url
        )

        geo_map = Table([[mapa_img]], colWidths=[geo_right])

        geo_map.setStyle(TableStyle([
            ("LINK", (0, 0), (0, 0), map_url),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))

        layout_geo = Table([
            [geo_title, ""],
            [geo_content, geo_map],
            [createdAt, ""]
        ], colWidths=[geo_left, geo_right])

        layout_geo.setStyle(TableStyle([
            ("SPAN", (0, 0), (1, 0)),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("SPAN", (0, 0), (1, 0)),
        ]))

        self.elementos.append(layout_geo)

    # ---------------------------------------------------
    # STYLE HELPER
    # ---------------------------------------------------
    def styleSection(self, table):
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("SPAN", (0, 0), (-1, 0)),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Courier-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ]))

    # ---------------------------------------------------
    # PUBLIC RUN
    # ---------------------------------------------------
    def runBuild(self):
        self.buildPDFSchema()
        print("PDF Generated ✔")
