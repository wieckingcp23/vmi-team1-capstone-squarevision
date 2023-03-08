from Detector import *
import tkinter as tk
import os

def mainMode():
    videoPath = 0

    configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.onVideo()

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
""" 
image=Image.open('vmi.png')
image2=image.resize((75,75),Image.ANTIALIAS)
newImage =ImageTk.PhotoImage(image2)

lbl = tk.Label(lblFrame, image=newImage)
lbl.grid(row=0, column=0, sticky =tk.W+tk.E)

image3=Image.open('vmi.png')
image4=image3.resize((75, 75),Image.ANTIALIAS)
newImage2 =ImageTk.PhotoImage(image4)
lbl2 = tk.Label(lblFrame, image=newImage2)
lbl2.grid(row=0, column=2, sticky =tk.W+tk.E) """


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)



#Internal Camera GUI
lblInternal = tk.Label(buttonFrame, text = "Use Internal Camera", font =('Arial', 13))
lblInternal.grid(row=0, column=0, sticky =tk.W+tk.E)
btninternal = tk.Button(buttonFrame, text="Internal Camera",  activebackground='#4444ff')
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
btnExternal = tk.Button(buttonFrame, text="External Camera", activebackground='#4444ff')
btnExternal.grid(row=1, column=1, sticky =tk.W+tk.E)
lblExtInst = tk.Label(buttonFrame, text="Uses an external camera", font=('Arial', 10))
lblExtInst.grid(row=1, column=2, sticky =tk.W)
lblExtInst.grid(row=1, column=2, sticky =tk.W)


def on_enter(e):
    btnExternal['background'] = 'grey'

def on_leave(e):
    btnExternal['background'] = 'SystemButtonFace'




#timer GUI
lblTimer = tk.Label(buttonFrame, text = "Set Timer (in Seconds)", font=('Arial', 13))
lblTimer.grid(row=3, column=0,sticky =tk.W+tk.E)
txtTimer = tk.Text(buttonFrame,height = .5, width = 1, font=('Arial', 13))
txtTimer.grid(row=3, column=1,sticky =tk.W+tk.E)
btnTimer = tk.Button(buttonFrame, text = "Enter", activebackground='#4444ff')
btnTimer.grid(row=3, column=2, sticky =tk.W+tk.E)

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


buttonFrame.pack(fill = 'x')
#buttonFrame.pack()



root.mainloop()
