# Necessary Modules
import json
import sys
import threading
from random import choice

import MongoDB
import TTS
from TTS import print_and_speak  # Import TTS always before Settings
import Settings
from Input_system import define_input
import vocabulary

# Optional modules
modules = {}
for module in vocabulary.optional_modules:
    try:
        modules[module] = __import__(module)
    except ImportError:
        pass

config = Settings.Configuration()

if __name__ == '__main__':
    # import face_recognition

    # face_thread = threading.Thread(target=face_recognition.start_face_recog)
    # face_thread.start()
    # time.sleep(10)
    name_thread = threading.Thread(target=Settings.name_change_detector)
    name_thread.start()
    print_and_speak(f"\n"
                    f"Hi {Settings.user_name} I am JARVIS "
                    f"voice by {config.get_setting('Text to Speech', 'name')}")
    input_function = define_input()
    PAUSE_PROGRAM = False

    while True:

        cmd = input_function().lower()

        if 'jarvis' in cmd.split()[0]:
            cmd = cmd.replace('jarvis ', '', 1)
        if any(element in cmd.split() for element in vocabulary.greeting):
            from vocabulary import response_greeting

            print_and_speak(choice(response_greeting))
        elif 'play' in cmd.split()[0]:
            try:
                stream: modules["youtube_player"].YoutubePlayer = \
                    modules['youtube_player'].YoutubePlayer(str(cmd.split()[1:]))
            except ModuleNotFoundError:
                print_and_speak('The youtube player module is not installed')
                continue
            except Exception:
                continue
            Settings.program_sound = False
        elif any(element in cmd for element in vocabulary.close_player):
            try:
                # noinspection PyUnboundLocalVariable
                stream.stop()
            except Exception:
                continue
        elif any(element in cmd for element in vocabulary.pause_player) or \
                any(element in cmd for element in vocabulary.resume_player):
            try:
                stream.pause_or_resume()
            except Exception:
                continue
        elif any(element in cmd.split() for element in vocabulary.personal):
            try:
                modules['chitchat'].processing_chitchat(cmd)
            except ModuleNotFoundError:
                print_and_speak('The chitchat module is not installed')
                continue
            except Exception:
                pass
        elif any(element in cmd.split() for element in vocabulary.search_query):
            try:
                search = modules['Search'].query(cmd)
            except ModuleNotFoundError:
                print_and_speak('The search module is not installed')
                continue
            except Exception:
                continue
        elif any(element in cmd for element in vocabulary.settings_vocab):
            Settings.setting_mode()
        elif any(element in cmd for element in vocabulary.database):
            print_and_speak("Enter the following credentials to access student database:")
            TTS.speak("Username")
            username = input("Username: ")
            # username = ""
            TTS.speak("Password")
            password = input("Password: ")
            # password = ''
            MongoDB.initialise_database(username, password)
            TTS.speak("Enter the enrollment number for which to fetch data")
            enroll_no = int(input("Enrollment Number: "))
            data = MongoDB.get_data(enroll_no)
            # data = MongoDB.get_data(1805680240)
            if data is not None:
                print(json.dumps(data, indent=4, sort_keys=True))
        elif any(element in cmd for element in vocabulary.download):
            stream: modules["youtube_player"].YoutubePlayer = \
                modules['youtube_player'].YoutubePlayer(str(cmd.split()[1:]), True)
        elif any(element in cmd for element in vocabulary.exit_words):
            sys.exit(0)
