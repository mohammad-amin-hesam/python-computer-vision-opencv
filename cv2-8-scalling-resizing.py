from cv2 import cv2
import numpy as np

# Load our input image
image = cv2.imread("./image.jpg")

# # Let's make our image 3/4 of it's original size
# image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
# cv2.imshow("Scaling - Linear Interpolation", image_scaled)
# cv2.waitKey()

# # Let's double the size of our image
# img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# cv2.imshow("Scaling - Cubic Interpolation", img_scaled)
# cv2.waitKey()

# # Let's skew the re-sizeing by setting exact dimensions
# img_scaled = cv2.resize(image, (900, 400), interpolation=cv2.INTER_AREA)
# cv2.imshow("Scaling - Skewed Size", img_scaled)
# cv2.waitKey()

# cv2.destroyAllWindows()

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow("Original", image)

cv2.imshow("Smaller ", smaller)
cv2.imshow("Larger", larger)

cv2.waitKey()
cv2.destroyAllWindows()