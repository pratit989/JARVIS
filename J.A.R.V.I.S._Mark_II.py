import os
import random
import time
import webbrowser
from sys import exit as terminate

import pafy
import pyttsx3
import requests
import speech_recognition as sr
from playsound import playsound
from selenium.common.exceptions import NoSuchElementException

# import lookup_exe
import lookup_drive_change
from run_lookup import RunLookup

os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')

# Use cmd to install modules if the pycharm pip doesn't works
RunLookup()

speech = sr.Recognizer()
engine = 0

try:
    engine = pyttsx3.init()
except ImportError:
    terminate('Requested driver is not found')
except RuntimeError:
    terminate('Driver fails to initialize')

if engine == 0:
    terminate("Please install pywin32")
else:
    voices = engine.getProperty('voices')
    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_enUS_ZiraM')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


speak_text_cmd('Please wait, booting up all systems, loading the required Modules.')

greeting_dict = {'hello': 'hello', 'hi': 'hi', 'Hello': 'Hello', 'Hi': 'Hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch', 'Open': 'Open', 'Launch': 'Launch'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'when': 'when', 'how': 'how',
                        'where': 'where', "how's": "how's", "How's": "How's", "who's": "who's",
                        "Who's": "Who's", "what's": "what's", "What's": "What's", "Where's ": "Where's ",
                        "where's": "where's", "When's": "When's", "when's": "when's", 'explain': 'explain'}
websites_dict = {'facebook': 'https://www.facebook.com', 'Facebook': 'https://www.facebook.com',
                 'Twitter': 'https://www.twitter.com', 'Quora': 'https://www.quora.com', 'YouTube': 'www.youtube.com'}
goodbye_dict = {'bye': 'bye', 'goodbye': 'goodbye', 'buy': 'buy', 'bike': 'bike', 'exit': 'exit'}
thank_you_dict = {'thanks': 'thanks', 'thank': 'thank', 'good': 'good'}
garbage_dict = {'...': '...', '-': '-'}
how_dict = {'how ': 'how ', 'jarvis how ': 'jarvis how ', "how's ": "how's ",
            "How's ": "How's "}
who_dict = {'who ': 'who ', "who's ": "who's ",
            "Who's ": "Who's "}
what_dict = {'what ': 'what ', 'jarvis what ': 'jarvis what ', "what's ": "what's ",
             "What's ": "What's "}
where_dict = {'where ': 'where ', "Where's ": "Where's ", "where's ": "where's "}
when_dict = {'when ': 'when ', "When's ": "When's ",
             "when's ": "when's ", "jarvis when's ": "jarvis when's "}
whom_dict = {'whom ': 'whom ', "Whom's ": "Whom's ",
             "whom's ": "whom's ", 'to whom ': 'to whom ', 'To whom ': 'To whom ', 'jarvis to whom ': 'jarvis to whom ',
             'whom': 'whom'}
which_dict = {'which ': 'which', 'Which ': 'Which ', 'Jarvis which ': 'Jarvis which ', 'jarvis which': 'jarvis which'}
listening_ability_question_dict = {'can ': 'can ', 'am ': 'am ', 'are you ': 'are you ', 'Are you ': 'Are you ',
                                   'Can ': 'Can ', 'Am ': 'Am '}
weather_dict = {'weather': 'weather', 'temperature': 'temperature'}
time_dict = {'what is the time': 'what is the time', "what's the time": "what's the time",
             'what is the current time': 'what is the current time', 'what time it is': 'what time it is',
             'what date it is': 'what date it is', "what's the date": "what's the date",
             'what is the current date': 'what is the current date', 'what is the date': 'what is the date',
             "what is today's date": "what is today's date", "what's today's date": "what's today's date",
             "what's the current time": "what's the current time", 'what is the date and time': 'what is the time',
             'what is the current season': 'what is the current season', 'what is the season': 'what is the season',
             "what's the season": "what's the season", "what's the ongoing season": "what's the ongoing season",
             'what is the ongoing season': 'what is the ongoing season', 'what season is this': 'what season is this',
             'which is this season': 'which is this season', 'explain': 'explain'}
month_dict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
              '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December', 'Jan': 'Jan',
              'Feb': 'Feb', 'March': 'March', 'April': 'April', 'May': 'May', 'June': 'June', 'July': 'July',
              'Aug': 'Aug', 'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dec'}
youtube_valid_dict = {'play some ': 'play some ', 'play the ': 'play the ', 'play ': 'play '}
player_shutdown = {'close the player': 'close the player', 'turn the music of': 'turn the music of',
                   'turn it of': 'turn it of', 'turn of the player': 'turn of the player',
                   'Close the player': 'Close the player', 'Turn the music of': 'Turn the music of',
                   'Turn it of': 'Turn it of', 'Turn of the player': 'Turn of the player',
                   'close the plane': 'close the plane'}
player_pause = {'pause the player': 'pause the player', 'pause the music': 'pause the music',
                'pause song': 'pause song', 'Pause the player': 'Pause the player',
                'Pause the music': 'Pause the music',
                'Pause song': 'Pause song'}
player_resume = {'resume the player': 'resume the player', 'resume the music': 'resume the music',
                 'resume music': 'resume music', 'Resume the player': 'Resume the player',
                 'Resume the music': 'Resume the music',
                 'Resume music': 'Resume music'}
from_youtube = {'from YouTube': 'from Youtube', 'from youtube': 'from youtube'}
img_dict = {'do image search for': 'do image search for', 'do image search of': ' do image search of',
            'search for images of': 'search for images of', 'search images for': 'search images for',
            'get images of': 'get images of', 'search images of': 'search images of',
            'get images for': 'get images for',
            'give me some images of': 'give me some images of', 'give me images of': 'give me images of',
            'show me some images of': 'show me some images of', 'show me some images for': 'show me some images for'}

mp3_listening_problem_list = ['mp3/listening_problem_1.mp3',
                              'mp3/listening_problem_2.mp3']
mp3_struggling_list = ['mp3/struggling_1.mp3']
mp3_google_search = ['mp3/google_search_1.mp3', 'mp3/google_search_2.mp3']
mp3_greeting_list = ['mp3/greeting_accept_1.mp3', 'mp3/greeting_accept.mp3']
mp3_open_launch_list = ['mp3/open_1.mp3', 'mp3/open_2.mp3', 'mp3/open_3.mp3']
mp3_goodbye_list = ['mp3/bye.mp3']
mp3_thank_you_list = ['mp3/thank_you_1.mp3', 'mp3/thank_you_2.mp3']
mp3_listening_list = ['mp3/listening_robot_blip.mp3']

error_occurrence = 0
counter = 0


# To specify the file wanted when multiple instances are found.
def get_index(text_para):
    if 'first' in text_para:
        return 0
    elif 'second' in text_para:
        return 1
    elif 'third' in text_para:
        return 2
    elif 'fourth' in text_para:
        return 3
    elif 'fifth' in text_para:
        return 4
    elif '6' in text_para:
        return 5
    else:
        return None


# For browsing using the assistant
class Browser:

    def __init__(self, path_init, initiate=True, implicit_wait_time=10, explicit_wait_time=2):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        # chrome browser is used for scraping
        self.path = path_init
        self.implicit_wait_time = implicit_wait_time  # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        self.explicit_wait_time = explicit_wait_time  # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        if initiate:
            self.start()
        return

    def start(self):
        self.driver.implicitly_wait(self.implicit_wait_time)
        return

    def end(self):
        self.driver.quit()
        return

    def go_to_url(self, url_browser, wait_time=None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        self.driver.get(url_browser)
        print('Fetching results from: {}'.format(url_browser))
        speak_text_cmd("It's taking a lot more time than I thought. You may be having slow internet connection")
        time.sleep(wait_time)
        return

    @staticmethod
    def get_search_url(query, search_check):
        from urllib.parse import quote_plus
        query = quote_plus(query)
        if 'definition' in search_check:  # For searching querys which include 'definition'
            url_get_search = 'https://duckduckgo.com/?q={}&ia=definition'.format(query)
            return url_get_search
        elif 'defination' in search_check:  # For searching querys which include 'defination'
            url_get_search = 'https://duckduckgo.com/?q={}&ia=definition'.format(query)
            return url_get_search
        elif 'meaning' in query:  # For searching querys which include 'meaning'
            url_get_search = 'https://duckduckgo.com/?q={}&ia=definition'.format(query)
            return url_get_search
        elif 'who+is+the' in query:  # For searching querys which include 'who is the'
            if 'of' in search_check:  # For searching querys of the type 'who is the _____ of ______'
                url_get_search = 'https://www.bing.com/search?q={}'.format(query)
                return url_get_search
        else:
            url_get_search = 'https://duckduckgo.com/?q={}&ia=about'.format(query)
            return url_get_search

    def scrape(self, url_check, query):
        global counter
        output = ''
        if 'ia=definition' in url_check:
            try:
                definition_result = self.driver.find_element_by_class_name("zci__def__definition")
                if definition_result.text != "":
                    play_sound(mp3_google_search)
                    knowledge_temp = definition_result.text
                    if counter == -1:
                        for key_var, value_var in month_dict.items():
                            if value_var in definition_result.text:
                                if ' - ' in definition_result.text:
                                    definition_result.text = knowledge_temp.split(' - ')[1]
                        for key_var, value_var in garbage_dict.items():
                            if key_var in definition_result.text:
                                output = definition_result.text.replace(key_var, '')
                        if output == '':
                            output = definition_result.text
                        split_output = list(output)

                        list_words = []
                        for word in split_output:
                            if word == '.':
                                list_words.append(word)

                        number_of_splits = len(list_words)
                        output_final = ''
                        for split_num in range(0, number_of_splits):
                            if split_num == 0:
                                output_final = output_final + output.split('.')[split_num]
                            elif split_num > 0:
                                output_final = output_final + '.' + output.split('.')[split_num]
                        output_final = query, 'is', output_final
                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                        return True
                    else:
                        output = definition_result.text
                        split_output = list(output)

                        list_words = []
                        for word in split_output:
                            if word == '.':
                                list_words.append(word)

                        number_of_splits = len(list_words)
                        output_final = ''
                        for split_num in range(0, number_of_splits):
                            if split_num == 0:
                                output_final = output_final + output.split('.')[split_num]
                            elif split_num > 0:
                                output_final = output_final + '.' + output.split('.')[split_num]

                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                        return True
            except NoSuchElementException:
                pass
        try:
            answer = self.driver.find_element_by_class_name("b_focusTextLarge")
            output_final = answer.text
            print(output_final)
            speak_text_cmd(output_final)
            counter += 1
            return True
        except NoSuchElementException:
            try:
                answer = self.driver.find_element_by_class_name("b_focusTextMedium")
                print(answer.text)
                speak_text_cmd(answer.text)
                return True
            except NoSuchElementException:
                pass
        try:
            answer_1 = self.driver.find_element_by_class_name("b_vPanel")
            remover = self.driver.find_element_by_class_name("b_algo")
            remover = remover.text
            if answer_1.text != "":
                play_sound(mp3_google_search)
                knowledge_temp = answer_1.text
                knowledge_temp = knowledge_temp.replace(remover, '')
                if counter == -1:
                    for key_var, value_var in month_dict.items():
                        if value_var in answer_1.text:
                            if ' - ' in answer_1.text:
                                answer_1.text = knowledge_temp.split(' - ')[1]
                    for key_var, value_var in garbage_dict.items():
                        if key_var in answer_1.text:
                            output = answer_1.text.replace(key_var, '')
                    if output == '':
                        output = answer_1.text
                    split_output = list(output)

                    list_words = []
                    for word in split_output:
                        if word == '.':
                            list_words.append(word)

                    number_of_splits = len(list_words)
                    output_final = ''
                    for split_num in range(0, number_of_splits):
                        if split_num == 0:
                            output_final = output_final + output.split('.')[split_num]
                        elif split_num > 0:
                            output_final = output_final + '.' + output.split('.')[split_num]
                    output_final = output_final.replace(remover, '')
                    if 'reference' in output_final.lower():
                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                    else:
                        output_final = output_final.splitlines()[0]
                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                    return True
                else:
                    output = answer_1.text
                    split_output = list(output)

                    list_words = []
                    for word in split_output:
                        if word == '.':
                            list_words.append(word)

                    number_of_splits = len(list_words)
                    output_final = ''
                    for split_num in range(0, number_of_splits):
                        if split_num == 0:
                            output_final = output_final + output.split('.')[split_num]
                        elif split_num > 0:
                            output_final = output_final + '.' + output.split('.')[split_num]
                    output_final = output_final.replace(remover, '')
                    if 'reference' in output_final.lower():
                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                    else:
                        try:
                            output_final = output_final.splitlines()[0]
                        except IndexError:
                            pass
                        if output_final == '':
                            output_final = answer_1.text
                        print(output_final)
                        speak_text_cmd(output_final)
                        counter += 1
                    return True
        except NoSuchElementException:
            pass
        try:
            knowledge_panel_1 = self.driver.find_element_by_class_name("js-about-item-abstr")
            self.driver.find_element_by_css_selector("div.js-about-module-more").click()
            output = ''
            if knowledge_panel_1.text != "":
                play_sound(mp3_google_search)
                knowledge_temp = knowledge_panel_1.text
                if counter == -1:
                    for key_var, value_var in month_dict.items():
                        if value_var in knowledge_panel_1.text:
                            if ' - ' in knowledge_panel_1.text:
                                knowledge_panel_1.text = knowledge_temp.split(' - ')[1]
                    for key_var, value_var in garbage_dict.items():
                        if key_var in knowledge_panel_1.text:
                            output = knowledge_panel_1.text.replace(key_var, '')
                    if output == '':
                        output = knowledge_panel_1.text
                    split_output = list(output)

                    list_words = []
                    for word in split_output:
                        if word == '.':
                            list_words.append(word)

                    number_of_splits = len(list_words)
                    output_final = ''
                    for split_num in range(0, number_of_splits):
                        if split_num == 0:
                            output_final = output_final + output.split('.')[split_num]
                        elif split_num > 0:
                            output_final = output_final + '.' + output.split('.')[split_num]

                    print(output_final)
                    speak_text_cmd(output_final)
                    counter += 1
                    return True
                else:
                    output = knowledge_panel_1.text
                    split_output = list(output)

                    list_words = []
                    for word in split_output:
                        if word == '.':
                            list_words.append(word)

                    number_of_splits = len(list_words)
                    output_final = ''
                    for split_num in range(0, number_of_splits):
                        if split_num == 0:
                            output_final = output_final + output.split('.')[split_num]
                        elif split_num > 0:
                            output_final = output_final + '.' + output.split('.')[split_num]

                    print(output_final)
                    speak_text_cmd(output_final)
                    counter += 1
                    return True
        except NoSuchElementException:
            pass
        try:
            output = ''
            result = self.driver.find_element_by_class_name("result__snippet")
            play_sound(mp3_google_search)
            temp_result = str(result.text)
            if counter == -1:
                for key_var, value_var in month_dict.items():
                    if value_var in temp_result:
                        if ' - ' in temp_result:
                            temp_result = temp_result.split(' - ')[1]
                for key_var, value_var in garbage_dict.items():
                    if key_var in temp_result:
                        output = temp_result.replace(key_var, '')
                if output == '':
                    output = temp_result
                split_output = list(output)

                list_words = []
                for word in split_output:
                    if word == '.':
                        list_words.append(word)

                number_of_splits = len(list_words)
                output_final = ''
                for split_num in range(0, number_of_splits):
                    if split_num == 0:
                        output_final = output_final + output.split('.')[split_num]
                    elif split_num > 0:
                        output_final = output_final + '.' + output.split('.')[split_num]

                print(output_final)
                speak_text_cmd(output_final)
                counter += 1
                return True
            else:
                output = temp_result
                split_output = list(output)

                list_words = []
                for word in split_output:
                    if word == '.':
                        list_words.append(word)

                number_of_splits = len(list_words)
                output_final = ''
                for split_num in range(0, number_of_splits):
                    if split_num == 0:
                        output_final = output_final + output.split('.')[split_num]
                    elif split_num > 0:
                        output_final = output_final + '.' + output.split('.')[split_num]

                print(output_final)
                speak_text_cmd(output_final)
                counter += 1
                return True
        except NoSuchElementException:
            pass
        try:
            output = ''
            final_attempt = self.driver.find_element_by_css_selector("li.b_ans.b_top.b_topborder.b_tophb")
            final_attempt = final_attempt.text
            play_sound(mp3_google_search)
            temp_result = final_attempt
            if counter == -1:
                for key_var, value_var in month_dict.items():
                    if value_var in final_attempt:
                        if ' - ' in final_attempt:
                            temp_result = final_attempt.split(' - ')[1]
                for key_var, value_var in garbage_dict.items():
                    if key_var in temp_result:
                        output = temp_result.replace(key_var, '')
                if output == '':
                    output = temp_result
                split_output = list(output)

                list_words = []
                for word in split_output:
                    if word == '.':
                        list_words.append(word)

                number_of_splits = len(list_words)
                output_final = ''
                for split_num in range(0, number_of_splits):
                    if split_num == 0:
                        output_final = output_final + output.split('.')[split_num]
                    elif split_num > 0:
                        output_final = output_final + '.' + output.split('.')[split_num]

                print(output_final)
                speak_text_cmd(output_final)
                counter += 1
                return True
            else:
                output = temp_result
                split_output = list(output)

                list_words = []
                for word in split_output:
                    if word == '.':
                        list_words.append(word)

                number_of_splits = len(list_words)
                output_final = ''
                for split_num in range(0, number_of_splits):
                    if split_num == 0:
                        output_final = output_final + output.split('.')[split_num]
                    elif split_num > 0:
                        output_final = output_final + '.' + output.split('.')[split_num]
                if output_final == '':
                    output_final = temp_result
                print(output_final)
                output_final = output_final
                output_final = str(output_final)
                speak_text_cmd(output_final)
                counter += 1
                return True

        except NoSuchElementException:
            try:
                alt = self.driver.find_element_by_css_selector("#ent-car-exp> div> div")
                alt = alt.text
                print(alt)
                speak_text_cmd(alt)
                return True
            except NoSuchElementException:
                pass
            pass

    def search(self, query, search_note_para, wait_time=None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        url_search = self.get_search_url(query, search_note_para)
        self.go_to_url(url_search, wait_time)
        results = self.scrape(url_search, query)
        return results


path = "chromedriver.exe"  # SET YOU PATH TO phantomjs
br = Browser(path)


# To define the function to play the given mp3 list.
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


part = 0
mic_prob = 0


# To recognize the given voice command and convert it to text.
def read_voice_cmd():
    global error_occurrence, part, mic_prob
    voice_text = ''
    if part == 0:
        os.system('cls')
        part += 2
    part -= 1

    try:

        with sr.Microphone() as source:
            if error_occurrence < 5:
                play_sound(mp3_listening_list)
            if block == 0:
                print('Listening...')
                audio = speech.listen(source=source, timeout=4, phrase_time_limit=5)
            elif block == 1:
                return chat_command()
        voice_text = speech.recognize_google(audio)
    except OSError:
        if mic_prob == 0:
            mic_prob += 1
            print('Microphone is not connected')
            speak_text_cmd('Microphone is not connected')
        return chat_command()
    except sr.UnknownValueError:

        if error_occurrence == 0:

            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1
        pass
    except sr.RequestError:
        print('Network error, please try again later.')
        if error_occurrence == 0:
            play_sound(mp3_struggling_list)
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
        elif error_occurrence == 2:
            play_sound(mp3_struggling_list)
            error_occurrence -= 2
    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1
        pass
    return voice_text


def chat_command():
    if error_occurrence < 5:
        play_sound(mp3_listening_list)
    chat_text = input('Type here: ').lower()
    return chat_text


# To define the valid note from the voice command which will be trigger a particular operation.
def is_valid_note(greet_dict, voice_note_par):
    for key_var, value_var in greet_dict.items():
        # 'Hello Jarvis'
        try:
            if value_var == voice_note_par.split(' ')[0]:
                return True
            elif key_var == voice_note_par.split(' ')[1]:
                return True
            elif value_var == voice_note_par.split(' ')[2]:
                return True
            elif key_var == voice_note_par.split(' ')[3]:
                return True
            elif value_var == voice_note_par.split(' ')[4]:
                return True
            elif key_var == voice_note_par.split(' ')[5]:
                return True
        except IndexError:
            pass

    return False


# To reply to a small talk, in this case the question how are you jarvis?
def how_are_you_jarvis(how_are_you_dict, voice_note_para):
    for key_var, value_var in how_are_you_dict.items():
        try:
            if key_var == voice_note_para.split('are you')[0]:
                return True
            elif value_var == voice_note_para.split('are you')[0]:
                return True
            elif key_var == voice_note_para.split('you been')[0]:
                return True
            elif value_var == voice_note_para.split('you been')[0]:
                return True
            elif key_var == voice_note_para.split('have you been')[0]:
                return True
            elif value_var == voice_note_para.split('is you')[0]:
                return True
            elif value_var == voice_note_para.split('you')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question what are you doing jarvis?
def what_are_you_doing(what_are_you_doing_dict, voice_note_para):
    for key_var, value_var in what_are_you_doing_dict.items():
        try:
            if key_var == voice_note_para.split('are you doing')[0]:
                return True
            elif value_var == voice_note_para.split('were you doing')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question what am I doing?
def what_am_i_doing(what_am_i_doing_dict, voice_note_para):
    for key_var, value_var in what_am_i_doing_dict.items():
        try:
            if key_var == voice_note_para.split('am I doing')[0]:
                return True
            elif value_var == voice_note_para.split('am i doing')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question how is life jarvis?
def how_is_life_jarvis(how_is_life_dict, voice_note_para):
    for key_var, value_var in how_is_life_dict.items():
        # 'how is your life'
        try:
            if value_var == voice_note_para.split('is life')[0]:
                return True
            elif key_var == voice_note_para.split('life')[0]:
                return True
            elif value_var == voice_note_para.split('is your life')[0]:
                return True
            elif key_var == voice_note_para.split('your life')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question where do you live jarvis?
def where_do_you_live(where_do_you_live_dict, voice_note_para, what_is_your_address_dict):
    for key_var, value_var in where_do_you_live_dict.items():
        try:
            if key_var == voice_note_para.split('do you live')[0]:
                return True
            elif value_var == voice_note_para.split('do you live')[0]:
                return True
            elif key_var == voice_note_para.split('do you stay')[0]:
                return True
            elif value_var == voice_note_para.split('do you stay')[0]:
                return True
            if key_var == voice_note_para.split('is your house')[0]:
                return True
            elif value_var == voice_note_para.split('your house')[0]:
                return True
            if key_var == voice_note_para.split('is your home')[0]:
                return True
            elif value_var == voice_note_para.split('your home')[0]:
                return True
        except IndexError:
            pass
    for key_var, value_var in what_is_your_address_dict.items():
        try:
            if key_var == voice_note_para.split('is your address')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question whom am I talking to jarvis?
def whom_am_i_talking_to(whom_am_i_talking_to_dict, voice_note_para):
    for key_var, value_var in whom_am_i_talking_to_dict.items():
        if 'am I talking' in voice_note_para:
            if key_var == voice_note_para.split(' ')[0]:
                return True
        elif 'am i talking' in voice_note_para:
            if key_var == voice_note_para.split(' ')[0]:
                return True
    if 'who are you' == voice_note:
        return True

    return False


# To reply to a small talk, in this case the question who created you Jarvis?
def who_created_you(who_created_you_dict, voice_note_para):
    for key_var, value_var in who_created_you_dict.items():
        try:
            if key_var == voice_note_para.split('created you')[0]:
                return True
            elif value_var == voice_note_para.split('is your creator')[0]:
                return True
            elif key_var == voice_note_para.split('your creator')[0]:
                return True
            elif value_var == voice_note_para.split('has created you')[0]:
                return True
            elif key_var == voice_note_para.split('made you')[0]:
                return True
            elif value_var == voice_note_para.split('is your father')[0]:
                return True
            elif key_var == voice_note_para.split('your father')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question when were you created Jarvis?
def when_were_you_created(when_were_you_created_dict, voice_note_para, what_is_your_birth_date_dict):
    for key_var, value_var in when_were_you_created_dict.items():
        try:
            if key_var == voice_note_para.split('were you created')[0]:
                return True
            elif value_var == voice_note_para.split('were you born')[0]:
                return True
            elif key_var == voice_note_para.split('were you brought to life')[0]:
                return True
            elif value_var == voice_note_para.split('is your birthday')[0]:
                return True
            elif value_var == voice_note_para.split('your birthday')[0]:
                return True
        except IndexError:
            pass
    for key_var, value_var in what_is_your_birth_date_dict.items():
        try:
            if key_var == voice_note_para.split('is your birth date')[0]:
                return True
            elif value_var == voice_note_para.split('is your birthdate')[0]:
                return True
            elif value_var == voice_note_para.split('your birthdate')[0]:
                return True
            elif key_var == voice_note_para.split('your birth date')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question what is your name?
def what_is_your_name(what_is_your_name_dict, voice_note_para):
    for key_var, value_var in what_is_your_name_dict.items():
        try:
            if key_var == voice_note_para.split('is your name')[0]:
                return True
            elif value_var == voice_note_para.split('should I call you')[0]:
                return True
            elif key_var == voice_note_para.split('your name')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question to whom do you belong?
def to_whom_do_you_belong(whom_do_you_belong_dict, voice_note_para):
    for key_var, value_var in whom_do_you_belong_dict.items():
        try:
            if key_var == voice_note_para.split('do you belong to')[0]:
                return True
            elif key_var == voice_note_para.split('do you belong')[0]:
                return True
            elif value_var == voice_note_para.split("own's you")[0]:
                return True
            elif key_var == voice_note_para.split('own you')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question what is your nationality?
def what_is_your_nationality(what_is_your_nationality_dict, voice_note_para, which_is_your_country_dict):
    for key_var, value_var in what_is_your_nationality_dict.items():
        try:
            if key_var == voice_note_para.split('is your nationality')[0]:
                return True
            elif value_var == voice_note_para.split('your nationality')[0]:
                return True
            elif key_var == voice_note_para.split('is your country')[0]:
                return True
            elif value_var == voice_note_para.split('your country')[0]:
                return True
            elif key_var == voice_note_para.split('country do you belong to')[0]:
                return True
            elif value_var == voice_note_para.split('is your nation')[0]:
                return True
            elif key_var == voice_note_para.split('your nation')[0]:
                return True
        except IndexError:
            pass
    for key_var, value_var in which_is_your_country_dict.items():
        try:
            if key_var == voice_note_para.split('is your nationality')[0]:
                return True
            elif value_var == voice_note_para.split('your nationality')[0]:
                return True
            elif key_var == voice_note_para.split('is your country')[0]:
                return True
            elif value_var == voice_note_para.split('your country')[0]:
                return True
            elif key_var == voice_note_para.split('country do you belong to')[0]:
                return True
            elif value_var == voice_note_para.split('is your nation')[0]:
                return True
            elif key_var == voice_note_para.split('your nation')[0]:
                return True
        except IndexError:
            pass
    return False


# To reply to a small talk, in this case the question can you listen me?
def can_you_listen_me(listening_capacity_questioning_dict, voice_note_para):
    for key_var, value_var in listening_capacity_questioning_dict.items():
        try:
            if key_var == voice_note_para.split('you listen')[0]:
                return True
            elif value_var == voice_note_para.split('you hear')[0]:
                return True
            elif key_var == voice_note_para.split('I audible')[0]:
                return True
            elif value_var == voice_note_para.split('i audible')[0]:
                return True
            elif key_var == voice_note_para.split('I getting through')[0]:
                return True
            elif value_var == voice_note_para.split('I reaching through')[0]:
                return True
            elif key_var == voice_note_para.split('i getting through')[0]:
                return True
            elif value_var == voice_note_para.split('i getting through')[0]:
                return True
            elif key_var == voice_note_para.split('listening')[0]:
                return True
            elif value_var == voice_note_para.split('able to hear')[0]:
                return True
        except IndexError:
            pass
    return False


# The get weather function
def get_weather(weather_and_temperature_dict, voice_note_para):
    for key_var, value_var in weather_and_temperature_dict.items():
        try:
            if key_var == voice_note_para.split(' ')[0]:
                return True
            elif value_var == voice_note_para.split(' ')[1]:
                return True
            elif key_var == voice_note_para.split(' ')[2]:
                return True
            elif value_var == voice_note_para.split(' ')[3]:
                return True
            elif key_var == voice_note_para.split(' ')[4]:
                return True
            elif value_var == voice_note_para.split(' ')[5]:
                return True
            elif key_var == voice_note_para.split(' ')[6]:
                return True
            elif value_var == voice_note_para.split(' ')[7]:
                return True
            elif key_var == voice_note_para.split(' ')[8]:
                return True
        except IndexError:
            pass
    return False


# The procedure function to get weather
def weather_valid_note(voice_note_para, weather_and_temperature_dict):
    global city, url, unit
    url = ''
    if get_weather(weather_and_temperature_dict, voice_note_para):
        for key_var, value_var in weather_dict.items():
            try:
                if value_var != voice_note_para.split('weather')[0]:
                    if 'how is the weather' or 'how is weather' == voice_note_para:
                        if ' jarvis' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' jarvis', '')
                        elif ' jarvis' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' Jarvis', '')
                        elif 'jarvis ' in voice_note_para:
                            voice_note_para = voice_note_para.replace('jarvis ', '')
                        elif 'jarvis ' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' Jarvis ', '')
                        if 'of' in voice_note_para:
                            city = voice_note_para.split('in ')[1]
                        elif 'in' in voice_note_para:
                            city = voice_note_para.split('of ')[1]
                            if 'at' in city:
                                city = city.split('at ')[1]
                        elif 'at' in voice_note_para:
                            city = voice_note_para.split('at ')[1]
                            if 'in' in city:
                                city = city.split('at ')[1]
                        unit = '&units=metric'
                        api_address_0 = 'http://api.openweathermap.org/data/2.5/weather?appid' \
                                        '=c907c9810765d09be2499c639752a6ff&q='
                        url = api_address_0 + city + unit
                        return True
                    elif 'what is the weather' == voice_note_para:
                        if ' jarvis' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' jarvis', '')
                        elif ' jarvis' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' Jarvis', '')
                        elif 'jarvis ' in voice_note_para:
                            voice_note_para = voice_note_para.replace('jarvis ', '')
                        elif 'jarvis ' in voice_note_para:
                            voice_note_para = voice_note_para.replace(' Jarvis ', '')
                        if 'of' in voice_note_para:
                            city = voice_note_para.split('in ')[1]
                        elif 'in' in voice_note_para:
                            city = voice_note_para.split('of ')[1]
                            if 'at' in city:
                                city = city.split('at ')[1]
                        elif 'at' in voice_note_para:
                            city = voice_note_para.split('at ')[1]
                            if 'in' in city:
                                city = city.split('at ')[1]
                        unit = '&units=metric'
                        api_address_0 = 'http://api.openweathermap.org/data/2.5/weather?appid' \
                                        '=c907c9810765d09be2499c639752a6ff&q='
                        url = api_address_0 + city + unit
                        return True
            except IndexError:
                pass
                return False
        return False
    return False


# The function that defines the correct statement to get current time
def current_time(voice_note_para, time_ask_dict):
    global month_var, note, m, before_or_after_midday
    if 'jarvis ' in voice_note_para:
        voice_note_para = voice_note_para.replace('jarvis ', '')
    elif 'Jarvis ' in voice_note_para:
        voice_note_para = voice_note_para.replace('Jarvis ', '')
    elif ' jarvis' in voice_note_para:
        voice_note_para = voice_note_para.replace(' jarvis', '')
    elif ' Jarvis' in voice_note_para:
        voice_note_para = voice_note_para.replace(' Jarvis', '')
    for key_var, value_var in time_ask_dict.items():
        try:
            if key_var == voice_note_para:
                return True
        except IndexError:
            pass
    return False


def wiki_search(voice_note_para, wiki_w_h_words_dict):
    if 'jarvis ' in voice_note_para:
        voice_note_para = voice_note_para.replace('jarvis ', '')
    elif 'Jarvis ' in voice_note_para:
        voice_note_para = voice_note_para.replace('Jarvis ', '')
    elif ' jarvis' in voice_note_para:
        voice_note_para = voice_note_para.replace(' jarvis', '')
    elif ' Jarvis' in voice_note_para:
        voice_note_para = voice_note_para.replace(' Jarvis', '')
    for key_var, value_var in wiki_w_h_words_dict.items():
        try:
            if key_var in voice_note:
                if 'is the' in voice_note_para:
                    search_note_wiki = voice_note_para.split('is the ')[1]
                    return search_note_wiki
                elif 'are the' in voice_note_para:
                    search_note_wiki = voice_note_para.split('are the ')[1]
                    return search_note_wiki
                else:
                    if 'is' in voice_note_para:
                        search_note_wiki = voice_note_para.split('is ')[1]
                        return search_note_wiki
                    elif 'are' in voice_note_para:
                        search_note_wiki = voice_note_para.split('are ')[1]
                        return search_note_wiki
                    else:
                        search_note_wiki = voice_note_para
                        return search_note_wiki
        except IndexError:
            return False


def wiki_actual_search_function(search_note):
    import wikipedia
    global error_occurrence, counter
    if wikipedia.suggest(search_note) != '':
        try:
            test = wikipedia.summary(search_note, sentences=2)
            if search_note in test.lower():
                print('Would you also like to view images regarding the query?')
                speak_text_cmd('Would you also like to view images regarding the query?')
                voice_note_explain = read_voice_cmd()
                if 'yes' in voice_note_explain:
                    print(wikipedia.summary(search_note, sentences=2))
                    url_wiki = "https://www.google.co.in/search?q=" + search_note + "&source=lnms&tbm=isch"
                    webbrowser.open(url_wiki)
                    speak_text_cmd(wikipedia.summary(search_note, sentences=2))
                    return True
                elif 'no' in voice_note_explain:
                    print(wikipedia.summary(search_note, sentences=2))
                    speak_text_cmd(wikipedia.summary(search_note, sentences=2))
                    return True
                elif voice_note_explain == '':
                    speak_text_cmd("Fine don't answer. I will show it anyway")
                    print(wikipedia.summary(search_note, sentences=2))
                    speak_text_cmd(wikipedia.summary(search_note, sentences=2))
                    return True
                else:
                    speak_text_cmd('Sorry, I am experiencing some problems please search again')
            elif br.search(voice_note, search_note):
                return True
            else:
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens'
                                   '\\MSTTS_V110_enIN_HeeraM')
                if error_occurrence == 5:
                    error_occurrence = 0
                elif counter == 5:
                    counter = 0
                elif ' you ' in voice_note:
                    if error_occurrence == 5:
                        error_occurrence = 0
                    print('I am unable to understand you.')
                    speak_text_cmd('I am unable to understand you')
                elif ' your ' in voice_note:
                    if error_occurrence == 5:
                        error_occurrence = 0
                    print('I am unable to understand you.')
                    speak_text_cmd('I am unable to understand you')
                else:
                    counter -= 1
                    if counter == -1:
                        # web_browser.open('https://www.google.co.in/search?q={}'.format(voice_note)) (remove the _
                        # in web_browser)
                        br.search(voice_note, search_note)
                return True
        except wikipedia.exceptions.DisambiguationError as e:
            option_list = {}
            for o in list(e.options):
                if search_note in o.lower():
                    option_list.update({o: o})

            if len(option_list) == 1:
                for key_var in option_list.keys():
                    url_wiki = "https://www.google.co.in/search?q=" + key_var + "&source=lnms&tbm=isch"
                    webbrowser.open(url_wiki)
                    print(wikipedia.summary(key_var, sentences=2))
                    speak_text_cmd(wikipedia.summary(key_var, sentences=2))
                    continue
            elif len(option_list) > 1:
                speak_text_cmd('I have found multiple instances. Which one you want?')
                for num_wiki, o in enumerate(option_list.keys()):
                    print((num_wiki + 1), o.split('.')[0].split('_')[0])
                    speak_text_cmd(o.split('.')[0].split('_')[0])

                text_wiki = read_voice_cmd().lower()
                print(text_wiki)
                index_wiki = get_index(text_wiki)

                if index_wiki is not None:
                    print('{}"'.format(
                        option_list.get(list(option_list.keys())[index_wiki])))
                    speak_text_cmd('OK Sir')
                    url_wiki = "https://www.google.co.in/search?q=" + '{}"'.format(
                        option_list.get(list(option_list.keys())[index_wiki])) + "&source=lnms&tbm=isch"
                    webbrowser.open(url_wiki)
                    print(wikipedia.summary('{}"'.format(option_list.get(list(option_list.keys())[index_wiki])),
                                            sentences=2))
                    speak_text_cmd(
                        wikipedia.summary('{}"'.format(option_list.get(list(option_list.keys())[index_wiki])),
                                          sentences=2))
            pass
            return True
        except wikipedia.exceptions.PageError:
            if is_valid_note(google_searches_dict, voice_note):
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens'
                                   '\\MSTTS_V110_enIN_HeeraM')
                if error_occurrence == 5:
                    error_occurrence = 0
                elif counter == 5:
                    counter = 0
                elif ' you ' in voice_note:
                    if error_occurrence == 5:
                        error_occurrence = 0
                    print('I am unable to understand you.')
                    speak_text_cmd('I am unable to understand you')
                elif ' your ' in voice_note:
                    if error_occurrence == 5:
                        error_occurrence = 0
                    print('I am unable to understand you.')
                    speak_text_cmd('I am unable to understand you')
                else:
                    counter -= 1
                    if counter == -1:
                        # web_browser.open('https://www.google.co.in/search?q={}'.format(voice_note)) [Remove the '_'
                        # in web_browser]
                        br.search(voice_note, search_note)
            return True
    elif is_valid_note(google_searches_dict, voice_note):
        engine.setProperty('voice',
                           'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_enIN_HeeraM')
        if error_occurrence == 5:
            error_occurrence = 0
        elif counter == 5:
            counter = 0
        elif ' you ' in voice_note:
            if error_occurrence == 5:
                error_occurrence = 0
            print('I am unable to understand you.')
            speak_text_cmd('I am unable to understand you')
        elif ' your ' in voice_note:
            if error_occurrence == 5:
                error_occurrence = 0
            print('I am unable to understand you.')
            speak_text_cmd('I am unable to understand you')
        else:
            counter -= 1
            if counter == -1:
                # web_browser.open('https://www.google.co.in/search?q={}'.format(voice_note)) (remove the _ in
                # web_browser)
                br.search(voice_note, search_note)
        return True
    else:
        return False


def youtube(voice_note_para, youtube_dict):
    for key_var, value_var in youtube_dict.items():
        try:
            if key_var in voice_note_para:
                voice_note_para = voice_note_para.replace(key_var, '')
        except IndexError:
            pass
    for key_var, value_var in youtube_dict.items():
        import vlc
        if key_var not in voice_note_para:
            import urllib.request
            instance = 0
            from bs4 import BeautifulSoup
            import urllib.parse
            query = urllib.parse.quote(voice_note_para)
            url_song = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url_song)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                try:
                    if instance == 0:
                        instance += 1
                        url_song = 'https://www.youtube.com' + vid['href']
                        video = pafy.new(url_song)
                        best = video.getbest()
                        play_url = best.url
                        vlc_instance = vlc.Instance()
                        player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new(play_url)
                        media.get_mrl()
                        player.set_media(media)
                        player.play()
                        return player
                    else:
                        break
                except ValueError:
                    return False
            return False


def youtube_download(voice_note_para, youtube_dict):
    key_word = ''
    if 'download' in voice_note_para:
        from bs4 import BeautifulSoup
        import urllib.parse
        import urllib.request
        voice_note_para = voice_note_para.replace('download', '')
        instance_download = 0
        for key_var, value_var in youtube_dict.items():
            key_word = voice_note_para.replace(key_var, '')
        query = urllib.parse.quote(key_word)
        url_song = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url_song)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            try:
                if instance_download == 0:
                    instance_download += 1
                    url_song = 'https://www.youtube.com' + vid['href']
                    video = pafy.new(url_song)
                    print(video.title)
                    speak_text_cmd('I found a video with the following title' + video.title)
                    speak_text_cmd('Should I download it')
                    voice_note_para = read_voice_cmd()
                    if 'yes' in voice_note_para:
                        from pytube import YouTube
                        print('Ok, downloading. Please wait until it finishes')
                        speak_text_cmd('Ok, downloading. Please wait until it finishes')
                        YouTube(url_song).streams.first().download('C:\\')
                        print('Do you want the download as a video or a audio?')
                        speak_text_cmd('Do you want the download video song as a audio?')
                        voice_note_para = read_voice_cmd()
                        if 'yes' in voice_note_para:
                            import moviepy.editor as mp_edit
                            path_down_dir = "D:/"
                            video_title = video.title
                            vid_name = video_title.replace('|', '')
                            down_clip = mp_edit.VideoFileClip("C:\\" + vid_name + '.mp4')
                            down_clip.audio.write_audiofile("C:\\" + vid_name + '.mp3')
                            path_down_dir = os.path.realpath(path_down_dir)
                            os.startfile(path_down_dir)
                            return True
                        elif 'audio' in voice_note_para:
                            import moviepy.editor as mp_edit
                            path_down_dir = "D:/"
                            video_title = video.title
                            vid_name = video_title.replace('|', '')
                            down_clip = mp_edit.VideoFileClip("C:\\" + vid_name + '.mp4')
                            down_clip.audio.write_audiofile("C:\\" + vid_name + '.mp3')
                            path_down_dir = os.path.realpath(path_down_dir)
                            os.startfile(path_down_dir)
                            return True
                        elif 'video' in voice_note_para:
                            path_down_dir = "D:/"
                            path_down_dir = os.path.realpath(path_down_dir)
                            os.startfile(path_down_dir)
                            return True
                    elif 'no' in voice_note_para:
                        return True
            except ValueError:
                return False
            return False


def youtube_check(voice_note_para, youtube_dict):
    for key_var, value_var in youtube_dict.items():
        try:
            if key_var in voice_note_para:
                return True
        except IndexError:
            pass
    return False


def player_close(voice_note_para, close_word_dict):
    for key_var, value_var in close_word_dict.items():
        try:
            if key_var in voice_note_para:
                return True
        except IndexError:
            pass
    return False


def player_play(voice_note_para, resume_word_dict):
    for key_var, value_var in resume_word_dict.items():
        try:
            if key_var in voice_note_para:
                return True
        except IndexError:
            pass
    return False


def pause(voice_note_para, pause_word_dict):
    for key_var, value_var in pause_word_dict.items():
        try:
            if key_var in voice_note_para:
                return True
        except IndexError:
            pass
    return False


def image_search(voice_note_para, image_search_dict):
    for key_var, value_var in image_search_dict.items():
        try:
            if key_var in voice_note_para:
                key_img_word = voice_note_para.replace(key_var, '')
                url_image = "https://www.google.co.in/search?q= " + key_img_word + " &source=lnms&tbm=isch"
                webbrowser.open(url_image)
                return True
        except IndexError:
            pass
    return False


# The main function
if __name__ == '__main__':
    video_player = None
    url = ''
    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_enIN_HeeraM')
    speak_text_cmd("Hello there, this is jarvis, an indian artificial intelligence system created by Pratit")
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11')
    print()
    speak_text_cmd(
        "Would you like to talk to me or are you a shy kind of a person. If you are don't worry we can chat.")
    ans = input('Type Here:').lower()
    if 'chat' in ans:
        block = 1
    else:
        block = 0

    while True:
        
        city = 'Mumbai'
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN'
                                    '-US_ZIRA_11')
        voice_note = read_voice_cmd()
        print('User : {}'.format(voice_note))
        if error_occurrence == 1:
            error_occurrence -= 1
            continue
        elif 'who are you' in voice_note:
            engine.setProperty('voice',
                               'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_enIN_HeeraM'
                               )
            speak_text_cmd(
                "Weren't you paying attention, when I introduced myself."
                "I am an Indian Artificial Intelligence System Created by Pratit Todkar"
            )
        elif 'introduce' in voice_note:
            if 'you' in voice_note:
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens'
                                   '\\MSTTS_V110_enIN_HeeraM '
                                   )
                speak_text_cmd(
                    "I am an Indian Artificial Intelligence System Created by Pratit Todkar"
                    "I go by the name jarvis"
                )
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN'
                                   '-US_ZIRA_11')
            else:
                pass
        elif 'talk with me' in voice_note:
            block = 0
        elif 'chat with me' in voice_note:
            block = 1
        elif error_occurrence == 2:
            error_occurrence -= 2
            continue
        elif is_valid_note(greeting_dict, voice_note):
            play_sound(mp3_greeting_list)
            if error_occurrence == 5:
                error_occurrence = 0
            continue
        elif 'hey jarvis' == voice_note:
            speak_text_cmd('Yes, I am here')
            error_occurrence = 0
            continue
        elif 'convert video to MP3' in voice_note:
            import moviepy.editor as mp

            speak_text_cmd('Enter the path of the video file')
            path_vid = input()
            name = path_vid.replace('.mp4', '').rsplit('\\')[-1]
            clip = mp.VideoFileClip(path_vid)
            clip.audio.write_audiofile(os.path.expanduser('~user') + "\\Desktop\\" + name + '.mp3')
            path = os.path.expanduser('~user') + "\\Desktop\\"
            path = os.path.realpath(path)
            os.startfile(path)
        elif player_close(voice_note, player_shutdown):
            if video_player is not None:
                video_player.stop()
        elif player_play(voice_note, player_resume):
            if video_player is not None:
                video_player.pause()
        elif pause(voice_note, player_pause):
            if video_player is not None:
                video_player.pause()
        elif youtube_check(voice_note, youtube_valid_dict):
            video_player = youtube(voice_note, youtube_valid_dict)
        elif youtube_download(voice_note, from_youtube):
            print('Done')
            if 'no' in voice_note:
                pass
            else:
                speak_text_cmd('Download successful')
        elif is_valid_note(open_launch_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print('Opening please wait...')
            play_sound(mp3_open_launch_list)
            if is_valid_note(websites_dict, voice_note):
                # 'Launch Facebook'
                key = voice_note.split(' ')[1]
                webbrowser.open(websites_dict.get(key))
            else:
                key = voice_note.replace('open ', '').replace('launch ', '')
                print('Key is : ' + key)
                # print(list(lookup_drive_change.lookup_dict.keys()))

                opt_dict = {}
                for k in list(lookup_drive_change.lookup_dict.keys()):
                    if key in k.lower():
                        opt_dict.update({k: lookup_drive_change.lookup_dict.get(k)})

                # print(opt_dict)
                if len(opt_dict) == 1:
                    for key in opt_dict.keys():
                        print('explorer {}'.format(opt_dict.get(key)))
                        os.system('explorer {}'.format(opt_dict.get(key)))
                        continue
                elif len(opt_dict) > 1:
                    speak_text_cmd('I have found multiple instances. Which one you want?')
                    default = 0
                    index = None
                    for i, k in enumerate(opt_dict.keys()):
                        print(k.split('.')[0].split('_')[0] + ' from {} folder'.format(opt_dict.get(k).split('\\')[-2]))
                        speak_text_cmd(
                            k.split('.')[0].split('_')[0] + ' from {} folder'.format(opt_dict.get(k).split('\\')[-2]))

                        default = 1

                    text = read_voice_cmd().lower()
                    print(text)
                    index = get_index(text)

                    if index is not None:
                        print('explorer {}"'.format(
                            lookup_drive_change.lookup_dict.get(list(opt_dict.keys())[index])) + ' ' + str(index))
                        speak_text_cmd('OK Sir')
                        os.system(
                            'explorer {}"'.format(lookup_drive_change.lookup_dict.get(list(opt_dict.keys())[index])))
            if 'C' in voice_note:
                os.system('explorer C:\\"{}"'.format(
                    voice_note.replace('open ', '').replace('launch ', '').replace('from C', '').replace(' drive',
                                                                                                         '')))
        elif is_valid_note(thank_you_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print('You are welcome')
            play_sound(mp3_thank_you_list)
        elif 'lock ' in voice_note:
            if error_occurrence == 5:
                error_occurrence = 0
            for value in ['pc', 'system', 'windows', 'computer']:
                import ctypes

                ctypes.windll.user32.LockWorkStation()
        elif 'restart' in voice_note:
            if error_occurrence == 5:
                error_occurrence = 0
            for value in ['pc', 'system', 'windows', 'computer']:
                os.system("shutdown /r /t 1")
        elif 'shutdown' in voice_note:
            if error_occurrence == 5:
                error_occurrence = 0
            for value in ['pc', 'system', 'windows', 'computer']:
                os.system("shutdown /s /t 1")
        elif how_are_you_jarvis(how_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("I'm fine, 'm glad that you asked.")
            speak_text_cmd("I'm fine, 'm glad that you asked.")
        elif how_is_life_jarvis(how_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print(
                "Well my life is just as fun as any one of yours. I guess being superior dosen't changes life much "
                "for you.")
            speak_text_cmd(
                "Well my life is just as fun as any one of yours. I guess being superior dosen't changes life much "
                "for you.")
        elif where_do_you_live(where_dict, voice_note, what_dict):
            if error_occurrence == 5:
                error_occurrence = 0
            print(
                "Well I have got a nice place in your hard disk, it's a good neighbourhood. I plan on spending my "
                "lifetime there")
            speak_text_cmd(
                "Well I have got a nice place in your hard disk, it's a good neighbourhood. I plan on spending my "
                "lifetime there")
        elif whom_am_i_talking_to(whom_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("You're talking to an artificial intelligence named jarvis")
            speak_text_cmd("You're talking to an artificial intelligence named jarvis")
        elif what_am_i_doing(who_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print(
                "Do you mean here or with your life? If it's here I think it's pretty clear to both of us that you "
                "are talking to me. If it's about your life I think you would better ask it to yourself")
            speak_text_cmd(
                "Do you mean over here or with your life? If it's here I think it's pretty clear to both of us that "
                "you are talking to me. If it's about your life I think you would better ask it to yourself")
        elif what_are_you_doing(what_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("I think we both are smart enough here to know that, aren't we?")
            speak_text_cmd("I think we both are smart enough here to know that, aren't we?")
        elif who_created_you(who_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print('I was created by Pratit')
            speak_text_cmd(
                "I was created by Pratit and technically that makes him god for me.")
        elif when_were_you_created(when_dict, voice_note, what_dict):
            if error_occurrence == 5:
                error_occurrence = 0
            print('I was created on 30th November 2018')
            speak_text_cmd("I was created on thirtieth of November two thousand and eighteen")
        elif what_is_your_name(what_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("Well I told that to you when I introduced myself. I am telling you again my name is jarvis")
            speak_text_cmd("Well I told that to you when I introduced myself. I'm telling you again my name is jarvis")
        elif to_whom_do_you_belong(whom_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("I currently belong to my owner , Pratit.")
            speak_text_cmd("I currently belong to my owner , Pratit.")
        elif what_is_your_nationality(what_dict, voice_note, which_dict):
            if error_occurrence == 5:
                error_occurrence = 0
            print(
                "I consider myself the citizen of the world , but since I was born in India I am an Indian and by that "
                "logic a Maharashtrian")
            speak_text_cmd(
                "I consider myself the citizen of the world , but since I was born in India I'm an Indian and by that "
                "logic a Maharashtrian")
        elif can_you_listen_me(listening_ability_question_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            print("I'm able to hear you otherwise I wouldn't be responding to you")
            speak_text_cmd("I'm able to hear you otherwise I wouldn't be responding to you")
        elif weather_valid_note(voice_note, weather_dict):
            json_data = requests.get(url).json()
            if '404' == json_data['cod']:
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens'
                                   '\\MSTTS_V110_enIN_HeeraM')
                if 'in' in voice_note:
                    break
                elif 'of' in voice_note:
                    break
                else:

                    unit = '&units=metric'
                    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid' \
                                  '=c907c9810765d09be2499c639752a6ff&q= '
                    url = api_address + city + unit
                    json_data = requests.get(url).json()
                    if 'temperature' in voice_note:
                        formatted_data_temp = json_data['main']['temp']
                        data_temp = 'The current temperature in', city, 'is', formatted_data_temp, 'degree celsius'
                        print('The current temperature in', city, 'is', formatted_data_temp, 'degree celsius')
                        speak_text_cmd(data_temp)
                    elif 'weather' in voice_note:
                        formatted_data_temp = json_data['main']['temp']
                        data_temp = 'The current temperature in', city, 'is', formatted_data_temp, 'degree celsius'
                        print('The current temperature in', city, 'is', formatted_data_temp, 'degree celsius')
                        speak_text_cmd(data_temp)
                        formatted_data_description = json_data['weather'][0]['description']
                        if formatted_data_description == 'smoke':
                            data_description = 'The condition of', city, \
                                               'can be best described as and I quote. It is full of', \
                                               formatted_data_description
                            print('The condition of', city, 'can be best described as and I quote', city,
                                  'is covered in smoke')
                            speak_text_cmd(data_description)
                        elif formatted_data_description == 'haze':
                            data_description = city, 'is hazed'
                            print(city, 'is hazed')
                            speak_text_cmd(data_description)
                        elif formatted_data_description == 'few clouds':
                            data_description = city, 'is covered with few clouds'
                            print(city, 'is covered with few clouds')
                            speak_text_cmd(data_description)
                        elif formatted_data_description == 'overcast clouds':
                            data_description = city, 'is covered almost fully with clouds'
                            print(city, 'is covered almost fully with clouds')
                            speak_text_cmd(data_description)
            else:
                engine.setProperty('voice',
                                   'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens'
                                   '\\MSTTS_V110_enIN_HeeraM')
                json_data = requests.get(url).json()
                if 'temperature' in voice_note:
                    formatted_data_temp = json_data['main']['temp']
                    data_temp = 'The current temperature in', city, 'is', formatted_data_temp, 'degree celsius'
                    print('The current temperature in', city, 'is', formatted_data_temp, 'degree celsius')
                    speak_text_cmd(data_temp)
                elif 'weather' in voice_note:
                    formatted_data_temp = json_data['main']['temp']
                    data_temp = 'The current temperature in', city, 'is', formatted_data_temp, 'degree celsius'
                    print('The current temperature in', city, 'is', formatted_data_temp, 'degree celsius')
                    speak_text_cmd(data_temp)
                    formatted_data_description = json_data['weather'][0]['description']
                    if formatted_data_description == 'smoke':
                        data_description = 'The condition of', city, 'can be best described as and I quote. It is ' \
                                                                     'full of', formatted_data_description
                        print('The condition of', city, 'can be best described as and I quote', city,
                              'is covered in smoke')
                        speak_text_cmd(data_description)
                    elif formatted_data_description == 'haze':
                        data_description = city, 'is hazed'
                        print(city, 'is hazed')
                        speak_text_cmd(data_description)
                    elif formatted_data_description == 'few clouds':
                        data_description = city, 'is covered with few clouds'
                        print(city, 'is covered with few clouds')
                        speak_text_cmd(data_description)
                    elif formatted_data_description == 'overcast clouds':
                        data_description = city, 'is covered almost fully with clouds'
                        print(city, 'is covered almost fully with clouds')
                        speak_text_cmd(data_description)
        elif current_time(voice_note, time_dict):
            note = pd.datetime.now().date()
            month_var = str(pd.datetime.now().month)
            m = month_dict.get(month_var)
            if pd.datetime.now().hour > 12:
                before_or_after_midday = 'PM'
            elif pd.datetime.now().hour == 0:
                before_or_after_midday = 'AM'
            elif pd.datetime.now().hour == 12:
                before_or_after_midday = 'PM'
            else:
                before_or_after_midday = 'AM'
            if 'time' in voice_note:
                import pandas as pd

                time = 'The current time is', pd.datetime.now().hour, 'hours and', pd.datetime.now().minute, \
                       'minutes', before_or_after_midday
                print('The current time is', pd.datetime.now().hour, 'hours and', pd.datetime.now().minute, 'minutes',
                      before_or_after_midday)
                speak_text_cmd(time)
            elif 'date' in voice_note:
                date = "Today's date is", note.day, m, note.year
                print("Today's date is", note.day, m, note.year)
                speak_text_cmd(date)
            elif 'season' in voice_note:
                if int('6') > int(month_var) > int('4'):
                    print('The current ongoing season is Summer')
                    speak_text_cmd('The current ongoing season is Summer')
                elif int(month_var) == int('6'):
                    print('The current season is Monsoon')
                    speak_text_cmd('The current season is Monsoon')
                elif int(month_var) == int('4'):
                    print('The current ongoing season is Summer')
                    speak_text_cmd('The current ongoing season is Summer')
                elif int('9') > int(month_var) > int('6'):
                    print('The ongoing season is Monsoon')
                    speak_text_cmd('The ongoing season is Monsoon')
                elif int('9') == int(month_var):
                    print('The ongoing season currently is Autumn')
                    speak_text_cmd('The ongoing season currently is Autumn')
                elif int('10') == int(month_var):
                    print('The ongoing season currently is Autumn')
                    speak_text_cmd('The ongoing season currently is Autumn')
                elif int('10') < int(month_var):
                    print('The ongoing season is Winter')
                    speak_text_cmd('The ongoing season is Winter')
                elif int('1') == int(month_var):
                    print('The ongoing season is Spring')
                    speak_text_cmd('The ongoing season is Spring')
                elif int('2') == int(month_var):
                    print('The ongoing season is spring')
                    speak_text_cmd('The ongoing season is spring')
                elif int(month_var) == int('3'):
                    print('The ongoing season is spring')
                    speak_text_cmd('The ongoing season is spring')
        elif wiki_search(voice_note, google_searches_dict):
            print('Searching please wait...')
            playsound('mp3/search_1.mp3')
            if wiki_actual_search_function(wiki_search(voice_note, google_searches_dict)):
                print()
        elif image_search(voice_note, img_dict):
            print()
        elif 'Iron Man' in voice_note:
            print("I am not going to tell you anything about Tony, it's all confidential")
            speak_text_cmd("I am not going to tell you anything about tony It's all confidential")
        elif 'Tony Stark' in voice_note:
            print("I am not going to tell you anything about Tony, it's all confidential")
            speak_text_cmd("I am not going to tell you anything about tony It's all confidential")
        elif 'tony stark' in voice_note:
            print("I am not going to tell you anything about Tony, it's all confidential")
            speak_text_cmd("I am not going to tell you anything about tony It's all confidential")
        elif is_valid_note(goodbye_dict, voice_note):
            if error_occurrence == 5:
                error_occurrence = 0
            if 'exit' in voice_note:
                print('Goodbye')
                play_sound(mp3_goodbye_list)
                exit()
            else:
                print('Goodbye')
                play_sound(mp3_goodbye_list)
                counter = 5
                error_occurrence = 5
        else:
            if error_occurrence < 5:
                print("I'm unable to understand you.")
                speak_text_cmd('I am unable to understand you.')
