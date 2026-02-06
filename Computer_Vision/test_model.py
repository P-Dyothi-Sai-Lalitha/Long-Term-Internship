import cv2

face_cascade = cv2.CascadeClassifier(r"data\haarcascade_frontalface_default.xml")
model = cv2.face.LBPHFaceRecognizer_create()
model.read('face_model.yml')

name = {1:'Gousia', 2:'Sankeerthana', 3:'Agnes', 4:'Teju'}

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for(x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face,(200,200))
        label, confidence = model.predict(face)
        if confidence < 80 and label in name:
            text = name[label]
        else:
            text = 'unknown'
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 255), 1)
        cv2.putText(frame, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    cv2.imshow('frame_window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
