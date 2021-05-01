import cv2

img = cv2.imread('./cropped.jpg')


def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])


# image resizing
img_s = cv2.resize(img, dsize=(0, 0),
                   fx=0.5, fy=0.5)

# function calling
img_tile = concat_vh([[img_s, img_s, img_s, img_s],
                      [img_s, img_s, img_s, img_s]])
# show the output image
cv2.imshow('concat_vh.jpg', img_tile)
