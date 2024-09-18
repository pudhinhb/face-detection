import cv2
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)      #loading algorithm
cam = cv2.VideoCapture(0)   #initializing cam
while True:
    _,img = cam.read()#reading frame from cam
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting color img to gray
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)    #getting coordinates

    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
    cv2.imshow("face Detection",img)

    key= cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()