import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# Adjusting the rate (speed) of speech
engine.setProperty('rate', 170)  # You can adjust this value as needed

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()
