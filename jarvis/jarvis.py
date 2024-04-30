import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3


# def speak(audio):
#     engine.speak(audio)
#
#
# def time():
#     Time = datetime.datetime.now().strftime("%I:%M:%S")
#     speak(f"current time is{Time}")
#
#
# def date():
#     year = int(datetime.datetime.now().year)
#     months = int(datetime.datetime.now().month)
#     day = int(datetime.datetime.now().day)
#     speak(f"Current date is{year} {months} {day}")
#
#
# def wishme():
#     speak("Welcome back sir")
#     time()
#     date()
#     hour = datetime.datetime.now().hour
#     if hour >= 6 and hour < 12:
#         speak("Good morning sir")
#     elif hour >= 12 and hour < 18:
#         speak("Good afternoon sir")
#     else:
#         speak("Good evening sir")
#     speak("Jarvis at your servis please tell me how can i help you?")
#

# wishme()

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something...!')
        audio = r.listen(source)
        print('done!')

    try:
        text = r.recognize_google_cloud(audio)
        print('you said '+ text)

    except Exception as e:
        print(e)

get()

