import cv2
import numpy as np 
from matplotlib import pyplot as plt

img_grey = cv2.imread('.jpg', cv2.IMREAD_GRAYSCALE)
save_img = '.jpg'

max_output_value = 255
neighborhood_size = 99
subtract_from_mean = 10

img_binarized = cv2.adaptiveThreshold(img_grey, max_output_value,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                        neighborhood_size, subtract_from_mean) 

plt.imshow(img_binarized, cmap="gray"), plt.axis("off")
cv2.imwrite(save_img, img_binarized)
plt.show()
