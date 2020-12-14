from cv2 import cv2
import numpy as np

image = cv2.imread("./image.jpg")

cv2.imshow("Original", image)
cv2.waitKey()

# Let's define our kernel size
kernel = np.ones((5, 5), np.uint8)

# Now we erode
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Erosion", erosion)
cv2.waitKey()

#
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Dilation", dilation)
cv2.waitKey()

# Opening - Good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey()

# Closing - Good foe removing noise
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey()

cv2.destroyAllWindows()
