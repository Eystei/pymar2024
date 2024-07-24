from unittest import TestCase, main
import logging
from home_work.hw_11.library.book import Book
from home_work.hw_11.library.reader import Reader

logger = logging.getLogger(__name__)


class TestLibraryInteractions(TestCase):
    def setUp(self):
        self.book = Book(
            book_name="Harry Potter and the Goblet Fire",
            author="J. K. Rowling",
            num_pages=636,
            isbn="0747550794")

        self.pika = Reader("Pikachu")
        self.ash = Reader("Ash")

    def test_multiple_reservations(self):
        logger.info('Test 1: Multiple reservation flow')
        self.assertTrue(self.pika.reserve_book(self.book))
        self.assertFalse(self.ash.reserve_book(self.book))
        self.assertTrue(self.pika.cancel_reserve(self.book))
        self.assertTrue(self.ash.reserve_book(self.book))

    def test_get_book_flow(self):
        logger.info('Test 2: Get book flow')
        self.assertTrue(self.pika.reserve_book(self.book))
        self.assertTrue(self.pika.get_book(self.book))
        self.assertFalse(self.ash.get_book(self.book))
        self.assertTrue(self.pika.return_book(self.book))
        self.assertTrue(self.ash.reserve_book(self.book))
        self.assertTrue(self.ash.get_book(self.book))

    def test_invalid_return(self):
        logger.info('Test 3: Invalid return attempt')
        self.assertTrue(self.pika.reserve_book(self.book))
        self.assertTrue(self.pika.get_book(self.book))
        self.assertFalse(self.ash.return_book(self.book))


if __name__ == '__main__':
    main()
