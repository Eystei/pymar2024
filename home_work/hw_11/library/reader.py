from loguru import logger as log


class Reader:
    def __init__(self, name):
        self.name = name
        self.lib_books = []

    def reserve_book(self, book):
        if book.reserve(self.name):
            log.success(f"{self.name} reserved '{book.book_name}'.")
            return True
        else:
            log.error(f"{self.name} could not reserve '{book.book_name}'.")
            return False

    def cancel_reserve(self, book):
        if book.cancel_reserve(self.name):
            log.success(f"{self.name} cancel reserve '{book.book_name}'.")
            return True
        else:
            log.error(f"{self.name} could not cancel reserve '{book.book_name}'.")
            return False

    def get_book(self, book):
        if book.get_book(self.name):
            self.lib_books.append(book)
            log.success(f"{self.name} get '{book.book_name}'.")
            return True
        else:
            log.error(f"{self.name} could not get '{book.book_name}'.")
            return False

    def return_book(self, book):
        if book.return_book(self.name):
            self.lib_books.remove(book)
            log.success(f"{self.name} returned '{book.book_name}'.")
            return True
        else:
            log.error(f"{self.name} could not return '{book.book_name}'.")
            return False
