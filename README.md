# Voice Controller

## Overview:
Voice Command Controller is a Python-based application that allows users to control their computer using voice commands. The system integrates voice recognition with text-to-speech and keyboard control, providing a hands-free way to execute commands. The application includes a graphical user interface for easy configuration and management of voice commands and settings.

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
4. Go to the Vosk website (https://alphacephei.com/vosk/)
    - download and extract the small package for your chosen language.
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

## Files:
- main.py: Main script for running the voice command application.
- main_gui.py: GUI script for configuring settings and managing keyword mappings.
- settings.py: Manages application settings.
- setup.py: Sets up the environment by installing dependencies and creating configuration files.
- keyword_mappings.py: Manages keyword mappings and their display in the GUI.
- settings.json: Configuration file for application settings.
- keyword_mappings.json: Configuration file for keyword mappings.

## Troubleshooting:
- Missing Dependencies: If a required package is not installed, the setup script will attempt to install it. Ensure you have pip installed and accessible.
- Configuration Issues: If settings.json or keyword_mappings.json is missing or corrupted, the application will create default files.

## Contributing:
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact:
For questions or support, please contact me @ juicatron@gmail.com).
