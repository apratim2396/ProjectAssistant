import ctypes
import datetime
import json
import os
import _pyinstaller_hooks_contrib
import tkinter                       #not used yet
import random                        #not used yet
import operator                      #not used yet
import winshell                      #not used yet
import feedparser                    #not used yet
import requests                      #not used yet
import shutil                        #not used yet
from twilio.rest import Client       #not used yet
from bs4 import BeautifulSoup        #not used yet
import win32com.client as wincl      #not used yet
import smtplib
import subprocess
import sys
import time
import webbrowser
from urllib.request import urlopen
import pyjokes
import pyttsx3
import speech_recognition as sr
import wolframalpha
from ecapture import ecapture as ec
from wikipedia import wikipedia

s = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):            #we will use talk word to let the system speak
    engine.say(audio)
    engine.runAndWait()

def greet():
    name = ("Ruhi")
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

def sendEmail(to, msg, sub, content=None):
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
            pyttsx3.speak('Opening Youtube')
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
            pyttsx3.speak("according to wikipedia")
            print( results)
            pyttsx3.speak(results)

        elif "what is" in info:
            pyttsx3.speak('searching')
            Client = wolframalpha.Client("API_ID")
            res = client.info(info)

            try:
                print(next(res.results).text)
                pyttsx3.speak(next(res.results).text)
            except StopIteration:
                print("No Result")

        elif 'open google' in info:
            pyttsx3.speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'time' or 'the time' or 'samay btao' in info:
            strTime = datetime.datetime.now().strftime("% H:% M: % S")
            pyttsx3.speak("Time now is {strTime}")

        elif 'send an email' or 'send a mail' or 'send mail' in info:
            try:
                pyttsx3.speak("to whom you want to send email?")
                to = input()
                pyttsx3.speak("what will be the subject of the email ?")
                sub = commands()
                pyttsx3.speak("what msg do you want to send ?")
                msg  = commands()
                sendEmail(to, msg, sub)
                pyttsx3.speak("email sent successfully!")
            except Exception as e:
                print(e)
                pyttsx3.speak("Sorry Email not sent")

        elif 'i love you' in info or 'do you love me' in info:
            pyttsx3.speak("Tinder download kar lo aap, Yaha Daal nahi galne wali")

        elif 'who are you' in info:
            pyttsx3.speak("I am your amazing assistant")

        elif 'you suck' in info or 'you are dumb' in info:
            pyttsx3.speak("I'm just like you")
        
        elif 'how are you' in info or 'how are you doing' in info:
            pyttsx3.speak("I'm gud what about you")
        
        elif 'can you be my girlfriend' in info:
            pyttsx3.speak("I think you need to use tinder")
            webbrowser.open("https://tinder.com/")

        elif 'do you love me' in info:
            pyttsx3.speak("I love you as a friend; sorry not sorry")
        
        elif 'what is temperature' in info:
            webbrowser.open("https://www.google.com/search?q=what+is+temperature&rlz=1C1JJTC_enIN935IN935&oq=what+is+tempera&aqs=chrome.0.0i433i512j69i57j0i512j0i457i512j0i512l6.8690j1j7&sourceid=chrome&ie=UTF-8")
            print(results)
            pyttsx3.speak(results)
        elif 'who made you' in info or 'reason for you' in info or 'why were you made' in info:
            pyttsx3.speak("My master Yash was so single that he decided to make an Artificial Girlfriend for him. Yes He is my love.")

        elif 'tell me joke' in  info or 'i am bored' in info:
            pyttsx3.speak(pyjokes.get_joke())

        elif "calculate" or "solve" in info:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = info.lower().split().index('calculate')
            info = info.split()[indx + 1:]
            res = client.info(' '.join(info))
            answer = next(res.results).text
            print("answer: " + answer)
            pyttsx3.speak("the calculated value is " + answer)

        elif 'shutdown' in info:
            pyttsx3.speak("Thand Rakhh Band kar rhi hu")
            os.system("shutdown /s /t 30")

        elif "restart" in info:
            subprocess.call(["shutdown", "/r"])

        elif 'find location of' in info or "where is" in info:
            if len(sys.info) > 1:
                map_string =' '.join(sys.info[1:])
                webbrowser.open('https://www.google.com/maps/place/' + map_string)
            else:
                print("Speak again")

        elif 'news' in info:
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                pyttsx3.speak('Bringingthe news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    pyttsx3.speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e)) 
        elif 'better than siri' in info or 'better then siri' in info or 'better than alexa' in info or 'better then alexa' in info or 'better than cortana' in info or 'better then cortana' in info:
            pyttsx3.speak("Hah! Mai itni sundar hu mai kya karu, they are nothing in comparision to me")
            
        elif 'i am sad' in info:
            pyttsx3.speak('dont be sad I am here for you')
            pyttsx3.speak('Achha mai kuch songs suggest karti hu! aap sun na chahoge ? Say yes if you want to listen')
            commands()
            if 'yes' in info:
                pyttsx3.speak('Okey tell me hindi or english')
                commands()
                if 'hindi' in info:
                    webbrowser.open('https://youtu.be/-F8spsC9eFw')
                else:
                    webbrowser.open('https://youtu.be/pSbF6ZQ2vTc')
        
        elif "open camera" in info or "take a photo" in info:
            ec.capture(0, "assist Camera ", "img.jpg")
        
        elif 'set reminder'or 'remind me' in info:
            pyttsx3.speak("what shall i reminf you ?")
            commands()
            pyttsx3.speak("in how much time ?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            pyttsx3.speak(info)

        elif 'how can i impress someone' in info:
            pyttsx3.speak('Let me suggest you some results')
            webbrowser.open("https://www.google.com/search?q=how+to+impress+someone&rlz=1C1JJTC_enIN935IN935&oq=How+to+impress+someone&aqs=chrome.0.0i512l10.12441j1j4&sourceid=chrome&ie=UTF-8")

        elif 'what i shoul do ?' in info:
            pyttsx3.speak("why dont you try to learn something new ? What about coding ? or Padh lo thoda na bhai")

        elif 'how is the market' in info:
            webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
        
        elif 'feeling sad' in info:
            pyttsx3.speak("Dont be sad, lets watch some movies together")

        elif 'lock window' in info:
            pyttsx3.speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "don't listen" in info or "stop listening" in info:
            pyttsx3.speak("For How much time i need to be stop")
            a = int(commands())
            time.sleep(a)
            print(a)
