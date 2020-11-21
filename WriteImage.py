import  cv2 as cv

img = cv.imread("Ronaldo.jpg", 1)

cv.imshow("Image", img)

#Create a new image

cv.imwrite("New-Ronaldo.png", img)

cv.waitKey(0)
