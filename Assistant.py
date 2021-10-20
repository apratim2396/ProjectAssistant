import subprocess
from urllib.request import HTTPSHandler  
import wolframalpha
import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import pyjokes
import datetime
import time
import tkinter
import json
import random, operator, webbrowser, os
import winshell
import feedparser
from bs4 import BeautifulSoup
from urlib.requests import urlopen
from twilio.rest import Client
from client.texui import progress
from ecapture import ecapture as ec
import shutil
import ctypes
import smtplib
 #almost all imports completed will see if any left 
 # Now Starting to code
#info variable fortaking query
s = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('vioices')
engine.setProperty('voice', voices[1].id)

def talk(audio):            #we will use talk word to let the system speak
    engine.say(audio)
    engine.runAndWait()

def greet():
    name = ("yash")
    pyttsx3.speak("Hello Master!" + name + "here")
    pyttsx3.speak("What can I do for you ?")
    
def commands():
    with sr.Microphone() as source:
        print("Listening Baby")
        s.pause_threshold = 1
        audio = s.listen(source)
        s.adjust_for_ambient_noise(source)

    try:
        print("Recognising")
        info = s.recognize_google(audio, language = 'en-US')
        print(f"{info}\n")
    except Exception as e:
        print(e)
        print("could not be recognised" )
        talk( "voice not recognised")
        return "None"

def sendEmail(to, msg, sub):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

    return info


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    greet()

    pyttsx3.speak('What can I do for you')

    while True:

        info =  commands().lower()
        if 'open youtube' in info or ('play') in info: 
            speak('Opening Youtube')
            webbrowser.open("youtube.com")

        elif 'play songs' in info or ('play music') in info: 
            pyttsx3.speak('Opening Youtube')
            webbrowser.open("https://www.youtube.com/watch?v=3GI_uE4SxSU") 

        elif 'data strength' or 'internet speed' in info:
            pyttsx3.speak('opening fast.com')
            webbrowser.open("fast.com")
        
        elif 'open whatsapp' or 'whatsapp' or 'whats app' in info:
            pyttsx3.speak('opening whatsapp')
            webbrowser.open("web.whatsapp.com")
        elif 'instagram' in info:
            pyttsx3.speak('opening Instagram')
            webbrowser.open("instagram.com")
        
        elif "wikipedia" in info:
            pyttsx3.speak('searching in wikipedia')
            info = info.replace("wikipedia", "")
            results = wikipedia.summary(info, sentence=3)
            speak("according to wikipedia")
            print( results)
            speak(results)

        elif "what is" in info:
            pyttsx3.speak('searching')
            Client = wolframalpha.Client("API_ID")
            res = client.info(info)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Result")

        elif 'open google' in info:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'time' or 'the time' or 'samay btao' in info:
            strTime = datetime.datetime.now().strftime("% H:% M: % S")
            speak("Time now is {strTime}")

        elif 'send an email' or 'send a mail' or 'send mail' in info:
            try:
                speak("to whom you want to send email?")
                to = input()
                speak("what will be the subject of the email ?")
                sub = commands()
                speak("what msg do you want to send ?")
                msg  = commands()
                sendEmail(to, msg, sub)
                speak("email sent successfully!")
            except Exception as e:
                print(e)
                pyttsx3.speak("Sorry Email not sent")

        elif 'i love you' in info or 'do you love me' in info:
            speak("Tinder download kar lo aap, Yaha Daal nahi galne wali")

        elif 'who is are' in info:
            speak("I am your amazing assistant")

        elif 'you suck' in info or 'you are dumb' in info:
            speak("I'm just like you")
        
        elif 'how are you' in info or 'how are you doing' in info:
            speak("I'm gud what about you")
        
        elif 'can you be my girlfriend' in info:
            speak("I think you need to use tinder")
            webbrowser.open("https://tinder.com/")

        elif 'do you love me' in info:
            speak("I love you as a friend; sorry not sorry")
        
        elif 'what is temperature' in info:
            webbrowser.open("https://www.google.com/search?q=what+is+temperature&rlz=1C1JJTC_enIN935IN935&oq=what+is+tempera&aqs=chrome.0.0i433i512j69i57j0i512j0i457i512j0i512l6.8690j1j7&sourceid=chrome&ie=UTF-8")
            print(results)
            pyttsx3.speak(results)
        elif 'who made you' in info or 'reason for you' in info or 'why were you made' in info:
            pyttsx3.speak("My master Yash was so single that he decided to make an Artificial Girlfriend for him. Yes He is my love.")

        elif 'joke' in  info:
            pyttsx3.speak(pyjokes.get_joke())
            
