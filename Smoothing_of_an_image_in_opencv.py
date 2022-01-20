import cv2
import  numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('leuvenB.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dest=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gfilter=cv2.GaussianBlur(img,(5,5),0)
mf=cv2.medianBlur(img,5)#always take kernel odd except 1
bilateralfilter=cv2.bilateralFilter(img,9,75,75)
titles=['image','2d convolution','blur','gfilter','mf','bilateralfilter']
image=[img,dest,blur,gfilter,mf,bilateralfilter]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
