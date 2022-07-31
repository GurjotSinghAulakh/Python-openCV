import cv2

import numpy as np

"""
    It takes an array of images, and stacks them horizontally and vertically to create a single image
    
    :param scale: This is the scale at which we want to resize the images
    :param imgArray: This is the array of images that we want to stack
    :return: the stacked images.

"""

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


# Reading the image from the path and storing it in the variable img.
img = cv2.imread("../Resources/konferansebord.jpg")

# It converts the image to a grayscale image.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Stacking the images horizontally and vertically.
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))

# Stacking the image horizontally.
# imgHor = np.hstack((img, img))

# It stacks the image vertically.
# imgVer = np.vstack((img, img))

# It shows the image.
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)

cv2.imshow("ImageStack",imgStack)

# It waits for a key to be pressed.
cv2.waitKey(0)
