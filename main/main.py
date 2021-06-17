from typing import Text
import pyautogui
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import os
import random
import smtplib
from word2number import w2n
from searchGoogle import searchGoogle, searchYoutube
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(str):
    """It's a speaking function which can convert text to Speech"""
    engine.say(str)
    engine.runAndWait()


def hello(command):
    """It's a greeting Function to give response to greeting"""
    speak("Hello Sir, How are you")
    if "moumita" not in command and len(command.split(" ")) > 1:
        command = command.split(" ")
        speak(f"By the way, My name is Moumita, not {command[1]}")
def wordToNumber(string):
    """It's a word To Number converting Function"""
    num = 1
    for word in string.split(" "):
        try:
           num = w2n.word_to_num(word)
        except:
            continue
    return num
def sendGmail(password, emailOfReceiver, Subject, Body):
    """Sending email to gmail users"""
    message = f"Subject: {Subject}\n\n{Body}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("shahedparves111@gmail.com", password)
    server.sendmail("shahedparves111@gmail.com",
                    emailOfReceiver,
                    message)
def wishMe():
    """It's a wishing function that will wish me according to the time. And run on every time I run it"""
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
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
    speak("Please call me with my name. To start the process")

def webBrowser(string):
    """It wil open the webbrowser chrome. Every time I want to open a domain"""
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
    web = webbrowser.get(chrome_path)
    domain = string.replace('open ', '')
    web.open(domain.replace(" ", '') + '.com')
    speak(f"opening {domain}")


def listen():
    """It listen's to my words and conversts it to text"""
    print("Listening")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        # r.phrase_threshold = 0.5
        # r.energy_threshold = 
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-US")
        return command
    except Exception as e:
        speak("Please Say it again.")


def goto(linenum):
    """It's a simple goto function"""
    global line
    line = linenum


def musicPlayer(command):
    """It starts the music player and plays a random song of my computer also a playlist of my computer"""
    if 'bangla' in command:
        os.startfile("C:\\Users\\Moumita\\Music\\Playlists\\Bangla_Songs.zpl")
    elif 'play' in command:
        os.startfile(os.path.join(
            musicDir, songs[random.randint(0, len(songs))]))


    # elif 'forward' in command or 'next' in command:
    #     press('f10') #pyautogui Function
    # elif 'previous' in command or 'back' in command:
    #     press('f9') #pytutogui Function
if __name__ == '__main__':
    greetings = ["hello", "moumita", "hi"]
    someGreetQuestions = ["what's up", "what are you doing",
                          "what's going on", "what is going on"]
    musicDir = 'C:\\Users\\Moumita\\Music'
    songs = os.listdir(musicDir)
    wishMe()
    i = 0
    line = 1
    while True:
        if line == 2:
            break
        query = str(listen()).lower()
        print(query)
        if query == "moumita":
            speak("Hello sir I'm Moumita in your service. How may I help you.")
            while True:
                command = str(listen()).lower()
                print(command)
                if any(word in command for word in greetings):
                    hello(command)
                elif "i am fine" in command:
                    speak("That's great! Sirrrr")
                elif command in someGreetQuestions:
                    speak("I am working well, Sir. At present, I am waiting for you order. What about you?")
                elif "open" in command:
                    webBrowser(command)
                elif "quit" in command:
                    speak("I am closing Sir.")
                    goto(2)
                    break
                elif "send email" in command:
                    speak("Please Enter the email Address, where you want to send email")
                    emailOfReceiver = pyautogui.prompt(text="Enter Your Email",title="Email Address")
                    speak("Please Enter your password")
                    password = pyautogui.password(text="Enter Your pass",title="Email Address")
                    Subject = pyautogui.prompt(text="Enter The Subject of email",title="Subject")
                    Body = pyautogui.prompt(text="Enter The Body of email",title="Body")
                    try:
                        sendGmail(password, emailOfReceiver, Subject, Body)
                        speak("Email Sent")
                    except:
                        speak("Something went wrong. Please enter your pass and receiver email again")
                        emailOfReceiver = pyautogui.prompt(text="Enter Your Email",title="Email Address")
                        password = pyautogui.password(text="Enter Your pass",title="Email Address")
                        try:
                            sendGmail(password, emailOfReceiver, Subject, Body)
                            speak("Email Sent")
                        except:
                            speak("Sorry! Again Something getting wrong. Closing the email sending process")


                elif 'shutdown' in command:
                    speak("Are you sure?")
                    answer = str(listen()).lower()
                    answerCanBe = ['yes', 'yep', 'ya', 'yup']
                    if any(word in command for word in answerCanBe):
                        os.system('shutdown')
                    else:
                        speak("Not shutting down the computer")
                elif "silence" in command:
                    speak("Ok sir. Please call me with my name when you need me")
                    break
                elif any(word in command for word in ['song', 'music', 'gun', 'gan', 'gaan']):
                    musicPlayer(command)
                elif "search" in command:
                    command = command.replace("search", '')
                    if "google" in command:
                        command = command.replace("google", '').replace("on", '')
                        webbrowser.open(f"https://www.google.com/search?q={command}")
                        speak("Do you want to open any link")
                        ans = listen()
                        if "yes" in ans or "yep" in ans or "yup" in ans:
                            num = wordToNumber(ans)
                            searchGoogle(command, num)
                            speak(f"Opening first {num} link")
                        else:
                            speak("Ok, Not opening any link")
                            speak()
                    elif "youtube" in command:
                        command = command.replace("youtube", '').replace('on', '')
                        searchYoutube(command)
                elif "burpsuite" in command or "burp" in command:
                    os.startfile("F:\Burpsuite_Software\launch_bat.vbs")
                else:
                    if command != 'none':
                        if i == 0:
                            speak(f'There is no argument like {command}')
                        elif i == 1:
                            speak("Whattt!")
                        elif i == 2:
                            speak("What the fuck are you saying Nivrito, I can't understand. I am leaving")
                            goto(2)
                            break
                        i += 1
        else:
            speak(f"My name is not {query}. Please call me correctly Or I will not Help you")
    
    # pyautogui.press('win')
    # pyautogui.write('music')