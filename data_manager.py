import file_handling


@file_handling.connection_handler
def all_question_list(cursor):
    cursor.execute("""
                    SELECT * FROM question
                    ORDER BY id ASC                    
                    """)
    question = cursor.fetchall()
    print(question)
    return question


@file_handling.connection_handler
def all_answer_list(cursor):
    cursor.execute("""
                    SELECT * FROM answer
                    ORDER BY id ASC    
    """)
    answer = cursor.fetchall()
    return answer


@file_handling.connection_handler
def update_question(cursor, question_id, title, message):
    sql = 'UPDATE question SET title = %(title)s, message = %(message)s WHERE id = %(id)s'
    values = {'title': title, 'message': message, 'id': question_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def edit_answer(cursor, answer_id, message):
    sql = 'UPDATE answer SET message = %(message)s WHERE id = %(answer_id)s'
    values = {'message': message, 'answer_id': answer_id}
    cursor.execute(sql,values)


@file_handling.connection_handler
def export_to_file_question(cursor, title, message):
    sql = 'INSERT INTO question(title, message) VALUES (%(title)s, %(message)s) '
    values = {'title': title, 'message': message}
    cursor.execute(sql, values)


@file_handling.connection_handler
def export_to_file_answer(cursor, message, question_id):
    sql = 'INSERT INTO answer(message, question_id) VALUES (%(message)s, %(question_id)s) '
    values = {'message': message, 'question_id': question_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def list_a_question(cursor):
    # questions = question_list()
    # for question in questions:
    #     id = question['id']
    #     title = question['title']
    #     message = question['message']
    cursor.execute("""
                    SELECT id, title, message FROM question
    """)
    question_list = cursor.fetchall()
    return question_list


@file_handling.connection_handler
def choose_answer(cursor, question_id):
    # answers = all_answer_list()
    # print(answers)
    # list_answer = []
    # for answer in answers:
    #     if answer['question_id'] == question_id:
    #         list_answer.append(answer)
    # return list_answer
    cursor.execute("""SELECT * FROM answer WHERE question_id = %(question_id)s""", {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


@file_handling.connection_handler
def choose_question(cursor, question_id):
    # questions = all_question_list()
    # print(questions)
    # for question in questions:
    #     if question['id'] == question_id:
    #         return question
    cursor.execute("""SELECT * FROM question WHERE id = %(question_id)s""", {'question_id': question_id})
    question = cursor.fetchone()
    return question


@file_handling.connection_handler
def show_answer(cursor, answer_id):
    cursor.execute("""SELECT * FROM answer WHERE id = %(answer_id)s""", {'answer_id': answer_id})
    answer = cursor.fetchone()
    return answer

# def answer_list(): #przekazac w slowniku
#     answer = file_handling.import_file(filename='sample_data/answer.csv')
#     return answer


# def answer_list(): #przekazac w slowniku
#     answer = file_handling.import_file(filename='sample_data/answer.csv')
#     return answer


# def question_list():
#     question = file_handling.import_file(filename='sample_data/question.csv')
#     return question


# def export_to_file_answer(message, question_id):
#     list_dict = add_dict_to_list_answer(message, question_id)
#     file_handling.export_ans(list_dict)


# def new_dictionary(title, message):
#     headers = ['submission_time', 'view_number', 'vote_number', 'tittle', 'message', 'image']
#     new_dict = {}
#     for header in headers:
#         new_dict[header] = 0
#     for key, values in new_dict.items():
#         if key == 'message':
#             new_dict[key] = message
#         if key == 'title':
#             new_dict[key] = title
#     return new_dict


# def add_dict_to_list_question(title, message):
#     list_dict = question_list()
#     new_dict = new_dictionary(title, message)
#     list_dict.append(new_dict)
#     return list_dict


# def new_dictionary_ans(message, question_id):
#     answers = answer_list()
#     answer = answers[0]
#     headers = [key for key, values in answer.items()]
#     new_dict = {}
#     for header in headers:
#         new_dict[header] = 0
#     for key, values in new_dict.items():
#         if key == 'message':
#             new_dict[key] = message
#         if key == 'question_id':
#             new_dict[key] = question_id
#     return new_dict


# def add_dict_to_list_answer(message, question_id):
#     list_dict = answer_list()
#     new_dict = new_dictionary_ans(message, question_id)
#     list_dict.append(new_dict)
#     return list_dict


# def new_id_question():
#     questions = question_list()
#     id_list = []
#     for question in questions:
#         for id in question['id']:
#             id_list.append(int(id))
#
#     for i in range(len(sorted(id_list))):
#         if i not in id_list:
#             return i
#
#     return len(id_list)


# def export_questions(list_dict):
#     file_handling.export_file(filename='sample_data/question.csv', list_dict)
#
# def export_answer(list_dict):
#     file_handling.file_export(filename='sample_data/answer.csv', list_dict)


#tutaj funkcje a propos question i answer
#tutaj zapisanie przy funkcji z utli przeniesionej