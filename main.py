import login
import home
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('std_manage.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY,
                          username TEXT UNIQUE,
                          password TEXT,
                          role TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                          id TEXT PRIMARY KEY,
                          name TEXT,
                          gender TEXT,
                          age INTEGER,
                          mid INTEGER,
                          final INTEGER,
                          gpa INTEGER,
                          user_id INTEGER,
                          FOREIGN KEY(user_id) REFERENCES users(id)
                      )''')
    conn.commit()
    login.login()
