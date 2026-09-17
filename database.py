import sqlite3 as sql


def get_db():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
    return conn
def get_all_student():
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    conn.close()
    return rows
def get_student_by_id(id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?",
                   (id,))
    student=cursor.fetchone()
    conn.close()
    return student

def post_student(student):
    conn=get_db()
    cursor=conn.cursor()
    id=student["id"]
    name=student["name"]
    cursor.execute("INSERT INTO students VALUES(?,?) ",
                   (id, name))
    conn.commit()
    conn.close()
def update_student(id, name):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("UPDATE students SET name=? WHERE id=?",
                   (name, id))
    conn.commit()
    conn.close()
def delete_student(id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("DELETE from students WHERE id=?",
                   (id,))
    conn.commit()
    conn.close()