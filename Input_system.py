import Settings
from TTS import print_and_speak
import speech_recognition
from playsound import playsound

speech = speech_recognition.Recognizer()


# Speech to Text
def listen_voice_cmd():
    try:
        with speech_recognition.Microphone() as source:
            print('\nListening...')
            if Settings.program_sound:
                playsound(r'mp3/listening_robot_blip.mp3')
            audio = speech.listen(source=source, timeout=4, phrase_time_limit=5)
            voice_text = speech.recognize_google(audio, language="en-IN")
            return voice_text
    except OSError:
        print_and_speak('Microphone is not connected')
    except speech_recognition.UnknownValueError:
        if Settings.program_sound:
            playsound(r'mp3/struggling_1.mp3')
    except speech_recognition.RequestError:
        print_and_speak('I am currently facing a network issue. Please try again later')
    except speech_recognition.WaitTimeoutError:
        pass


# Text input
def read_chat_cmd():
    if Settings.program_sound:
        playsound(r'mp3/listening_robot_blip.mp3')
    text = input("\nType here:")
    return text


# Defines what kind of input function to be called, Chat or Talk.
def define_input():
    print_and_speak("Would you like to talk or chat with me?")
    input_selected = str(input(":").lower())
    while input_selected != 'chat' and input_selected != 'talk':
        print_and_speak('Please choose a proper input type.\nChat or Talk?')
        input_selected = input(':')
    if input_selected == 'chat':
        return read_chat_cmd
    else:
        return listen_voice_cmd
