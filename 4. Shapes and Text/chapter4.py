# Importing the OpenCV library.
import cv2

# Importing the numpy library.
import numpy as np

# It creates a 512x512 image with 3 channels (RGB) and 8 bits per channel.
img = np.zeros((512, 512, 3), np.uint8)

# It prints the shape of the image.
# print(img.shape)

# Setting the value of all the pixels in the image to blue.
# img[:] = 255, 0, 0

# It draws a line from the top left corner to the bottom right corner of the image.
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# It draws a rectangle with the top left corner at (0,0) and the bottom right corner at (250, 350).
# The color of the rectangle is red. The thickness of the rectangle is 2.
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2)


# It draws a circle with the center at (400, 50) and a radius of 30. The color of the circle is
# yellow. The thickness of the circle is 2.
cv2.circle(img, (400, 50), 30, (255, 255, 0), 2)


# Writing the text "OPENCV" on the image.
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

# It shows the image in a window.
cv2.imshow("Image", img)

# It waits for a key to be pressed.
cv2.waitKey(0)