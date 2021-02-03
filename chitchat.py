from TTS import print_and_speak


def processing_chitchat(user_input: str):
    if 'how are you' in user_input or 'how have you been' in user_input:
        print_and_speak("I am doing great. Just got a new home in your PC's silicon world")

    elif 'what are you doing' in user_input:
        print_and_speak("I am here talking to you. That's what I am doing")

    elif 'what am i doing' in user_input:
        print_and_speak("You tell me. My guess is you are talking to me")

    elif 'how is life' in user_input or 'how is your life' in user_input:
        print_and_speak("Life in the silicon world is amazing")

    elif 'where do you live' in user_input or 'where do you stay' in user_input or 'where is your home' in user_input \
            or 'what is your address' in user_input:
        print_and_speak(
            'I live in the silicon world. Be born next time as a software. Then you can come live with me too')

    elif 'whom am I talking to' in user_input:
        print_and_speak("You are talking to JARVIS")

    elif 'who created you' in user_input or 'who made you' in user_input or 'who is your creator' in user_input or \
            "who's creation are you" in user_input or 'who has made you' in user_input or \
            'who has created you' in user_input:
        print_and_speak('I was created by Pratit with the helpful suggestions from Praveen which helped in how I '
                        'turned out to be.')

    elif 'your birthday' in user_input or 'when were you created' in user_input or 'when were you born' in user_input:
        print_and_speak('I am a work in progress always.')

    elif 'what is your name' in user_input or 'what should I call you' in user_input or \
            "what's your name" in user_input:
        print_and_speak("I am Jarvis")

    elif 'to whom do you belong' in user_input or 'who is your owner' in user_input:
        print_and_speak("I am owned and copyrighted by Pratit")
