import psycopg2

from app.schemas import User, SignUp


def get_all_user():
    try:
        conn = psycopg2.connect(dbname="kino_go", host="127.0.0.1", user="postgres", password="123")
        curser = conn.cursor()

        sql = """
        SELECT * from users
        """

        curser.execute(sql)
        all_users = curser.fetchall()
        return all_users
    except BaseException as error:
        raise error
    finally:
        curser.close()
        conn.close()


def check_email(email: str):
    for i in get_all_user():
        if email in i:
            return False
        return True


def add_user_for_db(user: User):
    try:
        conn = psycopg2.connect(dbname="kino_go", host="127.0.0.1", user="postgres", password="123")
        curser = conn.cursor()

        sql = """
        INSERT INTO users(email, password, first_name, last_name, age)
        VALUES(%s, %s, %s, %s, %s)
        """
        user_data = tuple([i for i in user.dict().values()])

        curser.execute(sql, user_data)

        conn.commit()
        answer = "You registered"
        return answer
    except BaseException as error:
        raise error
    finally:
        curser.close()
        conn.close()


def check_user(user: SignUp):
    for i in get_all_user():
        if i[1] == user.email:
            return i


def check_password_signup(firs_password, second_password: str):
    if firs_password == second_password:
        return True
    return False
