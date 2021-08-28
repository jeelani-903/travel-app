import sqlite3

sql_query = """
    CREATE TABLE IF NOT EXISTS auth(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    );
"""
sql_query1 = """
     CREATE TABLE IF NOT EXISTS details(
       id INTEGER PRIMARY KEY,
       fname TEXT,
       lname TEXT,
       email TEXT,
       mobile INTEGER
   );
"""


def execute_query(sql_query):
    with sqlite3.connect("auth.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result


def execute_query1(sql_query1):
    with sqlite3.connect("details.db") as conn:
        cur = conn.cursor()
        result1 = cur.execute(sql_query1)
        conn.commit()
    return result1


if __name__ == '__main__':
    execute_query(sql_query)
    execute_query1(sql_query1)
