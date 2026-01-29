import cv2
import os
face_cascade = cv2.CascadeClassifier(r"data\haarcascade_frontalface_default.xml")

user_id = input('Enter user id:')
save_path = f"dataset/user_{user_id}"
os.makedirs(save_path, exist_ok = True)
cam = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cam.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors = 5,
                                     minSize = (30,30))

    for (x,y,w,h) in face:
        count +=1
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (200,200))
        cv2.imwrite(f'{save_path}/{count}.jpg', face_img)

    cv2.imshow("faces", frame)       
    if cv2.waitKey(1)& 0xFF == ord('q') or count >= 50:
        break

cv2.destroyAllWindows()
