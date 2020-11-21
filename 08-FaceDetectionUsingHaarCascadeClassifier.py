import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")#Access the cascade classifier

img = cv.imread("Team.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)#convert the color image to the gary color
face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 10) #Detecting the person

for (x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2) #Draw teh rectangle and create outline thick, color as Blue also

cv.imshow("Image", img)
cv.waitKey(0)