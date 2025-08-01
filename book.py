# book.py

import sqlite3

def add_book(title, author, quantity):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title, author, quantity))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id=?", (book_id,))
    conn.commit()
    conn.close()
