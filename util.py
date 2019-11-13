#for all layers and for business logic layer
import data_manager

def list_a_question():
    questions = data_manager.question_list()

    for question in questions:
        id = question['id']
        title = question['title']
        message = question['message']
        return id, title, message

def user_input():
    user_input = input()
    return user_input

def new_dict():
    dodaj = dictionary dodaj title

def add_question():
