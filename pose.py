import cv2
import mediapipe as mp
import numpy as np
import time
import handtrackingmodule as h


def fingers_up(lm_list):
    """Returns a list of 5 ints [thumb, index, middle, ring, pinky], 1 = up."""
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb: compare x (sideways). Assumes a right hand, mirrored feed.
    fingers.append(1 if lm_list[4][1] > lm_list[3][1] else 0)

    # Other four fingers: compare y (tip above PIP joint = up)
    for tip in tips[1:]:
        fingers.append(1 if lm_list[tip][2] < lm_list[tip - 2][2] else 0)

    return fingers


def classify_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"
    if fingers == [1, 1, 1, 1, 1]:
        return "OPEN PALM"
    if fingers == [0, 1, 0, 0, 0]:
        return "POINTING"
    if fingers == [0, 1, 1, 0, 0]:
        return "PEACE"
    if fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"
    return "UNKNOWN"

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = h.handDetector()

while True:
    success, img = cap.read()
    if not success:
         print("Failed to grab frame")
         break

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4]) 
            #for thumb

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,"FPS-"+ str(int(fps)), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)

    if lmList:
        fingers = fingers_up(lmList)
        gesture = classify_gesture(fingers)
        print(fingers, gesture)
        cv2.putText(img, gesture, (20, 60),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    

cap.release()
cv2.destroyAllWindows()


if __name__ == "__main__":
    main()