# Necessary Modules
from importlib import import_module
import sys
import threading
import time
from random import choice
import MongoDB
import Search
import TTS
from TTS import print_and_speak  # Import TTS always before Settings
import Settings
from Input_system import define_input
import vocabulary

# Optional modules
modules = {}
for module in vocabulary.optional_modules:
    try:
        modules[module] = import_module(module)
    except ImportError:
        pass

config = Settings.Configuration()

if __name__ == '__main__':
    import face_recognition

    face_thread = threading.Thread(target=face_recognition.start_face_recog)
    face_thread.start()
    while not Settings.video_status:
        time.sleep(1)
        pass  # Exit loop after starting webcam & detecting someone
    name_thread = threading.Thread(target=Settings.name_change_detector)
    name_thread.start()
    print_and_speak(f"\nHi {Settings.user_name} I am JARVIS voice by {config.get_setting('Text to Speech', 'name')}")
    Settings.kill_thread = True
    input_function = define_input()
    PAUSE_PROGRAM = False

    while True:

        try:
            cmd = input_function().lower()
        except AttributeError:
            print_and_speak("Failed to get Input")

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
            if not Settings.logged_in:
                print_and_speak("Enter the following credentials to access student database:")
                TTS.speak("Username")
                username = input("Username: ")
                TTS.speak("Password")
                password = input("Password: ")
                Settings.logged_in = True
            else:
                pass
            # username = ""
            # password = ''
            if Settings.logged_in:
                MongoDB.initialise_database(username, password)
                TTS.speak("Enter the enrollment number for which to fetch data")
                enroll_no = int(input("Enrollment Number: "))
                data = MongoDB.get_data(enroll_no)
                # data = MongoDB.get_data(1805680240)
                if data is not None:
                    for n in data:
                        print(f"{str(n).capitalize()}: {data[n]}")
                    # print(json.dumps(data, indent=4, sort_keys=True))
        elif any(element in cmd for element in vocabulary.download):
            stream: modules["youtube_player"].YoutubePlayer = \
                modules['youtube_player'].YoutubePlayer(str(cmd.split()[1:]), True)
        elif any(element in cmd for element in vocabulary.voice_to_chat):
            from Input_system import read_chat_cmd
            input_function = read_chat_cmd
        elif any(element in cmd for element in vocabulary.chat_to_voice):
            from Input_system import listen_voice_cmd
            input_function = listen_voice_cmd
        elif any(element in cmd for element in vocabulary.covid_tracker):
            Search.open_page('https://dkcovid19-tracker.herokuapp.com/')
        elif any(element in cmd for element in vocabulary.exit_words):
            sys.exit(0)
