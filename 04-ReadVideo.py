import cv2 as cv

#Create variable for video assign from in the PC 0th ip camera
#cap = cv.VideoCapture(0)

#This how we need to read the external video
cap = cv.VideoCapture("play.mp4")

#Using pc ip camera showing the output using the  imshow()
while(True):
    ret, frame = cap.read() #Read the ip camera or external video input and assign to the frame

    cv.imshow("Video Frame", frame)

#When the user press the e button, then that window will be close
    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()