import cv2
import time
from send_email import send_email

video = cv2.VideoCapture(1)
time.sleep(1.5)


first_frame = None
status_arr = []
while True:
    status = 0
    check, frame = video.read()
    # gray scaling
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gauss = cv2.GaussianBlur(gray_frame, (21,21), 0)

    # captured the first frame
    if first_frame is None:
        first_frame = gray_frame_gauss

    delta_frame = cv2.absdiff(first_frame, gray_frame_gauss)

    thres_frame = cv2.threshold(delta_frame, 50, 255,
                                cv2.THRESH_BINARY)[1]

    dil_frame = cv2.dilate(thres_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if rectangle.any():
            status = 1

    status_arr.append(status)
    status_arr = status_arr[-2:]

    if len(status_arr) > 1 :
        if status_arr[0] == 1 and status_arr[1] == 0:
            send_email()
        print(status_arr)

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()