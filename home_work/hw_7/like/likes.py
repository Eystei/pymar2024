"""Module for the Likes class implementation."""


class Likes:
    @staticmethod
    def likes(*names: str | list[str]) -> str:
        if all(isinstance(name, (str, list)) for name in names) == 0:
            raise TypeError("Names must be strings or lists of strings")

        names_list: list[str] = []
        for name in names:
            if isinstance(name, str):
                names_list.append(name)
            else:
                names_list.extend(name)

        num_likes = len(names_list)

        if num_likes == 0:
            return "no one likes this"

        if num_likes == 1:
            return f"{names_list[0]} likes this"

        if num_likes == 2:
            return f"{names_list[0]} and {names_list[1]} like this"

        if num_likes == 3:
            return f"{names_list[0]}, {names_list[1]} and {names_list[2]} like this"

        return f"{names_list[0]}, {names_list[1]} and {num_likes - 2} others like this"
