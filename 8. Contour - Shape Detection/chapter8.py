# It imports the OpenCV library.
import cv2


# It imports the numpy library, and it renames it to np.
import numpy as np


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


def getContours(img):

    # It finds the contours in the image.
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Drawing the contours of the shapes in the image.
    for cnt in contours:

        # It calculates the area of the contour.
        area = cv2.contourArea(cnt)
        
        # print(area)

        if area > 500:
            
            # It draws the contours of the shapes in the image.
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

            # Calculating the perimeter of the contour.
            peri = cv2.arcLength(cnt, True)

            # print(peri)

            # Approximating the contour to a polygon.
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # print(len(approx))

            # Getting the number of corners in the shape.
            objCor = len(approx)

            # Getting the x and y coordinates of the top left corner of the rectangle, and the width
            # and height of the rectangle.
            x, y, w, h = cv2.boundingRect(approx)

            # Checking if the number of corners in the shape is 3, and if it is, it is assigning the
            # value "Tri" to the variable objectType.
            if objCor == 3:
                objectType = "Tri"

            # Checking if the number of corners in the shape is 4, and if it is, it is checking if the
            # aspect ratio of the shape is 1, and if it is, it is assigning the value "Square" to the
            # variable objectType. If the aspect ratio of the shape is not 1, it is assigning the
            # value "Rectangle" to the variable objectType.
            elif objCor == 4:
                aspRatio = w/float(h)
                if 0.95 < aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"

            # Checking if the number of corners in the shape is greater than 4, and if it is, it is
            # assigning the value "Circle" to the variable objectType.
            elif objCor > 4:
                objectType = "Circle"

            # Assigning the value "None" to the variable objectType.
            else:
                objectType = "None"

            # Drawing a rectangle around the shape.
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Writing the text "Tri", "Square", "Rectangle", "Circle", or "None" on the image.
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 3)


# Assigning the path of the image to the variable path.
path = "../Resources/shapes.png"

# It reads the image from the path, and it assigns it to the variable img.
img = cv2.imread(path)

# Creating a copy of the image, and it is assigning it to the variable imgContour.
imgContour = img.copy()

# Converting the image to gray scale.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring the image.
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

# Detecting the edges of the image.
imgCanny = cv2.Canny(img, 150, 200)

# It creates a blank image with the same width and height as the image.
imgBlank = np.zeros_like(img)

# Finding the contours in the image, and it is drawing the contours of the shapes in the image.
getContours(imgCanny)

# Stacking the images horizontally and vertically.
imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))

# Showing the image in a window.
cv2.imshow("Stack", imgStack)

# Waiting for a key to be pressed.
cv2.waitKey(0)
