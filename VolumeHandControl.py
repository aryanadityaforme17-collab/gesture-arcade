import cv2
import time
import numpy as np
import handtrackingmodule as h
import math
from pycaw.pycaw import AudioUtilities
 
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
# print(f"Audio output: {device.FriendlyName}")
# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
#print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
volRange=volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(-20.0, None)
minVol=volRange[0]
maxVol=volRange[1]

wCam,hCam=640,480

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector = h.handDetector()

while True:
    success, img = cap.read()
    if not success:
        print("frame nhi aa rha")
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        # print(lmList[4],lmList[8])

        x1,y1,x2,y2=lmList[4][1],lmList[4][2],lmList[8][1],lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1), 7, (0, 0, 0), cv2.FILLED) 
        cv2.circle(img,(x2,y2), 7, (0, 0, 0), cv2.FILLED) 
        cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)
        cv2.circle(img,(cx,cy), 7, (0, 0, 0), cv2.FILLED) 

        length=math.hypot(x2-x1,y2-y1)
        print(length)

        if length<160:
            cv2.circle(img,(cx,cy), 7, (255, 0, 0), cv2.FILLED) 
            volume.SetMasterVolumeLevel(0.4078*length-65.25, None)
            cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
            cv2.rectangle(img,(50,int(150+25*(160-length)/16)),(85,400),(0,255,0),cv2.FILLED)
            cv2.putText(img,f'{int(length/1.6)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,"FPS-"+ str(int(fps)), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()