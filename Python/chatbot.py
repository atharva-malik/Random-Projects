"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

genai.configure(api_key="ENTER_API_KEY")

r = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty('rate', 175)


def aOutput(output):
    print("Astra: " + output)
    engine.say(output)
    engine.runAndWait()

def aInput():
    with sr.Microphone() as source:
        print("Now listening...")
        audio = r.listen(source)
        print("Now processing...")
    try:
        output = r.recognize_google(audio)
        if "hey astra" in output.lower():
            output = output.lower()
            output = output[output.find("hey astra"):]
            output = output.replace("hey astra ", "")
        else:
            output = "_e " + output
    except sr.UnknownValueError:
        output = "_e Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        output = "_e Could not request results from Google Speech Recognition service; {0}".format(e)
    return output

# Set up the model
generation_config = {
    "temperature": 0.9, #* How random the bot can be (0-0.9)
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE" #! Change this is you don't have a sense of humour.
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE" #! Change this is you don't have a sense of humour.
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE" #! Change this is you don't have a sense of humour.
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE" #! Change this is you don't have a sense of humour.
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])
convo.send_message("For all intents and purposes your name is now Astra. This is what you will call yourself, and this is what I will call you!")
convo.send_message("Who r u?") # This is to let the name settle in.

while True:
    try:
        inp = aInput()
        if "stop" in inp.lower():
            break
        if inp[0] == "_" and inp[1] == "e":
            raise Exception("Nothing Detected!")
        print("You: " + inp)
        convo.send_message(inp)
        aOutput((convo.last.text).replace("**", "").replace("* ", ""))
    except Exception as e:
        print(e)
        print("Could not send message, restarting conversation...")
