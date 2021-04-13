# 선명하게

import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(".jpg", cv2.IMREAD_GRAYSCALE) 

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])  # 커널 생성

image_sharp = cv2.filter2D(image, -1, kernel)

plt.imshow(image_sharp, cmap="gray"), plt.axis("off")
plt.show()
