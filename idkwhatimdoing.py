#!/usr/bin/env python3
import random
print("hey does this work")


def hello_world(rock_paper_scissors):
    choices = ['rock', 'paper', 'scissors']
    winning = 'i my have won this one'
    tie = 'run it back'
    random_element = random.choice(choices)
    print(random_element, rock_paper_scissors)
    if rock_paper_scissors == 'rock' and random_element == 'scissors':
        print(winning)
    elif rock_paper_scissors == 'rock' and random_element == 'rock':
        print(tie)
    elif rock_paper_scissors == 'scissors' and random_element == 'rock':
        print(winning)
    elif rock_paper_scissors == 'scissors' and random_element == 'scissors':
        print(tie)
    elif rock_paper_scissors == 'paper' and random_element == 'rock':
        print(winning)
    elif rock_paper_scissors == 'paper' and random_element == 'paper':
        print(tie)
    elif rock_paper_scissors != 'paper' and rock_paper_scissors != 'rock' and rock_paper_scissors != 'scissors':
        print('make sure you pick rock paper or scissors')
    else:
        print('you may have lost')

    return


message = hello_world('rock')

print(message)
