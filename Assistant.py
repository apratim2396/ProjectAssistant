import subprocess  
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

    return info


    