import time
import datetime
from Final_proj.main_bot import talk
import pywhatkit
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
rec_name = {
    'professor': '+17203978057',
    'black': '+919819261263'
}


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_msg(name, message, hour, minute):
    # pywhatkit.sendwhatmsg('+15107389141', 'happy birthday', time_hour=17, time_min=29)
    pywhatkit.sendwhatmsg(name, message, hour, minute)


def get_msg_info():
    talk('To Whom you want to send message')
    name_chk=get_info()
    name=rec_name[name_chk]
    print(name)
    talk('what message would you like to send')
    message = get_info()
    now = datetime.datetime.now()
    hour=now.hour
    minute=now.minute+2
    time.sleep(1)
    send_msg(name, message, hour, minute)

get_msg_info()


