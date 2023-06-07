import time


import cv2
from datetime import datetime
from save_to_s3 import get_file
import threading





def get_image(filename, img):
    cv2.imwrite('./imgs/' + filename + '.png', img)
    threading.Timer(5, get_image).start()






if __name__ == '__main__':
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    # Wide  1024X576
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)

    fps = webcam.get(cv2.CAP_PROP_FPS)
    w = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("Width: " + w)
    print("Height: " + h)
    print("FPS: " + fps)

    while webcam.isOpened():

        now = datetime.now()
        status, frame = webcam.read()

        ##### ROI SETTING ######
        # x, y, width, height = 100, 100, 200, 200
        # roi = frame[y:y+height, x:x+width]

        # if (int(webcam.get(1)) % fps == 0):
        # cv2.imwrite('./imgs/' + str(now.strftime('%Y%m%d%H%M%S%f')) + '.png', frame)
        if status:
            cv2.imshow("test", frame)

        if cv2.waitKey(1) & 0xFF == ord('t'):
            # frame1 = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            get_file(frame)
            # print(type(frame))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
