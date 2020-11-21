import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.isOpened())#When the VideoCapture(1), Then result will be false because we dont have index 1 camera.But when the VideoCapture(1), Then result will be true.

while(cap.isOpened()):
    ret, frame = cap.read()

    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))#Print width of frame
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#Print height of frame

    cv.imshow("Frame", frame)


    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()