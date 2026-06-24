import math
def _distance(lmList,p1,p2):
    x1,y1,x2,y2=lmList[p1][1],lmList[p1][2],lmList[p2][1],lmList[p2][2]
    length=math.hypot(x2-x1,y2-y1)
    return length

def  _hand_scale(p0,p9):
    x1,y1,x2,y2=p0[1],p0[2],p9[1],p9[2]
    return math.hypot(x2-x1,y2-y1)
    
def fingers_up(lm_list):
    #[thumb, index, middle, ring, pinky]
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb: compare x (sideways). Assumes a right hand, mirrored feed.
    fingers.append(1 if lm_list[4][1] > lm_list[3][1] else 0)

    # Other four fingers: compare y (tip above PIP joint = up)
    for tip in tips[1:]:
        fingers.append(1 if lm_list[tip][2] < lm_list[tip - 2][2] else 0)

    return fingers
    
    


def classify_gesture(fingers,lmList):
    pinch = _distance(lmList, 4, 8) / _hand_scale(lmList[0],lmList[9])
    if pinch < 0.3 and fingers[2] and fingers[3] and fingers[4]:
        return "OK"
    if fingers == [0, 0, 0, 0, 0]:
        return "STONE"
    if fingers == [1, 1, 1, 1, 1]:
        return "PAPER"
    if fingers == [0, 1, 0, 0, 0]:
        return "POINTING"
    if fingers == [0, 1, 1, 0, 0]:
        return "SCISSOR"
    if fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"
    if fingers == [0, 0, 1, 0, 0]:
        return "F**K YOU"
    if fingers == [0, 0, 0, 0, 1]:
        return "Need to pee"
    return "UNKNOWN"