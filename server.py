from flask import Flask, render_template, redirect, request, url_for
import data_manager
import util

app = Flask(__name__)

@app.route('/')
def list_page():
    questions = data_manager.question_list()
    return render_template('list.html', questions = questions)

@app.route('/add', methods=['POST', 'GET'])
def add_question():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        title=request.form['title']
        print (title
        return
    #request.form


@app.route('/question/<question_id>')
def display_question(question_id):
    question = util.choose_question(question_id)
    answers = util.choose_answer(question_id)
    return render_template('question.html', question=question, answers=answers)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )