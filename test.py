from Detector import *
import tkinter as tk
from tkinter import *
import customtkinter
import os

#Sets the input camera device + updates GUI
def setVid(x):
    global vid
    vid = x
    selection = "You have selected "
    if (x == 0):
        selection += "the Internal Camera"
    if (x == 1):
        selection += "the External Camera"
    lblRBOut.config(text = selection)

def number():
    try:
        y = int(txtConf.get())
        global conf
        conf = int(y)/100
        if (y <= 0):
            answer.config(text = "Confidence Threashold of " + txtConf.get() + " is too low",
                          background = "red", font=('Arial bold', 10))
        elif (y > 100):
            answer.config(text = "Confidence Threashold of " + txtConf.get() + " is too high",
                          background = "red", font=('Arial bold', 10))
        else:
            if (75 <= y <= 100):
                answer.config(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThis can limit the number of objects recognized", 
                              background = "yellow", font=('Arial bold', 10))
                return conf
            elif(1 <= y <= 25):
                answer.config(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThis can result in excessive feedback", 
                              background = "yellow", font=('Arial bold', 10))
                return conf
            else:
                answer.config(text = "Confidence Threashold = " + txtConf.get(), background = "light grey", font=('Arial', 10))
                return conf

    except ValueError:
        answer.config(text = "ERROR: " + txtConf.get() + " is an invalid input", background = "red", font=('Arial bold', 10))

def nms():
    try:
        p = int(txtNMS.get())
        global nms
        nms = int(p)/100
        print(nms)
        if (p <= 0):
            ansNMS.config(text = "A NMS Threashold of " + txtNMS.get() + " is too low",
                          background = "red", font=('Arial bold', 10))
        elif (p > 100):
            ansNMS.config(text = "A NMS Threashold of " + txtNMS.get() + " is too high",
                          background = "red", font=('Arial bold', 10))
        else:
            if (45 <= p <= 100):
                ansNMS.config(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis will limit the identification of close objects", 
                              background = "yellow", font=('Arial bold', 10))
                return nms
            elif(1 <= p <= 10):
                ansNMS.config(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis can result in excessive object tagging", 
                              background = "yellow", font=('Arial bold', 10))
                return nms
            else:
                ansNMS.config(text = "NMS Threashold = " + txtNMS.get(), background = "light grey", font=('Arial', 10))
                return nms
    
    except ValueError:
        ansNMS.config(text = "ERROR: " + txtNMS.get() + " is an invalid input", background = "red", font=('Arial bold', 10))


#Runs the default settings
def mainMode():
    videoPath = 0

    configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.onVideo()

def customMode():
    videoPath = 0

    configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.customVideo(vid, conf, nms)

#mainMode()

###########################################################
###########################################################
###########################################################
###########################################################
###########################################################

#GUI Stuff
root = tk.Tk()
root.geometry("900x500")
root.title("Square Vision")
#root.config(bg="light grey")
var = tk.StringVar()
#Frame Grid
lblFrame = tk.Frame(root)
lblFrame.columnconfigure(0, weight=1)
lblFrame.columnconfigure(1, weight=1)
lblFrame.columnconfigure(2, weight=1)
lblFrame.config(bg="light grey")

label = tk.Label(lblFrame, text="Square Vision 2D v.5.0", font=('Arial', 18))
label.grid(row=0, column=1, sticky =tk.W+tk.E)
label2 = tk.Label(lblFrame, text="Sprint 5 | Team 1", font=('Arial', 14))
label2.grid(row=1, column=1, sticky =tk.W+tk.E)
label3 = tk.Label(lblFrame, text="CIS 490 Capstone | 3/9/23", font=('Arial', 12))
label3.grid(row=2, column=1, sticky =tk.W+tk.E)
label4 = tk.Label(lblFrame, text="Welcome to Square vision, an object regcogniton software \nplease select how you would like to execute the program", 
                  font=('Arial', 13))
label4.grid(row=3, column=1, sticky =tk.W+tk.E)
label5 = tk.Label(lblFrame, text="", font=('Arial', 14))
label5.grid(row=4, column=1, sticky =tk.W+tk.E)


lblFrame.pack()

##########################################
# BUTTON PANE
##########################################
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)


##########################################
# CAMERA SELECTION
##########################################
lblCamera = tk.Label(buttonFrame, text="Select Camera",font=('Arial', 13))
lblCamera.grid(row=0, column=0, sticky =tk.E)
r1 = tk.Radiobutton(buttonFrame, text='Internal Camera', variable=var, value=0, command=lambda:setVid(0))
r1.grid(row=0, column=1, sticky =tk.W+tk.E)
r2 = tk.Radiobutton(buttonFrame, text='External Camera', variable=var, value=1, command=lambda:setVid(1))
r2.grid(row=1, column=1, sticky =tk.W+tk.E)
lblRBOut = tk.Label(buttonFrame, width=20, text='Select what camera you want to use')
lblRBOut.grid(row=0, column=2, sticky =tk.W+tk.E)


########################################
# CONFIDENCE THREASHOLD
##########################################
lblConfTxt = tk.Label(buttonFrame, text = "Set Confidence Threashold", font=('Arial', 13))
lblConfTxt.grid(row=3, column=0,sticky =tk.W+tk.E)
txtConf = tk.Entry(buttonFrame)
txtConf.grid(row=3, column=1,sticky =tk.W+tk.E)
btnConf = tk.Button(buttonFrame, text = "Confirm Confidence Threashold", command=number, activebackground='#4444ff')
btnConf.grid(row=4, column=1, sticky =tk.W+tk.E)
answer = tk.Label(buttonFrame, text="Determine how confidently the algorithm \ncan identify objects")
answer.grid(row=3, column=2, sticky =tk.W+tk.E)

########################################
# NMS THREASHOLD
##########################################
lblConfNMS = tk.Label(buttonFrame, text = "Object Overlap Threashold", font=('Arial', 13))
lblConfNMS.grid(row=5, column=0,sticky =tk.W+tk.E)
txtNMS = tk.Entry(buttonFrame)
txtNMS.grid(row=5, column=1,sticky =tk.W+tk.E)
btnNMS = tk.Button(buttonFrame, text = "Confirm NMS Threashold", command=nms, activebackground='#4444ff')
btnNMS.grid(row=6, column=1, sticky =tk.W+tk.E)
ansNMS = tk.Label(buttonFrame, text="Determine close object recongnition clarity")
ansNMS.grid(row=5, column=2, sticky =tk.W+tk.E)




spacer2 = tk.Label(buttonFrame, text="Select Execution Method", font=('Arial', 14))
spacer2.grid(row=7, column=1, sticky =tk.W+tk.E)


##########################################
# EXECUTION
##########################################
btnCustom = tk.Button(buttonFrame, text="Custom Settings", command=lambda:customMode(), font=('Arial', 14))
btnCustom.grid(row=8, column=0,sticky =tk.W+tk.E)
def on_enter(e):
    btnCustom['background'] = 'grey'

def on_leave(e):
    btnCustom['background'] = 'SystemButtonFace'
btnDefault = tk.Button(buttonFrame, text="Default Settings", command=lambda:mainMode(), font=('Arial', 14))
btnDefault.grid(row=8, column=2, sticky =tk.W+tk.E)
def on_enter(e):
    btnDefault['background'] = 'grey'

def on_leave(e):
    btnDefault['background'] = 'SystemButtonFace'
lblDefaultDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50%", font=('Arial', 13), anchor="w")
lblDefaultDes.grid(row=9, column=2, sticky =tk.N)





#buttonFrame.pack(fill = 'x')
buttonFrame.pack()



root.mainloop()
