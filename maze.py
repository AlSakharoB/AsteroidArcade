from PIL import Image

img = Image.open("PressStart2.png")
array = []
def picture():
    for x in range(933):
        for y in range(149):
            red, green, blue, hz = img.getpixel((x, y))
