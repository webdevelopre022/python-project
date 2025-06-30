import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0=male, 1=female

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning, Sir.")
    elif hour < 18:
        speak("Good Afternoon, Sir.")
    else:
        speak("Good Evening, Sir.")
    speak("Jarvis at your service. How may I assist you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        print("Could not understand, please repeat.")
        return "None"
    return query.lower()

def send_email(to_addr, content):
    # ⚠️ Replace with your actual credentials in secure way
    SERVER = smtplib.SMTP('smtp.gmail.com', 587)
    SERVER.ehlo()
    SERVER.starttls()
    SERVER.login('your_email@gmail.com', 'your_password')
    SERVER.sendmail('your_email@gmail.com', to_addr, content)
    SERVER.close()

def main():
    wish_me()
    while True:
        query = take_command()
        if query == "none":
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'open vs code' in query:
            code_path = "C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'play music' in query:
            music_dir = "C:\\Users\\RAHUL\\Desktop\\music"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send email' in query:
            try:
                speak("What should I say?")
                body = take_command()
                to = "rahul@example.com"
                send_email(to, body)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email.")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye, Sir!")
            break

if __name__ == "__main__":
    main()
