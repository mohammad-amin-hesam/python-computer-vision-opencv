from cv2 import cv2
import numpy as np

image = cv2.imread("./image.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey()

# Creating our 3x3 kernel
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# We use the cv2.filter2D to convolve the kernel with an image
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow("3x3 Kernel Blurring", blurred)
cv2.waitKey()

# Creating our 7x7 kernel
kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow("7x7 Kernel Blurring", blurred2)
cv2.waitKey()

cv2.destroyAllWindows()

# Averaging done by convolving the image with a normalized box filter.
# This takes the pixels under the box and replaces the centeral element
# Box size needs to add and positive
blur = cv2.blur(image, (3, 3))
cv2.imshow("Averaging", blur)
cv2.waitKey()

# Instead of box filter, gaussian kernel
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gaussian Blurring", Gaussian)
cv2.waitKey()

# Takes median of all the pixels under kernel area and centeral
# Element is replaced with this median value
median = cv2.medianBlur(image, 5)
cv2.imshow("Median Blurring", median)
cv2.waitKey()

# Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral Blurring", bilateral)
cv2.waitKey()
cv2.destroyAllWindows()


# Parameters, after none are - the filter strength 'h' (5-10 is a good range)
# Next is hForColorComponents, set as same value as h agian
#
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow("Fast Means Denoising", dst)
cv2.waitKey()
cv2.destroyAllWindows()