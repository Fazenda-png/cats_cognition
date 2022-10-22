import cv2 as cv

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

cascade = cv.CascadeClassifier("treinamento/cascade.xml")

while True:
