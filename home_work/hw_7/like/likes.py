"""Module for the Likes class implementation."""


# pylint: disable=too-few-public-methods
class Likes:
    @staticmethod
    def likes(*names: str) -> str:

        if not all(isinstance(name, str) and name for name in names):
            raise TypeError("Names must be strings and not empty string.")

        num_likes = len(names)

        if num_likes == 0:
            return "no one likes this"

        if num_likes == 1:
            return f"{names[0]} likes this"

        if num_likes == 2:
            return f"{names[0]} and {names[1]} like this"

        if num_likes == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"

        return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"
