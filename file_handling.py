import csv

def import_answer(filename):
    answer = []
    try:
        with open(filename, 'r') as new_file:
            reader = csv.reader(new_file)
            import_data = list(reader)
            header = import_data[0]
            import_data.pop(0)
            for line in import_data:
                dict_temp = {}
                for i in range(len(header)):
                    dict_temp[header[i]] = line[i]
                answer.append(dict_temp)
    except FileNotFoundError:
        print('File not found')
    return answer

def import_question(filename):
    question = []
    try:
        with open(filename, 'r') as new_file:
            reader = csv.reader(new_file)
            import_data = list(reader)
            header = import_data[0]
            import_data.pop(0)
            for line in import_data:
                dict_temp = {}
                for i in range(len(header)):
                    dict_temp[header[i]] = line[i]
                question.append(dict_temp)
    except FileNotFoundError:
        print('File not found')

    return question

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
