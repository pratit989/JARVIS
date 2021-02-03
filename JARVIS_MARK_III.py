# Necessary Modules
from random import choice

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
    print_and_speak("\nHello I am JARVIS voice by " + config.get_setting('Text to Speech', 'name'))
    input_function = define_input()

    while True:
        cmd = input_function().lower()
        if 'jarvis' in cmd.split()[0]:
            cmd = cmd.replace('jarvis ', '', 1)
            pass
        if any(element in cmd.split() for element in vocabulary.greeting):
            from vocabulary import response_greeting

            print_and_speak(choice(response_greeting))
        elif 'play' in cmd.split()[0]:
            try:
                stream: modules["Youtube_player"].YoutubePlayer = \
                    modules['Youtube_player'].YoutubePlayer(str(cmd.split()[1:]))
            except ModuleNotFoundError:
                print_and_speak('The youtube player module is not installed')
                continue
            except Exception:
                continue
        elif any(element in cmd for element in vocabulary.close_player):
            try:
                # noinspection PyUnboundLocalVariable
                stream.stop()
            except Exception:
                continue
        elif any(element in cmd for element in vocabulary.pause_player) or\
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
        elif any(element in cmd for element in vocabulary.exit_words):
            exit(0)
