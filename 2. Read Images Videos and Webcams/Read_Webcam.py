# Importing the opencv library.
import cv2

# Capturing the video from the webcam.
cap = cv2.VideoCapture(0)

# The below code is setting the width, height and brightness of the video.
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)


# This is a while loop that is reading the video from the webcam and 
# displaying it in a window.
while True:

    # Reading the video from the webcam and storing it in the variable img.
    success, img = cap.read()

    # Displaying the video in a window.
    cv2.imshow("Video", img)

    # This is a conditional statement that is checking if the user has pressed the 'q' key. If the
    # user has pressed the 'q' key, then the program will break out of the while loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break