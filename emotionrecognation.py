import speech_recognition as sr
import librosa
import numpy as np
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = None
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            query = None
        return query, audio

def detect_emotion(audio):
   
    with open("temp.wav", "wb") as f:
        f.write(audio.get_wav_data())

    y, sr = librosa.load("temp.wav")

    pitch = librosa.yin(y, fmin=75, fmax=300).mean()
    volume = np.mean(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max))
    if pitch > 200:
        return "excited"
    elif volume < -20:
        return "calm"
    else:
        return "neutral"
def speak_emotion(audio):
    emotion = detect_emotion(audio)
    speak(f"I detect you are feeling {emotion}.")
    if emotion == "excited":
        speak("You seem excited")
    elif emotion == "calm":
        speak("You seem calm")
    else:
        speak("You seem neutral")