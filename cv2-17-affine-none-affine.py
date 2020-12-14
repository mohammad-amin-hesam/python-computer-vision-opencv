from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./image.jpg")

cv2.imshow("Original", image)
cv2.waitKey()

# Cordinates of the 4 corners of the original image
points_A = np.float32([[230, 15], [700, 215], [85, 610], [530, 780]])

# Cordinates of the 4 corners of the desidred output
# We use a ratio of an A4 Paer 1 : 1.41
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M
M = cv2.getPerspectiveTransform(points_A, points_B)

warped = cv2.warpPerspective(image, M, (420, 594))

cv2.imshow("warpPerspective", warped)
cv2.waitKey()
cv2.destroyAllWindows()
