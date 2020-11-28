from cv2 import cv2
import numpy as np

input = cv2.imread('./image.jpg')

cv2.imshow("Hello world", input)

cv2.waitKey()
# cv2.waitkey(0)
# this just works when 0 key pressed!

cv2.destroyAllWindows()


print(input.shape)
print("Height image is:", input.shape[0], "pixels")
print("Width image is:", input.shape[1], "pixels")


# This is how to we can save our output image:
cv2.imwrite("output.jpg", input)
