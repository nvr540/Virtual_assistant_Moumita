from posixpath import curdir
import pyautogui
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import os
from pyautogui import *
import random
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(str):
    engine.say(str)
    engine.runAndWait()
def hello(command):
    speak("Hello Sir, How are you")
    if "moumita" not in command and len(command.split(" ")) > 1:
        command = command.split(" ")
        speak(f"By the way, My name is Moumita, not {command[1]}")
def statusAnswer():
    speak("I am working well, Sir. At present, I am waiting for you order. What about you?")
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >=6  and hour <= 12:
        speak("Good Morning, Nivrita. I'm Moumita in your service")
    elif hour >= 12 and hour <= 15:
        speak("Good Noon, Nivrito. I'm Moumita in your service")
    elif hour >= 15 and hour <= 18:
        speak("Good afternoon, Nivrito. I'm Moumita in your service")
    elif hour >= 18 and hour <= 21:
        speak("Good Evening, Nivrito. I'm Moumita in your service")
    elif hour >= 21 and hour <= 24:
        speak("Good Night, Nivrito. I'm Moumita in your service")
    else:
        speak("Good night Nivrito. You should sleep now. Do you need any help")
def webBrowser(string):  
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
    web = webbrowser.get(chrome_path)
    domain = string.replace('open ','')
    web.open(domain.replace(" ",'') + '.com')
    speak(f"opening {domain}")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.phrase_threshold = 0.5
        r.energy_threshold = 700
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-US")
        return command
    except Exception as e:
        speak("Please Say it again.")
def musicPlayer(command):
    if 'bangla' in command:
        os.startfile("C:\\Users\\Moumita\\Music\\Playlists\\Bangla_Songs.zpl")
    elif 'play' in command:
        os.startfile(os.path.join(musicDir ,songs[random.randint(0, len(songs))]))
    # elif 'forward' in command or 'next' in command:
    #     press('f10') #pyautogui Function
    # elif 'previous' in command or 'back' in command:
    #     press('f9') #pytutogui Function
if __name__ == '__main__':
    greetings = ["hello", "moumita", "hi"]
    someGreetQuestions = ["what's up", "what are you doing", "what's going on", "what is going on"]
    musicDir = 'C:\\Users\\Moumita\\Music'
    songs = os.listdir(musicDir)
    # wishMe()
    i = 0;
    while True:
        command = str(listen()).lower()
        print(command)
        if any(word in command for word in greetings):
            hello(command)
        elif "i am fine" in command:
            speak("That's great! Sirrrr")
        elif command in someGreetQuestions:
            statusAnswer()
        elif "open" in command:
            webBrowser(command)
        elif "quit" in command:
            break
        elif any(word in command for word in ['song', 'music', 'gun','gan','gaan']):
            musicPlayer(command)
        else:
            if command != 'none':
                if i == 0:
                    speak(f'There is no argument like {command}')
                elif i == 1:
                    speak("Whattt!")
                elif i == 2:
                    speak("What the fuck are you saying Nivrito, I can't understand. I am leaving")
                    break
                i+=1
    # hotkey('alt', 'f9')