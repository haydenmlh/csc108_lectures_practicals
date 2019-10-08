'''
Generating random numbers from software alone is not possible
(possible with hardware though). Software is pseudorandom, random numbers
based on deterministic methods.
'''
from random import randint

def roll_six() -> int:
    not_six = True
    rolls_required = 0
    while not_six:
        current = randint(1, 6)
        if current == 6:
            rolls_required += 1
            not_six = False
            return rolls_required
        else:
            print(current)
            rolls_required += 1


def roll_until(threshold: int) -> int:
    current = 0
    rolls = 0
    while current < threshold:
        current += randint(1, 6)
        rolls += 1
    return rolls

def guess_number() -> int:
    number = 33
    current = 0
    count = 0
    while current != number:
        current = int(input())
        if current < number:
            print('Too low')
            count += 1
        elif current > number:
            print('Too high')
            count += 1
        else:
            count += 1
            return count