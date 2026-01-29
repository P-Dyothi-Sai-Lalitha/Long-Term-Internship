import cv2

cam = cv2.VideoCapture("Images\Tang_Li_Ci.mp4")

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_colour.mp4v", fourcc, 20.0, (frame_width, frame_height))
while True:
    
    ret, frame = cam.read()
    cv2.putText(frame, "Tang Li Ci", (55, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 6)
    cv2.line(frame,(55,65), (220,65), (255,0,0),3)
    cv2.rectangle(frame,(220,20),(280,50), (255,0,0),2)
    cv2.rectangle(frame,(290,20),(320,50), (255,0,0),2)
    cv2.circle(frame,(30,30), 20,(255,0,0),3)
    out.write(frame)
    cv2.imshow("Tang Li Ci",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()
