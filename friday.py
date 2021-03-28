import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices') #get current voice property 
engine.setProperty('voice', voices[1].id) # 1 for female voice (default is male)
engine.say("hello Selva!")
engine.runAndWait()

def speak(audiotxt):
    engine.say(audiotxt)
    engine.runAndWait()
    
def getTime():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for 12 hr clock (If 24 hr is needed then use %H instead of %I)
    speak("The current time is")
    speak(Time)
    
getTime()   

