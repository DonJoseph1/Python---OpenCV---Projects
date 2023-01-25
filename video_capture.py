from tabnanny import check
import cv2, time

video=cv2.VideoCapture(0)

while True:

    a=a+1
    check, frame = video.read()

    print(type(check))
    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",gray)

    #Python waiting for you to  press a key
    key=cv2.waitKey(1)

    if key ==ord('q'):
        break

#Number of frames
print(a)

#Stop Videoq
video.release()
cv2.destroyAllWindowsd