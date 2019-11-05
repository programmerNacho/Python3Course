import requests
from io import BytesIO
from PIL import Image # Pillow library for image manipulation
import os

r = requests.get("https://wallpaperplay.com/walls/full/1/a/7/132645.jpg")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(os.path.abspath(path), image.format)
except IOError:
    print("Cannot save image.")