# # # import os
# # # import platform
# # # from pathlib import Path
# # #
# # #
# # # BASE_DIR = Path(__file__).resolve().parent.parent
# # #
# # # def abrir_pdf(caminho_pdf):
# # #     sistema = platform.system()
# # #
# # #     if sistema == "Windows":
# # #         os.startfile(caminho_pdf)
# # #
# # #
# # # # exemplo de uso
# # # abrir_pdf(BASE_DIR/"assets/reports/JM Report-photo - Copy.pdf")
# #
# # import os
# # import platform
# # from pathlib import Path
# # import tkinter as tk
# # from tkinter import filedialog
# #
# #
# # # raiz do projecto (ajusta conforme a estrutura)
# # BASE_DIR = Path(__file__).resolve().parent.parent
# #
# #
# # def abrir_pdf(caminho_pdf):
# #     sistema = platform.system()
# #
# #     if sistema == "Windows":
# #         os.startfile(caminho_pdf)
# #     elif sistema == "Darwin":
# #         os.system(f"open '{caminho_pdf}'")
# #     else:
# #         os.system(f"xdg-open '{caminho_pdf}'")
# #
# #
# # def selecionar_e_abrir_pdf():
# #     root = tk.Tk()
# #     root.withdraw()
# #
# #     caminho = filedialog.askopenfilename(
# #         title="Selecionar PDF",
# #         initialdir=BASE_DIR,  # 👈 pasta padrão
# #         filetypes=[("Ficheiros PDF", "*.pdf")]
# #     )
# #
# #     if caminho:
# #         abrir_pdf(caminho)
# #
# #
# # # executar
# # selecionar_e_abrir_pdf()
# #
# #
# # # pip install folium
# #
# # # import folium
# # #
# # import webbrowser
# # import folium
# # import requests
# # import json
# # from pathlib import Path
# #
# #
# #
#
#
# com
# base
# no
# codigo
# abaxio, sugira
# uma
# interface
# de
# dashboard
# e
# uma
# de
# login
# futuristica
# para
# o
# software.faca
# um
# mockup
# de
# cada
# uma
# das
# interfaces
#
# import customtkinter as ctk
# from model.Tabs import Tabs
# from model.Pallet import Pallet
# from model.Properties import Properties
#
#
# class App:
#     def __init__(self):
#         # ICON
#         self.dataSource = {}
#         self.selected_item = None
#         self.imageView = None
#
#         ctk.set_appearance_mode('dark')
#         ctk.set_default_color_theme('dark-blue')
#
#         self.root = ctk.CTk()
#         self.root.title('JM-Image Analyzer')
#
#         # windows size
#         width = self.root.winfo_screenwidth()
#         height = self.root.winfo_screenheight()
#         self.root.geometry(f'{width}x{height}')
#
#         # main frame
#         self.main_frame = ctk.CTkFrame(self.root)
#         self.main_frame.pack(fill='both', expand=True)
#
#         # Column Configuration
#         self.main_frame.columnconfigure(0, weight=1)
#         self.main_frame.columnconfigure(1, weight=5)
#         self.main_frame.columnconfigure(2, weight=1)
#         self.main_frame.rowconfigure(0, weight=1)
#
#         self.properties = Properties(self.main_frame)
#         self.tabs = Tabs(self.main_frame, self.properties)
#         self.pallet = Pallet(self.main_frame, on_folder_selected=self.onFolderSelected)
#
#         self.tabs.setMiniMap(self.pallet.getMiniMap())
#
#     def onFolderSelected(self, path):
#         self.tabs.carouselButtonLoader(path)
#
#     def run(self):
#         self.root.mainloop()
#
#
# if __name__ == '__main__':
#     app = App()
#     app.run()
#
# from reportlab.platypus import Flowable, Image
#
#
# class ClickableImage(Flowable):
#
#     def __init__(self, path, width, height, url):
#         super().__init__()
#         self.img = Image(path, width=width, height=height)
#         self.width = width
#         self.height = height
#         self.url = url
#
#     def draw(self):
#         self.img.drawOn(self.canv, 0, 0)
#
#         # 🔥 link externo padrão (abre browser)
#         self.canv.linkURL(
#             self.url,
#             (0, 0, self.width, self.height),
#             relative=1,
#             kind="URI"
#         )
#
#
# from datetime import datetime
# from pathlib import Path
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
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# class GeneratePDFReport:
#
#     def __init__(self, image_model):
#         self.imageModel = image_model
#
#         self.doc = SimpleDocTemplate(
#             str(BASE_DIR / f"assets/reports/JM Report-{self.imageModel.fileName}.pdf"),
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
#         print(BASE_DIR)
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
#             [f"Latitude: {self.imageModel.gpsInfo.latitude}"],
#             [f"Longitude: {self.imageModel.gpsInfo.longitude}"],
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
#             BASE_DIR / "assets/snap/mapa.png",
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
#
#
# import customtkinter as ctk
# from PIL import Image
#
#
# class ImageView:
#
#     def __init__(self, master):
#
#         self.master = master
#         self.master.pack_propagate(False)
#
#         self.image_label = ctk.CTkLabel(
#             self.master,
#             text=""
#         )
#         self.image_label.pack(fill='both', expand=True)
#
#         self.current_pil = None
#         self.setImage('assets/logo.png')
#
#     # ------------------------------
#     # SET IMAGE COM TRANSIÇÃO
#     # ------------------------------
#     def setImage(self, path):
#         new_image = Image.open(path).convert("RGBA").resize((890, 850))
#
#         if self.current_pil is None:
#             self.current_pil = new_image
#             self._update_label(new_image)
#             return
#
#         # converter a imagem antiga também
#         old_image = self.current_pil.convert("RGBA")
#
#         self._fade_transition(old_image, new_image)
#
#     # ------------------------------
#     # ANIMAÇÃO FADE
#     # ------------------------------
#     def _fade_transition(self, old_img, new_img, step=0):
#         alpha = step / 10
#         blended = Image.blend(old_img, new_img, alpha)
#         self._update_label(blended)
#         if step < 10:
#             self.master.after(30, lambda: self._fade_transition(old_img, new_img, step + 1))
#         else:
#             self.current_pil = new_img
#
#     # ------------------------------
#     # UPDATE LABEL
#     # ------------------------------
#     def _update_label(self, pil_image):
#
#         self.my_image = ctk.CTkImage(
#             light_image=pil_image,
#             size=(890, 850)
#         )
#
#         self.image_label.configure(image=self.my_image)
#
#
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
#
# from tkintermapview import TkinterMapView
# from PIL import ImageGrab
#
#
# class MiniSateliteMap:
#
#     def __init__(self, master,
#                  LAT_INICIAL=-25.9692,
#                  LON_INICIAL=32.5732):
#
#         self.master = master
#         self.master.pack_propagate(False)
#
#         self.map_widget = None
#         self.marker = None
#
#         self._job = None
#         self.map_ready = False
#
#         self._last_bbox = (0, 0, 364, 198)
#
#         self._create_map(master, LAT_INICIAL, LON_INICIAL)
#
#     # --------------------------------------------------
#
#     def _create_map(self, frame, lat, lon):
#
#         self.map_widget = TkinterMapView(frame, corner_radius=0)
#         self.map_widget.pack(fill="both", expand=True)
#
#         # 🔥 MAPA LEVE
#         self.map_widget.set_tile_server(
#             "https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
#         )
#
#         self.map_widget.set_position(lat, lon)
#         self.map_widget.set_zoom(12)
#
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#         # 🔥 marca mapa como pronto após render inicial
#         # self.map_widget.after(1500, self._mark_map_ready)
#
#     # --------------------------------------------------
#
#     def _mark_map_ready(self):
#         self.map_ready = True
#         print("✔ Mapa pronto")
#
#         self._auto_capture_fixed_area()
#
#     # --------------------------------------------------
#
#     def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):
#
#         if isinstance(lat, tuple):
#             lat = self._converter_gps(lat)
#
#         if isinstance(lon, tuple):
#             lon = self._converter_gps(lon)
#
#         if lat_ref == "S":
#             lat = -abs(lat)
#
#         if lon_ref == "W":
#             lon = -abs(lon)
#
#         # 🔥 debounce
#         if self._job:
#             self.map_widget.after_cancel(self._job)
#
#         self._job = self.map_widget.after(
#             300,
#             lambda: self._update_map(lat, lon)
#         )
#
#     # --------------------------------------------------
#
#     def _update_map(self, lat, lon):
#
#         self.map_widget.set_position(lat, lon)
#
#         # 🔥 marker leve (sem recriar)
#         if self.marker:
#             self.marker.set_position(lat, lon)
#         else:
#             self.marker = self.map_widget.set_marker(lat, lon)
#         self.map_widget.after(3000, self._mark_map_ready)
#
#     # --------------------------------------------------
#
#     def _auto_capture_fixed_area(self):
#
#         if not self.map_ready:
#             return
#
#         x1, y1, x2, y2 = self._last_bbox
#
#         root_x = self.map_widget.winfo_rootx()
#         root_y = self.map_widget.winfo_rooty()
#
#         bbox = (
#             root_x + x1,
#             root_y + y1,
#             root_x + x2,
#             root_y + y2
#         )
#
#         img = ImageGrab.grab(bbox=bbox)
#         img.save(BASE_DIR / "assets/snap/mapa.png")
#
#         print("📸 Captura realizada:", bbox)
#
#     # --------------------------------------------------
#
#     def _converter_gps(self, valor):
#         graus, minutos, segundos = valor
#         return graus + minutos / 60 + segundos / 3600
#
#
# from tkintermapview import TkinterMapView
#
#
# class NormalMap:
#
#     def __init__(self, master, LAT_INICIAL=-25.9692, LON_INICIAL=32.5732):
#         self.master = master
#         self.map_widget = None
#         self.master.pack_propagate(False)
#         self.marker = None
#
#         self.openStreetMapWidgets(master, LAT_INICIAL, LON_INICIAL)
#
#     def openStreetMapWidgets(self, frame, LAT_INICIAL, LON_INICIAL):
#         self.map_widget = TkinterMapView(frame, corner_radius=0)
#         self.map_widget.pack(fill='both', expand=True)
#
#         frame.columnconfigure(0, weight=1)
#         frame.rowconfigure(2, weight=1)
#
#         # 🌍 Usar mapa normal (OpenStreetMap)
#         self.map_widget.set_tile_server(
#             "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
#         )
#
#         self.map_widget.set_position(LAT_INICIAL, LON_INICIAL)
#         self.map_widget.set_zoom(10)
#
#         # 📌 Marcador
#         # self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
#         self.marker = self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
#
#         return self.map_widget
#
#     def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):
#
#         # Converter DMS
#         if isinstance(lat, tuple):
#             lat = self.converter_gps(lat)
#
#         if isinstance(lon, tuple):
#             lon = self.converter_gps(lon)
#
#         # Hemisfério
#         if lat_ref == "S":
#             lat = -abs(lat)
#
#         if lon_ref == "W":
#             lon = -abs(lon)
#
#         print("FINAL:", lat, lon)
#
#         # mover mapa
#         self.map_widget.set_position(lat, lon)
#
#         # remover marcador antigo
#         if self.marker:
#             self.marker.delete()
#
#         # criar novo marcador
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#     def converter_gps(self, valor, ref=None):
#
#         graus, minutos, segundos = valor
#
#         decimal = graus + (minutos / 60.0) + (segundos / 3600.0)
#
#         if ref in ["S", "W"]:
#             decimal = -decimal
#
#         return decimal
#
#
# import customtkinter as ctk
# import os
#
# from model.MineSateliteMap import MiniSateliteMap
#
#
# class Pallet:
#
#     def __init__(self, master, on_folder_selected):
#
#         self.on_folder_selected = on_folder_selected
#
#         self.selected_item = None
#         self.dataSource = {}
#         self.master = master
#         # ________________________ Pallet Side ________________________
#
#         self.palletFrame = ctk.CTkFrame(master)
#         self.palletFrame.grid(row=0, column=0, sticky='nswe')
#
#         # coluna única expansível
#         self.palletFrame.columnconfigure(0, weight=1)
#
#         # ⭐ Header / Content /
#         self.palletFrame.rowconfigure(0, weight=0)  # title
#         self.palletFrame.rowconfigure(1, weight=1)  # scroll area
#
#         # ---------- Title ----------
#         self.titleLab = ctk.CTkLabel(
#             self.palletFrame,
#             text='Media File Explore',
#             font=('Berlin Sans FB Demi', 32)
#         )
#
#         self.titleLab.grid(row=0, column=0, sticky='we', pady=(40, 10))
#
#         # ---------- ScrollPane for images ----------
#         self.scrollPane = ctk.CTkScrollableFrame(self.palletFrame)
#         self.scrollPane.grid(row=1, column=0, sticky='nswe', pady=(26, 10), padx=20)
#
#         self.loadImagesDir()
#
#         self.miniMap = ctk.CTkFrame(self.palletFrame)
#         self.miniMap.grid(row=2, column=0, sticky='nswe', padx=20, pady=(0, 10))
#
#         self.mini_sateliteMap = MiniSateliteMap(self.miniMap)
#
#     def getMiniMap(self):
#         return self.mini_sateliteMap
#
#     def loadImagesDir(self):
#
#         path = 'C:/Users/JM-Tecnologias/Downloads'
#
#         # ---------- limpar ----------
#         self.dataSource = {}
#
#         # guardar pasta raiz
#         self.dataSource[0] = {
#             "srcPath": path,
#             "type": "root"
#         }
#
#         # ---------- LISTAR DIRECTORIAS ----------
#         folders = []
#
#         for entry in os.scandir(path):
#
#             if entry.is_dir():
#                 folders.append(entry)
#
#         total_folders = len(folders)
#
#         # ---------- UI LOAD ----------
#         for idx, entry in enumerate(folders, start=1):
#             folder_name = entry.name
#             folder_path = entry.path  # ⭐ caminho completo
#
#             # ⭐ DATA SOURCE
#             self.dataSource[idx] = {
#                 "name": folder_name,
#                 "absolutePath": folder_path,
#                 "type": "folder"
#             }
#
#             lab = ctk.CTkLabel(
#                 self.scrollPane,
#                 text=f"📁 {folder_name}",
#                 compound='left',
#                 font=('Comic Sans MS', 16),
#                 anchor='w'
#             )
#
#             lab.pack(fill='x', padx=8, pady=2)
#
#             # ⭐ IMPORTANTÍSSIMO (bug clássico evitado)
#             lab.bind(
#                 "<Button-1>",
#                 lambda e, widget=lab, data=self.dataSource[idx]:
#                 self.on_click(e, widget, data)
#             )
#
#     def on_click(self, event, widget, data):
#
#         if self.selected_item and self.selected_item.winfo_exists():
#             self.selected_item.configure(fg_color="transparent")
#
#         widget.configure(fg_color="#1f6aa5")
#         self.selected_item = widget
#
#         path = data.get('absolutePath')
#
#         # dispara evento externo
#         if self.on_folder_selected:
#             self.on_folder_selected(path)
#
#
# import customtkinter as ctk
# from PIL import Image
# from PIL.ExifTags import TAGS
#
# from model.GeneratePDFReport import GeneratePDFReport
# from model.ImageModel import ImageModel
# import os
#
# import platform
# from pathlib import Path
# import tkinter as tk
# from tkinter import filedialog
#
# # raiz do projecto (ajusta conforme a estrutura)
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# class Properties:
#     def __init__(self, master):
#         self.master = master
#         self.master.pack_propagate(False)
#         self.imageModel = None
#
#         # ______________________ Ponto de teste_______________________
#         # Right
#         self.detaisFrame = ctk.CTkFrame(master)
#         self.detaisFrame.grid(row=0, column=2, sticky='nswe')
#
#         # coluna única expansível
#         self.detaisFrame.columnconfigure(0, weight=1)
#         #
#         # ⭐ Header / Content /
#         self.detaisFrame.rowconfigure(0, weight=0)  # title
#         self.detaisFrame.rowconfigure(1, weight=1)  # scroll area
#         # self.detaisFrame.grid_propagate(False)
#
#         # ---------- Title ----------
#         ctk.CTkLabel(
#             self.detaisFrame,
#             text='Selected Image Details',
#             font=('Berlin Sans FB Demi', 32)
#         ).grid(row=0, column=0, sticky='we', pady=(40, 10))
#
#         self.detaisFrame.grid_columnconfigure(0, weight=1)
#
#         # ---------- Details Frame ----------
#         self.detais = ctk.CTkFrame(self.detaisFrame)
#         self.detais.grid(row=1, column=0, sticky='nswe', padx=20, pady=(26, 0))
#
#         self.detais.grid_columnconfigure(0, weight=1)
#         # self.detais.grid_propagate(False)
#
#         row = 0
#
#         # ---------- Device Details ----------
#         ctk.CTkLabel(
#             self.detais,
#             text='Device Detalis',
#             font=('Berlin Sans FB Demi', 32),
#             anchor='w'
#         ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
#         row += 1
#
#         self.deviceMaker = ctk.CTkLabel(
#             self.detais,
#             text='Camera: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#
#         )
#         self.deviceMaker.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         self.deviceModel = ctk.CTkLabel(
#             self.detais,
#             text='Model: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.deviceModel.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         ctk.CTkLabel(
#             self.detais,
#             text='Software:',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#             # wraplength=353,
#             # bg_color='red'
#         ).grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         self.deviceSoftware = ctk.CTkLabel(
#             self.detais,
#             text='N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#             # wraplength=353,
#             # bg_color='red'
#         )
#         self.deviceSoftware.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         # ---------- GPS Details ----------
#         ctk.CTkLabel(
#             self.detais,
#             text='GPS Detalis',
#             font=('Berlin Sans FB Demi', 32),
#             anchor='w'
#             # bg_color='red'
#         ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
#         row += 1
#
#         self.gpsLatitude = ctk.CTkLabel(
#             self.detais,
#             text='Latitude: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#             # bg_color='red'
#         )
#         self.gpsLatitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         self.gpsLongitude = ctk.CTkLabel(
#             self.detais,
#             text='Longitude: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#             # bg_color='red'
#         )
#         self.gpsLongitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         self.gpsAltitude = ctk.CTkLabel(
#             self.detais,
#             text='Altitude: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#             # bg_color='red'
#         )
#         self.gpsAltitude.grid(row=row, column=0, sticky='we', padx=(20, 0))
#         row += 1
#
#         # ---------- Image Specifications ----------
#         ctk.CTkLabel(
#             self.detais,
#             text='Image Specifications',
#             font=('Berlin Sans FB Demi', 32),
#             anchor='w'
#         ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
#         row += 1
#
#         self.ExposureTime = ctk.CTkLabel(
#             self.detais,
#             text='Exposure Time: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.ExposureTime.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.ShutterSpeedValue = ctk.CTkLabel(
#             self.detais,
#             text='Shutter Speed Value: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.ShutterSpeedValue.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.IOSSpeeddRatings = ctk.CTkLabel(
#             self.detais,
#             text='IOS Speedd Ratings: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.IOSSpeeddRatings.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.FocalLength = ctk.CTkLabel(
#             self.detais,
#             text='Focal Length: 523,45',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.FocalLength.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.FocalLengthIn35mmFilm = ctk.CTkLabel(
#             self.detais,
#             text='Focal LengthIn 35mm Film: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.FocalLengthIn35mmFilm.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         # ---------- Date Specifications ----------
#         ctk.CTkLabel(
#             self.detais,
#             text='Date Specifications',
#             font=('Berlin Sans FB Demi', 32),
#             anchor='w'
#         ).grid(row=row, column=0, sticky='we', pady=(20, 10), padx=20)
#         row += 1
#
#         self.DateTimeOriginal = ctk.CTkLabel(
#             self.detais,
#             text='Date&Time Original: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.DateTimeOriginal.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.DateTimeDigitized = ctk.CTkLabel(
#             self.detais,
#             text='DateTimeDigitized: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.DateTimeDigitized.grid(row=row, column=0, sticky='we', padx=20)
#         row += 1
#
#         self.OffsetTime = ctk.CTkLabel(
#             self.detais,
#             text='OffsetTime: N/A',
#             font=('Comic Sans MS', 14),
#             anchor='w'
#         )
#         self.OffsetTime.grid(row=row, column=0, sticky='we', padx=20)
#
#         # ---------- BUTTON FRAME DETAILS ----------
#
#         self.buttonFrameDetails = ctk.CTkFrame(self.detaisFrame)
#         self.buttonFrameDetails.grid(
#             row=2,
#             column=0,
#             sticky='we',
#             padx=20,
#             pady=(5, 10)
#         )
#
#         self.buttonFrameDetails.grid_columnconfigure(0, weight=1)
#
#         # ---------- Title ----------
#         ctk.CTkLabel(
#             self.buttonFrameDetails,
#             text='Actions',
#             font=('Berlin Sans FB Demi', 32),
#             anchor='w'
#         ).grid(row=0, column=0, sticky='we', padx=40, pady=(10, 5))
#
#         # ---------- Buttons Frame ----------
#         buttons_frame = ctk.CTkFrame(
#             self.buttonFrameDetails,
#             fg_color="transparent"
#         )
#
#         buttons_frame.grid(
#             row=1,
#             column=0,
#             sticky='we',
#
#         )
#
#         # configurar colunas
#         buttons_frame.grid_columnconfigure(0, weight=1)
#         buttons_frame.grid_columnconfigure(1, weight=1)
#
#         # -------- PRIMEIRA LINHA --------
#         ctk.CTkButton(
#             buttons_frame,
#             text="Export",
#             fg_color="transparent",
#             height=40,
#             bg_color="#1f6aa5",
#             corner_radius=0,
#             font=('Berlin Sans FB Demi', 16),
#             command=lambda: self.exportDadaToPDF()
#         ).grid(row=0, column=0, padx=5, pady=5, sticky="we")
#
#         ctk.CTkButton(
#             buttons_frame,
#             text="Batch Analysis",
#             fg_color="transparent",
#             height=40,
#             bg_color="#1f6aa5",
#             corner_radius=0,
#             font=('Berlin Sans FB Demi', 16)
#         ).grid(row=0, column=1, padx=5, pady=5, sticky="we")
#
#         # -------- SEGUNDA LINHA --------
#         ctk.CTkButton(
#             buttons_frame,
#             text="Open Report",
#             fg_color="transparent",
#             height=40,
#             bg_color="#1f6aa5",
#             corner_radius=0,
#             font=('Berlin Sans FB Demi', 16),
#             command=lambda: self.selecionar_e_abrir_pdf()
#         ).grid(row=1, column=0, padx=5, pady=5, sticky="we")
#
#         ctk.CTkButton(
#             buttons_frame,
#             text="Action 4",
#             fg_color="transparent",
#             height=40,
#             bg_color="#1f6aa5",
#             corner_radius=0,
#             font=('Berlin Sans FB Demi', 16)
#         ).grid(row=1, column=1, padx=5, pady=5, sticky="we")
#
#     def exportDadaToPDF(self):
#         print(self.imageModel)
#         pdf = GeneratePDFReport(self.imageModel)
#         pdf.runBuild()
#
#     def abrir_pdf(self, caminho_pdf):
#         sistema = platform.system()
#
#         if sistema == "Windows":
#             os.startfile(caminho_pdf)
#         elif sistema == "Darwin":
#             os.system(f"open '{caminho_pdf}'")
#         else:
#             os.system(f"xdg-open '{caminho_pdf}'")
#
#     def selecionar_e_abrir_pdf(self):
#         root = tk.Tk()
#         root.withdraw()
#
#         caminho = filedialog.askopenfilename(
#             title="Selecionar PDF",
#             initialdir=BASE_DIR / 'assets/reports',  # 👈 pasta padrão
#             filetypes=[("Ficheiros PDF", "*.pdf")]
#         )
#
#         if caminho:
#             self.abrir_pdf(caminho)
#
#     def getImageData(self, path=None):
#         self.metaDataSouce = {}
#         self.metaDataSouce['absolutePath'] = path
#
#         img = Image.open(path)
#         if os.path.isfile(path):
#             filename = os.path.basename(path)
#             name, ext = os.path.splitext(filename)
#             # print("Ficheiro:", filename)
#             # print("Nome:", name)
#             # print("Extensão:", ext)
#             self.metaDataSouce['fileName'] = name
#
#         # ---------- EXIF ----------
#         exifData = img._getexif()
#         if exifData:
#             for tag_id, value in exifData.items():
#                 tag = TAGS.get(tag_id, tag_id)
#
#                 self.metaDataSouce[tag] = value
#
#         return self.metaDataSouce
#
#     def updateImageProperties(self, path):
#
#         data = self.getImageData(path)
#         self.imageModel = self.build_image_model(data)
#
#         # -------- DEVICE ----------
#         self.deviceMaker.configure(text=f"Camera: {self.imageModel.make}")
#         self.deviceModel.configure(text=f"Model: {self.imageModel.model}")
#         self.deviceSoftware.configure(text=f"{self.imageModel.software}")
#         # -------- GPS ----------
#         gps = data.get('GPSInfo')
#
#         if gps:
#             self.gpsLatitude.configure(text=f"Latitude: {self.imageModel.gpsInfo.latitude}")
#
#             self.gpsLongitude.configure(text=f"Longitude: {self.imageModel.gpsInfo.longitude}")
#
#             self.gpsAltitude.configure(text=f"Altitude: {self.imageModel.gpsInfo.altitude}")
#             # ---------- Image Specifications ----------
#         self.ExposureTime.configure(text=f"Exposure Time: {self.imageModel.ExposureTime}")
#         self.ShutterSpeedValue.configure(text=f"Shutter Speed Value: {self.imageModel.ShutterSpeedValue}")
#         self.IOSSpeeddRatings.configure(text=f"IOS Speed Ratings: {self.imageModel.ISOSpeedRatings}")
#         self.FocalLength.configure(text=f"Focal Length: {self.imageModel.FocalLength}")
#         self.FocalLengthIn35mmFilm.configure(
#             text=f"Focal Length In 35mm Film: {self.imageModel.FocalLengthIn35mmFilm}")
#         # ---------- Date Specifications ----------
#         self.DateTimeOriginal.configure(text=f"Date/Time Original: {self.imageModel.DateTimeOriginal}")
#         self.DateTimeDigitized.configure(text=f"Date/Time Digitized: {self.imageModel.DateTimeDigitized}")
#         self.OffsetTime.configure(text=f"OffsetTime: {self.imageModel.OffsetTime}")
#
#         print(self.imageModel)
#
#     def build_image_model(self, exif: dict) -> ImageModel:
#
#         gps_data = parse_gps_info(exif.get("GPSInfo"))
#
#         clean_data = {
#             "make": exif.get("Make"),
#             "model": exif.get("Model"),
#             "software": exif.get("Software"),
#             "absolutePath": exif.get("absolutePath"),
#             'fileName': exif.get('fileName'),
#
#             "gpsInfo": gps_data,
#
#             "ExposureTime": exif.get("ExposureTime", 0),
#             "ShutterSpeedValue": exif.get("ShutterSpeedValue", 0),
#             "ISOSpeedRatings": exif.get("ISOSpeedRatings", 0),
#             "FocalLength": exif.get("FocalLength", 0),
#             "FocalLengthIn35mmFilm": exif.get("FocalLengthIn35mmFilm", 0),
#             "DateTimeOriginal": exif.get("DateTimeOriginal", ""),
#             "DateTimeDigitized": exif.get("DateTimeDigitized", ""),
#             "OffsetTime": exif.get("OffsetTime", ""),
#         }
#
#         return ImageModel.model_validate(clean_data)
#
#
# def converter_gps(valor, ref=None):
#     graus, minutos, segundos = valor
#
#     decimal = graus + (minutos / 60.0) + (segundos / 3600.0)
#
#     if ref in ["S", "W"]:
#         decimal = -decimal
#
#     return decimal
#
#
# def parse_gps_info(gps_raw: dict):
#     if not gps_raw:
#         return None
#
#     lat_ref = gps_raw.get(1)
#     lat = gps_raw.get(2)
#     lon_ref = gps_raw.get(3)
#     lon = gps_raw.get(4)
#
#     lat = converter_gps(lat)
#     lon = converter_gps(lon)
#
#     # Hemisfério
#     if lat_ref == "S":
#         lat = -abs(lat)
#
#     if lon_ref == "W":
#         lon = -abs(lon)
#
#     alt = gps_raw.get(6)
#     altitude = alt
#
#     return {
#         "latitude": lat,
#         "longitude": lon,
#         "altitude": altitude
#     }
#
#
# from tkintermapview import TkinterMapView
#
#
# class SateliteMap:
#
#     def __init__(self, master, LAT_INICIAL=-25.9692, LON_INICIAL=32.5732):
#         self.master = master
#         self.map_widget = None
#         self.master.pack_propagate(False)
#         self.marker = None
#
#         self.seteliteMapWidgets(master, LAT_INICIAL, LON_INICIAL)
#
#         # self.master.grid_columnconfigure(1, weight=1)
#
#     def seteliteMapWidgets(self, frame, LAT_INICIAL, LON_INICIAL):
#         self.map_widget = TkinterMapView(frame, corner_radius=0)
#         # map_widget.pack(fill="both", expand=True)
#         self.map_widget.pack(fill='both', expand=True)
#
#         frame.columnconfigure(0, weight=1)
#         frame.rowconfigure(1, weight=1)
#
#         self.map_widget.set_tile_server(
#             "https://mt0.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
#         )
#
#         self.map_widget.set_position(LAT_INICIAL, LON_INICIAL)
#         self.map_widget.set_zoom(10)
#
#         # Marcador
#         # self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
#         self.marker = self.map_widget.set_marker(LAT_INICIAL, LON_INICIAL)
#
#         return self.map_widget
#
#     def updatePosition(self, lat, lon, lat_ref=None, lon_ref=None):
#
#         # Converter DMS
#         if isinstance(lat, tuple):
#             lat = self.converter_gps(lat)
#
#         if isinstance(lon, tuple):
#             lon = self.converter_gps(lon)
#
#         # Hemisfério
#         if lat_ref == "S":
#             lat = -abs(lat)
#
#         if lon_ref == "W":
#             lon = -abs(lon)
#
#         print("FINAL:", lat, lon)
#
#         # mover mapa
#         self.map_widget.set_position(lat, lon)
#
#         # remover marcador antigo
#         if self.marker:
#             self.marker.delete()
#
#         # criar novo marcador
#         self.marker = self.map_widget.set_marker(lat, lon)
#
#     def converter_gps(self, valor, ref=None):
#
#         graus, minutos, segundos = valor
#
#         decimal = graus + (minutos / 60.0) + (segundos / 3600.0)
#
#         if ref in ["S", "W"]:
#             decimal = -decimal
#
#         return decimal
#
#
#
#
#
