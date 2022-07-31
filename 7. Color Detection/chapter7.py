# It imports the OpenCV library.
import cv2


# It imports the numpy library, and renames it to np.
import numpy as np

"""
    It does nothing
    
    :param a: The array to be sorted
"""

def empty(a):
    pass


def stackImages(scale, imgArray):

    # Getting the number of rows in the array.
    rows = len(imgArray)

    # Getting the number of columns in the array.
    cols = len(imgArray[0])

    # It checks if the first element in the array is a list.
    rowsAvailable = isinstance(imgArray[0], list)

    # Getting the width of the first image in the array.
    width = imgArray[0][0].shape[1]

    # Getting the height of the first image in the array.
    height = imgArray[0][0].shape[0]

    # Checking if the first element in the array is a list.
    if rowsAvailable:

        # Looping through the rows in the array.
        for x in range(0, rows):

            # Looping through the columns in the array.
            for y in range(0, cols):

                # It checks if the shape of the image is the same as the shape of the first image in
                # the array.
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:

                    # It resizes the image to the width and height of the first image in the array.
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)

                else:
                    # It resizes the image to the width and height of the first image in the array.
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)

                # It checks if the image is a grayscale image, and if it is, it converts it to a BGR
                # image.
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # It creates a blank image with the same width and height as the first image in the array.
        imageBlank = np.zeros((height, width, 3), np.uint8)

        # It creates a list with the same number of elements as the number of rows in the array.
        hor = [imageBlank] * rows

        # Looping through the rows in the array, and stacking the images horizontally.
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])

        # It stacks the images vertically.
        ver = np.vstack(hor)

    else:
        for x in range(0, rows):

            # It checks if the shape of the image is the same as the shape of the first image in the
            # array.
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:

                # It resizes the image to the width and height of the first image in the array.
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)

            else:
                # It resizes the image to the width and height of the first image in the array.
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)

            # It checks if the image is a grayscale image, and if it is, it converts it to a BGR
            # image.
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # It stacks the images horizontally.
        hor = np.hstack(imgArray)

        # Assigning the value of hor to ver.
        ver = hor

    # It returns the stacked images.
    return ver



# Setting the path to the image.
path = "../Resources/konferansebord.jpg"

# It creates a window with the name "TrackBars".
cv2.namedWindow("TrackBars")

# It resizes the window to 640x240 pixels.
cv2.resizeWindow("TrackBars", 640, 240)

# It creates a trackbars in the window "TrackBars". 
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


# A while loop that runs forever.
while True:

    # It reads the image from the path.
    img = cv2.imread(path)

    # It converts the image from BGR to HSV.
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # It gets the position of the trackbars.
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    # It creates an array with the values of the trackbars.
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # It creates a mask that is black everywhere except where the HSV image is between the lower and
    # upper bounds.
    mask = cv2.inRange(imgHSV, lower, upper)

    # Creating a new image where the pixels are the same as the original image, except where the mask
    # is black.
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    # Stacking the images horizontally and vertically.
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))

    # It displays the images.
    cv2.imshow("Stacked Images", imgStack)

    # It waits for a key to be pressed.
    cv2.waitKey(1)

