import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

r = sr.Recognizer()

for k,v in enumerate(sr.Microphone().list_microphone_names):
    print(k,v)


def intro():
    data = ''' Hi i am proto welcome to the lecture
    '''
    engine.say(data)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('say something....')
    audio = r.listen(source)

try:
    data = 'google thinks you said '+ r.recognize_google(audio)
    engine.say(data)
    engine.runAndWait()
except:
    pass


# def myfunc():
#     pass


# myfunc()