import sqlite3
from datetime import datetime

def issue_book(book_id, user):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM books WHERE book_id=?", (book_id,))
    result = cursor.fetchone()

    if result and result[0]>0:
        cursor.execute("INSERT INTO issued_books (book_id, user, issue_date) VALUES (?,?,?)",(book_id, user, datetime.now().strftime("%Y-%m-%d")))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id =?",(book_id,))
        conn.commit()
        print("Book Issued Successfully.")
    else:
        print("Book Not Available.")
    conn.close()
def return_book(issue_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT book_id FROM issued_books WHERE issue_id=?", (issue_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE books SET quantity = quantity+1 WHERE book_id=?",(result[0],))
        cursor.execute("UPDATE issued_books SET return_date = ? WHERE issue_id = ?",(datetime.now().strftime("%Y-%m-%d"), issue_id))
        conn.commit()
        print("Book returned Successfully.")
    else:
        print("Issue ID not found.")
    conn.close()

def view_issued_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM issued_books")
    records = cursor.fetchall()
    conn.close()
    return records
    

