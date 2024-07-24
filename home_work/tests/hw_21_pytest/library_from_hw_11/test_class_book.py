import pytest
import logging
from home_work.hw_11.library.book import Book

logger = logging.getLogger(__name__)


@pytest.fixture
def book():
    return Book(
        book_name="Harry Potter Philosopher's Stone",
        author="J. K. Rowling",
        num_pages=636,
        isbn="0747550794")


def test_reserve_not_reserved(book):
    logger.info('Test 1: reserving a book that is not currently reserved')
    result = book.reserve("Pikachu")
    assert result
    assert book.reserved
    assert book.reserved_by == "Pikachu"


def test_reserve_already_reserved(book):
    logger.info('Test 2: attempting to reserve a book that is already reserved')
    book.reserve("Ash")
    result = book.reserve("Pikachu")
    assert not result


def test_reserve_while_booked(book):
    logger.info('Test 3: attempting to reserve a book that is already checked out')
    book.get_book("Ash")
    result = book.reserve("Pikachu")
    assert not result


def test_cancel_reservation_success(book):
    logger.info('Test 4: successfully cancelling a reservation')
    book.reserve("Pikachu")
    result = book.cancel_reserve("Pikachu")
    assert result
    assert not book.reserved
    assert book.reserved_by is None


def test_cancel_reservation_wrong_user(book):
    logger.info('Test 5: attempting to cancel a reservation by someone other')
    book.reserve("Ash")
    result = book.cancel_reserve("Pikachu")
    assert not result


def test_get_book_success(book):
    logger.info('Test 6: successfully getting a book after reserving it')
    book.reserve("Pikachu")
    result = book.get_book("Pikachu")
    assert result
    assert book.reader_name == "Pikachu"


def test_get_book_reserved_by_another(book):
    logger.info('Test 7: attempting to get a book that is reserved by another user')
    book.reserve("Ash")
    result = book.get_book("Pikachu")
    assert not result


def test_return_book_success(book):
    logger.info('Test 8: successfully returning a book that was checked out')
    book.get_book("Pikachu")
    result = book.return_book("Pikachu")
    assert result
    assert book.reader_name is None


def test_return_book_not_the_borrower(book):
    logger.info('Test 9: attempting to return a book by someone who didn\'t check it out')
    book.get_book("Ash")
    result = book.return_book("Pikachu")
    assert not result
