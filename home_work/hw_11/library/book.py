import logging

logger = logging.getLogger(__name__)


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = False
        self.reserved_by = None
        self.reader_name = None

    def reserve(self, reader_name):
        if self.reserved:
            logger.info(f"Sorry, this book is reserved by {self.reserved_by}.")
            return False
        elif self.reader_name:
            logger.info(f"Sorry, this book is currently being read by {self.reader_name}.")
            return False
        else:
            self.reserved = True
            self.reserved_by = reader_name
            logger.info("Good choice! Book reserved.")
            return True

    def cancel_reserve(self, reader_name):
        if reader_name != self.reserved_by:
            logger.info("You didn't reserve this book.")
            return False
        else:
            self.reserved = False
            self.reserved_by = None
            logger.info("Book reservation cancelled.")
            return True

    def get_book(self, reader_name):
        if self.reader_name:
            logger.warning(f"This book is currently being read by {self.reader_name}.")
            return False
        elif self.reserved and self.reserved_by != reader_name:
            logger.info(f"Oops. This book is reserved by {self.reserved_by}.")
            return False
        else:
            self.reader_name = reader_name
            self.reserved = False
            self.reserved_by = None
            logger.info("Good choice! Enjoy it!")
            return True

    def return_book(self, reader_name):
        if reader_name == self.reader_name:
            self.reader_name = None
            logger.info("Thanks. Book has been returned.")
            return True
        else:
            logger.info("You didn't get this book.")
            return False
