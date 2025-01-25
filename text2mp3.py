import logging
import pyttsx3

# Reset logging configuration to avoid conflicts
logging.basicConfig(level=logging.ERROR)  # Suppress lower-level messages like DEBUG or INFO

def text_to_speech_with_rate(text, file_name, rate, volume, voice_index):
    try:
        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Set the speech rate
        engine.setProperty("rate", rate)

        # Set the volume (1.0 is the maximum)
        engine.setProperty("volume", volume)

        # Set the voice (use voice_index to toggle between voices)
        voices = engine.getProperty("voices")
        if voice_index < len(voices):
            engine.setProperty("voice", voices[voice_index].id)

        # Save to an audio file
        engine.save_to_file(text, file_name)

        # Run the engine to process text-to-speech
        engine.runAndWait()

        print(f"Audio file saved successfully as {file_name}!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Text to convert to speech
text = """To prepare for a hot tub or steam room session, drink 16–32 ounces of water 1–2 hours before and another 8–16 ounces 15–30 minutes prior. 
During longer sessions, sip water if you're in the steam room for more than 10–15 minutes. After the session, drink 16–24 ounces to replenish lost fluids. 
Avoid caffeine or alcohol beforehand, as they can cause dehydration. Listen to your body and step out if you feel dizzy or lightheaded. 
Wear a towel or lightweight clothing, shower before entering, and consult a doctor if you have medical conditions. 
Keep sessions between 10–20 minutes, sip water if thirsty, and step out if the heat feels overwhelming. 
After the session, cool down gradually, rehydrate, and moisturize your skin. Avoid using a steam room on a full stomach or immediately after eating, 
and use it in moderation, about 2–3 times a week."""

# Call the function to generate speech
text_to_speech_with_rate(text, r"C:\Users\thevi\OneDrive\Audio\TTS\test.mp3", rate=220, volume=0.9, voice_index=1)
