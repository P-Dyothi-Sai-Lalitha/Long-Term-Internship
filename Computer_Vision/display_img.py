import cv2

img = cv2.imread("Images\watermelon.jpg",0)

#imread()takes 2 parameters
#1st parameter is image path
#2nd parameter is flag
# GO to properties of image and then security and copy the objectname from images folder

print(img)

cv2.imshow('window_name',img)
#imshow()displays the image
#imshow takes 2 parameter
#first parameter is window name
#2nd parameter is variable name

cv2.waitKey(0)
#waitKey(0) allows theimage to not close after opening
#0 is used to close only whem we click x button
#any number other than 0 closes the window in that milliseconds

#-215 Assesertion Error image proper not read properly
#unicode error , then place "r" before the quotes near the path

cv2.destroyAllWindows()
#if the picture doesn't close and show "not responding" then use the above command
#if parameters is null, then all windos are closed
#if parameters i.e window name is given then only that window closes

#task = display two images, add, and display
