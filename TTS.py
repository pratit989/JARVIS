import pyttsx3
from Settings import Configuration

config = Configuration()

# Text to Speech
try:
    engine = pyttsx3.init(driverName=config.get_setting('Text to Speech', 'driver'))
    engine.setProperty('voice', config.get_setting('Text to Speech', 'voice_id'))
    engine.setProperty('rate', config.get_setting('Text to Speech', 'rate'))
except ImportError:
    print('\nThe requested driver is not found.')
except RuntimeError:
    print('\nCheck if numpy is giving this error.\nThe driver failed to initialise')


def speak(text):
    try:
        engine.endLoop()
    except RuntimeError:
        pass
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass


def print_and_speak(text):
    try:
        engine.endLoop()
    except RuntimeError:
        pass
    print(text)
    engine.say(text)
    engine.runAndWait()
