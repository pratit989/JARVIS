import webview
from TTS import speak
from urllib.parse import quote as encode


def get_elements(session):
    # Get answer element
    def get_answer():
        try:
            answer = session.get_elements('[data-tts="answers"]')
            speak(answer[0]['outerText'])
        except IndexError:
            get_description()
        except KeyError:
            get_description()

    # Get description element
    def get_description():
        try:
            description = session.get_elements('[data-attrid="wa:/description"]')
            speak(description[0]['outerText'])
        except IndexError:
            speak("Here are the search results for your query.")
        except KeyError:
            speak("Here are the search results for your query.")
    get_answer()


def query(user_input: str):
    search_window(encode(user_input))


def search_window(to_search: str):
    window = webview.create_window('JARVIS', url='https://www.google.co.in/search?q=' + to_search)
    webview.start(get_elements, window)
