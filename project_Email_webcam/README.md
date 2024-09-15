# Overview:
This project implements a motion detection system using a webcam, with the additional feature of sending an email alert whenever movement is detected. By capturing live video through the primary webcam, the project processes each frame to identify motion, stores relevant images of detected activity, and sends an email with the captured image attached. This system is particularly useful for home security or monitoring restricted areas.

# Features:
1. Real-time motion detection: Uses OpenCV to capture and analyze frames from the webcam.<br>
2. Email alert: Sends an automated email with an image attachment when motion is detected.<br>
3. Efficient frame processing: Converts frames to grayscale and applies Gaussian blur to reduce noise and unnecessary data processing.<br>
4. Contour detection: Detects and highlights moving objects using contours and bounding rectangles.<br>
5. Threaded execution: Utilizes Python's threading module for asynchronous email sending and folder cleanup to improve performance.<br>

# Methodology:
1. ### Capture Frames:
    The primary webcam is used to capture live video feed.<br>

2. ### Frame Preprocessing:

    Convert the frames to grayscale to minimize data size.<br>
    Apply Gaussian blur to reduce noise.<br>
    Compare the current frame with the first frame using frame differencing.<br>

3. ### Motion Detection:
    Apply a threshold to isolate significant changes in the frame.<br>
    Detect contours and determine if the area of the contour is large enough to be considered meaningful motion.<br>
    Draw bounding rectangles around detected motion.<br>

4. ### Alert Mechanism:

    When motion is detected, save the frame as an image in the project folder.<br>
    When the motion stops (detected through frame comparison), an email is sent to the predefined receiver with an attached image from the moment of motion.<br>
    After the email is sent, the saved images are cleaned up asynchronously.<br>

5. ### Threading:
   The email sending and folder cleanup processes are performed using separate threads to ensure the main video feed is not interrupted.<br>


# Output:
The program runs a live feed from the webcam, showing both the processed grayscale image and the motion-detected image with bounding rectangles.
When motion is detected

![image](https://github.com/user-attachments/assets/f9f13b05-185a-4e09-a826-41cd6b1fb1c6)<br>
<br>
![image](https://github.com/user-attachments/assets/e9694dc7-492c-4230-b09a-1afc07114a8c)












    
