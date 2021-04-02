from PIL import Image
from PIL import ImageChops

image1 = Image.open("image1.jpg")  # no cats
image2 = Image.open("image2.jpg")  # with cats

image = ImageChops.subtract(image2, image1)

mask1 = Image.eval(image, lambda a: 0 if a <= 24 else 255)
mask2 = mask1.convert('1')

blank = Image.eval(image, lambda a: 0)

new = Image.composite(image2, blank, mask2)
new.show()
