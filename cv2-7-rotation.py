from cv2 import cv2
import numpy as np

image = cv2.imread("./image.jpg")
height, width = image.shape[:2]

# Divide by two to rototate the image around its center
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Other way
# img = cv2.imread("./image.jpg")

# rotated_image = cv2.transpose(img)

# cv2.imshow("Rotated Image - Method 2", rotated_image)
# cv2.waitKey()
