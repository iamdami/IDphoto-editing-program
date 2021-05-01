# 수정 예정

from PIL import Image
import numpy as np

im = Image.open('./afterGrapcut.jpg')

# Thumbnail 이미지 생성
size = (413, 531)
im.thumbnail(size)

mask_ = np.array(im)

for i in range(len(mask_)):
    for j in range(len(mask_[i])):
        if np.sum(mask_[i][j]) < 9:  # 이 값이 낮아질수록 머리에 하얀 게 줄었음! 너무 많이 줄이면 배경에 점 생김
            for k in range(3):
                mask_[i][j][k] = 120
(Image.fromarray(mask_, 'RGB')).save('./changeColor.jpg') 
