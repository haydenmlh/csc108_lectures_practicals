from typing import List

def sum_mult_table(N: int) -> int:
    '''Return the sum of the numbers in an NxN multiplication table
    >>> sum_mult_table(0)
    0
    >>> sum_mult_table(1)
    1
    >>> sum_mult_table(2)
    9
    '''
    total = 0
    for i in range(N):
        for j in range(N):
            total += (i+1)*(j+1)
    return total


def check_imports(forbidden: List[str], imports: List[str]) -> bool:
    '''Returns False iff any string in forbidden is a substring of any string
    in imports.
    >>> check_imports(['math'], ['import typing', 'import re'])
    True
    >>> check_imports(['math'], ['import typing', 'import math'])
    False
    '''
    for i in imports:
        for j in forbidden:
            if j in i:
                return False
    return True

def enrolled_teams(teams:List[List[int]], enrolled_students:List[int]) -> bool:
    '''Returns True if all the team members are enrolled students.
    >>> enrolled_teams([[1, 2], [3, 4]], [1, 2, 3, 4])
    True
    >>> enrolled_teams([[1, 2], [3, 4]], [1, 2, 3])
    False
    '''
    for i in range(len(teams)):
        for j in range(len(teams[i])):
            found = False
            for h in range(len(enrolled_students)):
                if teams[i][j] == enrolled_students[h]:
                    found = True
            if not found:
                return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()