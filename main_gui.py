import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from settings import load_setting, update_setting
from keyword_mappings import mapping_gui

FLAG_FILE = 'stop_flag.txt'

def on_closing():
    def confirm_quit():
        try:
            with open(FLAG_FILE, 'w') as f:
                f.write('stop')
        except Exception as e:
            print(f"Error writing {FLAG_FILE}: {e}")
        root.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Quit Confirmation")
    dialog.geometry("350x200")

    message = (
        "!WARNING!\n\n"
        "If you quit while the engine is speaking the program will\n"
        "hang.\n\n"
        "Stop Voice Recognition and wait for the speaking to finish\n"
        "before quitting.\n\n"
        "Do you want to quit?"
    )

    label = tk.Label(dialog, text=message, wraplength=350, justify='center')
    label.pack(side=tk.TOP, anchor='n', expand=True, padx=20, pady=5)

    ok_button = tk.Button(dialog, text="Quit", command=confirm_quit, width=15)
    ok_button.place(x=60, y=155, width=100)

    cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy, width=15)
    cancel_button.place(x=200, y=160, width=100)

    dialog.grab_set()
    dialog.transient(root)
    
    center_window(dialog)

def find_model_dir():
    directory = filedialog.askdirectory()
    if directory:
        required_file = os.path.join(directory, 'conf/model.conf')
        if os.path.isfile(required_file):
            update_setting('model_directory', directory)
        else:
            messagebox.showerror("Invalid Model", "The selected directory does not contain a valid Vosk model.")

def setup_voice_options(engine):
    voices = engine.getProperty('voices')
    words_to_remove = {"Microsoft", "Desktop"}
    return [
        ''.join(word for word in voice.name.split() if word not in words_to_remove).split('-')[0]
        for voice in voices
    ]

def toggle_voice_recognition():
    current_state = load_setting('run_voice_recognition')
    new_state = not current_state
    update_setting('run_voice_recognition', new_state)
    if new_state:
        print("Start Recoginizing Voice")
    else:
        print("Stop Recoginizing Voice")

def get_engine():
    return engine

def center_window(window):
    window.update_idletasks()
    
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def start_gui():
    global root
    global vosk_model_button
    global engine
    
    root = tk.Tk()  
    root.resizable(False, False)
    root.title("Voice Controller")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("525x100")
    play_voice_var = tk.BooleanVar(value=load_setting('play_voice'))
    voice_var = tk.StringVar(value=load_setting('voice'))
    vosk_model_var = tk.StringVar(value=load_setting('model_directory'))

    engine = pyttsx3.init()
    voice_options = setup_voice_options(engine)
    selected_voice = tk.StringVar(value=voice_var.get())

    tk.Checkbutton(
        root,
        text="Enable Voice Feedback",
        variable=play_voice_var,
        command=lambda: update_setting('play_voice', play_voice_var.get())
    ).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    def on_voice_change(*args):
        update_setting('voice', selected_voice.get())
    
    selected_voice.trace('w', on_voice_change)
    
    tk.OptionMenu(root, selected_voice, *voice_options).grid(row=0, column=1, padx=10, sticky=tk.W)

    vosk_model_button = tk.Button(root, text="Set Vosk Model", command=find_model_dir)
    vosk_model_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

    tk.Button(root, text="Open Mapping Window", command=mapping_gui).grid(row=0, column=3, padx=10, sticky=tk.W)

    toggle_voice_recognition_button = tk.Button(root, text="Toggle Voice Recognition", command=toggle_voice_recognition)
    toggle_voice_recognition_button.grid(row=1, column=0, columnspan=4, pady=10)
    
    center_window(root)
    
    root.mainloop()
