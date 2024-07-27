import logging
from robot.api.deco import keyword
from home_work.hw_11.library.book import Book
from home_work.hw_11.library.reader import Reader

logger = logging.getLogger(__name__)


@keyword
def create_book(book_name, author, num_pages, isbn):
    return Book(book_name=book_name, author=author, num_pages=num_pages, isbn=isbn)


@keyword
def create_reader(name):
    return Reader(name)


@keyword
def reserve_book(reader, book):
    return reader.reserve_book(book)


@keyword
def cancel_reserve(reader, book):
    return reader.cancel_reserve(book)


@keyword
def get_book(reader, book):
    return reader.get_book(book)


@keyword
def return_book(reader, book):
    return reader.return_book(book)


@keyword
def log_message(message):
    logger.info(message)
