import unittest
from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

        # Add books
        self.discovery = Book("The discovery of India", "Jawaharlal Nehru", "9780143031031", "1946")
        self.india_after = Book("India after Gandhi", "Ramachandra Guha", "9780330393908", "2007")
        self.gitanjali = Book("Gitanjali", "Rabindranath Tagore", "9789382563792", "1910")
        self.train = Book("Train to Pakistan", "Khushwant Singh", "9780143065883", "1956")
        self.god_small = Book("The God of small things", "Arundhati Roy", "9780679457312", "1997")

        for b in [self.discovery, self.india_after, self.gitanjali, self.train, self.god_small]:
            self.library.add_book(b)

        # Add members
        self.bhowmik = Member("Bhowmik", "MEM004")
        self.ramesh = Member("Ramesh Kumar", "MEM001")
        self.ranjith = Member("Ranjith", "MEM002")
        self.harsha = Member("Harsha", "MEM003")

        for m in [self.bhowmik, self.ramesh, self.ranjith, self.harsha]:
            self.library.register_member(m)

    def test_borrow_books_as_per_dataset(self):
        self.library.borrow_book("MEM004", "9780330393908")
        self.library.borrow_book("MEM001", "9780679457312")
        self.library.borrow_book("MEM002", "9789382563792")
        self.library.borrow_book("MEM002", "9780143031031")

        self.assertIn("9780330393908", self.bhowmik.borrowed_books)
        self.assertIn("9780679457312", self.ramesh.borrowed_books)
        self.assertIn("9789382563792", self.ranjith.borrowed_books)
        self.assertIn("9780143031031", self.ranjith.borrowed_books)
        self.assertEqual(len(self.harsha.borrowed_books), 0)

if __name__ == "__main__":
    unittest.main()
