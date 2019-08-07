import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice ', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network Problem. Check your connection')
    return voice_text


if __name__ == '__main__':

    speak_text_cmd(
        'Hello Sir this is JARVIS. I was created by Pratit as a project for his Science exhibition. My name is short for Just A Rather Very Intelligent System. My programme is coded in python language')

    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('Hello Sir. How can I help you?')
            continue
        elif 'open' in voice_note:
            speak_text_cmd('Ok Sir. Opening please wait')
            os.system('explorer C:\\ "{}"'.format(voice_note.replace('open ', '')))
            continue
        elif 'bye' in voice_note:
            speak_text_cmd('Bye Sir. Happy to help you. Have a good day.')
            exit()
exit()