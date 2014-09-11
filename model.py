class Book(object):
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
