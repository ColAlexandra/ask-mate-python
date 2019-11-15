import file_handling
import util


def question_list():
    question = file_handling.import_file(filename='sample_data/question.csv')
    return question


def answer_list():
    answer = file_handling.import_file(filename='sample_data/answer.csv')
    return answer


# def export_questions(list_dict):
#     file_handling.export_file(filename='sample_data/question.csv', list_dict)
#
# def export_answer(list_dict):
#     file_handling.file_export(filename='sample_data/answer.csv', list_dict)

