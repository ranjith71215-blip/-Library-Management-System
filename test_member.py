import unittest
from library_system.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.bhowmik = Member("Bhowmik", "MEM004")
        self.ramesh = Member("Ramesh Kumar", "MEM001")
        self.ranjith = Member("Ranjith", "MEM002")
        self.harsha = Member("Harsha", "MEM003")

    def test_bhowmik_books(self):
        self.bhowmik.borrowed_books.append("9780330393908")
        self.assertIn("9780330393908", self.bhowmik.borrowed_books)

    def test_ramesh_books(self):
        self.ramesh.borrowed_books.append("9780679457312")
        self.assertIn("9780679457312", self.ramesh.borrowed_books)

    def test_ranjith_books(self):
        self.ranjith.borrowed_books.extend(["9789382563792", "9780143031031"])
        self.assertEqual(len(self.ranjith.borrowed_books), 2)

    def test_harsha_books(self):
        self.assertEqual(len(self.harsha.borrowed_books), 0)

if __name__ == "__main__":
    unittest.main()
