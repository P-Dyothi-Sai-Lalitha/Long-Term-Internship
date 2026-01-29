import cv2
import numpy as np
img = cv2.imread(r"Images/blank.jpg",1)

cv2.rectangle(img,(50,70),(200,50), (0,0,0),5)
#to draw a rectangle. it has 6 parameters 6parameters
#para1 = img(Varable)
#para2 = start point
#para3 = end point
#para4 = color(color code is in BGR)
#para5 = thickness
#para6 = line_type

cv2.circle(img,(200,200),(50),(0,0,255),3)
#to draw a circle. it has 6 parameters 6parameters
#para1 = img(Variable)
#para2 = center
#para3 = radius
#para4 = color(color code is in BGR)
#para5 = thickness
#para6 = line_type

cv2.rectangle(img,(200,100),(100,200), (0,0,0),5)

#distance between the parameters should be same
#1st and 2nd parameter should be reversed

print(img)

cv2.imshow('Shapes',img)

cv2.imwrite(r"Images/drawing_shapes.jpg",img)

#imwwrite() is used to save image
#first parameter is the filename(path)
#second parameer is the image/variable that is stored 
cv2.waitKey(0)
cv2.destroyAllWindows()
