from PIL import Image

img = Image.open("input2.jpg")


img = img.convert("RGB")


img.save("input2.bmp")
print("input2.bmp successfully created as RGB BMP.")
