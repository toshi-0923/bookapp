import cv2

img = cv2.imread("1.jpg")


def scale_box(img, width, height):
    scale = max(width / img.shape[1], height / img.shape[0])
    return cv2.resize(img, dsize=None, fx=scale, fy=scale)


#dst = scale_box(img, 100, 100)
#cv2.imwrite("media/1.jpg", dst)