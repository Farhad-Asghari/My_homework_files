# Creat a class Library with attributes name and books (a list of Book object). Provide methods to add and remove books.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"the book {book.title} is added in {self.name}")
        
    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"the book {book_title} is deleted from {self.name}")
                return print(f"the book {book_title} is not found in {self.name}")
            
library1 = Library("General library")
book1 = Book("freindship", "Garcia", 100)
book2 = Book("darkness", "Jack", 150)
library1.add_book(book1)
library1.add_book(book2)
library1.remove_book("freindship")

                