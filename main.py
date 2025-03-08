import cv2
import math

cap = cv2.VideoCapture(1)
points=[]
ratio = 10/137
def draw_circle(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points)==2:
            points=[]
        points.append((x, y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",draw_circle)

while True:
    _, frame = cap.read()
    for pt in points:
        cv2.circle(frame, pt, 5, (25, 15, 255), -1)

    #measure between 2 points
    if len(points)==2:
        pt1 = points[0]
        pt2 = points[1]
        cv2.line(frame, pt1, pt2, (0, 255, 0), 2)
        distance_px = math.hypot((pt2[0] - pt1[0]), (pt2[1] - pt1[1]))
        distance_cm = ratio * distance_px
        cv2.putText(frame, fr"{int(distance_cm)}cm",(pt1[0], pt1[1] - 10), cv2.FONT_HERSHEY_PLAIN, 2.5,(25,15,235),3)

    cv2.imshow('Frame', frame)
    key= cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()