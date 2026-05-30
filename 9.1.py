from PIL import Image
image = Image.open("картинка.jpg")
image.show()
print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель:", image.mode)