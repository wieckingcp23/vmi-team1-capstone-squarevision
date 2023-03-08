from Detector import *
import tkinter as tk
from tkinter import *
import os

x = 1

def print_selection():
    lblRBOut.config(text='you have selected ' + var.get())

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
    detector.customVideo(x)

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
var = tk.StringVar()


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

##########################################
#    Buttons 
##########################################


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

# Camera as Radiobuttons
lbl4 = tk.Label(buttonFrame, text="Select Camera",font=('Arial', 11))
lbl4.grid(row=0, column=0, sticky =tk.E)
r1 = tk.Radiobutton(buttonFrame, text='Internal Camera', variable=var, value='A', command=print_selection)
r1.grid(row=0, column=1, sticky =tk.W+tk.E)
r2 = tk.Radiobutton(buttonFrame, text='External Camera', variable=var, value='B', command=print_selection)
r2.grid(row=1, column=1, sticky =tk.W+tk.E)

lblRBOut = tk.Label(root, bg='white', width=20, text='empty')
lblRBOut.grid(row=0, column=2, sticky =tk.W+tk.E)







#Spacer 
lblSpace = tk.Label(buttonFrame)
lblSpace.grid(row=4, column=0,sticky =tk.W+tk.E)
lblSpace2 = tk.Label(buttonFrame)
lblSpace2.grid(row=5, column=2, sticky =tk.W+tk.E)

#Execution GUI
btnCustom = tk.Button(buttonFrame, text="Custom Settings", font=('Arial', 14))
btnCustom.grid(row=6, column=0,sticky =tk.W+tk.E)
def on_enter(e):
    btnCustom['background'] = 'grey'

def on_leave(e):
    btnCustom['background'] = 'SystemButtonFace'
btnDefault = tk.Button(buttonFrame, text="Default Settings", command=lambda:mainMode(), font=('Arial', 14))
btnDefault.grid(row=6, column=2, sticky =tk.W+tk.E)
def on_enter(e):
    btnDefault['background'] = 'grey'

def on_leave(e):
    btnDefault['background'] = 'SystemButtonFace'
lblDefaultDes = tk.Label(buttonFrame, text = "Default Definitions: \nInput Device = Internal Camera \nConfidence Threashold = 50%\nTimer Duration = Infinite", font=('Arial', 13), anchor="w")
lblDefaultDes.grid(row=7, column=2, sticky =tk.N)


#buttonFrame.pack(fill = 'x')
buttonFrame.pack()



root.mainloop()
