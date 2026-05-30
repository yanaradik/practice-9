from PIL import Image

image = Image.open("картинка.jpg")

w, h = image.size
small = image.resize((w // 3, h // 3))

mirror_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
mirror_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)

small.save("small_image.jpg")
mirror_horizontal.save("mirror_horizontal.jpg")
mirror_vertical.save("mirror_vertical.jpg")

print("Готово!")