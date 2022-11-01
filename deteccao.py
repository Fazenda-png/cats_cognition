import cv2 as cv

camera = cv.VideoCapture("cats.mp4")
cascade = cv.CascadeClassifier("treinamento/cascade.xml")
while True:
    
    _, imagem = camera.read()
    gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    objetos = cascade.detectMultiScale(gray, 1.25, 5)

    for (x,y,w,h) in objetos:
        cv.rectangle(imagem, (x,y),(x+w,y+h),(0,0,255),2)

    cv.imshow("Gato", imagem)
    k = cv.waitKey(60)
    if k == 27:
        break
    
cv.destroyAllWindows()
camera.release()