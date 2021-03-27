import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') #get current voice property 
engine.setProperty('voice', voices[1].id) # 1 for female voice (default is male)
engine.say("hello Selva!")
engine.runAndWait()

def speak(audiotxt):
    engine.say(audiotxt)
    engine.runAndWait()

speak("Good Night")