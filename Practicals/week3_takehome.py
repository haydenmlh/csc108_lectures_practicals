# 1.
# mssg
# msisa
# arh

def can_drink_beer(age: int, country_name: str, contains_alcohol: bool) -> bool:
    ''' blah bblah blah
    >>> can_drink_beer(10, 'USA', False)
    True
    >>> can_drink_beer(24, 'USA', True)
    False
    >>> can_drink_beer(25, 'USA', True)
    True
    >>> can_drink_beer(15, 'Beerland', True)
    True
    >>> can_drink_beer(15, 'dumbland', True)
    False
    >>> can_drink_beer(16, 'dumbland', True)
    True
    '''
    if not contains_alcohol:
        return True
    else:
        if country_name == 'USA':
            if age < 25:
                return False
            else:
                return True
        elif country_name == 'Beerland':
            return True
        else:
            if age < 16:
                return False
            else:
                return True


x = '0123456789'
print(x[::2][3])

''' Question 4
a:b:c is sliced first. Order matters
'''

''' Question 5
>>> f(11)
CH
>>> f(300)
AH
>>> f(5)
DF
No errors
'''

'''Question 6
'''

VOWELS = 'aeiou'
def past_tense(str: str) -> str:
    '''Returns past tense of a given word. Follows grammar rules:
    if it ends with e, add d
    if it ends with y, and has a vowel before the y, add ed
    if it ends with y and has no vowel before the y, remove the Y and add ied
    for all other cases, add ed
    >>> past_tense('try')
    'tried'
    >>> past_tense('fat')
    'fated'
    >>> past_tense('ghost')
    'ghosted'
    >>> past_tense('slay')
    'slayed'
    >>> past_tense('die')
    'died'
    '''
    if str[-1] == 'e':
        return str + 'd'
    if str[-1] == 'y':
        if str[-2] in VOWELS:
            return str + 'ed'
        else:
            return str[:-1] + 'ied'
    else:
        return str + 'ed'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.testmod(verbose=1)
