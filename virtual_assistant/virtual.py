import pyttsx3

import datetime
#import speech_recognition as sr

engine = pyttsx3.init()  # line 1

engine.setProperty('rate', 150)  # line 2

engine.setProperty('volume', 0.9)  # line 3

voices = engine.getProperty('voices')  # line 4

engine.setProperty('voice', voices[0].id)  # line 5

engine.say('so here is a little song i wrote,i hope that you get it note for note....be happy...dont worry')  # line 6

engine.runAndWait()  # line 7

def speak (audio):

    engine.say(audio)

    engine.runAndWait()

speak ("Talking is amaziing")

def time():

    Time = datetime.datetime.now().strftime("%H:%M:%S")# gives us the current time and date

    speak("The time is:")

    speak(Time)

time()

def year():

    Year = int(datetime.datetime.now().year) # we apply the int() function in order to make our results readable

    Month = int(datetime.datetime.now().month)

    Day = int(datetime.datetime.now().day)

    speak("Today's date is:")

    speak(Day)

    speak (Month)

    speak(Year)

year()
