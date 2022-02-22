#python 3.7.1

import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir...!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir...!")

    else:
        speak("Good Evening Sir...!")
    print("Tell me how i can help you...")
    speak("Tell me how i can help you...")


def takecommand():
    #Its takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        #print("Recognition...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again Please...")
        print("Say that again Please...")
        return "None"
    return query



if __name__=="__main__":
    #speak("Girja eye Recognition!!")
    #speak('Welcome Girja')
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('Wikipedia',"")
            results = wikipedia.summary(query,sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)
            time.sleep(5)

        elif 'open' in query:
          speak('opening...',)
          query = query.replace('open',"")
          speak(query)
          print('Opening',query)
          query = query+'.com'
          results = webbrowser.open(query)
          time.sleep(5)

        elif 'mobile' in query:
            speak('opening...')
            query = query.replace('mobile',"")
            speak(query)
            print('Opening',query)
            query = query +'.exe'
            os.startfile(query)
            time.sleep(3)

        elif 'play' in query:
            query = query.replace('play',"")
            speak('playing...'+ query +'Song on Youtube..')
            print('playing'+ query +' Song')
            pywhatkit.playonyt(query)
            time.sleep(6)

        elif 'time' in query:
            tim= datetime.datetime.now().strftime('%I:%M %p')
            print(tim)
            speak('current time is..'+ tim)

        elif 'jokes' in query:
            speak('Getting jokes ready')
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'close' in query or 'shutdown' in query:
            speak('Okh'+ query)
            break

        else:
            speak('Im sorry, but I cant help with that.')
            print('Im sorry, but I cant help with that.')
            continue
