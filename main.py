import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Reduce the speech speed
engine.setProperty('rate', 180)  # Adjust speed (default is ~200)
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

# Function to make Friday speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

# Function to greet the user based on the time of day
def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi, I'm Friday. How can I assist you?")

# Function to listen to the user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("There is an issue with the speech recognition service.")
            return None

# Function to get Wikipedia summary
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for this query: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to execute user commands
def execute_command(query):
    if 'hello' in query:
        speak("Hello! I am Friday. How can I help you?")
    elif 'how are you' in query:
        speak("I'm doing great, thank you for asking!")
    elif 'time' in query:
        speak(f"The current time is {get_time()}")
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif 'open instagram' in query:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif 'open facebook' in query:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif 'play music' in query:
        music_file = r"D:\MUSIC\Agar Tum Saath Ho - Tamasha 320 Kbps.mp3"  # Corrected path
        if os.path.exists(music_file):
            os.startfile(music_file)
            speak("Playing music.")
        else:
            speak("Music file not found.")
    elif 'search' in query:
        search_query = query.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching for {search_query}")
    elif 'what is' in query:
        topic = query.replace("what is", "").strip()
        summary = get_wikipedia_summary(topic)
        speak(summary)
    elif any(op in query for op in ['add', 'subtract', 'multiply', 'divide', 'modulus']):
        try:
            query = query.replace("add", "+").replace("subtract", "-").replace("multiply", "*").replace("divide", "/").replace("modulus", "%")
            result = eval(query)
            speak(f"The answer is {result}")
        except:
            speak("Sorry, I couldn't perform the calculation.")
    elif 'open whatsapp' in query:
        whatsapp_path = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2450.6.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
        if os.path.exists(whatsapp_path):
            os.startfile(whatsapp_path)
            speak("Opening WhatsApp.")
        else:
            speak("WhatsApp is not installed or the path is incorrect.")
    elif 'open spotify' in query:
        spotify_path = r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.253.438.0_x64__zpdnekdrzrea0\Spotify.exe"
        if os.path.exists(spotify_path):
            os.startfile(spotify_path)
            speak("Opening Spotify.")
        else:
            speak("Spotify is not installed.")
    elif 'power off' in query:
        speak("Shutting down.")
        exit()
    else:
        speak("I'm not sure how to respond to that.")

# Main function to run Friday
def run_assistant():
    greet()
    while True:
        query = listen()
        if query:
            execute_command(query)

# Run the assistant
if __name__ == "__main__":
    run_assistant()