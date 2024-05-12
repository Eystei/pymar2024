"""Module for main functionality."""

from home_work.hw_7.like.likes import Likes

if __name__ == '__main__':
    print(Likes.likes())
    print(Likes.likes("Ann"))
    print(Likes.likes("Виктор", "Алекс"))
    print(Likes.likes("Ann", "Alex", "Mark"))
    print(Likes.likes("Ann", "Alex", "Mark", "Max"))
