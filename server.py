from flask import Flask, render_template, redirect, request, url_for
import data_manager
import util
import file_handling

app = Flask(__name__)


@app.route('/')
def list_page():
    questions = data_manager.question_list()
    return render_template('list.html', questions = questions)


@app.route('/add', methods=['POST', 'GET'])
def add_question():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        list_dict = util.add_dict_to_list_question(title, message)
        file_handling.export_file(list_dict)
        return redirect(url_for('list_page'))


@app.route('/question/<question_id>/new_answer', methods=['POST', 'GET'])
def add_answer(question_id):
    if request.method == 'GET':
        return render_template('new_answer.html', question_id=question_id)
    elif request.method == 'POST':
        message = request.form['message']
        question_id = request.form['question_id']
        list_dict = util.add_dict_to_list_answer(message, question_id)
        file_handling.export_ans(list_dict)
        return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>')
def display_question(question_id):
    question = util.choose_question(question_id)
    answers = util.choose_answer(question_id)
    return render_template('question.html', question=question, answers=answers, question_id=question_id)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )