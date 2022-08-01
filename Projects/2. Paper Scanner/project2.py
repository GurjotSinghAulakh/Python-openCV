# It imports the OpenCV library.
import cv2

# Importing the numpy library, and it is giving it the alias np.
import numpy as np

# Setting the width and height of the image to 480 and 640 respectively, and it is setting the
# brightness of the image to 150.
widthImg = 480
heightImg = 640
cap = cv2.VideoCapture(0)
cap.set(10, 150)


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


"""
    We take an image, convert it to grayscale, blur it, apply Canny edge detection, dilate the edges,
    and then erode them
    
    :param img: The image we want to process
    :return: The image after it has been processed.
"""
def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres


def getContours(img):

    biggest = np.array([])
    maxArea = 0

    # It finds the contours in the image.
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Drawing the contours of the shapes in the image.
    for cnt in contours:

        # It calculates the area of the contour.
        area = cv2.contourArea(cnt)

        if area > 5000:

            # Calculating the perimeter of the contour.
            peri = cv2.arcLength(cnt, True)

            # Approximating the contour to a polygon.
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    # It draws the contours of the shapes in the image.
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 50)
    return biggest

"""
    It sorts the points in the following order: top-left, top-right, bottom-right, bottom-left
    
    :param myPoints: The points you want to reorder
    :return: The four points of the rectangle in the order of top-left, top-right, bottom-right,
    bottom-left.
"""
def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


def getWarp(img, biggest):

    biggest = reorder(biggest)

    # Creating a list of points that are the corners of the image.
    pts1 = np.float32(biggest)

    # Creating a list of points that are the corners of the image.
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

    # Calculating the perspective transform matrix.
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Applying the perspective transform matrix to the image.
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    return imgCropped


# Capturing the image from the webcam, and it is displaying the image.
while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()

    imgThres = preProcessing(img)
    biggest = getContours(imgThres)

    if biggest.size != 0:
        imgWraped = getWarp(img, biggest)
        imageArray = ([img, imgThres], [imgContour, imgWraped])
        cv2.imshow("ImageWraped", imgWraped)
        
    else:
        imageArray = ([img, imgThres], [img, img])

    stackedImages = stackImages(0.6, imageArray)

    cv2.imshow("WorkFlow", stackedImages)

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

