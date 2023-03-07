import tkinter as tk
import cv2
from tkinter import *
from PIL import ImageTk, Image
import time
import datetime


def toInput():
    global y
    y=txtTimer.get("1.0","end-1c")
 

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
        startTime = 0
        while total_seconds > 0:
            currentTime = time.time()
            fps = 1/(currentTime - startTime)
            startTime = currentTime

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
                    
            
            cv2.putText(img, "FPS: " + str(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.imshow("Square Vision", img)
            cv2.waitKey(1)
               
    countdown(y)
    
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

    startTime = 0

    (success, image) = cap.read()

    while True:
        currentTime = time.time()
        fps = 1/(currentTime - startTime)
        startTime = currentTime
        success, img = cap.read()

        #confidence threashold = how sure the algo is that an object is an object
        classIds, confs, bbox = net.detect(img, confThreshold= 0.5)
        print(classIds)

        if len(classIds) != 0:

            for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)

        cv2.imshow("Square Vision", img)
        cv2.putText(img, "FPS: " + str(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        (success, image) = cap.read()
    
    cv2.destroyAllWindows()


#GUI Stuff
root = tk.Tk()
root.geometry("900x500")
root.title("Square Vision")


#Frame Grid
lblFrame = tk.Frame(root)
lblFrame.columnconfigure(0, weight=1)
lblFrame.columnconfigure(1, weight=1)
lblFrame.columnconfigure(2, weight=1)

label = tk.Label(lblFrame, text="Square Vision v.5.0", font=('Arial', 18))
label.grid(row=0, column=1, sticky =tk.W+tk.E)
label2 = tk.Label(lblFrame, text="Sprint 5", font=('Arial', 14))
label2.grid(row=1, column=1, sticky =tk.W+tk.E)
label3 = tk.Label(lblFrame, text="CIS 490 Capstone | 3/9/23", font=('Arial', 12))
label3.grid(row=2, column=1, sticky =tk.W+tk.E)
lblFrame.pack()

image=Image.open('vmi.png')
image2=image.resize((75,75),Image.ANTIALIAS)
newImage =ImageTk.PhotoImage(image2)

lbl = tk.Label(lblFrame, image=newImage)
lbl.grid(row=0, column=0, sticky =tk.W+tk.E)

image3=Image.open('vmi.png')
image4=image3.resize((75, 75),Image.ANTIALIAS)
newImage2 =ImageTk.PhotoImage(image4)
lbl2 = tk.Label(lblFrame, image=newImage2)
lbl2.grid(row=0, column=2, sticky =tk.W+tk.E)


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)


#Camera GUI as Radiobuttons
rblbl = tk.Label(buttonFrame, text = "Select Internal Camera or External Camera:", font =('Arial', 13))
rblbl.grid(row=0, column=0, sticky =tk.W+tk.E)
rb1 = Radiobutton(buttonFrame, text = "Internal Camera", command=lambda:setVid(0))
rb1.grid(row=0, column=1, sticky =tk.W+tk.E)
rb2 = Radiobutton(buttonFrame, text = "External Camera", command=lambda:setVid(1))
rb2.grid(row=1, column=1, sticky =tk.W+tk.E)


#Internal Camera GUI
lblInternal = tk.Label(buttonFrame, text = "Use Internal Camera", font =('Arial', 13))
lblInternal.grid(row=0, column=0, sticky =tk.W+tk.E)
btninternal = tk.Button(buttonFrame, text="Internal Camera", command=lambda:setVid(0), activebackground='#4444ff')
btninternal.grid(row=0, column=1, sticky =tk.W+tk.E)
lblIntInst = tk.Label(buttonFrame, text="Uses the system's internal camera", font=('Arial', 10))
lblIntInst.grid(row=0, column=2, sticky =tk.W)
def on_enter(e):
    btninternal['background'] = 'grey'

def on_leave(e):
    btninternal['background'] = 'SystemButtonFace'

#External Camera GUI
lblExternal= tk.Label(buttonFrame, text = "Use External Camera", font =('Arial', 13))
lblExternal.grid(row=1, column=0, sticky =tk.W+tk.E)
btnExternal = tk.Button(buttonFrame, text="External Camera", command=lambda:setVid(1), activebackground='#4444ff')
btnExternal.grid(row=1, column=1, sticky =tk.W+tk.E)
lblExtInst = tk.Label(buttonFrame, text="Uses an external camera", font=('Arial', 10))
lblExtInst.grid(row=1, column=2, sticky =tk.W)
lblExtInst.grid(row=1, column=2, sticky =tk.W)


def on_enter(e):
    btnExternal['background'] = 'grey'

def on_leave(e):
    btnExternal['background'] = 'SystemButtonFace'


#Confidence Threashold GUI
lblConf = tk.Label(buttonFrame, text="Adjust Confidence Threashold", font=('Arial', 13))
lblConf.grid(row=2, column=0, sticky =tk.W+tk.E)
sliderConf = Scale(buttonFrame, from_ = 1, to = 100, orient = HORIZONTAL, command=change)
sliderConf.grid(row=2, column=1, sticky =tk.W+tk.E)
check = sliderConf.get()
if (check > 60.0):
    root.messagebox.showinfo("Warning: A confidence threshold this high can slow down your computer, or even crash it")
lblConfInst = tk.Label(buttonFrame, text="Confidence Threashold is how confident the\n algorithm is at identifing objects", font=('Arial', 10))
lblConfInst.grid(row=2, column=2, sticky =tk.W)

#timer GUI
lblTimer = tk.Label(buttonFrame, text = "Set Timer (in Seconds)", font=('Arial', 13))
lblTimer.grid(row=3, column=0,sticky =tk.W+tk.E)
txtTimer = tk.Text(buttonFrame,height = .5, width = 1, font=('Arial', 13))
txtTimer.grid(row=3, column=1,sticky =tk.W+tk.E)
btnTimer = tk.Button(buttonFrame, text = "Enter", command=lambda: toInput(), activebackground='#4444ff')
btnTimer.grid(row=3, column=2, sticky =tk.W+tk.E)

#Spacer 
lblSpace = tk.Label(buttonFrame)
lblSpace.grid(row=4, column=0,sticky =tk.W+tk.E)
lblSpace2 = tk.Label(buttonFrame)
lblSpace2.grid(row=5, column=2, sticky =tk.W+tk.E)

#Execution GUI
btnCustom = tk.Button(buttonFrame, text="Custom Settings", command=lambda:start(), font=('Arial', 14))
btnCustom.grid(row=6, column=0,sticky =tk.W+tk.E)
def on_enter(e):
    btnCustom['background'] = 'grey'

def on_leave(e):
    btnCustom['background'] = 'SystemButtonFace'
btnDefault = tk.Button(buttonFrame, text="Default Settings", command=lambda:default(), font=('Arial', 14))
btnDefault.grid(row=6, column=2, sticky =tk.W+tk.E)
def on_enter(e):
    btnDefault['background'] = 'grey'

def on_leave(e):
    btnDefault['background'] = 'SystemButtonFace'
lblDefaultDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50%\nTimer Duration = Infinite", font=('Arial', 13), anchor="w")
lblDefaultDes.grid(row=7, column=2, sticky =tk.N)


buttonFrame.pack(fill = 'x')
#buttonFrame.pack()



root.mainloop()
