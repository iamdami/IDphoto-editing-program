import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(".jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
image_50x50 = cv2.resize(image, (50, 50))  # 이미지 크기 50x50 픽셀로 변경

plt.imshow(image_50x50, cmap="gray"), plt.axis("off")
plt.show()
