import cv2 as cv

img=cv.imread('images/download.jpg')
cv.imshow('download',img)
def rescaleFrame(frame, scale=0.75):
    width=(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
cv.waitKey(0)
capture = cv.VideoCapture('video/vdo.mp4')
while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()