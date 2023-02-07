# This will create an mp3 file based on your input.
# You must choose which program will open this file
# After you close the program, the mp3 file will be deleted.

from gtts import gTTS
import os


def text_to_speech(speak, language='en'):
    tts = gTTS(text=speak, lang=language)
    tts.save("Test.mp3")
    os.system("Test.mp3")
    os.remove("Test.mp3")


speak = input("Entre text to speech: ")
text_to_speech(speak)
