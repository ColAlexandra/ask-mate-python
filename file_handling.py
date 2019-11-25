


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