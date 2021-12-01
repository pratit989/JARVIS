import pyttsx3  # Python Text-to-Speech Module
from Settings import Configuration  # Configuration for ADA

config = Configuration()  # Reading Configuration from config.ini

# Initialising Text to Speech engine with try-except
try:
    # Initialise Engine with Driver Name SAPI 5 from Config File
    engine = pyttsx3.init(driverName=config.get_setting('Text to Speech', 'driver'))
    # Setting Voice ID from Registry of windows
    engine.setProperty('voice', config.get_setting('Text to Speech', 'voice_id'))
    # Setting rate of speech by the AI
    engine.setProperty('rate', config.get_setting('Text to Speech', 'rate'))
except ImportError:
    # Triggers import error when driver is not installed
    print('\nThe requested driver is not found.')
except RuntimeError:
    # Runtime Error if Numpy is not installed
    print('\nCheck if numpy is giving this error.\nThe driver failed to initialise')


# Speech function to turn text input to speech
def speak(text):
    try:
        engine.endLoop()  # End any existing speech output
    except RuntimeError:
        pass
    engine.say(text)  # Trigger say function to speak input text
    try:
        engine.runAndWait()  # Run and wait until speech is complete
    except RuntimeError:
        pass


# Print & Speech function to turn text input to speech and print it
def print_and_speak(text):
    try:
        engine.endLoop()  # End any existing speech output
    except RuntimeError:
        pass
    print(text)  # Print text
    engine.say(text)  # Trigger say function to speak input text
    engine.runAndWait()  # Run and wait until speech is complete
