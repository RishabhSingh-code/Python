from database import connect
from book import add_book, view_books, delete_book
from issued_books import issue_book, return_book, view_issued_books

connect()
while True:
    print("---Library Management---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Issued Books")
    print("7. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        title = input("Book Title: ")
        author = input("Author: ")
        qty = int(input("Quantity: "))
        add_book(title, author, qty)
    
    elif choice == 2:
        for book in view_books():
            print(book)
    
    elif choice == 3:
        book_id = int(input("Enter Book ID to Delete: "))
        delete_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to Issue: "))
        user = input("User Name: ")
        issue_book(book_id, user)

    elif choice == 5:
        issue_id = int(input("ENter Issue ID to Return: "))
        return_book(issue_id)

    elif choice == 6:
        for rec in view_issued_books():
            print(rec)
    
    elif choice == 7:
        break

    else:
        print("Invalid Choice O_O")
