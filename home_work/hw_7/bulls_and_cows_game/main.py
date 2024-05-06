"""main.py module"""
import sys

from home_work.hw_7.bulls_and_cows_game.ascii_title import GAME_TITLE
from home_work.hw_7.bulls_and_cows_game.bulls_and_cows import BullsAndCows


# Быки и коровы
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в
# тайном числе (то есть количество коров)
# и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает
# всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
#
# Пример:
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!


if __name__ == '__main__':
    game = BullsAndCows()

    print(GAME_TITLE)
    print("\nWelcome to the Bulls and Cows game!")
    print("The computer has chosen a 4-digit number. Try to guess it!")
    print("\nTip: If you want to stop game. Enter: 'Exit'")

    while True:
        user_guess = input("Enter your guess:\n> ")
        print(game.secret_number)

        if user_guess.lower() == "exit":
            sys.exit()

        if len(user_guess) != 4 or user_guess.isdigit() == 0:
            print("Please enter 4-digit number.")
            continue

        bulls, cows = game.check_guess(guess=user_guess)
        print(f"Bulls: {bulls} | Cows: {cows}")

        if bulls == 4:
            print("Awesome ! YOU WIN !")
            sys.exit()
