import cv2
import numpy as np
cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("frame",fourcc,20,(640,480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1200)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,400)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1200)
cap.set(4,700)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame =cap.read()
    if ret == True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray)
        if cv2.waitKey(0) & 0xFF == ord('r'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
