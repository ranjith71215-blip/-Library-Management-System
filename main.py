from .library import Library
from .book import Book
from .member import Member

def main():
    library = Library()
    library.load_data()

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View All Members")
        print("8. View Overdue Books")
        print("9. Save & Exit")
        print("10. Create Manual Backup")
        print("0. Exit Without Saving")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year: ")
            library.add_book(Book(title, author, isbn, year))
            print("Book added successfully.")

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            library.register_member(Member(name, member_id))
            print("Member registered successfully.")

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            success, msg = library.borrow_book(member_id, isbn)
            print(msg)

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            success, msg = library.return_book(member_id, isbn)
            print(msg)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            results = library.find_book(keyword, by="title")
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == "6":
            for book in library.books.values():
                print(book)

        elif choice == "7":
            for member in library.members.values():
                print(member)

        elif choice == "8":
            overdue = library.overdue_books()
            if overdue:
                for book in overdue:
                    print(f"{book} - Overdue by {book.days_overdue()} days")
            else:
                print("No overdue books.")

        elif choice == "9":
            success, msg = library.save_data()
            print(msg)
            break

        elif choice == "10":
            success, msg = library.backup_data()
            print(msg)

        elif choice == "0":
            print("Exiting without saving...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
