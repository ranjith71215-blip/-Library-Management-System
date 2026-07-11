# library_system/__init__.py

"""
Library Management System Package
---------------------------------
This package provides classes and functionality for managing a library system:
- Book: Represents a book in the library
- Member: Represents a library member
- Library: Manages books, members, borrowing, and returning
"""
   
from .book import Book
from .member import Member
from .library import Library

__all__ = ["Book", "Member", "Library"]
