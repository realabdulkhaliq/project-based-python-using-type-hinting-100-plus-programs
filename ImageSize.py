import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/profile.png")  # Replace with your image path
# Get the size of the image
width, height = img.size
print(f"Image size: {width}x{height}")

