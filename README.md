# Screen Recording with OpenCV and PyAutoGUI

This Python script allows you to record the screen using OpenCV and PyAutoGUI libraries. It captures the screen continuously and saves the frames into a video file.

## Dependencies

The following libraries are required to run the script:

- [OpenCV](https://opencv.org/) (cv2) - Used for video processing and frame manipulation.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Used for capturing the screen.
- [NumPy](https://numpy.org/) - Used for array operations and transformations.
- [keyboard](https://keyboard.readthedocs.io/) - Used for detecting key presses.
- [pygetwindow](https://pypi.org/project/PyGetWindow/) - Used for window management and getting the active window.

You can install these dependencies using pip:

```bash
pip install opencv-python pyautogui numpy keyboard pygetwindow


## Usage
1. Clone the repository or download the script file (screen_recording.py).
2. Run the script using Python:
`python screen_recording.py`

3. Once the script starts, it will record the screen and save the frames into a video file named output.avi.

4. To stop the recording, press the 'q' key on your keyboard.

## Customization
 - You can modify the output file name and codec by changing the parameters of the cv2.VideoWriter object.

- The script includes a check for a specific window title to pause the recording when Google.com is active. You can modify or remove this check based on your requirements.

## License
- This project is licensed under the MIT License.

Feel free to modify the README.md file based on your specific needs and add any additional information or instructions you deem necessary.

## Credits
This project utilizes the following open-source libraries:

OpenCV
PyAutoGUI
NumPy
keyboard
pygetwindow

We would like to express our gratitude to the developers and contributors of these libraries for their valuable work.
