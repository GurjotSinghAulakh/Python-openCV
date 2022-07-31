# Importing the opencv library.
import cv2

# Reading the video file.
cap = cv2.VideoCapture("../Resources/videoplayback.mp4")


# This is a while loop that is reading the video file and displaying it.
while True:

    # Reading the video file and storing it in the variable img.
    success, img = cap.read()

    # Displaying the video file.
    cv2.imshow("Video", img)

    # This is a condition that is checking if the user has pressed the q key. 
    # If the user has pressed the q key, then the loop will break.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break