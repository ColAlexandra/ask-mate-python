import psycopg2
import psycopg2.extras
import os


def get_connection_string():
    user_name = os.environ.get('user_name')
    password = os.environ.get('password')
    host = os.environ.get('host')
    database_name = os.environ.get('database_name')

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        return'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environement variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur,*args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper

# import csv
#
#
# def import_file(filename):
#     list_dict = []
#     try:
#         with open(filename, 'r') as new_file:
#             reader = csv.reader(new_file)
#             import_data = list(reader)
#             header = import_data[0]
#             import_data.pop(0)
#             for line in import_data:
#                 dict_temp = {}
#                 for i in range(len(header)):
#                     dict_temp[header[i]] = line[i]
#                 list_dict.append(dict_temp)
#     except FileNotFoundError:
#         print('File not found')
#     return list_dict
#
#
# def export_file(list_dict):
#     filename = 'sample_data/question.csv'
#     try:
#         with open(filename, 'w') as csvfile:
#             title_list = list(list_dict[0])
#             writer = csv.DictWriter(csvfile, fieldnames=title_list)
#             writer.writeheader()
#             for data in list_dict:
#                 writer.writerow(data)
#     except PermissionError:
#         print('File not found')
#
#
# def export_ans(list_dict):
#     filename = 'sample_data/answer.csv'
#     try:
#         with open(filename, 'w') as csvfile:
#             title_list = list(list_dict[0])
#             writer = csv.DictWriter(csvfile, fieldnames=title_list)
#             writer.writeheader()
#             for data in list_dict:
#                 writer.writerow(data)
#     except PermissionError:
#         print('File not found')