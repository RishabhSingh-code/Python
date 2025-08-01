# 📚 Library Management System (Python + SQLite)

A command-line based Library Management System built in Python using SQLite.  
Supports user login, role-based access (admin/user), book management, and issue/return functionality.


<img width="1212" height="770" alt="Screenshot 2025-08-02 013219" src="https://github.com/user-attachments/assets/1fb564ae-b6dc-4f19-ac68-ec6ab136d60c" />
<img width="1366" height="723" alt="Screenshot 2025-08-02 013241" src="https://github.com/user-attachments/assets/2824037a-8742-4525-851b-e42eeb16751a" />
<img width="1363" height="652" alt="Screenshot 2025-08-02 013322" src="https://github.com/user-attachments/assets/a3874a40-2f4f-40de-ac78-1ac22fd9f254" />
<img width="1358" height="748" alt="Screenshot 2025-08-02 013352" src="https://github.com/user-attachments/assets/7f6d0c6d-fa9e-46ee-8486-fd5e108611ff" />
<img width="1176" height="652" alt="Screenshot 2025-08-02 013419" src="https://github.com/user-attachments/assets/d6bc3125-b6a0-46ff-acc4-ed081698fad5" />


---

## 🚀 Features

### 👨‍💼 Admin
- Add new books
- Delete books
- View all books
- Issue books to users
- Return books
- View all issued books

### 👨‍🎓 User
- View available books

---

## 🧱 Tech Stack

- **Language**: Python 3
- **Database**: SQLite (no setup required)
- **Interface**: CLI (command-line interface)

---
library_management_system/
├── book.py # Book management (add, view, delete)
├── issued_books.py # Book issue and return
├── database.py # Database setup (tables)
├── main.py # Main CLI interface
└── library.db # Auto-generated SQLite database file


---

## ⚙️ How to Run

1. Clone the repo or download the files:

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

Run the program:

bash
Copy code
python main.py

 Requirements
Python 3.x

No external libraries required (uses built-in sqlite3 and datetime)



