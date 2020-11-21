import cv2 as cv

cap = cv.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    #Get into the data from frame vairable and convert the data to gray output using cv.COLOR_BGR2GRAY
    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Frame", gray_vid)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()