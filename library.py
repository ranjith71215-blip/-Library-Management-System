import json
import os
import shutil
from .book import Book
from .member import Member

class Library:
    """Manages books and members"""

    def __init__(self):
        self.books = {}
        self.members = {}

    # --- Book Management ---
    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        return self.books.pop(isbn, None)

    def find_book(self, keyword, by="title"):
        results = []
        for book in self.books.values():
            if keyword.lower() in str(getattr(book, by, "")).lower():
                results.append(book)
        return results

    # --- Member Management ---
    def register_member(self, member):
        self.members[member.member_id] = member

    def find_member(self, member_id):
        return self.members.get(member_id)

    # --- Borrow/Return ---
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)
        if not member or not book:
            return False, "Member or Book not found"
        return member.borrow_book(book)

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)
        if not member or not book:
            return False, "Member or Book not found"
        return member.return_book(book)

    def overdue_books(self):
        return [book for book in self.books.values() if book.is_overdue()]

    # --- File Operations ---
    def save_data(self, books_file="data/books.json", members_file="data/members.json"):
        try:
            with open(books_file, "w") as bf:
                json.dump([b.to_dict() for b in self.books.values()], bf, indent=4)
            with open(members_file, "w") as mf:
                json.dump([m.to_dict() for m in self.members.values()], mf, indent=4)

            # Create backup after saving
            self.backup_data(books_file, members_file)

            return True, "Data saved and backup created successfully"
        except Exception as e:
            return False, f"Error saving data: {e}"

    def load_data(self, books_file="data/books.json", members_file="data/members.json"):
        try:
            if os.path.exists(books_file):
                with open(books_file, "r") as bf:
                    books_data = json.load(bf)
                    for b in books_data:
                        book = Book.from_dict(b)
                        self.books[book.isbn] = book
            if os.path.exists(members_file):
                with open(members_file, "r") as mf:
                    members_data = json.load(mf)
                    for m in members_data:
                        member = Member.from_dict(m)
                        self.members[member.member_id] = member
            return True, "Data loaded successfully"
        except Exception as e:
            return False, f"Error loading data: {e}"

    def backup_data(self, books_file="data/books.json", members_file="data/members.json", backup_dir="backup"):
        """Create backup copies of books and members JSON files (no dates in filenames)"""
        try:
            os.makedirs(backup_dir, exist_ok=True)

            books_backup = os.path.join(backup_dir, "books_backup.json")
            members_backup = os.path.join(backup_dir, "members_backup.json")

            shutil.copy2(books_file, books_backup)
            shutil.copy2(members_file, members_backup)

            return True, f"Backup created: {books_backup}, {members_backup}"
        except Exception as e:
            return False, f"Error creating backup: {e}"
