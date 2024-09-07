import tkinter as tk
from tkinter import messagebox
import json
import os

MAPPINGS_FILE = 'keyword_mappings.json'

def load_mappings():
    if os.path.exists(MAPPINGS_FILE):
        with open(MAPPINGS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_mappings(mappings):
    with open(MAPPINGS_FILE, 'w') as f:
        json.dump(mappings, f, indent=4)

def update_display():
    mappings = load_mappings()
    display_text = "\n".join(f"{key}: key={value['key']}, Feedback={value['feedback']}" for key, value in mappings.items())
    display_content.config(state=tk.NORMAL)
    display_content.delete(1.0, tk.END)
    display_content.insert(tk.END, display_text)
    display_content.config(state=tk.DISABLED)

def save_entry():
    keyword = keyword_entry.get().strip()
    key = key_entry.get().strip()
    feedback = feedback_entry.get().strip()

    if not keyword or not key or not feedback:
        messagebox.showerror("Error", "Keyword, Key, and Feedback are required.")
        return

    mappings = load_mappings()
    mappings[keyword] = {"key": key, "feedback": feedback}
    save_mappings(mappings)
    update_display()
    keyword_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    feedback_entry.delete(0, tk.END)

def mapping_gui():
    global keyword_entry, key_entry, feedback_entry, display_content

    mapping_window = tk.Tk()
    mapping_window.title("Keyword Mapping Window")
    
    tk.Label(mapping_window, text="Keyword:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    keyword_entry = tk.Entry(mapping_window, width=30)
    keyword_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

    tk.Label(mapping_window, text="Key:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    key_entry = tk.Entry(mapping_window, width=30)
    key_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    tk.Label(mapping_window, text="Feedback:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    feedback_entry = tk.Entry(mapping_window, width=30)
    feedback_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    tk.Button(mapping_window, text="Add Mapping", command=save_entry).grid(row=3, column=0, columnspan=2, pady=10)
    
    tk.Label(mapping_window, text="Keyword Mappings").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    
    display_frame = tk.Frame(mapping_window)
    display_frame.grid(row=5, column=0, columnspan=2, sticky='nsew')

    canvas = tk.Canvas(display_frame)
    text_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=text_frame, anchor="nw")

    canvas.pack(side="left", fill="both", expand=True)
    display_frame.grid_rowconfigure(0, weight=1)
    display_frame.grid_columnconfigure(0, weight=1)
    text_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    display_content = tk.Text(text_frame, wrap="word", height=15, width=50, state=tk.DISABLED)
    display_content.pack(padx=10, pady=10, fill="both", expand=True)

    update_display()

    mapping_window.mainloop()
