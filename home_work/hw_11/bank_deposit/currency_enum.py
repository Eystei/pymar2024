from enum import Enum


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    BYN = "BYN"

    def __str__(self) -> str:
        return self.value
