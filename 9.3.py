from PIL import Image, ImageFilter
images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

new_names = [
    "new_1.jpg",
    "new_2.jpg",
    "new_3.jpg",
    "new_4.jpg",
    "new_5.jpg"
]

for i in range(5):
    img = Image.open(images[i])
    img = img.filter(ImageFilter.CONTOUR)
    img.save(new_names[i])

    print(f"{new_names[i]} сохранен")