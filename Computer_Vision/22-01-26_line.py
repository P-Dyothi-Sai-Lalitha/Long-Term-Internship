import cv2
import numpy as np
img = cv2.imread(r"Images/blank.jpg",1)

cv2.line(img,(50,70),(200,50), (0,0,0),5)
#to draw a line. it has 6 parameters 6parameters
#para1 = img(Varable)
#para2 = start point
#para3 = end point
#para4 = color(color code is in BGR)
#para5 = thickness
#para6 = line_type
print(img)

cv2.imshow('line',img)
cv2.imwrite(r"Images/drawing_file.jpg",img)
#imwwrite() is used to save image
#first parameter is the filename(path)
#second parameer is the image/variable that is stored 
cv2.waitKey(0)
cv2.destroyAllWindows()
