
---

# Library Management System

### Author  
Ranjith Kumar G  

---

## Project Description  

The Library Management System is a Python-based console application that helps manage books and members in a small library. Users can add books, register members, borrow and return books, and view borrowed records. Data is stored in JSON files for persistence, and unit tests are included to validate the functionality.  

This project demonstrates Python fundamentals such as:  
* Classes and Objects (OOP)  
* File Handling (`JSON`)  
* Conditional Statements (`if`, `elif`, `else`)  
* Loops (`for`, `while`)  
* Input Validation  
* Modular Programming  
* Unit Testing (`unittest`)  

---

## Features  

| Feature            | Description                                      |
|--------------------|--------------------------------------------------|
| Add Book           | Add new books with title, author, ISBN, year     |
| Register Member    | Register new library members                     |
| Borrow Book        | Borrow a book by ISBN and member ID              |
| Return Book        | Return borrowed books                            |
| View Members       | See all registered members and their borrowed books |
| View Books         | See all books and their availability status      |

---

## Project Structure  

```text
week5-library-system/
│── library_system/
│ ├── __init__.py
│ ├── book.py
│ ├── member.py
│ ├── library.py
│ └── main.py
│── data/
│ ├── books.json
│ ├── members.json
│ └── backup/
│── tests/
│ ├── test_book.py
│ ├── test_member.py
│ └── test_library.py
│── requirements.txt
│── README.md
└── .gitignore
```

---

## How to Run  

From the project root (`Week-5`), run the main program:  

```bash
python -m library_system.main
```

This will start the interactive menu for managing books and members.  

---

## Sample Menu  

```text
========================================
           LIBRARY MAIN MENU
========================================
1. Add New Book
2. Register New Member
3. Borrow Book
4. Return Book
5. Search Books
6. View All Books
7. View All Members
8. View Overdue Books
9. Save & Exit
10. Create Manual Backup
0. Exit Without Saving
Enter your choice:
```

---

## Sample Data  

### books.json  
```json
[
    {"title": "The discovery of India", "author": "Jawaharlal Nehru", "isbn": "9780143031031", "year": "1946"},
    {"title": "India after Gandhi", "author": "Ramachandra Guha", "isbn": "9780330393908", "year": "2007"},
    {"title": "Gitanjali", "author": "Rabindranath Tagore", "isbn": "9789382563792", "year": "1910"},
    {"title": "Train to Pakistan", "author": "Khushwant Singh", "isbn": "9780143065883", "year": "1956"},
    {"title": "The God of small things", "author": "Arundhati Roy", "isbn": "9780679457312", "year": "1997"}
]
```

### members.json  
```json
[
    {"name": "Ramesh Kumar", "member_id": "MEM001", "borrowed_books": ["9780679457312"]},
    {"name": "Ranjith", "member_id": "MEM002", "borrowed_books": ["9789382563792", "9780143031031"]},
    {"name": "Harsha", "member_id": "MEM003", "borrowed_books": []},
    {"name": "Bhowmik", "member_id": "MEM004", "borrowed_books": ["9780330393908"]}
]
```

---

## How to Run Tests  

Run all tests from the project root:  

```bash
python -m unittest discover tests
```

Or run a single test file:  

```bash
python -m unittest tests.test_book
```

---

## Learning Outcomes  

By completing this project, you will learn how to:  
* Build classes for books, members, and library management  
* Handle JSON files for persistent storage  
* Implement borrowing and returning logic  
* Validate inputs (ISBN, member IDs)  
* Write unit tests for different modules  
* Organize code into a modular package  

---

## Technologies Used  

* Python 3  
* JSON  
* unittest  
* Visual Studio Code  

---

## Conclusion  

This Library Management System is a simple but practical Python project that demonstrates object-oriented programming, file handling, and testing. It provides a foundation for building more advanced systems such as database-driven or web-based library applications.  

---

