import cv2
import numpy as np
import datetime
cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("frame",fourcc,20,(640,480))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.isOpened())
while(cap.isOpened()):
    ret , frame = cap.read()
    if( ret == True):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='WIDTH: '+ str(cap.get(3)) + 'HEIGHT: '+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,244),2,cv2.LINE_AA)
        cv2.imshow("frame",frame)
        if cv2.waitKey(0) & 0xFF == ord('r'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
