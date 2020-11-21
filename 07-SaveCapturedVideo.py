import cv2 as cv

cap = cv.VideoCapture(0)
FourCC = cv.VideoWriter_fourcc(*"DIVX")#Using this fourcc, we are transfer the data to avi video output.
result = cv.VideoWriter("Output.avi", FourCC, 20.0, (640, 480))#Create a screen video using fourcc data.

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        result.write(frame)

        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
result.release()
cv.destroyAllWindows()