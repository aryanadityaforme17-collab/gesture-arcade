import cv2 as cv

img =cv.imread('images/parrot.jpg')
cv.imshow('Boston',img)

#Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)


#Edge Cascade
canny=cv.Canny(img,125,175)
cv.imshow('canny edges',canny)

#Dilatinng the image 
dilated=cv.dilate(canny,(5,5),iterations=3)
cv.imshow('dillated',dilated)

#eroding
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded',eroded)
#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',  resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)