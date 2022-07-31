# Importing the OpenCV library.
import cv2

# Importing the numpy library.
import numpy as np

# Reading the image from the path and storing it in the variable img.
img = cv2.imread("../Resources/konferansebord.jpg")

# Setting the width and height of the output image.
width, height = 250, 350

# Creating a list of points that are the corners of the image.
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])


# Creating a list of points that are the corners of the image.
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Calculating the perspective transform matrix.
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Applying the perspective transform matrix to the image.
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# It shows the image in a window.
cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

# It waits for a key to be pressed.
cv2.waitKey(0)