import json
import os

def save_settings(play_voice, model_directory, voice):
    settings = {
        'play_voice': play_voice,
        'model_directory': model_directory,
        'voice': voice,
        'run_voice_recognition': False
    }
    with open('settings.json', 'w') as file:
        json.dump(settings, file)

def update_setting(key, value):  
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    else:
        settings = {}

    settings[key] = value
    
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)
        
def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as file:
            settings = json.load(file)
            return (
                settings.get('play_voice', False),
                settings.get('model_directory', ''),
                settings.get('voice', ''),
                settings.get('run_voice_recognition', False)
            )
    return False, '', ''

def load_setting(key):
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as file:
            settings = json.load(file)
            return settings[key]
