from datetime import date
import sqlite3

from flask.templating import render_template


def auth_execute(sql_query):
    with sqlite3.connect("auth.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result


def create_user(name, email, password):
    sql_query = f''' INSERT INTO auth(name, email, password) VALUES("{name}", "{email}", "{password}")'''

    try:
        auth_execute(sql_query)
        return "Your Account has been Registered"

    except:
        return "Account Already Exists"


def login_validation(email, password):
    sql_query = f''' SELECT password FROM auth WHERE email = "{email}"'''
    result = auth_execute(sql_query).fetchall()[0][0]
    print(result, "|", password)
    if result == password:
        return True
    return False


def get_all_users():
    sql_query = f''' SELECT * FROM auth '''
    result = auth_execute(sql_query).fetchall()
    print(result)
