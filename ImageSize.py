import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/profile.png")  # Replace with your image path
# Get the size of the image
width, height = img.size
print(f"Image size: {width}x{height}")

# By Using Function
def get_image_size(image_path):
    """
    Get the size of an image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: A tuple containing the width and height of the image.
    """
    with Image.open(image_path) as img:
        return img.size
    
# Example usage
if __name__ == "__main__":
    image_path = "C:/Users/profile.png"  # Replace with your image path
    width, height = get_image_size(image_path)
    print(f"Image size: {width}x{height}")


# This code uses the Pillow library to get the size of an image.
# It defines a function `get_image_size` that takes the image path as an argument and returns the width and height of the image.
# The function is then called with an example image path, and the size is printed.