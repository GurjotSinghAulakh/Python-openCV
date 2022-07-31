# Importing the OpenCV library.
import cv2

# Reading the image from the path and storing it in the variable img.
img = cv2.imread("../Resources/konferansebord.jpg")

# Showing the image in a window.
cv2.imshow("Output", img)

# Waiting for a key to be pressed.
cv2.waitKey(0)

