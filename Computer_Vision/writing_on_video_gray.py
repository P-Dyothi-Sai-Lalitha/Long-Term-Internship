import cv2

cam = cv2.VideoCapture(r"Images\Tang_Li_Ci.mp4")

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_gray.mp4", fourcc, fps,
                      (frame_width, frame_height), isColor=False)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw everything on GRAY frame
    cv2.putText(gray, "Tang Li Ci", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 3)

    cv2.line(gray, (55, 65), (220, 65), 255, 3)
    cv2.rectangle(gray, (220, 20), (280, 50), 255, 2)
    cv2.rectangle(gray, (290, 20), (320, 50), 255, 2)
    cv2.circle(gray, (30, 30), 20, 255, 3)

    cv2.imshow("Grayscale Video", gray)
    out.write(gray)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
