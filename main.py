from PIL import Image
import cv2 as cv

im_file = "./data/divya.png"  #OPENING IMAGE
img = cv.imread(im_file)  

def grayScale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)  #CONVERTING TO GRAYSCALE

def displayImage(image):
    cv.imshow("Image", image)
    cv.waitKey(0)

displayImage(grayScale(img))