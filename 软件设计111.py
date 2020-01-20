import cv2
import numpy as np
import time
mx=0
my=0
flaglbt=0
input_movie = cv2.VideoCapture("shipin1.mp4")
ret, frame = input_movie.read()
cv2.imshow("frame",frame)
frame1=frame.copy()
h,w,c=frame.shape
events=[i for i in dir(cv2) if 'EVENT'in i]
print(events)
font=cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import serial
import serial.tools.list_ports
import time

def draw_rectangle(event,x,y,flags,param):
    global mx,my,flaglbt
    if event==cv2.EVENT_LBUTTONDOWN:
        print("mouse clickhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        flaglbt=1
        mx=x
        my=y
        
def getinspos(frame):
    global mx,my
    #print("I will find the instruments.")
    return mx,my    

cv2.setMouseCallback('frame', draw_rectangle)

def getmicnum(x1):
    return 1

def sendcmdtomic(n):
    #print("I will find the instruments somewhere.")
    return 1

def getsingpos(frame):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #print("I will find the singer.")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (xf,yf,wf,hf) in faces:
        frame = cv2.rectangle(frame,(xf,yf),(xf+wf,yf+hf),(255,0,0),2)
        roi_gray = gray[yf:yf+hf, xf:xf+wf]
        roi_color = frame[yf:yf+hf, xf:xf+wf]
        if 0<xf<=w/4:
            cv2.circle(frame,(int(w/2-150),int(4*h/5)),30,(0,255,0),-1)
        if w/4<xf<=w/2:
            cv2.circle(frame,(int(w/2-50),int(4*h/5)),30,(0,255,0),-1)
        if w/2<xf<=3*w/4:
            cv2.circle(frame,(int(w/2+50),int(4*h/5)),30,(0,255,0),-1)
        if 3*w/4<xf<=w:
            cv2.circle(frame,(int(w/2+150),int(4*h/5)),30,(0,255,0),-1)

def getmicnum(x2):
    return 2
    
def xsendcmdtomic(m):
    #print("I will find the singer somewhere.")
    return 1

while True:
    ret, frame = input_movie.read()
    cv2.circle(frame,(int(w/2-150),int(4*h/5)),30,(0,255,0),1)
    cv2.circle(frame,(int(w/2-50),int(4*h/5)),30,(0,255,0),1)
    cv2.circle(frame,(int(w/2+50),int(4*h/5)),30,(0,255,0),1)
    cv2.circle(frame,(int(w/2+150),int(4*h/5)),30,(0,255,0),1)
 
    x1=getinspos(frame)
    n=getmicnum(x1)
    sendcmdtomic(n)
    print("\n")
    x2=getsingpos(frame)
    m=getmicnum(x2)
    xsendcmdtomic(m)
    if flaglbt==1:
        print("drawrectanglehhhhhhhhhhhhhhhhhhhhh")
        cv2.rectangle(frame,(mx,my),(mx+100,my+100),(0,255,0),1)
        if 0<mx<=w/4:
            cv2.circle(frame,(int(w/2-150),int(4*h/5)),30,(0,255,0),-1)
        if w/4<mx<=w/2:
            cv2.circle(frame,(int(w/2-50),int(4*h/5)),30,(0,255,0),-1)
        if w/2<mx<=3*w/4:
            cv2.circle(frame,(int(w/2+50),int(4*h/5)),30,(0,255,0),-1)
        if 3*w/4<mx<=w:
            cv2.circle(frame,(int(w/2+150),int(4*h/5)),30,(0,255,0),-1)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(0)
        flaglbt=0
    cv2.imshow('frame', frame)
    key = cv2.waitKey(100)


print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Silicon" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)

def run():
    action= "empty"
    while action != "q":
        print ('q for quit,others for command')
        a = input("> ")
        ser.write(a.encode())
        time.sleep(1)

run()


cv2.waitKey(500)
input_movie.release()
cv2.destroyAllWindows()
