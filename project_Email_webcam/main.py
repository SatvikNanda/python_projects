import cv2
import time
from emailing import send_email
import glob
import os
from threading import Thread



video = cv2.VideoCapture(0) #'0' indicates that the code should use the primary camera of the laptop
time.sleep(1) #wait for 1 second before starting further action

first_frame = None

status_list = []
count = 1

def clean_folder():
    images = glob.glob("project_Email_webcam/images/*.png")
    for image in images:
        os.remove(image)
    print("images cleaned successfully")

while True:
    status = 0
    check, frame = video.read()
    

    #pre-processing of the frames
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#convert frame to grayscale to reduce the data, because by default we are using the blue, green and red frames.
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21,21), 0)#to blur the image because we dont need high precision

    cv2.imshow("My video", gray_frame_gau) #for seeing the video with the title "My video"

    #frame comparison
    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)#comparing the first_frame with the current frame
    
    #get accurate black and white frame comparison
    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]#only pick frames between 60 and 255
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    #get contours
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#get the contours of an object(boundaries)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:#if the object is small(i.e some background object which is irrelevant)
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)#create a rectangle around the frame
        if rectangle.any:
            status = 1
            cv2.imwrite(f"project_Email_webcam/images/{count}.png", frame)
            count = count+1
            all_images = glob.glob("project_Email_webcam/images/*.png")
            index = int(len(all_images)/2)
            resultant_image = all_images[index]
    
    status_list.append(status)
    status_list = status_list[-2:]


    print(status_list)
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(resultant_image, ))
        email_thread.daemon = True

        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        
        email_thread.start()
        
        print("Code completed, remove immages now")

        
        
        
    

    cv2.imshow("video", frame)
    

    
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

clean_thread.start()
video.release() #important to free up the resources and stop capturing the video
