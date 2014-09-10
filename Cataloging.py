import datetime

class Bookcase(object):
    def __init__(self, shelves, bookcase_id, books):
        self.bookcase_id = bookcase_id
        self.shelves = shelves
        self.books = books
    
    def list_books(bookcase):
        pass


class BookShelf(object):
    def __init__(self, shelf_id, bookcase_id, books):
        self.shelf_id = shelf_id
        self.bookcase_id = bookcase_id
        self.books = books

    def list_books(bookcase, shelf):
        pass


class Book(object):
    def __init__(self, title, author, pub_date, has_read):
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.has_read = has_read
        # self.date_added = datetime.datetime.now -add datetime of cataloging instance

    def book_description(self):
        print "Title: " + self.title
        print "Author: " + self.author
        print "Publication Date: " + self.pub_date
        # print "Located on Shelf " + self.shelf_id + " of Bookcase " + self.bookcase_id

        if self.has_read == True:
            print "Have Read: Yes"
        else:
            print "Have Read: No"

        # print "This book was added to your library on " + self.date_added

book1 = Book("Book Title", "Book Author", "Pub Date", False)
book2 = Book("Servants of the Storm", "Deliah Dawson", "2014", False)
book3 = Book("Graveyard Book", "Neil Gaiman", "2012", True)
book4 = Book("A Year and a Day", "Sara Harvey", "2009", True)

books = [book1, book2, book3, book4]
for book in books:
    book.book_description()
    print "\n"