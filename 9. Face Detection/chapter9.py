# Importing the OpenCV library.
import cv2

# Loading the cascade classifier.
faceCascade = cv2.CascadeClassifier("../Resources/haarcascades/haarcascade_frontalface_default.xml")

# Reading the image from the file.
img = cv2.imread("../Resources/family.jpg")

# Converting the image to gray scale.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting the faces in the image.
faces = faceCascade.detectMultiScale(imgGray, 2.1, 4)

# Drawing a rectangle around the face.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 10)

# Showing the image.
cv2.imshow("Result", img)

# Waiting for a key press.
cv2.waitKey(0)