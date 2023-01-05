import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(txt):
    engine.say(txt)
    engine.runAndWait()

talk("Hello, Bro,fessor")
talk("Hello, Everyone. vola!")
talk("I am Genie, Prathmesh's Personal Assistant")
talk("Today we are giving presentation on Prathmesh's final project. Smart P. A.  that is me")
talk("Now prathmesh will brief you further")
talk("Thanks")


