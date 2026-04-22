# import os
# import platform
# from pathlib import Path
#
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# def abrir_pdf(caminho_pdf):
#     sistema = platform.system()
#
#     if sistema == "Windows":
#         os.startfile(caminho_pdf)
#
#
# # exemplo de uso
# abrir_pdf(BASE_DIR/"assets/reports/JM Report-photo - Copy.pdf")

import os
import platform
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


# raiz do projecto (ajusta conforme a estrutura)
BASE_DIR = Path(__file__).resolve().parent.parent


def abrir_pdf(caminho_pdf):
    sistema = platform.system()

    if sistema == "Windows":
        os.startfile(caminho_pdf)
    elif sistema == "Darwin":
        os.system(f"open '{caminho_pdf}'")
    else:
        os.system(f"xdg-open '{caminho_pdf}'")


def selecionar_e_abrir_pdf():
    root = tk.Tk()
    root.withdraw()

    caminho = filedialog.askopenfilename(
        title="Selecionar PDF",
        initialdir=BASE_DIR,  # 👈 pasta padrão
        filetypes=[("Ficheiros PDF", "*.pdf")]
    )

    if caminho:
        abrir_pdf(caminho)


# executar
selecionar_e_abrir_pdf()


# pip install folium

# import folium
#
import webbrowser
import folium
import requests
import json
from pathlib import Path



