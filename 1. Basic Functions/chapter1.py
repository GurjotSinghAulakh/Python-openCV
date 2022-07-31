# Importing the OpenCV library.
import cv2

# Importing the numpy library.
import numpy as np

# Reading the image from the path and storing it in the variable img.
img = cv2.imread("../Resources/konferansebord.jpg")

"""
    Kernel values are multiplied with pixel values. If all of them are zero, 
    the output will be zero. If it is not 1, the output is multiplied by the 
    value you provide into kernel. It is 1 to maintain the pixel value and ALL 
    1 since that is what the erosion filter accomplishes. 
    Kernels are often 1, 0, -1 combinations, depending on the kernel's aim. 
    As an example, in your case, a kernel of 5x5 1s is multiplied by 5x5 
    sub-images (which I think sums of pixel values of it).
"""

# Creating a kernel of 5x5 zeros.
kernel = np.ones((5, 5), np.uint8)

# Converting the image to gray scale.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring the image.
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Detecting the edges of the image.
imgCanny = cv2.Canny(img, 150, 200)


""" 
    Dilation adds pixels to the boundaries of objects in an image, while 
    erosion removes pixels on object boundaries. The number of pixels 
    added or removed from the objects in an image depends on the size 
    and shape of the structuring element used to process the image.
"""

# The below code is dilating the image.
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)


"""
    Erosion shrink-ens the image pixels i.e. it is used for shrinking of element
    using element B. Erosion removes pixels on object boundaries.: The value of 
    the output pixel is the minimum value of all the pixels in the neighborhood. 
    A pixel is set to 0 if any of the neighboring pixels have the value 0.
"""

# The below code is eroding the image.
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


# Showing the images in a window.
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

# Waiting for a key to be pressed.
cv2.waitKey(0)