import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib

#Text to Speech intialization

engine = pyttsx3.init()
voices = engine.getProperty('voices') #get current voice property 
engine.setProperty('voice', voices[1].id) # 1 for female voice (default is male)
rate = engine.getProperty('rate')   # getting details of current speaking rate                       
engine.setProperty('rate', 190)
#engine.say("hello Selva!")
engine.runAndWait()

def speak(audiotxt):
    engine.say(audiotxt)
    engine.runAndWait()

#Current Time function
    
def getTime():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for 12 hr clock (If 24 hr is needed then use %H instead of %I)
    speak("The current time is")
    speak(Time)

#Current Date function
    
def getDate():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Date = datetime.datetime.now().day
    speak("The current date is ")
    speak(Date)
    speak(Month)
    speak(Year)
    
#Wish the Person

def wishMe():
    speak("Welcome back! Selva")
    getTime()
    getDate()
    
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 20:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
        
    speak("It's Friday at your Service! Please tell me how can I help you today ?")

def listenToCommand():
    r = sr.Recognizer() #used to recognize the voice
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 #represents the minimum length of silence (in seconds) that will register as the end of a phrase
        audio = r.listen(source)
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-US")
        print(query)
        
    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"
    return query

if __name__ == '__main__':
    
    #wishMe() UNCOMMENT IT AT THE END
    
    while True:
        
        query = listenToCommand().lower() #all query will be stored in lower for better recognition
        
        if 'time' in query:
            getTime()
            
        elif 'date' in query:
            getDate()
            
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(result)
            speak(result)
            










        
