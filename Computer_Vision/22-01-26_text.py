import cv2
import numpy as np
img = cv2.imread(r"Images/blank.jpg",1)
cv2.putText(img,"Hello World",(200,200),1,2,(0,0,0))

#to draw a line. it has 6 parameters 6parameters
#para1 = img(Varable)
#para2 = text
#para3 = coordinates
#para4 = font number
#para5 = fontsize
#para6 = color
#para7 = bold/italic
print(img)

cv2.imshow('Text',img)
#cv2.imwrite(r"Images/Text_file.jpg",img)

#imwwrite() is used to save image
#first parameter is the filename(path)
#second parameer is the image/variable that is stored 
cv2.waitKey(0)
cv2.destroyAllWindows()
