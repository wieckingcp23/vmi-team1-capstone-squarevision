import cv2
import tkinter
from tkinter import *
from tkinter import ttk




def start():
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
        classIds, confs, bbox = net.detect(img, confThreshold=0.5)
        print(classIds, bbox)

        if len(classIds) != 0:

            for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)




        cv2.imshow("Square Vision", img)
        cv2.waitKey(1)


window = tkinter.Tk("Cap")
window.configure(bg='lightgrey')

window.geometry('400x400')

L1 = ttk.Label(window, text="PreCapstone")
L1.grid(column=0, row=0)


WLabel = ttk.Label(window, text="     Sprint 1     ")

WLabel.grid(column=10, row=10)


button = ttk.Button(window, text='Start Program', command=lambda:start())


button.grid(column = 20, row = 30)

L2 = ttk.Label(window, text="     Fall 2022    ")
L2.grid(column=10, row=40)

L3 = ttk.Label(window, text="     Team 1     ")
L3.grid(column=0, row=50)


window.mainloop()


