from PIL import Image
image = Image.open(r"C:\Users\Lomon\Desktop\5ebc32a14a54f96d9cb9913dbdf2a9f7.jpg")
image.show()
print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель:", image.mode)