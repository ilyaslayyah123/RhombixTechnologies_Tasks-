# Custom Voice Assistant with Emotion Detection
This project is a Python-based voice assistant capable of performing various tasks, such as opening web applications, searching the web, and more. Recently enhanced with emotion detection, the assistant now tailors responses based on detected emotions like calm, excited, or neutral.

# Features
  # Voice Commands: 
           Recognizes and executes commands for opening websites (YouTube, Google, GitHub, etc.), searching Google, playing music, and providing the current time.
  # Emotion Detection:
                Identifies the speaker's emotional tone using pitch and volume analysis to detect if the user is calm, excited, or neutral. The assistant then adjusts responses accordingly.
  # Text-to-Speech Output:
            Provides responses using pyttsx3 to enhance user interaction.Technologies Used
Python: Core programming language.
  # Speech Recognition: 
        Processes user commands.
  # Librosa: 
          Analyzes audio signals for emotion detection.
  #  Pyttsx3: 
     Converts text responses to speech.
# Setup and Installation
# Clone this repository
git clone 
cd voice-assistant-emotion-detection
# Install required libraries:
pip install pyttsx3 SpeechRecognition wikipedia webbrowser numpy librosa
# Run the assistant:
python voice_Assistant.py
## Usage
Run the assistant: Upon launching, the assistant will greet you and listen for voice commands.
Emotion Detection: Speak normally, and the assistant will detect your emotional tone and adjust its responses.
Voice Commands: Use commands like "open YouTube," "search for [term] on Google," "play music," or "what's the time."
# File Structure
voice_Assistant.py: Main file with assistant logic.
emotionrecognation.py: Handles emotion detection and audio processing.
# Contributing
Feel free to fork this project and submit pull requests for additional features, improvements, or bug fixes!

# License
This project is open-source under the MIT License.
