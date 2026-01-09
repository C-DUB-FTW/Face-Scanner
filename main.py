import cv2

caputre_cam = cv2.VideoCapture(0)
face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = caputre_cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        kW = 99
        kH = 99
        if kW % 2 == 0:
            kW -= 1
        if kH % 2 == 0:
            kH -= 1
        face_roi = frame[y:y+h, x:x+w]
        face_roi = cv2.GaussianBlur(face_roi, (kW, kH), 30)
        frame[y:y+h, x:x+w] = face_roi
        cv2.putText(frame, "Sexy", (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255))

    cv2.imshow('Face detect', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("z"):
        break

caputre_cam.release()
cv2.destroyAllWindows()