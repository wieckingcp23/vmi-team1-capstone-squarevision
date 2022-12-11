import cv2
import tkinter
from tkinter import *
from tkinter import ttk



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


    while True:
        success, img = cap.read()
        #confidence threashold = how sure the algo is that an object is an object
        classIds, confs, bbox = net.detect(img, confThreshold = x)
        print(classIds, bbox)

        if len(classIds) != 0:

            for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)




        cv2.imshow("Square Vision", img)
        cv2.waitKey(1)

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

#sets the value that determines internal or external camera
def setVid(value):
    global vid
    vid = value

#slider output
def change(val):
    global x
    x = int(val)/100
    return x


master = tkinter.Tk("Cap")
master.title("Capstone Sprint 2")
master.configure(bg='lightgrey')
master.geometry('450x450')

L1 = ttk.Label(master, text="Fall 2022 Pre-Capstone").grid(column=0, row=0)
L2 = ttk.Label(master, text="Team 1").grid(column=0, row=1)


#These are the start up buttons
buttonCustom = ttk.Button(master, text='Start Custom Settings', command=lambda:start()).grid(column = 1, row = 20)
buttonDefault = ttk.Button(master, text='Start Default Settings', command=lambda:default()).grid(column = 1, row = 22)
L3 = ttk.Label(master, text= "Run Custom Settings             ->").grid(column=0, row=20)
L4 = ttk.Label(master, text= "Run Default Settings             ->").grid(column=0, row=22)

#Camera variable selection buttons - working (somehow)
internal = ttk.Button(master, text="Internal Camera", command=lambda:setVid(0)).grid(column = 1, row = 10)
external = ttk.Button(master, text="External Camera", command=lambda:setVid(1)).grid(column = 1, row = 11)
L5 = ttk.Label(master, text= "Use Internal Camera             ->").grid(column=0, row=10)
L6 = ttk.Label(master, text= "Use External Camera             ->").grid(column=0, row=11)

#Confidence Threashold selection with slider (DID NOT WORK) - NOW IS WORKING (HOW????)
s1 = Scale(master, from_ = 1, to = 99, orient = HORIZONTAL, command=change).grid(column=1, row=2)


#Confidence Threashold selection with User input (NOT WORKING)
#L7 = ttk.Label(master, text="Adjust Confidence Threashold").grid(column=0, row=2)
#num = ttk.Label(master, text="Enter a Number from 0.0 to 0.99 ").grid(column =1, row =1)
#e1 = ttk.Entry(master).grid(column=1, row=2)

master.mainloop()