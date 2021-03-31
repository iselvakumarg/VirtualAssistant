import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
import wolframalpha
import time
import os


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

#SENDING EMAIL FUNCTIONALITY

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    #for this func. to work, you must enable low security in your gmail settings (sender's mail)
    server.login("username@gmail.com", "password")
    server.sendmail("username@gmail.com", to, content)
    server.close()
    
    
#CPU USAGE & BATTERY

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
 
    
#TELL JOKE
def joke():
    joke = pyjokes.get_joke()
    speak(joke)


#TAKE SCREENSHOT
def screenshot():
    image = pyautogui.screenshot()
    image.save(r"C:\Users\SELVAKUMAR\Dropbox\My PC (DESKTOP-8IQTHPU)\Desktop\screenshot.png") #add your path save to screenshot


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
            
       elif 'send email' in query:
            try:
                speak("What should I say?")
                content = listenToCommand()
                
                speak("Who is the Receiver?")
                receiver = ("Enter Receiver's Email : ")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent.")
                
            except Exception as e:
                print(e)
                speak("Unable to send Email.")
        

        #OPEN YOUTUBE
        
        elif 'search youtube' in query:
            speak("what should I search")
            search_term = listenToCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open("https://www.youtube.com/results?search_query="+search_term)
            
        #SEARCH ON GOOGLE
        
        elif 'search google' in query:
            speak("what should I search")
            search_term = listenToCommand().lower()
            speak('Searching....')
            wb.open('https://www.google.com/search?q='+search_term)
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            joke()
            
        elif 'go offline' in query:
            speak("going offline sir!")
            quit()
            
        elif 'write a note' in query:
            speak("what should I write, Sir?")
            notes = listenToCommand()
            file = open('notes.txt', 'w')
            speak("Sir should I include Date and Time?")
            ans = listenToCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("Done taking notes, SIR!")
            else:
                file.write(notes)
                
        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'remember that' in query:
            speak("What should I remember? ")
            memory = listenToCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
            
        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak('You asked me to remember that'+remember.read())
            
        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            speak("User asked to locate"+ location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            
        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is : " + answer)
            speak("The answer is: "+ answer)
            
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")
                
        elif 'stop  listening' in query:
            speak('For how many second you want me to stop listening to your commands?')
            ans = int(listenToCommand())
            time.sleep(ans)
        
        elif 'logout' in query:
            os.system('shutdown -l')
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            










        
