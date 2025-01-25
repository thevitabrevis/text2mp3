import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import logging
import pyttsx3
import os
import json

# Configuration file
CONFIG_FILE = "tts_config.json"

# Default configuration
DEFAULT_CONFIG = {
    "rate": 200,
    "volume": 1.0,
    "voice_index": 0,
    "last_directory": os.path.expanduser("~"),
    "input_text": ""
}

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return DEFAULT_CONFIG

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

config = load_config()

# Reset logging configuration
logging.basicConfig(level=logging.ERROR)

def text_to_speech_with_rate(text, file_name, rate, volume, voice_index):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)
        voices = engine.getProperty("voices")
        if 0 <= voice_index < len(voices):
            engine.setProperty("voice", voices[voice_index].id)
        else:
            raise ValueError("Invalid voice index")

        engine.save_to_file(text, file_name)
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False

def convert_button_clicked():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to convert.")
        return

    try:
        rate = int(rate_entry.get())
        volume = float(volume_entry.get())
        voice_index = int(voice_index_entry.get())

        if volume < 0 or volume > 1:
            raise ValueError("Volume must be between 0 and 1")
        if rate < 0:
            raise ValueError("Rate must be positive")

        filename_suggestion = input_text[:20].replace(" ", "_") + ".mp3"

        if config.get("last_directory"):
            file_path = os.path.join(config["last_directory"], filename_suggestion)
            if os.path.exists(config["last_directory"]):
                if text_to_speech_with_rate(input_text, file_path, rate, volume, voice_index):
                    status_label.config(text=f"Last saved: {file_path}", fg="darkgreen", font=("", 10, "bold"))
            else:
                messagebox.showerror("Error", f"Default directory does not exist: {config['last_directory']}. Please set a new default directory.")
                config["last_directory"] = os.path.expanduser("~")
                save_config(config)
                directory_label.config(text=f"Default Directory: {config['last_directory']} (This is the default)")
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".mp3",
                filetypes=[("MP3 Files", "*.mp3")],
                initialdir=os.path.expanduser("~"),
                initialfile=filename_suggestion
            )
            if file_path:
                config["last_directory"] = os.path.dirname(file_path)
                save_config(config)
                if text_to_speech_with_rate(input_text, file_path, rate, volume, voice_index):
                    status_label.config(text=f"Last saved: {file_path}", fg="darkgreen", font=("", 10, "bold"))

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def change_directory():
    new_directory = filedialog.askdirectory()
    if new_directory:
        config["last_directory"] = new_directory
        save_config(config)
        directory_label.config(text=f"Default Directory: {config['last_directory']} (This is the default)")

def on_closing():
    config["rate"] = int(rate_entry.get())
    config["volume"] = float(volume_entry.get())
    config["voice_index"] = int(voice_index_entry.get())
    config["input_text"] = input_text_area.get("1.0", tk.END).strip()
    save_config(config)
    window.destroy()

window = tk.Tk()
window.title("Text to Speech Converter")
window.protocol("WM_DELETE_WINDOW", on_closing)

input_label = tk.Label(window, text="Input Text:")
input_label.pack(pady=(10, 0))
input_text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
saved_text = config.get("input_text", "")
if saved_text:
    input_text_area.insert("1.0", saved_text)
input_text_area.pack(padx=10, pady=(0, 10))

input_frame = tk.Frame(window)
input_frame.pack()

rate_label = tk.Label(input_frame, text="Rate:")
rate_label.grid(row=0, column=0, padx=5, pady=5)
rate_entry = tk.Entry(input_frame, width=5)
rate_entry.insert(0, str(config["rate"]))
rate_entry.grid(row=0, column=1, padx=5, pady=5)

volume_label = tk.Label(input_frame, text="Volume (0-1):")
volume_label.grid(row=0, column=2, padx=5, pady=5)
volume_entry = tk.Entry(input_frame, width=5)
volume_entry.insert(0, str(config["volume"]))
volume_entry.grid(row=0, column=3, padx=5, pady=5)

voice_index_label = tk.Label(input_frame, text="Voice Index:")
voice_index_label.grid(row=0, column=4, padx=5, pady=5)
voice_index_entry = tk.Entry(input_frame, width=5)
voice_index_entry.insert(0, str(config["voice_index"]))
voice_index_entry.grid(row=0, column=5, padx=5, pady=5)

convert_button = tk.Button(window, text="Convert", command=convert_button_clicked)
convert_button.pack(pady=(0, 5))

# Status Label
status_label = tk.Label(window, text="", fg="darkgreen", font=("", 10, "bold"))
status_label.pack()

# Directory display and change button
directory_label = tk.Label(window, text=f"Default Directory: {config['last_directory']} (This is the default)")
directory_label.pack()
change_dir_button = tk.Button(window, text="Change Default Directory", command=change_directory)
change_dir_button.pack(pady=(0, 10))

exit_button = tk.Button(window, text="Exit", command=on_closing)
exit_button.pack(pady=(0,10))

window.mainloop()