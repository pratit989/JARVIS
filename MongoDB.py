import Settings
import urllib.parse

import pymongo as pymongo
from pymongo import errors
from TTS import print_and_speak


def initialise_database(username, password):
    global db, col
    print_and_speak("Initialising Database...")
    try:
        encoded_pass = urllib.parse.quote_plus(password)
        encoded_username = urllib.parse.quote_plus(username)
        client = pymongo.MongoClient(
            f"mongodb+srv://{encoded_username}:{encoded_pass}@vpregistration.fepjd.mongodb.net/usersDB"
            f"?retryWrites=true&w=majority")
        db = client.test
        db = client.get_default_database()
        col = db["users"]
        col.find_one()
        print_and_speak("Database successfully initialised\n")
        print_and_speak(f"Welcome {username}")
    except errors.OperationFailure as error:
        print_and_speak(error.details['errmsg'])
        print_and_speak("Database failed to initialised\n")
        Settings.logged_in = False


def get_data(enrollment_no):
    print_and_speak(f"Fetching data for enrollment number {enrollment_no}\n")
    query = {'EnrollmentNO': enrollment_no}
    doc = col.find(query, {'_id': 0, 'salt': 0, 'hash': 0, '__v': 0})
    try:
        data = doc[0]
        print_and_speak(f"The enrollment number belongs to {data['fullname']}\nRoll number: {data['RollNo']}")
        return data
    except IndexError:
        print_and_speak(f"No student data found that matches the enrollment number {enrollment_no}")


'''initialise_database('darshan123', 'Test123')
integer = int(input('enroll no: '))
get_data(integer)'''
