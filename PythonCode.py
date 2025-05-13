import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np

cap = cv2.VideoCapture("http://192.168.131.133:4747/video")
ws, hs = 1200, 700
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

port = "COM5"
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s')  # pin 9 Arduino
servo_pinY = board.get_pin('d:10:s')  # pin 10 Arduino

detector = FaceDetector()
servoPos = [90, 90]  # initial servo position

while True:
    success, img = cap.read()
    if not success:
        continue

    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]

        # Convert coordinates to servo degree
        servoX = np.interp(fx, [0, ws], [0, 180])
        servoY = np.interp(fy, [0, hs], [0, 180])

        servoX = max(0, min(180, servoX))
        servoY = max(0, min(180, servoY))

        servoPos[0] = servoX
        servoPos[1] = servoY

        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        cv2.putText(img, str(pos), (fx+15, fy-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)
        cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "TARGET LOCKED", (50, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    else:
        cv2.putText(img, "NO TARGET", (50, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)

    cv2.putText(img, f'Servo X: {int(servoPos[0])}°', (20, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])}°', (20, 80), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    servo_pinX.write(servoPos[0])
    servo_pinY.write(servoPos[1])

    # Resize frame to be very small (300x200)
    img_resized = cv2.resize(img, (300, 200))

    cv2.imshow("Image", img_resized)
    cv2.waitKey(1)
