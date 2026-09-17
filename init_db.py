import sqlite3 as sql

conn=sql.connect("database.db")
cursor=conn.cursor()
cursor.execte("""
              CREATE TABLE IF NOT EXISTS students(
                  id INTERGER PRIMSRY KEY,
                  naem TEXT NOT NULL
              )
              
              """)
conn.commit()
conn.close()