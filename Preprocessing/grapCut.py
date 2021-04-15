import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread('.jpg')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

rectangle = (0, 56, 256, 150)  # 사각형 좌표: 시작점 x, 시작점 y, 너비, 높이

mask = np.zeros(image_rgb.shape[:2], np.uint8)  # 초기 마스크 생성

bgdModel = np.zeros((1, 65), np.float64)  # grabCut에 사용할 임시 배열 생성
fgdModel = np.zeros((1, 65), np.float64)


# grabCut 실행
cv2.grabCut(image_rgb,  # 원본 이미지
            mask,  # 마스크
            rectangle,  # 사각형
            bgdModel,  # 배경 위한 임시 배열
            fgdModel,  # 전경 위한 임시 배열
            5,  # 반복 횟수
            cv2.GC_INIT_WITH_RECT)  # 사각형 사용한 초기화
            
# 배경인 곳 0, 그외 1로 설정한 마스크 생성
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# 이미지에 새로운 마스크 곱해 배경 제외
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
plt.imshow(image_rgb_nobg), plt.axis("off")  # 이미지 출력
plt.show()

plt.imshow(mask, cmap='gray'), plt.axis("off")  # 마스크 출력
plt.show()

plt.imshow(mask_2, cmap='gray'), plt.axis("off")  # 마스크 출력
plt.show()
