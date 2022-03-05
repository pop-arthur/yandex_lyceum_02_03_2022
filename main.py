from datetime import datetime
from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db = input()

    global_init(db)
    session = create_session()

    for user in session.query(User).all():
        if user.address == "module_1":
            if "engineer" not in user.speciality and "engineer" not in user.position:
                print(user.id)

    session.close()


if __name__ == '__main__':
    main()
