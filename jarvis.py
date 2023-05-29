import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hello, sir good Evening, I am Jarvis..your personal Assistant, Memory 1 Terabyte, cpu intelcore i3 5th generation, clock speed 2.7 gigahertz      How can i help you sir ')
engine.say('Current time is'+datetime.datetime.now().strftime('%I:%M %p'))

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'raju sharma' in command:
        talk('Raju sharma is an young energetic boy who is currently studying in Ace institute of management. ')
    elif 'marry' in command:
        talk('No, raju you already have a girlfriend')
    elif 'what is your name' in command:
        talk('My name is jarvis')
    elif 'what is my name' in command:
        talk('Your name is Mohan Sharma.')
    elif 'thank' in command:
        talk('Thanks for using me sir, Have a good day sir')
    elif 'virgin' in command:
        talk('No, government and life f*ks me daily.')
    elif 'temperature' in command:
        search="temperature in Kathmamdu"
        url=f"https://www.google.com/search?q={search}"
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        talk(f"current{search} is {temp}")
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
