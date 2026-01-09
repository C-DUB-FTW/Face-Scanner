import cv2

caputre_cam = cv2.VideoCapture(0)

face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = caputre_cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detect.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)


    cv2.imshow('Face detect', frame)

    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

caputre_cam.release()
cv2.destroyAllWindows()
