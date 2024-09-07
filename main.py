import keyword
import subprocess
import sys
import os
import json
from turtle import listen

def run_setup():
    try:
        subprocess.check_call([sys.executable, 'setup.py'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run setup.py: {e}")
        sys.exit(1)
        
run_setup()

import pyttsx3
from vosk import Model, KaldiRecognizer
from pynput.keyboard import Key, Controller
import time
import threading
import main_gui as gui
import pyaudio
from settings import load_setting, update_setting
from keyword_mappings import load_mappings

FLAG_FILE = 'stop_flag.txt'

engine = None
model = None
recognizer = None
keyboard = None
p = None
stream = None
mappings = {}
play_voice = False

def check_flag_file():
    if os.path.exists(FLAG_FILE):
        os.remove(FLAG_FILE)
        sys.exit()

def initialize():
    """Initialize components for voice recognition."""
    global engine, model, recognizer, keyboard, p, stream, mappings
    
    print("INIT MAIN LOOP")
    engine = gui.get_engine()
    model = Model(load_setting('model_directory'))
    recognizer = KaldiRecognizer(model, 16000)
    keyboard = Controller()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    play_voice = load_setting('play_voice')
    voices = engine.getProperty('voices')
    selected_voice = load_setting('voice')
    for voice in voices:
        if selected_voice in voice.name:
            engine.setProperty('voice', voice.id)
    
    mappings = load_mappings()
    print(f"Loaded mappings: {mappings}")
    
def run_main_loop():
    initialized = False
    
    while True:
        check_flag_file() 
        try:          
            run_voice_recognition = load_setting('run_voice_recognition')
            
            if run_voice_recognition:
                if not initialized:
                    print("INIT MAIN LOOP")
                    initialize()
                    initialized = True
                    
                main()  
            else:
                initialized = False
                time.sleep(0.25)  
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(1) 

def start_gui():
    gui.start_gui()

def main():
    def try_word(word, play_voice=False):
        if mappings:
            for keyword, mapping in mappings.items():
                if word == keyword:
                    print(mapping['feedback'])
                    if play_voice:
                        engine.say(mapping['feedback'])
                        engine.runAndWait()
                
                    key_to_press = mapping['key']

                    if hasattr(Key, key_to_press):
                        keyboard.press(getattr(Key, key_to_press))
                        keyboard.release(getattr(Key, key_to_press))
                    else:
                        keyboard.press(key_to_press)
                        keyboard.release(key_to_press)
                
                    break 
        else:
            print(f"No mappings found for word: {word}")
                    
    def listen_for_keyword():
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            recognized_text = json.loads(result).get('text','')
            words = recognized_text.split()
            
            for word in words:
                print(f"Word Recognized::{word}")
                try_word(word)
    
    listen_for_keyword()


if __name__ == "__main__":
    update_setting('run_voice_recognition', False)

    gui_thread = threading.Thread(target=start_gui, daemon=True)
    gui_thread.start()

    run_main_loop()