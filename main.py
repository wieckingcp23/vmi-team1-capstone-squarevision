import tkinter as tk
import cv2
from tkinter import *
from PIL import ImageTk, Image
import time
import datetime


def toInput():
    global y
    y=textbox.get("1.0","end-1c")
 

#sets the value that determines internal or external camera
def setVid(value):
    global vid
    vid = value

#slider output
def change(val):
    global x
    x = int(val)/100
    return x

#this is where we will let the user customize options
def start():
    cap = cv2.VideoCapture(vid)
    cap.set(3, 640)
    cap.set(4, 480)
    classNames = []
    classFile = 'coco.names'
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    
    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'
    
    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    def countdown(s):
        total_seconds = int(s)
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            print(timer, end="\r")
            time.sleep(.001)
            total_seconds -=.1
            
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold = x)
            #print(classIds, bbox)
            
            if len(classIds) != 0:
                
                for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                    cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)
                    
            cv2.imshow("Square Vision", img)
            cv2.waitKey(1)
    
    countdown(y)
       

# This is the orginial scrpit - do not change
def default():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    classNames = []
    classFile = 'coco.names'
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)


    while True:
        success, img = cap.read()
        #confidence threashold = how sure the algo is that an object is an object
        classIds, confs, bbox = net.detect(img, confThreshold= 0.5)
        print(classIds, bbox)

        if len(classIds) != 0:

            for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)




        cv2.imshow("Square Vision", img)
        cv2.waitKey(1)
#
#
#
#
#
#
#
#GUI Stuff
root = tk.Tk()

root.geometry("900x500")
root.title("Square Vision")


lblFrame = tk.Frame(root)
lblFrame.columnconfigure(0, weight=1)
lblFrame.columnconfigure(1, weight=1)
lblFrame.columnconfigure(2, weight=1)

label = tk.Label(lblFrame, text="Square Vision", font=('Arial', 18))
label.grid(row=0, column=1, sticky =tk.W+tk.E)
#label.pack(padx=20, side = TOP, anchor = N)
label2 = tk.Label(lblFrame, text="Sprint 3", font=('Arial', 14))
label2.grid(row=1, column=1, sticky =tk.W+tk.E)
label3 = tk.Label(lblFrame, text="CIS 490 Capstone | 1/31/23", font=('Arial', 12))
label3.grid(row=2, column=1, sticky =tk.W+tk.E)
lblFrame.pack()

image=Image.open('vmi.png')
image2=image.resize((100,100),Image.ANTIALIAS)
newImage =ImageTk.PhotoImage(image2)
lbl = tk.Label(lblFrame, image=newImage)
lbl.grid(row=0, column=0, sticky =tk.W+tk.E)

#image3=Image.open('denis.jpg')
image3=Image.open('vmi.png')
image4=image3.resize((100,100),Image.ANTIALIAS)
newImage2 =ImageTk.PhotoImage(image4)
lbl2 = tk.Label(lblFrame, image=newImage2)
lbl2.grid(row=0, column=2, sticky =tk.W+tk.E)


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)



label4 = tk.Label(buttonFrame, text = "Use Internal Camera", font =('Arial', 13))
label4.grid(row=0, column=0, sticky =tk.W+tk.E)
internal = tk.Button(buttonFrame, text="Internal Camera", command=lambda:setVid(0))
internal.grid(row=0, column=1, sticky =tk.W+tk.E)


label5 = tk.Label(buttonFrame, text = "Use Internal Camera", font =('Arial', 13))
label5.grid(row=1, column=0, sticky =tk.W+tk.E)
external = tk.Button(buttonFrame, text="External Camera", command=lambda:setVid(1))
external.grid(row=1, column=1, sticky =tk.W+tk.E)

lblB = tk.Label(buttonFrame, text="Uses the system's internal camera", font=('Arial', 10))
lblB.grid(row=0, column=2, sticky =tk.W)
lblD = tk.Label(buttonFrame, text="Uses an external camera", font=('Arial', 10))
lblD.grid(row=1, column=2, sticky =tk.W)


label6 = tk.Label(buttonFrame, text="Adjust Confidence Threashold", font=('Arial', 13))
label6.grid(row=2, column=0, sticky =tk.W+tk.E)
s1 = Scale(buttonFrame, from_ = 1, to = 100, resolution =2, orient = HORIZONTAL, command=change)
s1.grid(row=2, column=1, sticky =tk.W+tk.E)
lblC = tk.Label(buttonFrame, text="Confidence Threashold is how confident the\nalgorithm is at identifing objects", font=('Arial', 10))
lblC.grid(row=2, column=2, sticky =tk.W+tk.E)

lbl7 = tk.Label(buttonFrame, text = "Set Timer (in Seconds)", font=('Arial', 13))
lbl7.grid(row=3, column=0,sticky =tk.W+tk.E)
textbox = tk.Text(buttonFrame,height = .5, width = 1, font=('Arial', 13))
textbox.grid(row=3, column=1,sticky =tk.W+tk.E)
btnTxt = tk.Button(buttonFrame, text = "Enter", command=lambda: toInput())
btnTxt.grid(row=3, column=2, sticky =tk.W+tk.E)


label9 = tk.Label(buttonFrame)
label9.grid(row=4, column=0,sticky =tk.W+tk.E)
label10 = tk.Label(buttonFrame)
label10.grid(row=5, column=2, sticky =tk.W+tk.E)

custom = tk.Button(buttonFrame, text="Custom Settings", command=lambda:start(), font=('Arial', 14))
custom.grid(row=6, column=0,sticky =tk.W+tk.E)

btndefault = tk.Button(buttonFrame, text="Default Settings", command=lambda:default(), font=('Arial', 14))
btndefault.grid(row=6, column=2, sticky =tk.W+tk.E)

lblDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50%\nTimer Duration = Infinite", font=('Arial', 13), anchor="w")
lblDes.grid(row=7, column=2, sticky =tk.N)

""" image35=Image.open('denis.jpg')
image45=image35.resize((100,100),Image.ANTIALIAS)
newImage25 =ImageTk.PhotoImage(image45)
dj = tk.Label(buttonFrame, image=newImage25)
dj.grid(row=7, column=0, sticky =tk.W+tk.E) """



#buttonFrame.pack(fill = 'x')
buttonFrame.pack()



root.mainloop()