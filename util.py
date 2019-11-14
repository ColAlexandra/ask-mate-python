import data_manager


def list_a_question():
    questions = data_manager.question_list()

    for question in questions:
        id = question['id']
        title = question['title']
        message = question['message']
        return id, title, message


def new_dictionary(title, message):
    questions = data_manager.question_list()
    question = questions[0]
    headers = [key for key, values in question.items()]
    new_dict = {}
    for header in headers:
        new_dict[header] = 0
    for key, values in new_dict.items():
        if key == 'message':
            new_dict[key] = message
        if key == 'title':
            new_dict[key] = title
        if key == 'id':
            new_dict[key] = new_id_question()
    return new_dict


def add_dict_to_list_question():
    list_dict = data_manager.question_list()
    new_dict = new_dictionary()
    list_dict.append(new_dict)
    return list_dict


def choose_question(question_id):
    questions = data_manager.question_list()
    for question in questions:
        if question['id'] == question_id:
            return question


def choose_answer(question_id):
    answers = data_manager.answer_list()
    list_answer = []
    for answer in answers:
        if answer['question_id'] == question_id:
            list_answer.append(answer)
    return list_answer


def new_id_question():
    questions = data_manager.question_list()
    id_list = []
    for question in questions:
        for id in question['id']:
            id_list.append(id)
    for i in range(len(sorted(id_list))):
        if i not in id_list:
            return str(i)

    return str(len(id_list))

