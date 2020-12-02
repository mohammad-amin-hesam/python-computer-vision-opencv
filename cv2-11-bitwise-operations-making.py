from cv2 import cv2
import numpy as np

# If you're wondering why only two dimensions, well this is a grayscale image,
# if we doing a colored image, we'd use
# rectangle = np.zeros((300, 300, 3), np.uint8)

# Making a square
square = np.zeros((300, 300), np.uint8)
