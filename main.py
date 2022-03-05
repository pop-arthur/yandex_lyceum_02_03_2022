from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/mars_explorer.db")
    session = create_session()

    user = User()
    user.surname = "Бледный"
    user.name = "Кирилл"
    user.age = 24
    user.position = "местный дед инсайд"
    user.speciality = "солист группы Пошлая Моль"
    user.address = "Москва"
    user.email = "kirill777@mail.ru"
    session.add(user)


    user = User()
    user.surname = "Del Ray"
    user.name = "Lana"
    user.age = 35
    user.position = "cooker"
    user.speciality = "singer"
    user.address = "America"
    user.email = "lanochka@gmail.com"
    session.add(user)

    user = User()
    user.surname = "Popov"
    user.name = "Arthur"
    user.age = 17
    user.position = "DJ"
    user.speciality = "perfect music player"
    user.address = "101 alfa"
    user.email = "popov.art@hotmail.com"
    session.add(user)

    session.commit()


if __name__ == '__main__':
    main()
