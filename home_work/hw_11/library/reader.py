from log_.logging_setup import get_logger

log = get_logger(__name__)


class Reader:
    def __init__(self, name):
        self.name = name
        self.lib_books = []

    def reserve_book(self, book):
        result = book.reserve(self.name)
        if result:
            log.success(f"{self.name} reserved '{book.book_name}'.")
        else:
            log.error(f"{self.name} could not reserve '{book.book_name}'.")
        return result

    def cancel_reserve(self, book):
        result = book.cancel_reserve(self.name)
        if result:
            log.success(f"{self.name} canceled reserve for '{book.book_name}'.")
        else:
            log.error(f"{self.name} could not cancel reserve for '{book.book_name}'.")
        return result

    def get_book(self, book):
        result = book.get_book(self.name)
        if result:
            self.lib_books.append(book)
            log.success(f"{self.name} got '{book.book_name}'.")
        else:
            log.error(f"{self.name} could not get '{book.book_name}'.")
        return result

    def return_book(self, book):
        result = book.return_book(self.name)
        if result:
            self.lib_books.remove(book)
            log.success(f"{self.name} returned '{book.book_name}'.")
        else:
            log.error(f"{self.name} could not return '{book.book_name}'.")
        return result
