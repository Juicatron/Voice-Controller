# Voice Controller
## Inspiration:
I was playing a modded version of Skyrim called Lorerim and kept accidentally pressing the wrong 'F' keys and struggling to get back to the WASD keys quickly enough, which led to my character dying repeatedly. Since dying so often couldn't possibly be due to a lack of skill, I decided to blame it on my controls and find a solution.

So, I spent a day creating a Python script to help me switch loadouts and stances more quickly. It works, but if you use voice feedback, you need to wait for the engine to finish speaking before issuing the next command. For a faster experience, you can uncheck the voice feedback option.

Feel free to use this script however you like, but be warned: it’s probably not optimized, there are better ways to do it, and I will probably forget about it.

This was also my first time making a GUI and I'm still learning Python, so don't judge me.

## Overview:
Voice Controller is a Python-based application that allows users to control their computer using voice commands. The system integrates voice recognition with text-to-speech and keyboard control, providing a hands-free way to execute commands. The application includes a graphical user interface for easy configuration and management of voice commands and settings.

## Features:
- Voice Recognition: Uses Vosk for real-time voice recognition.
- Text-to-Speech: Provides voice feedback using pyttsx3.
- Keyboard Control: Executes keyboard commands based on recognized keywords.
- Graphical User Interface: Allows users to configure settings and manage keyword mappings.
- Automatic Setup: Installs required dependencies and creates necessary configuration files.

## Requirements:
- Python 3.x
- Dependencies: pyttsx3, vosk, pyaudio, pynput, tkinter

## Installation:
1. Press the green "Code" button on the repository page.
2. Download the ZIP file.
3. Extract the file to your desired directory.
4. Go to the [Vosk Website](https://alphacephei.com/vosk/models)
    - Download and extract the small package for your chosen language.
5. Download Python if you don’t already have it.
    - Installation Guides: The Python documentation provides detailed installation instructions for different operating systems. Here are direct links to the installation sections:
        - Windows: [Installing Python on Windows](https://docs.python.org/3/using/windows.html)
        - macOS: [Installing Python on macOS](https://docs.python.org/3/using/mac.html)
        - Linux: [Installing Python on Linux](https://docs.python.org/3/using/unix.html)
6. Open a terminal.
7. Move to the directory of the Voice Command Controller.
8. Run the application using:
    - python main.py

## Usage:
1. Start the Application:
   - Run the application by executing:
       - python main.py
   - This command opens the main graphical user interface (GUI) of the application.
   - In the GUI, you can select a voice from the dropdown menu.
   - Click the 'Set Vosk Model' button and choose the folder where you extracted the Vosk model you downloaded.
       - If this step is not completed the program will not work. 

2. Managing Mappings:
   - Click the 'Open Mapping Window' button to open the keyword mapping editor.
   - In the mapping editor, you can:
       - Add New Mappings: Enter a keyword, associated key, and feedback, then click 'Add Mapping.'
       - Modify Existing Mappings: Reuse the same keyword to update its mapping.
   - Ensure you define a keyword, the corresponding key to press, and the feedback text for each mapping.

5. Toggle Voice Recognition:
   - To start or stop voice recognition, click the 'Toggle Voice Recognition' button.
   - When enabled, the application will listen for and react to voice commands according to the mappings you've set up.

6. Directly Changing keyword_mappings.json
   - Open keyword_mappings.json with any text editor.
   - You will see content similar to the following:
        {
            "example": {
                "key": "'example'",
                "feedback": "Example Feedback"
            }
        }
   - You can modify the contents as needed, but ensure that the following formatting remains correct:
       -  Quotation marks ""
       -  Curly braces {} for objects
       -  Commas , separating items
   
   - If you have made changes and the file becomes invalid, use [JSONLint](https://jsonlint.com) to check the validity:
       - Copy and paste your code into the input box on JSONLint.
       - Press 'Validate JSON.'
   - JSONLint will highlight any errors and indicate where the issue is.
   
## Files:
- main.py: Main script for running the voice command application.
- main_gui.py: GUI script for configuring settings and managing keyword mappings.
- settings.py: Manages application settings.
- setup.py: Sets up the environment by installing dependencies and creating configuration files.
- keyword_mappings.py: Manages keyword mappings and their display in the GUI.
- settings.json: Configuration file for application settings. (Created when the program is run)
- keyword_mappings.json: Configuration file for keyword mappings. (Created when the program is run)

## Troubleshooting:
### Running the Script
- If 'python main.py' doesn’t work, try running the script with 'python3 main.py' instead.
  
### Automatic Package Installation
- All required packages should download automatically when you start the program. If you encounter issues, ensure that you have an active internet connection and try running python setup.py manually to install the packages.

### Configuration Files
- The settings.json and keyword_mappings.json files will be automatically created. If you suspect these files are causing issues, try deleting them. The program will recreate them on the next run.

### Vosk Model Issues
- If the command line keeps showing the error message 'Error in main loop: 'NoneType' object has no attribute 'read', it indicates the Vosk model is not set up correctly.
    - Ensure that the Vosk model directory contains the following subdirectories:
        - am
        - conf
        - graph
        - ivector
    - If the selected directory does not have these subdirectories, it is the wrong directory.
 
### Voice Feedback Not Playing
- If no voice feedback is playing and you have checked 'Enable Voice Feedback,' ensure that you have selected a voice from the dropdown menu.

### Keyword Recognition Issues
- If your keywords are not being recognized, run the program and check the command line output. It will show the recognized words, for example: Recognized word::example.
    - Note that keywords like "two," "to," "too," "for," and "four" might cause issues due to their similarity. To resolve this, create mappings for each keyword with the same key.

### Invalid Key in Keyword Mapping
- If your keyword is recognized and displayed in the command line as shown below, it means that the key associated with the keyword is not valid. To fix this, check the mappings to ensure that the key specified is correct and valid.
  - Recognized word::example
  - Example Feedback
  - Error in main loop: 'example'

### Permissions Issues
- Ensure that you have the necessary permissions to read and write files in the directory where the program is running. Sometimes, lack of permissions can prevent the program from creating or accessing files.

### Python Version
- Make sure you are using a compatible version of Python. The program is designed for Python 3.x. Running it with Python 2.x might cause unexpected issues.
  
## License:
This project is licensed under the MIT License. See the LICENSE file for details.
