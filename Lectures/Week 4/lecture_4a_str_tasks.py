VOWELS = 'aeiouAEIOU'

def reverse_string(str: str) -> str:
    ''' Given a string, reverses the string
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('star')
    'rats'
    '''
    reverse = ''
    for s in str:
        reverse = s + reverse

    return reverse


def capitalize(str: str) -> str:
    '''Given a string, capitalize the entire string
    >>> capitalize('aaa')
    'AAA'
    >>> capitalize('aBa')
    'ABA'
    '''
    capitalized = ''
    for s in str:
        capitalized = str.upper()

    return capitalized


def contains_vowels(str: str) -> bool:
    '''Returns if the string contains vowels
    >>> contains_vowels('abc')
    True
    >>> contains_vowels('bbc')
    False
    '''
    count = 0

    for s in str:
        if s in VOWELS:
            count += 1
    return count > 0


if __name__ == '__main__':
    import doctest

    doctest.testmod()
