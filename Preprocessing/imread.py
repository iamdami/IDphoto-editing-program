import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(".jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
plt.imshow(image, cmap="gray"), plt.axis("off")  # 이미지 출력
plt.show()
type(image)  # 데이터 타입 확인
image  # 이미지 데이터 확인
image.shape  # 차원 확인 (해상도)
