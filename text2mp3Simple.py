from gtts import gTTS

text = """To prepare for a hot tub or steam room session, drink 16–32 ounces of water 1–2 hours before and another 8–16 ounces 15–30 minutes prior. 
During longer sessions, sip water if you're in the steam room for more than 10–15 minutes. After the session, drink 16–24 ounces to replenish lost fluids. 
Avoid caffeine or alcohol beforehand, as they can cause dehydration. Listen to your body and step out if you feel dizzy or lightheaded. 
Wear a towel or lightweight clothing, shower before entering, and consult a doctor if you have medical conditions. 
Keep sessions between 10–20 minutes, sip water if thirsty, and step out if the heat feels overwhelming. 
After the session, cool down gradually, rehydrate, and moisturize your skin. Avoid using a steam room on a full stomach or immediately after eating, 
and use it in moderation, about 2–3 times a week."""

tts = gTTS(text, lang='en', tld='com')
tts.save("steam_room_instructions.mp3")
print("MP3 file saved successfully!")