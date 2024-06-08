from book import Book
from reader import Reader


def main():
    book = Book(
        book_name="Atlas Shrugged",
        author="Ayn Rand",
        num_pages=1168,
        isbn="1234567890")

    pika = Reader("Pickachu")
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


if __name__ == "__main__":
    main()
