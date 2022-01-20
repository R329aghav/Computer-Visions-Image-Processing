import cv2
from matplotlib import pyplot as plt
import numpy as np
# img=cv2.imread("sudoko.jpg")
img=cv2.imread("messi5.jpg",0)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3,)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelcombined=cv2.bitwise_or(sobelX,sobely)
canny=cv2.Canny(img,100,200)
titles=['img','lap','sobelx','sobely','sobelcombined','canny']
image=[img,lap,sobely,sobelX,sobelcombined,canny]
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
