import random

random_number = random.randint(1, 100)
high = 100
low = 100


def guessNumber(number, high, low):
    number = int(input("pick a number between 1-100"))
    if number == random_number:
        return 'congrats you guessed it.'
    elif number > random_number:
        high = number
        guessNumber(random_number, high, low)
    elif number < random_number:
        low = number
        guessNumber(random_number, high, low)
    else:
        return 'i may have fucked up'
    return


print(guessNumber(random_number, high, low))
