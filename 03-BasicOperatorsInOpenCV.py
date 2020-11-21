import cv2 as cv

img = cv.imread("New-Ronaldo.png", 1)

cv.imshow("Image", img)

#Create a variable for the esc button in keyboard
e = cv.waitKey()

#How to add keyboard function for the program
#When the user press esc button that window will be close
if e == 27:
    cv.destroyAllWindows()
#When the user press the s button, the new image file will be create
elif e == ord("s"):
    cv.imwrite("The New-Ronaldo.png", img)
    cv.destroyAllWindows()