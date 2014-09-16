class Book(object):
    """Class for creating individual book objects.
    
    The defaults for bookcase and shelf are empty strings because
    a book can be created without placing it on a bookcase shelf.
    
    The default for the has_read setting is False because it is assumed
    that books are being cataloged as they are gotten.

    Methods for the Book class reflect things people might do with books:
    - Mark a book as read.
    - Mark a book as unread.
    - Place a book on a bookcase shelf.
    - Get a description of the book.
    """

    bookcase = ""
    shelf = ""
    has_read = False
    
    def __init__(self, title, author, pub_date):
        self.title = title
        self.author = author
        self.pub_date = pub_date

    def book_description(self):
        print "Title: " + self.title
        print "Author: " + self.author
        print "Publication Date: " + self.pub_date

        if self.has_read == True:
            print "Have Read: Yes"
        else:
            print "Have Read: No"

    def mark_as_read(self):
        self.has_read = True

    def mark_as_unread(self):
        self.has_read = False

    def place_on_shelf(self, bookcase, shelf):
        self.bookcase = bookcase
        self.shelf = shelf

class Bookcase(object):
    """Class for creating individual bookcase objects.

    Main focus is to give a bookcase an id and assign it shelves.

    Not sure if I actually need this class, or if just Shelf objects would be enough.
    """

    bookcase_shelves = []

    def __init__(self, bookcase_id):
        self.bookcase_id = bookcase_id

    def add_shelf(self, shelf):
        if shelf not in self.bookcase_shelves:
            self.bookcase_shelves.append(shelf)
            print shelf + " added."
        else:
            print "Shelf in Bookcase already."

    def remove_shelf(self, shelf):
        self.bookcase_shelves.remove(shelf)

class Bookshelf(object):
    """Class for creating individual bookshelf objects.

    Main focus is to give a bookshelf an id and assign it to a bookcase.
    """

    def __init__(self, shelf_id):
        self.shelf_id = shelf_id


