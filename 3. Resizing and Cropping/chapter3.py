# Importing the OpenCV library.
import cv2

# Importing the numpy library.
import numpy as np

# Reading the image from the path and storing it in the variable img.
img = cv2.imread("../Resources/konferansebord.jpg")

# It prints the size of the image.
print(img.shape)

# It resizes the image to 300x400 pixels.
imgResize = cv2.resize(img, (300, 400))

# It prints the size of the image.
print(imgResize.shape)

# Cropping the image.
imgCropped = img[0:200, 200:500]

# It shows the image in a window.
cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

# It waits for a key to be pressed.
cv2.waitKey(0)
