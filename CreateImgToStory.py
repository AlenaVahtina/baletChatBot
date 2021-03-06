from PIL import Image, ImageFont, ImageDraw
from connect import *

fontPath = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
sans16 = ImageFont.truetype(fontPath, 16)

text = info_class.plan+'\n'+info_class.place
img = Image.open("test.jpg")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, font=sans16)
img.save('test-out.jpg')