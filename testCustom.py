from Detector import *
import tkinter as tk
from tkinter import *
import customtkinter
import os

#Sets the input camera device + updates GUI
def setVid(x):
    global vid
    vid = x
    selection = "Camera Selected: "
    if (x == 0):
        selection += "Internal Camera"
    if (x == 1):
        selection += "External Camera"
    lblRBOut.configure(text = selection, fg_color='lime', corner_radius = 10, text_color = "black")

def number():
    try:
        y = int(txtConf.get())
        global conf
        conf = int(y)/100
        if (y <= 0):
            answer.configure(text = "ERROR: Confidence Threashold = " + txtConf.get() + "\nThis is too low", 
                             font=('Arial bold', 14), fg_color='red', corner_radius = 10)
        elif (y > 100):
            answer.configure(text = "ERROR: Confidence Threashold =  " + txtConf.get() + "\n This is too high", 
                             font=('Arial bold', 14), fg_color='red', corner_radius = 10)
        else:
            if (75 <= y <= 100):
                answer.configure(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThe rate of objects successfully \nidentified will be severly limited", 
                                 font=('Arial bold', 14), fg_color='yellow', corner_radius = 10, text_color = "black")
                return conf
            elif(1 <= y <= 25):
                answer.configure(text = "Warning: Confidence Threashold = " + txtConf.get() + " \nThis can result in excessive feedback", 
                               font=('Arial bold', 14), fg_color='yellow', corner_radius = 10, text_color = "black")
                return conf
            else:
                answer.configure(text = "Confidence Threashold = " + txtConf.get(),  
                                 font=('Arial', 14), fg_color='lime', corner_radius = 10, text_color = "black")
                return conf

    except ValueError:
        answer.configure(text = "ERROR: " + txtConf.get() + " is an invalid input", 
                         font=('Arial bold', 14), fg_color='red', corner_radius = 10)

def nms():
    try:
        p = int(txtNMS.get())
        global nms
        nms = int(p)/100
        print(nms)
        if (p <= 0):
            ansNMS.configure(text = "A NMS Threashold of " + txtNMS.get() + " is too low", 
                             font=('Arial bold', 14), fg_color='red', corner_radius = 10, text_color = "black")
        elif (p > 100):
            ansNMS.configure(text = "A NMS Threashold of " + txtNMS.get() + " is too high",
                          font=('Arial bold', 14), fg_color='red', corner_radius = 10, text_color = "black")
        else:
            if (45 <= p <= 100):
                ansNMS.configure(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis can result in excessive \nobject tagging", 
                               font=('Arial bold', 14), fg_color='yellow', corner_radius = 10, text_color = "black")
                return nms
            elif(1 <= p <= 10):
                ansNMS.configure(text = "Warning: NMS Threashold = " + txtNMS.get() + " \nThis will limit the identification \nof objects that are close together", 
                               font=('Arial bold', 14), fg_color='yellow', corner_radius = 10, text_color = "black")
                return nms
            else:
                ansNMS.configure(text = "NMS Threashold = " + txtNMS.get(), 
                                 font=('Arial', 14), fg_color='lime', corner_radius = 10, text_color = "black")
                return nms
    
    except ValueError:
        ansNMS.configure(text = "ERROR: " + txtNMS.get() + " is an invalid input", font=('Arial bold', 14))

#Runs the default settings
def mainMode():
    videoPath = 0

    configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.onVideo()

#Runs the custom settings
def customMode():
    videoPath = 0

    configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.customVideo(vid, conf, nms)

###########################################################
###########################################################
###########################################################
###########################################################
###########################################################

#GUI Stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("775x500")
root.title("Square Vision")
var = tk.StringVar()
customtkinter.set_default_color_theme("dark-blue")

#Frame Grid
lblFrame = customtkinter.CTkFrame(master=root, width=800, height=500)
lblFrame.grid(row=0, column=1, padx=20)
#lblFrame = tk.Frame(root)

lblFrame.columnconfigure(0, weight=7)
lblFrame.columnconfigure(1, weight=7)
lblFrame.columnconfigure(2, weight=7)
label = customtkinter.CTkLabel(lblFrame, text="Square Vision 2D v.5.0", font=('Arial', 18))
label.grid(row=0, column=1, sticky =tk.W+tk.E)
label2 = customtkinter.CTkLabel(lblFrame, text="Sprint 5 | Team 1", font=('Arial', 14))
label2.grid(row=1, column=1, sticky =tk.W+tk.E)
label3 = customtkinter.CTkLabel(lblFrame, text="CIS 490 Capstone | 3/9/23", font=('Arial', 12))
label3.grid(row=2, column=1, sticky =tk.W+tk.E)
label4 = customtkinter.CTkLabel(lblFrame, text="Welcome to Square vision, an object regcogniton software! \nPlease select how you would like to execute the program", 
                  font=('Arial', 13))
label4.grid(row=3, column=1, sticky =tk.W+tk.E)
lblFrame.pack(fill="both")

##########################################
# BUTTON PANE
##########################################
buttonFrame = customtkinter.CTkFrame(master=root, width=900, height=500)
buttonFrame.columnconfigure(0, weight=7)
buttonFrame.columnconfigure(1, weight=7)
buttonFrame.columnconfigure(2, weight=7)
buttonFrame.columnconfigure(3, weight=7)

##########################################
# CAMERA SELECTION
##########################################
lblCamera = customtkinter.CTkLabel(buttonFrame, text="Select Camera",font=('Arial', 14))
lblCamera.grid(row=0, column=0, sticky =tk.W+tk.E)
r1 = customtkinter.CTkRadioButton(buttonFrame, text='Internal Camera', variable=var, value=0, command=lambda:setVid(0))
r1.grid(row=0, column=1, sticky =tk.W+tk.E, padx=20, pady=0)
r2 = customtkinter.CTkRadioButton(buttonFrame, text='External Camera', variable=var, value=1, command=lambda:setVid(1))
r2.grid(row=1, column=1, sticky =tk.W+tk.E, padx=20, pady=5)
lblRBOut = customtkinter.CTkLabel(buttonFrame, width=20, text='Select what camera you want to use', font=('Arial', 14))
lblRBOut.grid(row=0, column=2, sticky =tk.W+tk.E)


########################################
# CONFIDENCE THREASHOLD
##########################################
lblConfTxt = customtkinter.CTkLabel(buttonFrame, text = "Set Confidence Threashold", font=('Arial', 14))
lblConfTxt.grid(row=3, column=0,sticky =tk.W+tk.E, padx=20, pady=0)
txtConf = customtkinter.CTkEntry(buttonFrame)
txtConf.grid(row=3, column=1,sticky =tk.W+tk.E, padx=20, pady=0)
btnConf = customtkinter.CTkButton(buttonFrame, text = "Confirm Confidence Threashold", command=number,)
btnConf.grid(row=4, column=1, sticky =tk.W+tk.E, padx=20, pady=10)
answer = customtkinter.CTkLabel(buttonFrame, text="Determine how confidently the algorithm \ncan identify objects", font=('Arial', 14))
answer.grid(row=3, column=2, sticky =tk.W+tk.E, padx=15, pady=0)

########################################
# NMS THREASHOLD
##########################################
lblConfNMS = customtkinter.CTkLabel(buttonFrame, text = "Object Overlap Threashold", font=('Arial', 14))
lblConfNMS.grid(row=5, column=0,sticky =tk.W+tk.E, padx=20, pady=0)
txtNMS = customtkinter.CTkEntry(buttonFrame)
txtNMS.grid(row=5, column=1,sticky =tk.W+tk.E, padx=20, pady=0)
btnNMS = customtkinter.CTkButton(buttonFrame, text = "Confirm NMS Threashold", command=nms)
btnNMS.grid(row=6, column=1, sticky =tk.W+tk.E, padx=20, pady=0)
ansNMS = customtkinter.CTkLabel(buttonFrame, text="Determine close object recongnition clarity", font=('Arial', 14))
ansNMS.grid(row=5, column=2, sticky =tk.W+tk.E, padx=20, pady=10)



##########################################
# EXECUTION
##########################################
btnCustom = customtkinter.CTkButton(buttonFrame, text="Custom Settings", command=lambda:customMode(), font=('Arial bold', 12))
btnCustom.grid(row=9, column=0,sticky =tk.W+tk.E)
lblCustomDes= tk.Label(buttonFrame, text = "\nThis will execute the program \nin the configuration specified above\n", font=('Arial', 13), anchor="w")
lblCustomDes.grid(row=8, column=0, sticky =tk.N)
btnDefault = customtkinter.CTkButton(buttonFrame, text="Default Settings", command=lambda:mainMode(), font=('Arial bold', 12))
btnDefault.grid(row=9, column=2, sticky =tk.W+tk.E)
lblDefaultDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50% \nNMS Threashold = 20%", font=('Arial', 13), anchor="w")
lblDefaultDes.grid(row=8, column=2, sticky =tk.N)

#buttonFrame.pack(fill = 'y')
buttonFrame.pack(fill = "both")



root.mainloop()
