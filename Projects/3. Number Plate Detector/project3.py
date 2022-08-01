# It imports the OpenCV library.
import cv2

# Loading the cascade classifier.
nPlatesCascade = cv2.CascadeClassifier("../Resources/haarcascades/haarcascade_russian_plate_number.xml")
minArea = 0
color = (255, 0, 255)


# It reads the image from the file.
img = cv2.imread("../Resources/car.jpeg")

# Converting the image to gray scale.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting the number-plates in the image.
numberPlates = nPlatesCascade.detectMultiScale(imgGray, 2.1, 4)

# Drawing a rectangle around the face.
while True:
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    # Waiting for a key press.
    cv2.waitKey(0)
