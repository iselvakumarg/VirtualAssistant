# VirtualAssistant - FRIDAY 1.0.0

*A Mockup Virtual Asssitant of the MARVEL character IRONMAN*

### BASIC REQUIREMENT
---
  - Any Operating System with [Python](https://www.python.org/downloads/) latest version.
  - Anaconda3 

### PACKAGES USED
---
  1. [pyttsx3](https://pypi.org/project/pyttsx3/) - text to speech library
  2. datetime - used to get the current date and time & it is a pre-defined library
  3. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/1.3.0/) - library for performing speech recognition through online and offline
  4. pyaudio - provides Python bindings for PortAudio, the cross-platform audio I/O library
  
      downloading this package might get some errors through pypi website, If you face issues try :-
      
      ```pip install pipwin```
      
      ```pipwin install pyaudio```
  5. [wikipedia](https://pypi.org/project/wikipedia/) - is a Python library that makes it easy to access and parse data from Wikipedia
      
  6. smtplib - defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listner daemon.
  
   7. [psutil](https://pypi.org/project/psutil/) - cross-platform lib for process and system monitering in Python.
  
  8. [pyjokes](https://pypi.org/project/pyjokes/) - a basic joke library for python
  
  9. [pyautogui](https://pypi.org/project/PyAutoGUI/) - This package will let python to control the mouse and keyboard and other GUI automation tasks.

  10. [wolframalpha](https://pypi.org/project/wolframalpha/) - News api
  
  11. time - manage time 

  12. os - to interact with the OS

### Instruction for .EXE conversion 
---

To convert the .py file to an .exe file first download the [pyinstaller](https://pypi.org/project/pyinstaller/) package.

``` pyinstaller --onefile 'friday.py' ```

This will take around 3 - 5 minutes to convert the file to exe and which can use as a private cli to use the virtual assistant in the system locally.


  
  
  
