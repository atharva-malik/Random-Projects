# gTTS is not on computer

# Import the gTTS module for text
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os

# #mytext = 'Convert this Text to Speech in Python'
  
# Language we want to use 
language = 'en'
  

# #myobj = gTTS(text=mytext, lang=language, slow=False)
  

# #myobj.save("output.mp3")
  
# Play the converted file 
# #os.system("start output.mp3")

# let's do it
import time

# import winsound for paying beep sounds.
import winsound as sound

while True:
    score = 0
    roundNum = str(score)
    my_time = 30
    numOfRounds = eval(input("How many rounds do you want(should be at least 1)?\n"))
    numOfMiniRounds = eval(input("How many sub rounds do you want?(should be at least 1)\n"))
    for i in range(numOfRounds):
        score += 1/numOfMiniRounds  # Making a score
        roundNum = str(score)  # Converting score to string
        roundCalc = gTTS(text=roundNum, lang=language, slow=False)  # Converting text to speech
        roundCalc.save("output.mp3")  # Saving the conversion
        sound.Beep(400, 5000)  # Playing beep sound
        os.system("start output.mp3")  # Starting the file
        time.sleep(my_time) # Waiting for a certain Time
        my_time -= 30/(numOfMiniRounds*numOfRounds)  # Subtracting the certain Time
        break