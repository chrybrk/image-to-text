import pytesseract

from PIL import Image

image = Image.open(input("image: "))
text = pytesseract.image_to_string(image)
with open(input("output: "), "w") as file: file.write(text)
