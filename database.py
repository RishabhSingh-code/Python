import sqlite3
def connect():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        quantity INTEGER
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issued_books (
        issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user TEXT,
        issue_date TEXT,
        return_date TEXT
    )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()  
