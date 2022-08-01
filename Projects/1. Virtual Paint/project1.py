# Importing the opencv library.
import cv2

# Importing the numpy library and renaming it to np.
import numpy as np

# Setting the width and height of the frame.
frameWidth = 640
frameHeight = 480

# The above code is setting the width and height of the frame.
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Defining the color range for the color detection.
myColors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]]

# Defining the color of the circle that will be drawn on the screen.
myColorValues = [[51, 153, 255],  ## BGR
                 [255, 0, 255],
                 [0, 255, 0],
                 [255, 0, 0]]

# Creating a list of points.
myPoints = []  ## [x , y , colorId ]


"""
    It takes an image, a list of colors, and a list of color values, and returns a list of points
    
    :param img: The image we're going to find the color in
    :param myColors: This is a list of lists. Each list contains the HSV values of a color
    :param myColorValues: This is a list of BGR values for each color
    :return: The x and y coordinates of the center of the object.
    """
def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newPoints

"""
    It takes an image and returns the x and y coordinates of the center of the largest contour

    :param img: The image to be processed
    :return: The x and y coordinates of the center of the contour.
"""
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

"""
    For each point in the list of points, draw a circle on the image with the color of the point's
    cluster.
    
    :param myPoints: The list of points that we want to draw on the canvas
    :param myColorValues: This is a list of colors that we want to use to draw the points
"""
def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break