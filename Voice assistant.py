import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from pathlib import Path
import numpy as np
import bs4
import urllib.request as url

path = "https://www.indiatoday.in/news.html"
http_response = url.urlopen(path)
webpage = bs4.BeautifulSoup(http_response,'lxml')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Sir i am Khushi your Assistant please tell me how may i help you ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play cradles' in query:
             os.startfile('C://Users//OMRAJ//Downloads//Sub Urban - Cradles [NCS Release].mp3')
        
        elif 'play music' in query:
            music_dir = 'F://songs'
            songs = os.listdir(music_dir)  
            os.startfile(os.path.join(music_dir, songs[0]))
            so=np.array(songs)
            i=0
        elif 'play next song' in query:
            i=i+1
            os.startfile(os.path.join(music_dir,so[i]))
        elif 'play previous song' in query:
            i=i-1
            os.startfile(os.path.join(music_dir,so[i]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'news' in query:
            speak("Which type of news you want to hear sir")
        elif 'about movies'in query:
            h4=webpage.find('div',id="itg-news-section-2")
            mov=h4.findAll('p')
            for i in range(len(mov)):
                title1=mov[i]['title']
                speak(title1)
        elif 'about elections'in query:
            h4=webpage.find('div',id="itg-news-section-3")
            el=h4.findAll('p')
            for i in range(len(el)):
                title1=el[i]['title']
                speak(title1)
        elif 'about sports'in query:
            h4=webpage.find('div',id="itg-news-section-4")
            spr=h4.findAll('p')
            for i in range(len(spr)):
                title1=spr[i]['title']
                speak(title1)

        
        elif 'email to Rajat' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajat.bhardwaj2000@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rajat bhai. I am not able to send this email")    

