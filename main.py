import speech_recognition as sr  # Speech recognition library
import webbrowser                # For opening URLs in a web browser
import pyttsx3                   # Text to speech conversion
import musicLibrary              # Custom module for music links (make sure you have this module)
import os                        # To interact with the operating system
import datetime                  # To get current date and time

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process recognized voice commands
def processCommand(c):
    c = c.lower()  # Convert command to lowercase for easy matching

    if "open google" in c:
        webbrowser.open("https://google.com")  # Opens Google
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com/")  # Opens YouTube
    elif "open hotstar" in c:
        webbrowser.open("https://www.hotstar.com/in/home")  # Opens Hotstar
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")  # Opens Facebook
    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")  # Opens Gmail
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")  # Opens LinkedIn
    elif c.startswith("play"):
        song = c.split(" ")[1]  # Gets the song name
        link = musicLibrary.music.get(song)  # Fetch the link from your musicLibrary dictionary
        if link:
            webbrowser.open(link)  # Opens the song link
        else:
            speak("Song not found in your music library.")
    elif "open music" in c:
        musicpath = "C:\\Users\\sarth\\Downloads\\ishqhai.mp3"  # Path to your music file
        if os.name == "nt":  # Check if the OS is Windows
            os.startfile(musicpath)  # Play music
    elif "the time" in c:
        hour = datetime.datetime.now().strftime("%H")  # Get current hour
        min = datetime.datetime.now().strftime("%M")  # Get current minute
        speak(f"Sir, the time is {hour} and {min} minutes.")  # Announce the time
    elif "open camera" in c:
        os.system("start microsoft.windows.camera:")  # Open Windows Camera
    elif "open calculator" in c:
        os.system("calc")  # Open Calculator
    else:
        speak("I did not understand that command.")  # Fallback response

# Main program starts here
if __name__ == "__main__":
    speak("Starting the JARVIS BOT")  # Speak on startup
    while True:
        r = sr.Recognizer()
        print("Recognizing...!")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)  # Short listen for wake word
                word = r.recognize_google(audio)  # Recognize speech using Google API
                
                if word.lower() == "jarvis":
                    speak("Yes")  # Jarvis acknowledges the wake word
                    
                    with sr.Microphone() as source:
                        print("Jarvis Active...! Listening for your command.")
                        audio = r.listen(source)  # Listen for the actual command
                        command = r.recognize_google(audio)  # Recognize the spoken command
                        processCommand(command)  # Process the command
        except Exception as e:
            print(f"Error found: {e}")  # Print errors to console



