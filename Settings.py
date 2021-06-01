import time

import TTS
from configparser import ConfigParser
from configparser import NoSectionError
from configparser import NoOptionError
from datetime import datetime

program_sound = True
user_name = 'Stranger'
video_status = False
kill_thread = False


def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )


def name_change_detector():
    global user_name
    past_user: str
    past_user = user_name
    while True:
        if past_user != user_name:
            TTS.print_and_speak(f"Hi {user_name} good {get_part_of_day(datetime.now().hour)}")
            past_user = user_name
            time.sleep(0.5)


def setting_mode():
    TTS.speak("Welcome to Settings Mode.")
    print('SETTINGS MODE')
    Configuration().section_selection()


class Configuration:
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('config.ini')

    def get_setting(self, section: str, option: str):
        try:
            information = str(self.parser.get(section, option))
            return information
        except NoSectionError:
            self.parser.add_section(section)
            with open('config.ini', 'w+') as file:
                self.parser.write(file)
        except NoOptionError:
            self.parser.set(section, option, '')
            return self.default_set(section=section, option=option)

    def default_set(self, section: str, option: str):
        print('GETTING STARTED\n')
        index = 0
        print('Voices:')
        voices = TTS.engine.getProperty('voices')
        # noinspection PyTypeChecker
        for voice in voices:
            print(f'{str(index)}. {voice.name}')
            index += 1
        try:
            TTS.print_and_speak('Select a voice for me.')
        except Exception:
            pass
        user_choice = int(input(':'))
        self.parser.set(section, 'voice_id', voices[user_choice].id)
        self.parser.set(section, 'name', str(voices[user_choice].name).split('Desktop')[0])
        self.parser.set(section, 'age', str(voices[user_choice].age))
        self.parser.set(section, 'gender', str(voices[user_choice].gender))
        self.parser.set(section, 'driver', 'sapi5')
        self.parser.set(section, 'rate', '170')
        with open('config.ini', 'w+') as file:
            self.parser.write(file)
        return self.get_setting(section=section, option=option)

    def section_selection(self):
        print("\nSECTION SELECTION")
        index = 0
        sections = self.parser.sections()
        for section in sections:
            print(f'{str(index)}) {section}')
            index += 1
        TTS.speak("Select the category of setting that you would like to change? Enter it's index number")
        selected = int(input('Type:'))
        self.option_selection(section=sections[selected])

    def option_selection(self, section):
        print("\nOPTION SELECTION")
        index = 0
        options = self.parser.options(section)
        for option in options:
            print(str(index) + ') ' + option)
            index += 1
        TTS.speak(f"The following are all the options in{section}Select the option you want to change the value "
                  "for.")
        selected = int(input('Type:'))
        self.set_value(section, option=options[selected])

    def set_value(self, section: str, option: str):
        print('\n')
        TTS.speak(f'The current value for {option} is:')
        print(f'{option} = {self.parser.get(section, option)}')
        TTS.speak("Enter the new value")
        value = input("Enter the new value:")
        self.parser.set(section, option, value)
        with open('config.ini', 'w') as file:
            self.parser.write(file)
