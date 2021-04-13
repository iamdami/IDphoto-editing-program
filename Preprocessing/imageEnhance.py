import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(".jpg", cv2.IMREAD_GRAYSCALE) 
image_enhanced = cv2.equalizeHist(image)  # 이미지 대비 향상
plt.imshow(image_enhanced, cmap="gray"), plt.axis("off")
plt.show()


image_bgr = cv2.imread(".jpg") 
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)  # YUV로 변경
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])  # 히스토그램 평활화 적용
image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)  # RGB로 변경
plt.imshow(image_rgb), plt.axis("off")
plt.show()
