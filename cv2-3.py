from cv2 import cv2
import numpy as np

image = cv2.imread("./image.jpg")
##########################################################################
# B, G, R = image[14, 32]

# print(R, G, B)
# print(image.shape)

# gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# print(gray_img.shape)

# # H: 0 - 180, S: 0 - 255, V: 0 - 255

# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# cv2.imshow("HSV image", hsv_image)
# cv2.imshow("Hue channel", hsv_image[:, :, 0])
# cv2.imshow("Sturation channel", hsv_image[:, :, 1])
# cv2.imshow("Value channel", hsv_image[:, :, 2])

# cv2.waitKey()
# cv2.destroyAllWindows()

##########################################################################
# OpenCV's 'split' function splites the image into each color index
# B, G, R = cv2.split(image)

# print(B.shape)
# cv2.imshow("Red", R)
# cv2.imshow("Blue", B)
# cv2.imshow("Green", G)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # Let's re-make the original image,
# merged = cv2.merge([B, G, R])
# cv2.imshow("Merged", merged)

# # Let's amplify the blue color
# merged = cv2.merge([B+100, G, R])
# cv2.imshow("Merged with Blue Amplified", merged)

# cv2.waitKey()
# cv2.destroyAllWindows()
##########################################################################
B,G,R = cv2.split(image)

# Let's create a matrix of zeros
# with dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype = "uint8")

print("Zeros", zeros)
print("Image shape[:2]", image.shape[:2])

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey()
cv2.destroyAllWindows()
##########################################################################