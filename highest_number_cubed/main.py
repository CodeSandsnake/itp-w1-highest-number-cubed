"""This is the entry point of the program."""


def highest_number_cubed(limit):
    number = 0
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number - 1