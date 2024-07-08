"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="ENTER_API_KEY")

def aOutput(output): # Plans for future audio input
    print("Gemini: " + output)

def aInput(): # Plans for future audio input
    output = input("Enter Text: ")
    return output

# Set up the model
generation_config = {
    "temperature": 0.9, #* How random the bot can be
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

while True:
    try:
        inp = aInput()
        if inp[0] == "_" and inp[1] == "e":
            raise Exception("Nothing Detected!")
        if "stop" in inp.lower():
            break
        print("You: " + inp)
        convo.send_message(inp)
        aOutput((convo.last.text).replace("**", "").replace("* ", ""))
    except Exception as e:
        print(e)
        print("Could not send message, restarting conversation...")
