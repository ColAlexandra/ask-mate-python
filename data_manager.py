import file_handling

def question_list():
    question = file_handling.import_question(filename='sample_data/question.csv')
    return question

def answer_list():
    answer = file_handling.import_answer(filename='sample_data/answer.csv')
    return answer

