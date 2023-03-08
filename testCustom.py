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
    lblRBOut.configure(text = selection)

def number():
    try:
        y = int(txtConf.get())
        global conf
        conf = int(y)/100
        if (y <= 0):
            answer.configure(text = "Confidence Threashold of " + txtConf.get() + " is too low", font=('Arial bold', 10))
        elif (y > 100):
            answer.configure(text = "Confidence Threashold of " + txtConf.get() + " is too high", font=('Arial bold', 10))
        else:
            if (75 <= y <= 100):
                answer.configure(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThis can limit the number of objects recognized", font=('Arial bold', 10))
                return conf
            elif(1 <= y <= 25):
                answer.configure(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThis can result in excessive feedback", 
                               font=('Arial bold', 10))
                return conf
            else:
                answer.configure(text = "Confidence Threashold = " + txtConf.get(),  font=('Arial', 10))
                return conf

    except ValueError:
        answer.configure(text = "ERROR: " + txtConf.get() + " is an invalid input", font=('Arial bold', 10))

def nms():
    try:
        p = int(txtNMS.get())
        global nms
        nms = int(p)/100
        print(nms)
        if (p <= 0):
            ansNMS.configure(text = "A NMS Threashold of " + txtNMS.get() + " is too low",
                           font=('Arial bold', 10))
        elif (p > 100):
            ansNMS.configure(text = "A NMS Threashold of " + txtNMS.get() + " is too high",
                          font=('Arial bold', 10))
        else:
            if (45 <= p <= 100):
                ansNMS.configure(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis will limit the identification of close objects", 
                               font=('Arial bold', 10))
                return nms
            elif(1 <= p <= 10):
                ansNMS.configure(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis can result in excessive object tagging", 
                               font=('Arial bold', 10))
                return nms
            else:
                ansNMS.configure(text = "NMS Threashold = " + txtNMS.get(), font=('Arial', 10))
                return nms
    
    except ValueError:
        ansNMS.configure(text = "ERROR: " + txtNMS.get() + " is an invalid input", font=('Arial bold', 10))


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
root = customtkinter.CTk()
root.geometry("900x500")
root.title("Square Vision")
var = tk.StringVar()
#Frame Grid
lblFrame = tk.Frame(root)
lblFrame.columnconfigure(0, weight=1)
lblFrame.columnconfigure(1, weight=1)
lblFrame.columnconfigure(2, weight=1)
lblFrame.config(bg="light grey")

label = customtkinter.CTkLabel(lblFrame, text="Square Vision 2D v.5.0", font=('Arial', 18))
label.grid(row=0, column=1, sticky =tk.W+tk.E)
label2 = customtkinter.CTkLabel(lblFrame, text="Sprint 5 | Team 1", font=('Arial', 14))
label2.grid(row=1, column=1, sticky =tk.W+tk.E)
label3 = customtkinter.CTkLabel(lblFrame, text="CIS 490 Capstone | 3/9/23", font=('Arial', 12))
label3.grid(row=2, column=1, sticky =tk.W+tk.E)
label4 = customtkinter.CTkLabel(lblFrame, text="Welcome to Square vision, an object regcogniton software \nplease select how you would like to execute the program", 
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
lblCamera = customtkinter.CTkLabel(buttonFrame, text="Select Camera",font=('Arial', 13))
lblCamera.grid(row=0, column=0, sticky =tk.E)
r1 = customtkinter.CTkRadioButton(buttonFrame, text='Internal Camera', variable=var, value=0, command=lambda:setVid(0))
r1.grid(row=0, column=1, sticky =tk.W+tk.E, padx=20, pady=0)
r2 = customtkinter.CTkRadioButton(buttonFrame, text='External Camera', variable=var, value=1, command=lambda:setVid(1))
r2.grid(row=1, column=1, sticky =tk.W+tk.E, padx=20, pady=5)
lblRBOut = customtkinter.CTkLabel(buttonFrame, width=20, text='Select what camera you want to use')
lblRBOut.grid(row=0, column=2, sticky =tk.W+tk.E)


########################################
# CONFIDENCE THREASHOLD
##########################################
lblConfTxt = customtkinter.CTkLabel(buttonFrame, text = "Set Confidence Threashold", font=('Arial', 13))
lblConfTxt.grid(row=3, column=0,sticky =tk.W+tk.E, padx=20, pady=0)
txtConf = customtkinter.CTkEntry(buttonFrame)
txtConf.grid(row=3, column=1,sticky =tk.W+tk.E, padx=20, pady=0)
btnConf = customtkinter.CTkButton(buttonFrame, text = "Confirm Confidence Threashold", command=number,)
btnConf.grid(row=4, column=1, sticky =tk.W+tk.E, padx=20, pady=10)
answer = customtkinter.CTkLabel(buttonFrame, text="Determine how confidently the algorithm \ncan identify objects")
answer.grid(row=3, column=2, sticky =tk.W+tk.E, padx=15, pady=0)

########################################
# NMS THREASHOLD
##########################################
lblConfNMS = customtkinter.CTkLabel(buttonFrame, text = "Object Overlap Threashold", font=('Arial', 13))
lblConfNMS.grid(row=5, column=0,sticky =tk.W+tk.E)
txtNMS = customtkinter.CTkEntry(buttonFrame)
txtNMS.grid(row=5, column=1,sticky =tk.W+tk.E)
btnNMS = customtkinter.CTkButton(buttonFrame, text = "Confirm NMS Threashold", command=nms)
btnNMS.grid(row=6, column=1, sticky =tk.W+tk.E)
ansNMS = tk.Label(buttonFrame, text="Determine close object recongnition clarity")
ansNMS.grid(row=5, column=2, sticky =tk.W+tk.E)




spacer2 = customtkinter.CTkLabel(buttonFrame, text="Select Execution Method", font=('Arial', 14))
spacer2.grid(row=7, column=1, sticky =tk.W+tk.E)


##########################################
# EXECUTION
##########################################
btnCustom = customtkinter.CTkButton(buttonFrame, text="Custom Settings", command=lambda:customMode(), font=('Arial', 14))
btnCustom.grid(row=8, column=0,sticky =tk.W+tk.E)
btnDefault = customtkinter.CTkButton(buttonFrame, text="Default Settings", command=lambda:mainMode(), font=('Arial', 14))
btnDefault.grid(row=8, column=2, sticky =tk.W+tk.E)
lblDefaultDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50%", font=('Arial', 13), anchor="w")
lblDefaultDes.grid(row=9, column=2, sticky =tk.N)





#buttonFrame.pack(fill = 'x')
buttonFrame.pack()



root.mainloop()
