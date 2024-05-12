"""Module for the Likes class implementation."""


# pylint: disable=too-few-public-methods
class Likes:
    @staticmethod
    def likes(*names: str) -> str:

        if not all(isinstance(name, str) and name for name in names):
            raise TypeError("Names must be strings and not empty string.")

        match a := len(names):
            case 0:
                return "no one likes this"
            case 1:
                return f"{names[0]} likes this"
            case 2:
                return f"{names[0]} and {names[1]} like this"
            case 3:
                return f"{names[0]}, {names[1]} and {names[2]} like this"
            case _:
                return f"{names[0]}, {names[1]} and {a - 2} others like this"
