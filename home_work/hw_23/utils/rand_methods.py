import random
import string


class Randoms:

    @staticmethod
    def rand_word(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def int_gen(length: int) -> str:
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def email_gen(length: int) -> str:
        return f"{Randoms.rand_word(length)}@mail.com"

    @staticmethod
    def date_of_birth() -> str:
        year = random.randint(1900, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        return f"{year:04d}-{month:02d}-{day:02d}"
