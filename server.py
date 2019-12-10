from flask import Flask, render_template, redirect, request, url_for
import data_manager
import util

app = Flask(__name__)


@app.route('/')
def list_page():
    questions = data_manager.all_question_list()
    return render_template('list.html', questions = questions)


@app.route('/add', methods=['POST', 'GET'])
def add_question():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        data_manager.export_to_file_question(title, message)
        return redirect(url_for('list_page'))


@app.route('/question/<int:question_id>/new_answer', methods=['POST', 'GET'])
def add_answer(question_id):
    if request.method == 'GET':
        return render_template('new_answer.html', question_id=question_id)
    elif request.method == 'POST':
        message = request.form['message']
        question_id = request.form['question_id']
        data_manager.export_to_file_answer(message, question_id)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<int:question_id>')
def display_question(question_id):
    question = data_manager.choose_question(question_id)
    answers = data_manager.choose_answer(question_id)
    return render_template('question.html', question=question, answers=answers, question_id=question_id)


@app.route('/question/<int:question_id>/update', methods=['GET', 'POST'])
def update_question(question_id):
    question_choose = data_manager.choose_question(question_id)
    if request.method == 'GET':
        return render_template('update.html', question_id=question_id, question_choose=question_choose)
    elif request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        question = data_manager.update_question(question_id, title, message)
        return redirect(url_for('display_question', question_id=question_id, question=question))


@app.route('/answer/<answer_id>/')
def display_answer(answer_id):
    answer = data_manager.show_answer(answer_id)
    return render_template('answer.html', answer=answer, answer_id=answer_id)


@app.route('/answer/<answer_id>/edit/', methods=['GET', 'POST'])
def edit_answer(answer_id):
    answer = data_manager.show_answer(answer_id)
    if request.method == 'GET':
        return render_template('edit.html', answer_id=answer_id, answer=answer)
    elif request.method == 'POST':
        message = request.form['message']
        answer = data_manager.edit_answer(answer_id, message)
        return redirect(url_for('display_answer', answer_id=answer_id, answer=answer))


@app.route('/answer/<answer_id>/new-comment')
def add_comment_to_answer(answer_id):
    pass


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )