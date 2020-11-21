import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture("Play.mp4")

while cap.isOpened():
    _, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_RGBA2GRAY)
    face_detect =face_cascade.detectMultiScale(gray_img,1.1, 10)

    for(x, y, w, h) in face_detect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=2 )

        cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()