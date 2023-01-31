import time
import datetime

def countdown(s):
    total_seconds = int(s)
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -=1


s = input("Enter Seconds")

countdown(s)




    for i in range(1, int(y)):
        #while True:
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold = x)
            #print(classIds, bbox)
            
            if len(classIds) != 0:
                
                for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
                    cv2.putText(img, classNames[classIds-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0), 2)
                    
            cv2.imshow("Square Vision", img)
            cv2.waitKey(1)
            i = i + 1
            time.sleep(.001)
            #print(i)
    #net.setInputSwapRB(False)