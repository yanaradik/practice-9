from PIL import Image

image = Image.open(r"C:\Users\Lomon\Desktop\5ebc32a14a54f96d9cb9913dbdf2a9f7.jpg")

w, h = image.size
small = image.resize((w // 3, h // 3))

mirror_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
mirror_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)

small.save(r"C:\Users\Lomon\Desktop\small_image.jpg")
mirror_horizontal.save("mirror_horizontal.jpg")
mirror_vertical.save("mirror_vertical.jpg")

print("Готово!")