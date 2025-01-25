import pyttsx3
import logging

# Reset logging to avoid conflicts
logging.basicConfig(level=logging.ERROR)

def list_voices_and_test():
    try:
        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # List available voices
        voices = engine.getProperty('voices')
        for index, voice in enumerate(voices):
            print(f"Voice {index}: {voice.name}, ID: {voice.id}")

        # Test one of the voices
        engine.setProperty('voice', voices[2].id)  # Change the index as needed
        engine.say("Testing voice number 0.")
        engine.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'engine' in locals():
            engine.stop()  # Ensure the engine stops properly

# Run the function
list_voices_and_test()
