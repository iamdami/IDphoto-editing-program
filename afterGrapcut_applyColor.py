import numpy as np
import cv2

# Load the image
img = cv2.imread('./cropped.jpg')

# Create a 0's mask
mask = np.zeros(img.shape[:2], np.uint8)

# Create 2 arrays for background and foreground model
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Find the coordinates with the roi crop mouse
rect = (1, 2, 410, 520)
mask, bgdModel, fgdModel = cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img_seg = img * mask2[:, :, np.newaxis]
cv2.imshow('first', img_seg)
cv2.imwrite('./damdamAfterGrapcut3.jpg', img_seg)

indices = np.where(mask == 2)
img_seg[indices[0], indices[1], :] = [215, 199, 124]
cv2.imshow('second', img_seg)
cv2.imwrite('./damdamBgColored.jpg', img_seg)
cv2.waitKey()
