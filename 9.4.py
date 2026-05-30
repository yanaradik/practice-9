from PIL import Image, ImageDraw, ImageFont

img = Image.open("цвет.jpg")

draw = ImageDraw.Draw(img)

text = "Yana Photo"
width, height = img.size

font = ImageFont.truetype("times.ttf", 15)
x, y = img.size
for x in range(0, width, 200):
    for y in range(0, height, 100):
        draw.text((x, y), text,
                  fill=(255, 255, 255),
                  font=font)
color = (255, 255, 255)
draw.text((x, y), text, fill=color, font=font)
img.save("цветresult.jpg")

print("Готово!")