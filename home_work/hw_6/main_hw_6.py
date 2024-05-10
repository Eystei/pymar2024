"""
Module with functions to solve given problems.
"""

# problem_1
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite"
# => ["I", "love", "arrays", "they", "are", "my", "favorite"]

# problem_2
# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

# problem_3
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

# problem_4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

TEXT_1 = "Robin Singh"
TEXT_2 = "I love arrays they are my favorite"

FULL_NAME = ['Ivan', 'Ivanou']
CITY = 'Minsk'
COUNTRY = 'Belarus'

LIST_WITH_TEXT = ["I", "love", "arrays", "they", "are", "my", "favorite"]


def string_to_list(text: str) -> list:
    """Convert the string to a list of words."""
    return text.split(" ")


def list_to_string(data: list) -> str:
    """Convert the list of words to a string."""
    return " ".join(data)


def create_welcome_message(full_name_data: list, *country_info):
    """Create a welcome message."""
    return (f"Привет, {' '.join(full_name_data)}! "
            f"Добро пожаловать в {' '.join(country_info)}")


if __name__ == '__main__':
    # problem_1
    print(string_to_list(text=TEXT_1))
    print(string_to_list(text=TEXT_2))

    # problem_2
    print(create_welcome_message(FULL_NAME, CITY, COUNTRY))

    # problem_3
    print(list_to_string(data=LIST_WITH_TEXT))

    # problem_4
    ten_items_list = [f'{i}' for i in range(1, 11)]
    print(ten_items_list)

    ten_items_list.insert(2, 'new_item')
    print(ten_items_list)

    ten_items_list.pop(6)
    print(ten_items_list)
