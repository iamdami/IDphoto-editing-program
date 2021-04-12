import cv2
import numpy as np
from matplotlib import pyplot as plt


# 컬러 이미지 로드
image_bgr = cv2.imread(".jpg", cv2.IMREAD_COLOR)
image_bgr[0,0]  # 픽셀 확인
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)  # RGB로 변환
"""
Matplot lib 비롯, 대부분 이미지 앱 RGB 사용
컬러를 RGB로 변환
"""
plt.imshow(image_rgb), plt.axis("off")  # 이미지 출력
plt.show()
