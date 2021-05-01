from __future__ import print_function
import os
from PIL import Image

files = [
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg',
      './damdam.jpg']
# for문 이용해 수정 예정

result = Image.new("RGB", (1650, 1050))

for index, file in enumerate(files):
    path = os.path.expanduser(file)
    img = Image.open(path)
    img.thumbnail((413, 531), Image.ANTIALIAS)
    x = index % 4 * 413
    y = index // 4 * 525
    w, h = img.size
    result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('output.jpg'))
