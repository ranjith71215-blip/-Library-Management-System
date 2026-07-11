import unittest
from library_system.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.discovery = Book("The discovery of India", "Jawaharlal Nehru", "9780143031031", "1946")
        self.india_after = Book("India after Gandhi", "Ramachandra Guha", "9780330393908", "2007")
        self.gitanjali = Book("Gitanjali", "Rabindranath Tagore", "9789382563792", "1910")
        self.train = Book("Train to Pakistan", "Khushwant Singh", "9780143065883", "1956")
        self.god_small = Book("The God of small things", "Arundhati Roy", "9780679457312", "1997")

    def test_titles_and_authors(self):
        self.assertEqual(self.discovery.author, "Jawaharlal Nehru")
        self.assertEqual(self.india_after.author, "Ramachandra Guha")
        self.assertEqual(self.gitanjali.author, "Rabindranath Tagore")
        self.assertEqual(self.train.author, "Khushwant Singh")
        self.assertEqual(self.god_small.author, "Arundhati Roy")

    def test_isbn_values(self):
        self.assertEqual(self.discovery.isbn, "9780143031031")
        self.assertEqual(self.india_after.isbn, "9780330393908")
        self.assertEqual(self.gitanjali.isbn, "9789382563792")
        self.assertEqual(self.train.isbn, "9780143065883")
        self.assertEqual(self.god_small.isbn, "9780679457312")

    def test_borrow_and_return(self):
        self.discovery.check_out("MEM002")
        self.assertFalse(self.discovery.available)
        self.assertEqual(self.discovery.borrowed_by, "MEM002")

        success, msg = self.discovery.return_book()
        self.assertTrue(success)
        self.assertTrue(self.discovery.available)
        self.assertIsNone(self.discovery.borrowed_by)

if __name__ == "__main__":
    unittest.main()

