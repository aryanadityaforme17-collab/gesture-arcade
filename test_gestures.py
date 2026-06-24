import cv2
import mediapipe as mp
import gestures as g
import handtrackingmodule as h
import time
#DESIGNED FOR RIGHT HAND
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = h.handDetector()


while True:
    
    ok, img = cap.read()
    if not ok:
        print("image nhi pakad paya!!")
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    gesture='None'
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    if lmList:
        fingers = g.fingers_up(lmList)
        gesture = g.classify_gesture(fingers,lmList)
        print(fingers, gesture)
        from gestures import _distance, _hand_scale
        print(_distance(lmList,4,8) / _hand_scale(lmList[0],lmList[9]))

    cv2.putText(img, gesture, (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0, 0), 2)
    cv2.putText(img,"FPS-"+ str(int(fps)), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
   
    cv2.imshow("Gesture Test", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

