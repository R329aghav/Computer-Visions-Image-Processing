import cv2
import numpy as np
# img=cv2.imread("messi5.jpg",1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(0,255,0),10)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,255),10)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"open cv",(10,500),font,4,(155,233,56),cv2.LINE_AA)


cv2.imshow("image",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
