import cv2
import numpy as np
img1 = cv2.imread(r"Images/lavender.jpg",1)
img2 = cv2.imread(r"Images/lavender.jpg",1)
img3 = img1+img2
print(img3)

cv2.imshow('Lavender',img3)

cv2.imwrite(r"Images/new_lavender.jpg",img3)
#imwwrite() is used to save image
#first parameter is the filename(path)
#second parameer is the image/variable that is stored 
cv2.waitKey(0)
cv2.destroyAllWindows()
