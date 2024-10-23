import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
    speak("Hello sir, I am Gini your voice assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def main():
    wishme()
    while True:
        query = take_command().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif "play music" in query:
            music_query = query.replace("play music", "").strip()
            if music_query:
                speak(f"Playing {music_query} on YouTube.")
                webbrowser.open(f"https://www.youtube.com/results?search_query={music_query}")
            else:
                speak("What music do you want to play?")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'search for' in query:
            search_query = query.replace('search for', '').strip()
            speak(f"Searching Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'calculate' in query:
            try:
                query = query.replace('calculate', '').strip()
                result = eval(query)
                speak(f"The result is {result}")
                print(f"Result: {result}")
            except Exception as e:
                speak("Sorry, I couldn't perform the calculation.")

        elif 'stop' in query:
            speak("Goodbye, Sir!")
            exit()

main()
