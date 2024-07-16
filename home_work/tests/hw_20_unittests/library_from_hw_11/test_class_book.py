from unittest import TestCase, main
from log_.logging_setup import get_logger

from home_work.hw_11.library.book import Book


logger = get_logger(__name__)


class TestBook(TestCase):
    def setUp(self):
        self.book = Book(
            book_name="Harry Potter Philosopher's Stone",
            author="J. K. Rowling",
            num_pages=636,
            isbn="0747550794")

    def test_reserve_not_reserved(self):
        logger.test('Test 1: reserving a book that is not currently reserved')
        result = self.book.reserve("Pikachu")
        self.assertTrue(result)
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, "Pikachu")

    def test_reserve_already_reserved(self):
        logger.test('Test 2: attempting to reserve a book that is already reserved')
        self.book.reserve("Ash")
        result = self.book.reserve("Pikachu")
        self.assertFalse(result)

    def test_reserve_while_booked(self):
        logger.test('Test 3: attempting to reserve a book that is already checked out')
        self.book.get_book("Ash")
        result = self.book.reserve("Pikachu")
        self.assertFalse(result)

    def test_cancel_reservation_success(self):
        logger.test('Test 4: successfully cancelling a reservation')
        self.book.reserve("Pikachu")
        result = self.book.cancel_reserve("Pikachu")
        self.assertTrue(result)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_cancel_reservation_wrong_user(self):
        logger.test('Test 5: attempting to cancel a reservation by someone other')
        self.book.reserve("Ash")
        result = self.book.cancel_reserve("Pikachu")
        self.assertFalse(result)

    def test_get_book_success(self):
        logger.test('Test 6: successfully getting a book after reserving it')
        self.book.reserve("Pikachu")
        result = self.book.get_book("Pikachu")
        self.assertTrue(result)
        self.assertEqual(self.book.reader_name, "Pikachu")

    def test_get_book_reserved_by_another(self):
        logger.test('Test 7: attempting to get a book that is reserved by another user')
        self.book.reserve("Ash")
        result = self.book.get_book("Pikachu")
        self.assertFalse(result)

    def test_return_book_success(self):
        logger.test('Test 8: successfully returning a book that was checked out')
        self.book.get_book("Pikachu")
        result = self.book.return_book("Pikachu")
        self.assertTrue(result)
        self.assertIsNone(self.book.reader_name)

    def test_return_book_not_the_borrower(self):
        logger.test('Test 9: attempting to return a book by someone who didn\'t check it out')
        self.book.get_book("Ash")
        result = self.book.return_book("Pikachu")
        self.assertFalse(result)


if __name__ == '__main__':
    main()
