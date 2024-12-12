
#Changing cat to use bat:
import os
import cv2


def main():


        #os.system("start microsoft.windows.camera:")

    imcap = cv2.VideoCapture(0)
    imcap.set(3, 640) # set width as 640
    imcap.set(4, 480) # set height as 480

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Face detection



    while True:
        success, img = imcap.read() # capture frame from video
        # converting image from color to grayscale 
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Getting corners around the face
        # 1.3 = scale factor, 5 = minimum neighbor can be detected
        faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  

        # drawing bounding box around face
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
            # displaying image with bounding box
        cv2.imshow('face_detect', img)
        # loop will be broken when 'q' is pressed on the keyboard
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyWindow('face_detect')


if __name__ == '__main__':
    main()

    #Help Received:
        #https://towardsdatascience.com/how-to-detect-objects-in-real-time-using-opencv-and-python-c1ba0c2c69c0
