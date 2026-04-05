import speech_recognition as sr
from gtts import gTTS
import os


def get_voice_input():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text

    except:
        return ""


def speak(text):

    tts = gTTS(text)

    tts.save("response.mp3")

    return "response.mp3"