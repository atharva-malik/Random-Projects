import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import webbrowser
import datetime
import time
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speakStartUp():
    print("Starting server...")
    speak("Starting server...")
    time.sleep(random.randint(0, 10))
    print("Debugging program...")
    speak("Debugging program...")
    time.sleep(random.randint(0, 10))
    print("Getting things ready...")
    speak("Getting things ready...")
    time.sleep(random.randint(0, 10))
    print("Starting engines...")
    speak("Starting engines...")
    time.sleep(random.randint(0, 10))
    print("All engines are now ready to use...")
    speak("All engines are now ready to use...")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am web automater 2 point o Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns a string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Now Listening")
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en")
        print(f"You said: {query}")

    except Exception:
        speak("Say that again please...")
        print("Say that again please...")
        return 'None'

    return query


if __name__ == '__main__':
    #speakStartUp()
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "url" in query:
            speak("Sir, can I please get the URL")
            Query = takeCommand().lower()
            usefulQuery = Query.replace(" ", "")
            if ".com" in usefulQuery:
                webbrowser.open(usefulQuery)

            else:
                superUsefulQuery = usefulQuery + ".com"
                webbrowser.open(superUsefulQuery)

        elif "stop" in query:
            print("Thank you for using me Sir, and if you ever need me again, you know where to go!")
            speak("Thank you for using me Sir, and if you ever need me again, you know where to go!")
            exit()

        elif query != "none":
            '''
            1. Access the query.
            2. Tell the redirection.
            3. Replace the " " with "+"'s
            4. webbrowser.open()
            '''
            speak("Sir, as you have not programmed me to do any thing with what you said, I am redirecting you to "
                  "Google")
            usefulQuery = query.replace(" ", "+")
            webbrowser.open("www.google.com/search?q=" + usefulQuery)

