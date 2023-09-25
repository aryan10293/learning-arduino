#!/usr/bin/env python3
import random

random_number = random.randint(1, 100)
high = 100
low = 1

print(random_number)


def guessNumber(high, low):

    # if number == random_number:
    #     return 'congrats you guessed it.'
    # elif number > random_number:
    #     high = number
    #     guessNumber(random_number, high, low)
    # elif number < random_number:
    #     low = number
    #     guessNumber(random_number, high, low)
    # else:
    #     return 'i may have fucked up'
    print(random_number)
    number = 1
    while number != random_number:
        number = int(input(f"Pick a number between {low}-{high}: "))
        if number > random_number:
            high = number
        elif number < random_number:
            low = number

    return 'that might have been the right number'


print(guessNumber(high, low))
