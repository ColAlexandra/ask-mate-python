def import_answer(filename='answer.csv'):
    answer = {}
    try:
        with open(filename, 'r') as new_file:
             reader= csv.reader(new_file)
            for line in new_file.readlines():
                answer.append(line.strip().split(','))
            return answer
    except FileNotFoundError:
        print('File not found')

def import_question(filename='question.csv'):
    question = []
    try:
        with open(filename, 'a+') as new_file:
            for line in new_file.readlines():
                question.append(line.strip().split(','))
            return question
    except FileNotFoundError:
        print('File not found')

def export_answer(answer, filename='answer.csv'):
    try:
        with open(filename,'a+') as new_file:
            for line in answer:
                new_file.write(','.join(line) + '\r\n')
    except PermissionError:
        print('No permission')

def export_question(question, filename='question.csv'):
    try:
        with open(filename,'a+') as new_file:
            for line in question:
                new_file.write(','.join(line) + '\r\n')
    except PermissionError:
        print('No permission')