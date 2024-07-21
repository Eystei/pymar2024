import pytest
import logging
from home_work.hw_11.library.reader import Reader
from home_work.hw_11.library.book import Book

logger = logging.getLogger(__name__)


@pytest.fixture
def book():
    return Book(
        book_name="Harry Potter and the Goblet of Fire",
        author="J. K. Rowling",
        num_pages=636,
        isbn="0747550794")


@pytest.fixture
def reader():
    return Reader(name="Angela")


def test_01_reserve_book_success(book, reader):
    logger.info("Test 1: successful reservation of a book")
    assert reader.reserve_book(book)


def test_02_reserve_book_failure_already_reserved(book, reader):
    logger.info("Test 2: attempt to reserve a book that is already reserved by someone else")
    book.reserve("Pikachu")
    result = reader.reserve_book(book)
    assert not result


def test_03_cancel_reserve_success(book, reader):
    logger.info("Test 3: successful cancellation of a reservation")
    reader.reserve_book(book)
    result = reader.cancel_reserve(book)
    assert result
    assert not book.reserved
    assert book.reserved_by is None


def test_04_cancel_reserve_failure_not_reserved(book, reader):
    logger.info("Test 4: attempt to cancel a reservation on a book that is not reserved")
    result = reader.cancel_reserve(book)
    assert not result


def test_05_get_book_success(book, reader):
    logger.info("Test 5: successful acquisition of a book")
    reader.reserve_book(book)
    result = reader.get_book(book)
    assert result
    assert book in reader.lib_books


def test_06_return_book_success(book, reader):
    logger.info("Test 6: successful return of a book")
    reader.reserve_book(book)
    reader.get_book(book)
    result = reader.return_book(book)
    assert result
    assert book not in reader.lib_books
