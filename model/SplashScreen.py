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

def background(canvas, doc):
    canvas.drawImage(
        "assets/bg1.jpg",
        0, 0,
        width=600,
        height=800
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
    ("BACKGROUND", (0,0), (-1,0), colors.whitesmoke),
    ("TEXTCOLOR", (0,0), (-1,0), colors.black),
    ("GRID", (0,0), (-1,-1), 1, colors.transparent),
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
    ("BOX", (0,0), (-1,-1), 2, colors.black),  # borda
]))

story.append(img_box)
story.append(Spacer(1, 10))


# ==============================
# 4. Tabela de dados
# ==============================
# ----------------------
# Título da tabela
# # ----------------------
# titulo_tabela = Paragraph("Device Information", styles["Heading2"])
#
# story.append(titulo_tabela)
# story.append(Spacer(1,10))


# ----------------------
# Dados da tabela
# ----------------------
# dados = [
#     ["Device Information", "", ""],
#     ["Produto", "Qtd", "Preço"],
#     ["Mouse", 2, "500 MZN"],
#     ["Teclado", 1, "1200 MZN"]
# ]
#
# tabela = Table(dados)
#
# tabela.setStyle(TableStyle([
#     ("SPAN", (0,0), (-1,0)),   # junta colunas
#     ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
#     ("ALIGN", (0,0), (-1,0), "CENTER"),
#
#     ("BACKGROUND", (0,1), (-1,1), colors.grey),
#     ("TEXTCOLOR", (0,1), (-1,1), colors.whitesmoke),
#
#     ("GRID", (0,0), (-1,-1), 1, colors.black),
# ]))
# story.append(tabela)
# story.append(Spacer(1, 30))

# style_centro = ParagraphStyle(
#     name="Centro",
#     alignment=0, # esquerdo
#     # alignment=1 centro
#     # alignment=2 direita
#     # alignment=4 justiicado
# )
#
# p = Paragraph("Texto Centralizado", style_centro)
#
# story.append(p)
#
# # texto justificado
# texto = Paragraph(
#     "Este relatório foi gerado automaticamente...",
#     ParagraphStyle(name="txt", alignment=4)
# )
#
# story.append(texto)





# ==============================
# 6. Rodapé simples
# ==============================
# rodape_style = ParagraphStyle(
#     name="Rodape",
#     fontSize=10,
#     alignment=1  # centralizado
# )
#
# rodape = Paragraph(
#     "Relatório gerado automaticamente pelo sistema JM-Image Analyzer",
#     rodape_style
# )
#
# story.append(rodape)


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
    ("SPAN", (0,0), (-1,0)),
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
]))

t2.setStyle(TableStyle([
    ("SPAN", (0,0), (-1,0)),
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
]))

t3.setStyle(TableStyle([
    ("SPAN", (0,0), (-1,0)),
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
]))

t4.setStyle(TableStyle([
    ("SPAN", (0,0), (-1,0)),
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
]))


# lado a lado (AGORA FUNCIONA)
layout = Table(
    [[t1, t2], [t3, t4]],
    colWidths=[250, 250]
)

layout.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "CENTER"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.transparent),
]))

story.append(layout)
story.append(Spacer(1,30))


# ==============================
# 7. Gerar PDF
# ==============================
doc.build(story, onFirstPage=background, onLaterPages=background)