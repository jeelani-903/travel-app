from createdb import execute_query, execute_query1
from datetime import date
import sqlite3

from flask.templating import render_template


def auth_execute(sql_query):
    with sqlite3.connect("auth.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result


def auth_execute1(sql_query1):
    with sqlite3.connect("details.db") as conn:
        cur = conn.cursor()
        result1 = cur.execute(sql_query1)
        conn.commit()
    return result1


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


def add_new_lname(lname):
    sql_query1 = "INSERT INTO details(lname) VALUES('%s')" % (lname)
    execute_query1(sql_query1)
    print("sql_query1")


def add_new_fname(fname):
    sql_query1 = "INSERT INTO details(fname) VALUES('%s')" % (fname)
    execute_query1(sql_query1)
    print("sql_query1")


def add_new_email(email):
    sql_query1 = "INSERT INTO details(email) VALUES('%s')" % (email)
    execute_query1(sql_query1)
    print("sql_query1")


def add_new_mobile(mobile):
    sql_query1 = "INSERT INTO details(mobile) VALUES(%s)" % (mobile)
    execute_query1(sql_query1)
    print("sql_query1")


def get_lname(lname):
    sql_query1 = "SELECT * FROM details "
    lname = auth_execute1(sql_query1)
    return lname


def get_fname(fname):
    sql_query1 = "SELECT * FROM details "
    fname = auth_execute1(sql_query1)
    return fname


def get_email(email):
    sql_query1 = "SELECT * FROM details "
    email = auth_execute1(sql_query1)
    return email


def get_mobile(mobile):
    sql_query1 = "SELECT * FROM details "
    mobile = auth_execute1(sql_query1)
    return mobile
