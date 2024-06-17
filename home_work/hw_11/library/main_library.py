from home_work.hw_11.library.book import Book
from home_work.hw_11.library.reader import Reader

book = Book(
    book_name="Atlas Shrugged",
    author="Ayn Rand",
    num_pages=1168,
    isbn="1234567890")

pika = Reader("Pikachu")
ash = Reader("Ash")

pika.reserve_book(book)
ash.reserve_book(book)
pika.cancel_reserve(book)
ash.reserve_book(book)
pika.get_book(book)
ash.get_book(book)
ash.return_book(book)
pika.get_book(book)
ash.get_book(book)
pika.return_book(book)
ash.get_book(book)
