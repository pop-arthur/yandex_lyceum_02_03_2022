from datetime import datetime
from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = create_session()

    jobs = db_sess.query(Jobs).all()
    answer = [[] for _ in range(len(jobs))]
    for i in range(len(jobs)):
        answer[i].append([0 for _ in range(6)])
        answer[i][0] = i + 1
        answer[i][1] = jobs[i].job
        answer[i][2] = db_sess.query(User).filter(User.id == jobs[i].team_leader).first().name

        if jobs[i].start_date and jobs[i].end_date:
            answer[i][3] = jobs[i].end_date - jobs[i].start_date
        else:
            answer[i][3] = "None"

        answer[i][4] = jobs[i].collaborators
        answer[i][5] = "Is finished" if jobs[i].is_finished else "Is not finished"

    db_sess.close()
    return render_template("index.html", answer=answer)


def main():
    global_init("db/mars_explorer.db")
    db_sess = create_session()

    db_sess.close()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
