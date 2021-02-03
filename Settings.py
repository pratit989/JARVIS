import TTS
from configparser import ConfigParser
from configparser import NoSectionError
from configparser import NoOptionError


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
            print(str(index) + '. ' + voice.name)
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
            print(str(index) + ') ' + section)
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
        TTS.speak("The following are all the options in" + section + "Select the option you want to change the value "
                                                                     "for.")
        selected = int(input('Type:'))
        self.set_value(section, option=options[selected])

    def set_value(self, section: str, option: str):
        print('\n')
        TTS.speak('The current value for ' + option + ' is:')
        print(option + ' = ' + self.parser.get(section, option))
        TTS.speak("Enter the new value")
        value = input("Enter the new value:")
        self.parser.set(section, option, value)
        with open('config.ini', 'w') as file:
            self.parser.write(file)
