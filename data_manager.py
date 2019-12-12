import file_handling


@file_handling.connection_handler
def all_question_list(cursor):
    cursor.execute("""SELECT * FROM question ORDER BY id ASC""")
    question = cursor.fetchall()
    return question


@file_handling.connection_handler
def all_answer_list(cursor):
    cursor.execute("""SELECT * FROM answer JOIN question ON answer.question_id=question_id""")
    answers = cursor.fetchall()
    return answers


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
def export_to_file_comment_answer(cursor, answer_id, message):
    sql = 'INSERT INTO comment(answer_id, message) VALUES (%(answer_id)s, %(message)s)'
    values = {'answer_id': answer_id, 'message': message}
    cursor.execute(sql, values)


@file_handling.connection_handler
def export_to_file_comment_question(cursor, question_id, message):
    sql = 'INSERT INTO comment(question_id, message) VALUES (%(question_id)s, %(message)s)'
    values = {'question_id': question_id, 'message': message}
    cursor.execute(sql, values)


@file_handling.connection_handler
def list_a_question(cursor):
    cursor.execute("""SELECT id, title, message FROM question""")
    question_list = cursor.fetchall()
    return question_list


@file_handling.connection_handler
def choose_answer(cursor, question_id):
    cursor.execute("""SELECT * FROM answer WHERE question_id = %(question_id)s""", {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


@file_handling.connection_handler
def choose_question(cursor, question_id):
    cursor.execute("""SELECT * FROM question WHERE id = %(question_id)s""", {'question_id': question_id})
    question = cursor.fetchone()
    return question


@file_handling.connection_handler
def show_answer(cursor, answer_id):
    cursor.execute("""SELECT * FROM answer WHERE id = %(answer_id)s""", {'answer_id': answer_id})
    answer = cursor.fetchone()
    return answer


@file_handling.connection_handler
def remove_question(cursor, id_):
    cursor.execute("""DELETE FROM question WHERE id = %(id)s""", {'id': id_})


@file_handling.connection_handler
def remove_chosen_answer(cursor, answer_id):
    cursor.execute("""DELETE FROM answer WHERE id = %(answer_id)s""", {'answer_id': answer_id})


@file_handling.connection_handler
def show_comments_to_answer(cursor, answer_id):
    cursor.execute("""SELECT * FROM comment WHERE answer_id=%(answer_id)s""", {'answer_id': answer_id})
    comments = cursor.fetchall()
    return comments


@file_handling.connection_handler
def show_comments_to_question(cursor, question_id):
    cursor.execute("""SELECT * FROM comment WHERE question_id=%(question_id)s""", {'question_id': question_id})
    comments = cursor.fetchall()
    return comments


@file_handling.connection_handler
def vote_up_question(cursor, question_id):
    cursor.execute("""SELECT vote_number FROM question WHERE id=%(question_id)s""", {'question_id': question_id})
    vote_number = cursor.fetchone()
    vote_up = vote_number['vote_number']
    if vote_up is None:
        vote_up = 1
    else:
        vote_up += 1
    return vote_up


@file_handling.connection_handler
def update_vote_question(cursor, question_id):
    vote_up = vote_up_question(question_id)
    sql = 'UPDATE question SET vote_number=%(vote_up)s WHERE id = %(question_id)s'
    values = {'vote_up': vote_up, 'question_id': question_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def vote_down_question(cursor, question_id):
    cursor.execute("""SELECT vote_number FROM question WHERE id=%(question_id)s""", {'question_id': question_id})
    vote_number = cursor.fetchone()
    vote_down = vote_number['vote_number']
    if vote_down is None:
        vote_down = -1
    else:
        vote_down -= 1
    return vote_down


@file_handling.connection_handler
def update_lower_question(cursor, question_id):
    vote_up = vote_down_question(question_id)
    sql = 'UPDATE question SET vote_number=%(vote_up)s WHERE id = %(question_id)s'
    values = {'vote_up': vote_up, 'question_id': question_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def vote_up_answer(cursor, answer_id):
    cursor.execute("""SELECT vote_number FROM answer WHERE id=%(answer_id)s""", {'answer_id': answer_id})
    vote_number = cursor.fetchone()
    vote_up = vote_number['vote_number']
    if vote_up is None:
        vote_up = 1
    else:
        vote_up += 1
    return vote_up


@file_handling.connection_handler
def update_vote_answer(cursor, answer_id):
    vote_up = vote_up_answer(answer_id)
    sql = 'UPDATE answer SET vote_number=%(vote_up)s WHERE id = %(answer_id)s'
    values = {'vote_up': vote_up, 'answer_id': answer_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def vote_down_answer(cursor, answer_id):
    cursor.execute("""SELECT vote_number FROM answer WHERE id=%(answer_id)s""", {'answer_id': answer_id})
    vote_number = cursor.fetchone()
    vote_down = vote_number['vote_number']
    if vote_down is None:
        vote_down = -1
    else:
        vote_down -= 1
    return vote_down


@file_handling.connection_handler
def update_lower_answer(cursor, answer_id):
    vote_up = vote_down_answer(answer_id)
    sql = 'UPDATE answer SET vote_number=%(vote_up)s WHERE id = %(answer_id)s'
    values = {'vote_up': vote_up, 'answer_id': answer_id}
    cursor.execute(sql, values)


@file_handling.connection_handler
def search_question(cursor, search_phrase):
    search_phrase = f'%{search_phrase.lower()}%'
    cursor.execute("""SELECT * FROM question WHERE LOWER(message) LIKE %(search_phrase)s OR LOWER(title) LIKE %(search_phrase)s""", {'search_phrase': search_phrase})
    search_result = cursor.fetchall()
    return search_result


@file_handling.connection_handler
def register_user(cursor, username, hash_password):
    cursor.execute("""INSERT INTO users(username, hash_password) VALUES (%(username)s, %(hash_password)s)""", {'username': username, 'hash_password': hash_password})


@file_handling.connection_handler
def get_hashed_password(cursor, username):
    cursor.execute("""SELECT hash_password FROM users WHERE username = %(username)s""", {'username': username})
    hashed_password = cursor.fetchone()
    return hashed_password['hash_password']


@file_handling.connection_handler
def username_exist(cursor, username):
    cursor.execute("""SELECT username from users""")
    list_of_users = [user['username'] for user in cursor.fetchall()]
    return username in list_of_users
