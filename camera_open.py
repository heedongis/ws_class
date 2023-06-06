import cv2
from datetime import datetime
from save_to_s3 import get_file


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# Wide  1024X576
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)
w = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)

while webcam.isOpened():
    now = datetime.now()

    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        # frame1 = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        get_file(frame)
        # print(type(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
