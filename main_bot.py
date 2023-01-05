import speech_recognition as sr
import pyttsx3
import subprocess
import pywhatkit
import os
from motivation import *
from loguru import logger as log

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(txt):
    engine.say(txt)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            log.info('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'genie' in command:
                # subprocess.call("a.py", shell=True)
                # talk(command)
                command=command.replace('genie', '')
                log.info(command)
    except:
        pass
    return command

def run_alexa():
    talk("Hi Prathmesh. what's up!")
    talk("How can I help you today?")
    command=take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk("playing the song" + song)
        pywhatkit.playonyt(song)

    if 'hi' in command:
        log.info("hii")
        quote=scrape_website()
        talk('dear. you sounds low today')
        talk("todays motivational quote just for you")
        talk(quote)
        # subprocess.call("motivation.py", shell=True)
        # talk(command)

    if 'list' in command:
        os.system('flask run')
        # subprocess.call('app.py', shell=True)
        talk(command)

    if "mail" in command:
        subprocess.call('mailbot.py', shell=True)
        talk(command)

    if "send" in  command:
        subprocess.call('whatsapp.py', shell=True)
        talk(command)

    if "start" in  command:
        subprocess.call('Bot_Intro.py', shell=True)
        # talk(command)

    if "search" in command:
        log.info("search")
        search = command.replace('search', '')
        talk("searching for" + search)
        pywhatkit.search(search)


run_alexa()