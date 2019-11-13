from flask import Flask, render_template, redirect, request
import data_manager

app = Flask(__name__)

@app.route('/')
def list_page():
    questions = data_manager.question_list()
    return render_template('list.html', questions = questions)

# @app.route('/add_question', methods=['GET'])
# def add_question():
#     #request.form
#     return redirect('/add')
#
# @app.route('/question/<question_id>')
# def display_question():
#     questions = data_manager.question_list()
#     return render_template('question.html', questions = questions )

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )