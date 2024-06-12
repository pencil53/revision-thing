import cv2

haarcascade = "left eye.xml"

eye_camera = cv2.VideoCapture(0)

eyecascade = cv2.CascadeClassifier(haarcascade)

while True:
    status,frame = eye_camera.read()
    grey_eye = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes = eyecascade.detectMultiScale(grey_eye)

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0), 3)


    cv2.imshow("eye detection", frame)
    if cv2.waitKey(10) == 27:
        break