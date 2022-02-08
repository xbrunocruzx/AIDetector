import cv2
import os
from time import sleep
from random import randrange
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def Menu():

    print("Selected File: ", os.path.basename(os.path.normpath(haarCascadeFile)), "\n\n")

    print("DETECTOR\n\n")
    print("1 - Image\n")
    print("2 - Video\n")
    print("3 - Webcam\n\n")
    print("0 - Exit\n\n")
    choice = int(input("> "))

    if choice == 0:
        exit(0)
    elif choice == 1:
            
        Tk().withdraw()
        filename = askopenfilename(filetypes=[("Images", ".jpg .png")])

        if filename == "":
            Menu()

        img = cv2.imread(filename)

        grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        coordinates = trained_data.detectMultiScale(grayscaled_img)

        for (x, y, w, h) in coordinates:
            cv2.rectangle(img , (x, y), (x+w, y+h), (0, 255, 0), 1)

        cv2.imshow('AI Detector (Image)', img)
        cv2.waitKey()

    elif choice == 2:

        Tk().withdraw()
        filename = askopenfilename(filetypes=[("Videos", ".mp4 .mov .webm .gif")])

        if filename == "":
            Menu()
            
        video = cv2.VideoCapture(filename)

        print("Press Q to exit")

        while True:

            successful_frame_read, frame = video.read()

            grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            coordinates = trained_data.detectMultiScale(grayscaled_img)

            for(x, y, w, h) in coordinates:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

            cv2.imshow('AI Detector (Video)', frame)
            key = cv2.waitKey(1)

            if key==81 or key==113:
                break

    elif choice == 3:

        cam = cv2.VideoCapture(0)

        print("Press Q to exit")

        while True:

            successful_frame_read, frame = cam.read()

            grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            coordinates = trained_data.detectMultiScale(grayscaled_img)

            for(x, y, w, h) in coordinates:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

            cv2.imshow('AI Detector (Cam)', frame)
            key = cv2.waitKey(1)

            if key==81 or key==113:
                break

    else:
        print("Invalid choice.")
        sleep(1)
        Menu()

print("\nChoose HaarCascade .xml File\n\n")
sleep(1)

Tk().withdraw()
haarCascadeFile = askopenfilename(filetypes=[("XML", ".xml")])
trained_data = cv2.CascadeClassifier(haarCascadeFile)

Menu()
