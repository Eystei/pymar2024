from unittest import TestCase, main
from log_.logging_setup import get_logger
from home_work.hw_11.library.reader import Reader
from home_work.hw_11.library.book import Book


logger = get_logger(__name__)


class TestReader(TestCase):
    def setUp(self):
        self.book = Book(
            book_name="Harry Potter and the Goblet of Fire",
            author="J. K. Rowling",
            num_pages=636,
            isbn="0747550794")
        self.reader = Reader(name="Angela")

    def test_01_reserve_book_success(self):
        logger.test("Test 1: successful reservation of a book")
        result = self.reader.reserve_book(self.book)
        self.assertTrue(result)
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.reader.name)

    def test_02_reserve_book_failure_already_reserved(self):
        logger.test("Test 2: attempt to reserve a book that is already reserved by someone else")
        self.book.reserve("Pikachu")
        result = self.reader.reserve_book(self.book)
        self.assertFalse(result)

    def test_03_cancel_reserve_success(self):
        logger.test("Test 3: successful cancellation of a reservation")
        self.reader.reserve_book(self.book)
        result = self.reader.cancel_reserve(self.book)
        self.assertTrue(result)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_04_cancel_reserve_failure_not_reserved(self):
        logger.test("Test 4: attempt to cancel a reservation on a book that is not reserved")
        result = self.reader.cancel_reserve(self.book)
        self.assertFalse(result)

    def test_05_get_book_success(self):
        logger.test("Test 5: successful acquisition of a book")
        self.reader.reserve_book(self.book)
        result = self.reader.get_book(self.book)
        self.assertTrue(result)
        self.assertIn(self.book, self.reader.lib_books)

    def test_06_return_book_success(self):
        logger.test("Test 6: successful return of a book")
        self.reader.reserve_book(self.book)
        self.reader.get_book(self.book)
        result = self.reader.return_book(self.book)
        self.assertTrue(result)
        self.assertNotIn(self.book, self.reader.lib_books)


if __name__ == "__main__":
    main()
