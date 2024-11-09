import pyttsx3
import datetime
import webbrowser
import wikipedia
import emotionrecognation

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        emotionrecognation.speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        emotionrecognation.speak("Good Afternoon ")
    else:
       emotionrecognation.speak("Good Evening ")
    emotionrecognation.speak("Hello sir, I am Gini your voice assistant. How can I help you?")

def main():
    print("Hello sir, I am Gini your voice assistant. How can I help you?")
    wishme()
    while True:
        query, audio = emotionrecognation.take_command()
        if query is not None:
            query = query.lower()  
            emotionrecognation.speak_emotion(audio)

            if 'open youtube' in query:
                emotionrecognation.speak( "Opening YouTube...")
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                emotionrecognation.speak(" Opening Google...")
                webbrowser.open("google.com")
            elif 'open github' in query:
                emotionrecognation.speak(" Opening GitHub...")
                webbrowser.open("github.com")
            elif 'open linkedin' in query:
                emotionrecognation.speak("Opening LinkedIn...")
                webbrowser.open("linkedin.com")

            elif "play music" in query:
                music_query = query.replace("play music", "").strip()
                if music_query:
                    emotionrecognation.speak(f"Playing {music_query} on YouTube.")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={music_query}")
                else:
                    emotionrecognation.speak("What music do you want to play?")

            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                emotionrecognation.speak(f"Sir, the time is {strTime}")

            elif 'search for' in query:
                search_query = query.replace('search for', '').strip()
                emotionrecognation.speak(f"Searching Google for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

            elif 'wikipedia' in query:
                emotionrecognation.speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                emotionrecognation.speak("According to Wikipedia")
                emotionrecognation.speak(results)
                print(results)

            elif 'calculate' in query:
                try:
                    query = query.replace('calculate', '').strip()
                    result = eval(query)
                    emotionrecognation.speak(f"The result is {result}")
                    print(f"Result: {result}")
                except Exception as e:
                    emotionrecognation.speak("Sorry, I couldn't perform the calculation.")

            elif 'stop' in query:
                emotionrecognation.speak("Goodbye,Sir!")
                exit()

        else:
           print(" ")
main()
