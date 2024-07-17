import pytest
from log_.logging_setup import get_logger
from home_work.hw_11.library.book import Book
from home_work.hw_11.library.reader import Reader

logger = get_logger(__name__)


@pytest.fixture
def book():
    return Book(
        book_name="Harry Potter and the Goblet Fire",
        author="J. K. Rowling",
        num_pages=636,
        isbn="0747550794")


@pytest.fixture
def readers():
    pika = Reader("Pikachu")
    ash = Reader("Ash")
    return pika, ash


def test_multiple_reservations(book, readers):
    pika, ash = readers
    logger.test('Test 1: Multiple reservation flow')
    assert pika.reserve_book(book)
    assert not ash.reserve_book(book)
    assert pika.cancel_reserve(book)
    assert ash.reserve_book(book)


def test_get_book_flow(book, readers):
    pika, ash = readers
    logger.test('Test 2: Get book flow')
    assert pika.reserve_book(book)
    assert pika.get_book(book)
    assert not ash.get_book(book)
    assert pika.return_book(book)
    assert ash.reserve_book(book)
    assert ash.get_book(book)


def test_invalid_return(book, readers):
    pika, ash = readers
    logger.test('Test 3: Invalid return attempt')
    assert pika.reserve_book(book)
    assert pika.get_book(book)
    assert not ash.return_book(book)
