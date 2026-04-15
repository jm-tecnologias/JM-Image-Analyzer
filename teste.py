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


# =====================
# Adiciona Imagem de fundo
# =====================
def background(canvas, doc):
    canvas.drawImage(
        "assets/bg1.jpg",
        0, 0,
        width=doc.pagesize[0],
        height=doc.pagesize[1]
    )


# ==============================
# 1. Criar documento PDF
# ==============================

doc = SimpleDocTemplate("relatorio.pdf")

# lista onde vai todo o conteúdo
story = []

# estilos padrão
styles = getSampleStyleSheet()

# ==============================
# 2. Título do relatório
# ==============================
titulo = Paragraph(
    "JM-Image Analyzer Report",
    styles["Title"]
)
story.append(titulo)
story.append(Spacer(1, 5))

headerData = [
    ["Created at:", "Image ID:", "Analyst:"]
]

headerTable = Table(
    headerData,
    colWidths=[180, 180, 180]
)

headerTable.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
    ("TEXTCOLOR", (0, 0), (0, 0), colors.black),
    ("GRID", (0, 0), (0, 0), 1, colors.transparent),
]))

story.append(headerTable)
story.append(Spacer(1, 5))

# ==============================
# 3. Texto descritivo
# ==============================
descricao = Paragraph(
    '<para backColor="lightgrey">Image Preview</para>',
    styles["Title"]
)
story.append(descricao)
story.append(Spacer(1, 5))

# ==============================
# 5. Inserir imagem
# ==============================
img = Image("assets/logo.png", width=450, height=230)

# colocar imagem dentro de uma tabela
img_box = Table([[img]])

img_box.setStyle(TableStyle([
    ("BOX", (0, 0), (-1, -1), 2, colors.black),  # borda
]))

story.append(img_box)
story.append(Spacer(1, 10))

# tabela esquerda (AGORA É TABLE)
t1_data = [
    ["Device Information", ""],
    ["Produto", "Qtd"],
    ["Mouse", 2],
    ["Teclado", 1]
]
t1 = Table(t1_data, colWidths=[120, 120])

# tabela direita (AGORA É TABLE)
t2_data = [
    ["Geographic Inormation", ""],
    ["Produto", "Qtd"],
    ["Mouse", 2],
    ["Teclado", 1]
]
t2 = Table(t2_data, colWidths=[120, 120])

t3_data = [
    ["Capture Metadata", ""],
    ["Produto", "Qtd"],
    ["Mouse", 2],
    ["Teclado", 1]
]
t3 = Table(t3_data, colWidths=[120, 120])

t4_data = [
    ["Time Inormation", ""],
    ["Produto", "Qtd"],
    ["Mouse", 2],
    ["Teclado", 1]
]
t4 = Table(t4_data, colWidths=[120, 120])

# alinhar cabeçalho dentro das tabelas
t1.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.green),
    ("SPAN", (0, 0), (-1, 0)),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (-1, 1), (0, 0), 0, colors.black),
    ('FONTNAME', (0, 0), (-1, -1), "Courier-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))

t2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.green),
    ("SPAN", (0, 0), (-1, 0)),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (-1, 1), (0, 0), 0, colors.black),
    ('FONTNAME', (0, 0), (-1, -1), "Courier-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))

t3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.green),
    ("SPAN", (0, 0), (-1, 0)),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (-1, 1), (0, 0), 0, colors.black),
    ('FONTNAME', (0, 0), (-1, -1), "Courier-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))

t4.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.green),
    ("SPAN", (0, 0), (-1, 0)),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (-1, 1), (0, 0), 0, colors.black),
    ('FONTNAME', (0, 0), (-1, -1), "Courier-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))

# lado a lado (AGORA FUNCIONA)
layout = Table(
    [[t1, t2], [t3, t4]],
    colWidths=[250, 250]
)

layout.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.transparent),
]))

story.append(layout)
story.append(Spacer(1, 30))

# ==============================
# 7. Gerar PDF
# ==============================
doc.build(story, onFirstPage=background, onLaterPages=background)
