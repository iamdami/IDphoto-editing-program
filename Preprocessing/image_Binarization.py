# 이미지 이진화

import cv2
import numpy as np
from matplotlib import pyplot as plt


image_grey = cv2.imread("./data/images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
max_output_value = 255
neighborhood_size = 99
subtract_from_mean = 10

image_binarized = cv2.adaptiveThreshold(image_grey, max_output_value,
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                         neighborhood_size, subtract_from_mean)  # 적응적 임계처리 적용
                                         
plt.imshow(image_binarized, cmap="gray"), plt.axis("off")
plt.show()
