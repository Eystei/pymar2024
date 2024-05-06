"""Module for the Likes class implementation."""


class Likes:
    """Class for generating 'likes' message based on the input names."""

    @staticmethod
    def likes(*names: str | list[str]) -> str:
        """Generates a 'likes' message based on the input names."""

        if all(isinstance(name, (str, list)) for name in names) == 0:
            raise TypeError("Names must be strings or lists of strings")

        if len(names) == 1:
            if isinstance(names[0], str):
                names = [names[0]]
            elif isinstance(names[0], list):
                names = names[0]

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
