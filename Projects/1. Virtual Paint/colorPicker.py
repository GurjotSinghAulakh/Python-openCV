# Importing the opencv library.
import cv2

# Importing the numpy library and renaming it to np.
import numpy as np

# The below code is setting the width and height of the frame.
frameWidth = 640
frameHeight = 480

# This is setting the width and height of the frame.
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

"""
    It does nothing
    
    :param a: The array to be sorted
"""

def empty(a):
    pass


# Creating a window called HSV and resizing it to 640x240. It is also creating a trackbar for each of
# the HSV values.
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:

    # Reading the video capture and assigning it to the variable img.
    success, img = cap.read()

    # Converting the image from BGR to HSV.
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Getting the trackbar position for each of the HSV values.
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    
    print(h_min)

   
    # Setting the lower and upper bounds for the HSV values.
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Creating a mask that is black everywhere except where the HSV image is between the lower and
    mask = cv2.inRange(imgHsv, lower, upper)

    # Taking the image and mask and applying the mask to the image.
    result = cv2.bitwise_and(img, img, mask=mask)

    # Converting the mask from grayscale to BGR.
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Stacking the images horizontally.
    hStack = np.hstack([img, mask, result])

    # Showing the image.
    cv2.imshow('Horizontal Stacking', hStack)

    # Checking if the user has pressed the q key. If they have, it will break out of the loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the video capture.
cap.release()

# Destroying all the windows that have been created.
cv2.destroyAllWindows()