class Member:
    """Represents a library member"""

    MAX_BORROW_LIMIT = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book if under limit"""
        if len(self.borrowed_books) >= Member.MAX_BORROW_LIMIT:
            return False, "Borrow limit reached (5 books max)"
        if not book.available:
            return False, "Book is not available"

        success, message = book.check_out(self.member_id)
        if success:
            self.borrowed_books.append(book.isbn)
        return success, message

    def return_book(self, book):
        """Return a borrowed book"""
        if book.isbn not in self.borrowed_books:
            return False, "This member did not borrow this book"

        success, message = book.return_book()
        if success:
            self.borrowed_books.remove(book.isbn)
        return success, message

    def to_dict(self):
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data['name'], data['member_id'])
        member.borrowed_books = data.get('borrowed_books', [])
        return member

    def __str__(self):
        return f"{self.name} ({self.member_id}) - Borrowed: {len(self.borrowed_books)}"
