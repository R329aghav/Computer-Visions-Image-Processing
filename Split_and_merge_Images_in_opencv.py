import cv2

import numpy as np
# img2=cv2.imread("lena.jpg")
img=cv2.imread("messi5.jpg")
img2=cv2.imread("leuvenB.jpg")

print(img.shape)#returns a tuple of number of rows and number of columns and channels
print(img.size)#returns total number of pixels is accesed
print(img.dtype)#returns image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[280:340,330:390]
img[273:333,100:160]=ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img,(512,512))
# dest=cv2.add(img2,img)
dest=cv2.addWeighted(img,.2,img2,.8,0)
cv2.imshow("image",dest)
cv2.waitKey(0)
cv2.destroyAllWindows()
