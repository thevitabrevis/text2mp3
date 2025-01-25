import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}")