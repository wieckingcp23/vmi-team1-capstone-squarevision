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
        classIds, confs, bbox = net.detect(img, confThreshold = .5)
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

#slider output - returns a float (not in use rn)
def change(val):
    x = int(val)/100
    conf = x
    print(conf)
    return conf


master = tkinter.Tk("Cap")
master.title("Capstone Sprint 2")
master.configure(bg='lightgrey')
master.geometry('450x450')

#These are the start up buttons
buttonCustom = ttk.Button(master, text='Start Program', command=lambda:start())
buttonDefault = ttk.Button(master, text='Default Settings', command=lambda:default())

#Camera variable selection buttons - working (somehow)
internal = ttk.Button(master, text="Internal Camera", command=lambda:setVid(0))
external = ttk.Button(master, text="External Camera", command=lambda:setVid(1))

#Confidence Threashold selection with slider (DID NOT WORK)
#s1 = Scale(master, from_ = 1, to = 99, orient = HORIZONTAL, command=change)
#s1.grid(column=1, row=2)
#s1.grid(column = 10, row = 70)

#Confidence Threashold selection with User input
L3 = ttk.Label(master, text="Adjust Confidence Threashold").grid(column=1, row=1)
num = ttk.Label(master, text="Enter a Number from 0.0 to 0.99 ").grid(column =1, row =2)
e1 = ttk.Entry(master).grid(row=4, column=2)

internal.grid(column = 1, row = 5)
external.grid(column = 1, row = 5)

buttonCustom.grid(column = 5, row = 30)
buttonDefault.grid(column = 5, row = 30)

L1 = ttk.Label(master, text="Fall 2022 Pre-Capstone").grid(column=5, row=0)

L2 = ttk.Label(master, text="Team 1").grid(column=3, row=1)



master.mainloop()