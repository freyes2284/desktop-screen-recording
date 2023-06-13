import cv2
import pyautogui
import numpy as np
import keyboard  # for keylogs
import pygetwindow as gw

# Get screen size
screen_size = (pyautogui.size().width, pyautogui.size().height)

# Define the codec using VideoWriter_fourcc() and create a VideoWriter object
# We specify output file name "output.avi", codec "XVID", FPS as 10.0, and screen size as obtained above
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
out = cv2.VideoWriter("output.avi", fourcc, 10.0, screen_size)

print("Screen recording started. Press 'q' to stop the recording.")

# Initial recording state
recording = True

# For capturing screen
while True:
    try:
        # Check for the window title
        window = gw.getActiveWindow()
        if window is not None and "Google" in window.title:
            recording = False
            print("Recording paused as Google.com is active")
        elif window is not None:
            recording = True
            print("Recording... Google.com is not active")

        # Capture screen using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the image into numpy array representation
        frame = np.array(img)
        
        # Convert the BGR image into RGB image
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # If 'q' is pressed on the keyboard, break the loop and stop the recording
        if keyboard.is_pressed('q'):
            print('Screen recording stopped.')
            break

        # Only write the frame if recording is True
        if recording:
            # Write the RGB image to file
            out.write(frame)

    except Exception as e:
        # If anything goes wrong, print the error and break the loop
        print(e)
        break

# Close the video file
out.release()
