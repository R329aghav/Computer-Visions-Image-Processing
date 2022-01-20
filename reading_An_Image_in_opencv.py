import cv2
img=cv2.imread("lena.jpg",0)
cv2.imshow("image",img)
k = cv2.waitKey(5000)
if(k == 27):
    cv2.destroyAllWindows()
elif k==ord('r'):
    cv2.imwrite("lena_copy_3.png",img)
    cv2.destroyWindow()
