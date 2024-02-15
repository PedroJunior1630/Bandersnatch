from PIL import Image, ImageDraw, ImageFont

# Criar uma imagem em branco
width, height = 300, 100
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Carregar uma fonte
font_path = "C:/Users/ph751/OneDrive/Documentos/MeusProjetos/Bandersnatch/Pixelfont.ttf"  # Substitua pelo caminho real da sua fonte TTF
font_size = 20
font = ImageFont.truetype(font_path, font_size)

# Adicionar texto à imagem com a fonte especificada
text = "Olá, Mundo!"
text_color = "black"
draw.text((10, 10), text, font=font, fill=text_color)

# Exibir a imagem
image.show()





