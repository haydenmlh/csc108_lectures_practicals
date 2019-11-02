from typing import List

def print_list(L: List):
    '''Print each element of List L on a separate line
    >>> print_list([1, 2])
    1
    2
    >>> print_list([1, 2, 3])
    1
    2
    3
    '''
    for i in range(len(L)):
        print(L[i])
    return

def print_list_even(L: List):
    '''Print elements of L that occur at even indices
    >>> print_list_even([1, 2, 3, 4])
    1
    3
    >>> print_list_even([1, 2])
    1
    '''
    i = 0
    while i < len(L):
        if i % 2 == 0:
            print(L[i])
        i += 1
    return

def print_list_reverse(L: List):
    '''Prints elements of L in reverse
    >>> print_list_reverse([1, 2])
    2
    1
    >>> print_list_reverse([1])
    1
    '''
    L.reverse()
    for i in L:
        print(i)
    return

def sum_elements(L: List[int]) -> int:
    '''Sum the elements of L from the first element until the total is over 100
    or the end of the list is reached and return the sum
    >>> sum_elements([1, 99, 1])
    100
    >>> sum_elements([99, 2, 1])
    101
    '''
    sum = 0
    i = 0
    while i < len(L) and sum < 100:
        sum += L[i]
        i += 1
    return sum

def duplicates(L: List) -> bool:
    '''Return True iff list L contains at least 2 adjacent elements with the
    same element with the same value.
    >>> duplicates([1, 1, 2])
    True
    >>> duplicates([1, 2, 1])
    False
    '''
    previous = None
    for i in L:
        if i == previous:
            return True
        previous = i
    return False




if __name__ == '__main__':
    import doctest
    doctest.testmod()