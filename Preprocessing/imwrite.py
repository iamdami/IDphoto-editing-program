import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(".jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드

cv2.imwrite("new.jpg", image) 
