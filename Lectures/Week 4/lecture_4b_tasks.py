def remove_spaces(string: str) -> str:
    '''Removes spaces from a string
    >>> remove_spaces('h e l l o')
    'hello'
    >>> remove_spaces('bo ll     y')
    'bolly'
    '''
    final = ''
    for i in string:
        if i != ' ':
            final += i
    return final


def count_spaces(string: str) -> int:
    '''Return the number of spaces  from a string
    >>> count_spaces('hello world')
    1
    >>> count_spaces('h e l l o')
    4
    '''
    counter = 0
    for i in string:
        if i == ' ':
            counter += 1
    return counter


def encrypt_caesar(plaintext: str, shift: int) -> str:
    '''Return the plaintext encrypted using a caesar cypher with rotation shift
    Assumption: plaintext includes ONLY whitespace and upper case characters
    >>> encrypt_caesar('ABCZ', 1)
    'BCDA'
    >>> encrypt_caesar('DE ZB', -2)
    'BC XZ'
    '''
    final = ''
    for i in plaintext:
        if not i.isspace():
            final += chr((ord(i) - 65 + shift) % 26 + 65)
        else:
            final += i

    return final


def decrypt_caesar(encrypted: str, shift: int) -> str:
    ''' Return the encrypted text using a caesar cypher with rotation shift
    given the shift.
    Assumption: encrypted includes ONLY whitespace and upper case characters
    >>> decrypt_caesar('BCDA', 1)
    'ABCZ'
    >>> decrypt_caesar('BC XZ', -2)
    'DE ZB'
    '''
    final = ''
    for i in encrypted:
        if not i.isspace():
            # ord('A') = 65
            final += chr((ord(i) - 65 - shift) % 26 + 65)
        else:
            final += i
    return final


if __name__ == '__main__':
    import doctest
    doctest.testmod()
