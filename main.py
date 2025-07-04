
import sqlite3
import sql
import random
from flask import Flask, render_template
import time

actual_answer = 0
right_answer = 0
start_time = 0

app = Flask(__name__)

@app.route("/starts_questions")
def start():
    global actual_answer
    global right_answer
    global start_time
    questions = sql.get_all_questions()

    if actual_answer >= len(questions):
        actual_answer = 0
        time_ = time.time() - start_time
        result = right_answer
        right_answer = 0  # обнуляємо після збереження
        return render_template('index3.html', right_question=result, time=round(time_, 2))

    if actual_answer ==0 :
        start_time = time.time()
    # Витягуємо одне питання
    question_text = questions[actual_answer][1]
    image_path = questions[actual_answer][2]
    answer_1 = questions[actual_answer][3]
    answer_2 = questions[actual_answer][4]
    answer_3 = questions[actual_answer][5]
    answer_4 = questions[actual_answer][6]

    # Список відповідей
    answer_options = [answer_1, answer_2, answer_3, answer_4]
    random.shuffle(answer_options)
    for i in range(4):
        if answer_options[i]==answer_1:
            answer_options.append('/right_question')
        else:
            answer_options.append('/starts_questions')


    actual_answer += 1

    return render_template(
        "index2.html",
        question=question_text,
        img=image_path,
        a=answer_options[0],
        b=answer_options[1],
        c=answer_options[2],
        d=answer_options[3],
        rel_a = answer_options[4],
        rel_b = answer_options[5],
        rel_c = answer_options[6],
        rel_d = answer_options[7],
    )
@app.route("/right_question")
def start_():
    global actual_answer, right_answer, start_time
    questions = sql.get_all_questions()

    if actual_answer >= len(questions):
        time_ = time.time() - start_time
        result = right_answer
        actual_answer = 0
        right_answer = 0
        return render_template('index3.html', right_question=result, time=round(time_, 2))

    if actual_answer == 0:
        start_time = time.time()

    # Витягуємо питання
    question = questions[actual_answer]
    question_text = question[1]
    image_path = question[2]
    answer_1 = question[3]
    answer_2 = question[4]
    answer_3 = question[5]
    answer_4 = question[6]

    # Перемішуємо
    answer_options = [answer_1, answer_2, answer_3, answer_4]
    random.shuffle(answer_options)

    rels = ["/right_question" if a == answer_1 else "/starts_questions" for a in answer_options]

    actual_answer += 1
    right_answer += 1

    return render_template(
        "index2.html",
        question=question_text,
        img=image_path,
        a=answer_options[0],
        b=answer_options[1],
        c=answer_options[2],
        d=answer_options[3],
        rel_a=rels[0],
        rel_b=rels[1],
        rel_c=rels[2],
        rel_d=rels[3],
    )

@app.route("/")
def start1():
    return render_template("index.html")

@app.route('/finish')
def finish():
    return render_template('index3.html')

correct = [("")]
uncorrect = [""]

app.run()






