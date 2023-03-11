import datetime
#from black import main
import pyttsx3
import datetime
from zmq import device
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib,ssl
import pyjokes 
import wikipedia as googleScrap
import pywhatkit
import pywhatkit as kit
from pywikihow import RandomHowTo, search_wikihow
from os import startfile
from pyautogui import click
import requests
from time import sleep
import psutil
import tkinter



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices',voices[2].id)
engine.setProperty('rate',165)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! How may i help you Sir?")
        print("Good Morning! How may i help you Sir?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!  How may i help you Sir?")
        print("Good afternoon! How may i help you Sir?")


    else:
        speak("Good Evening!  How may i help you Sir?")
        print("Good Evening! How may i help you Sir?")

def takecommand():

    #it takes input from MP from user (string)
    r = sr.Recognizer()
    
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
       # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login('lunaminipro9@gmail.com', "Luna.apk19")
        server.sendmail('lunaminipro9@gmail.com', 'crce.9147.ecs@gmail.com', content)
        server.close()

def emailer(msg):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "lunaminipro9@gmail.com"  # Enter your address
    receiver_email =  "crce.9147.ecs@gmail.com"# Enter receiver address
    password = "Luna.apk19"
    message = msg
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    speak ("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    speak("This May Also Help You Sir .")

def how_to(query):
    max_results = 1
    how_to = search_wikihow(query, max_results)
    assert len(how_to) == 1
    print(how_to[0].summary)
    speak("Here is " + query)

def search(query):
    query = query.replace("search","")
    query = query.replace("what is","")
    speak("Here is what I have found from google ")
    try:
        kit.search(query)
        result = googleScrap.summary(query,2)
        print(result)
    except:
        speak("Audible data not found")

def RAM():
    total_ram = psutil.virtual_memory()[0]
    total_ram = total_ram // 10**9
    available_ram = psutil.virtual_memory()[1]
    available_ram = available_ram // 10**9
    used_ram = psutil.virtual_memory()[3]
    used_ram = used_ram // 10**9
    
    print('>> Total RAM:', total_ram,"GB")
    print('>> Used RAM:', used_ram,"GB")
    print('>> Available RAM:', available_ram,"GB")
    print('>> RAM memory used:', psutil.virtual_memory()[2],"%")
    speak("Here are the RAM status")

def battery():
    battery = psutil.sensors_battery() 
    percentage = battery.percent  #fetching battery percentage
    sec_left = battery.secsleft   # fetching how many seconds left before battery drains out
    power = battery.power_plugged # fetching information whether charger is connected or not
    min_left = sec_left/60    # converting seconds left before battery drains out into minutes. NOTE: the value is in float
    min_left = int(min_left)  # converting float into integer to remove decimal points
    power = str(power)        # converting datatype of 'power' varibale which was in bool to string

    def p():
        true = "True"
        if true in power:  # if charger is connected that means its true then show the following sentence
            return("the battery is " + str(percentage) + "% " + "and charger is connected.")  
        else:  # if charger is not connected that means its false then show the following sentence
            return("the battery is " + str(percentage) + "%, " +  str(min_left) + " minutes left before it drains out and charger is not connected.")

    a = p()  #taking the output of funtion p in variable 
    print(a)
    speak(a)



if __name__ == "__main__":
    speak("Hi I am LUNA! ")
    wishMe()
    while True:
    # if 1:
        query = takecommand().lower() 

       
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "what can you do" in query:  
            print("I can do many things like:\n 1.  Tell  time \n 2.  Tell jokes.\n 3.  Play songs.\n 4.  Open websites.\n"
                " 5.  Launch desktop applications.\n 6.   Write a note..\n 7.  Answer any GK questions.\n 8.  Write a note.\n"
                " 9.  Answer any GK questions.\n 10. Search anything from Google.\n 11. Search anything from Wikipedia.\n 12. Play videos from YouTube.\n"
                " 13. Tell recipie or steps about anything\n 14. Tell batteryinternal drive & RAM status.\n 15. Tell boot time.\n 16.Open Email")

        elif "luna" in query or "Luna" in query:
            print("Yes Sir, I am online....")
            speak("Yes Sir, I am online.")

        elif "your name" in query or "who are you" in query:
             print("I am LUNA Your personal Assistant...")
             speak("I am LUNA Your personal Assistant ")

        elif 'open youtube' in query:
            speak("Sequencing")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sequencing")
            webbrowser.open("google.com")

        elif 'open email' in query:
            speak("Sequencing")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'open stack overflow' in query:
            speak("Sequencing")
            webbrowser.open("stackoverflow.com")
        
        elif 'open facebook' in query:
            speak("Sequencing")
            webbrowser.open("facebook.com")

        elif 'open hackerrank' in query:
            speak("Sequencing")
            webbrowser.open("hackerrank.com")

        elif 'youtube search' in query:
            speak("Sequencing")
            YouTubeSearch(query)

        elif 'download the video' in query:
            from Features import DownloadYouTube
            DownloadYouTube()

        elif "how to" in query:
            speak("Sequencing")
            how_to(query)

        elif 'play music' in query:
            speak("Initialising")
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            speak("Sequencing")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        elif 'open python code' in query:
            speak("Sequencing")
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open telegram' in query:
            speak("Sequencing")
            codePath = "E:\Telegram Desktop\Telegram.exe"
            os.startfile(codePath)

        elif 'open word' in query:
            speak("Sequencing")
            codePath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("Sequencing")
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open Brave' in query:
            speak("Sequencing")
            codePath = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(codePath)

        elif 'write a note' in query:
            speak("Sequencing")
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'joke' in query: 
           speak(pyjokes.get_joke())

        elif 'play' in query:
            speak("Sequencing")
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)  

        elif 'covid cases' in query:
            from Features import CoronaVirus

            speak ("which Country's Information do you want at the moment ?")
            cn = takecommand()
            CoronaVirus(cn)
            speak (f"")

        elif 'search about ' in query:
            speak("Sequencing")
            search(query)

        elif "RAM" in query or "ram" in query:
            speak("Sequencing")
            RAM()

        elif "battery" in query:
            speak("Sequencing")
            battery()  

        elif "boot time" in query: 
            speak("Sequencing")  
            print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

        elif 'thank' in query or 'thanks' in query:
            print("No Problem Sir :)")
            speak("No Problem Sir ")

        elif "bye" in query or "stop" in query or "ok bye" in query or "goodbye" in query or "exit" in query:
            speak("Thanks for giving me your time ,hope to see you again Sir...")
            print("Thanks for giving me your time ,hope to see you again <3...")
            break

top = tkinter.Tk()

top.mainloop()
