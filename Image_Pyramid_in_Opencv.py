# there are two pyramids methods 1 is gaussian pyramid and laplacian pyramid
#gaussian pyramid -->repeat filtering and subsampling
#blend the images and reconstruction of image
import  cv2
import numpy as np
from matplotlib import  pyplot as plt
img=cv2.imread('messi5.jpg')
# we have two methods on gaussian pyramids
# pyrDown,pyrUp
layer=img.copy()
gp=[layer]


for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)
layer=gp[5]
cv2.imshow("upper lavel Gaussian Pyramid",layer)
lp=[layer]
for i in range(5,0,-1):
    gaussian_expended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_expended)
    cv2.imshow(str(i),laplacian)
# lr=cv2.pyrDown(img)
# lr1=cv2.pyrDown(lr)
# lr2=cv2.pyrDown(lr1)
# hr=cv2.pyrUp(lr2)
cv2.imshow("Original Image",img)
# cv2.imshow("lr",lr)
# cv2.imshow("lr1",lr2)
# cv2.imshow("lr2",lr2)
# cv2.imshow("hr",hr)

cv2.waitKey(0)
cv2.destroyAllWindows()
