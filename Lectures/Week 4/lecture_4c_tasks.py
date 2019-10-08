def largest_char(s: str) -> str:
    '''Return the largest character in s.
    Assumption: len(s) > 0
    >>> largest_char('abczdef')
    'z'
    >>> largest_char('2   Z')
    'Z'
    '''
    curr_largest = s[0]
    for ch in s:
        if ch> curr_largest:
            curr_largest = ch
    return curr_largest

def replace_largest(s: str) -> str:
    '''Returns s minus all instances of the largest character.
    >>> replace_largest('abczdef')
    'abcdef'
    >>> replace_largest('2   Z')
    '2   '
    '''
    return s.replace(largest_char(s), '')

def tweet_check(s: str) -> bool:
    '''Returns True if s contains only alphanumeric or underscore
    False if it contains other characters
    >>> tweet_check('hel@lo')
    False
    >>> tweet_check('hel_lo')
    True
    >>> tweet_check('hello')
    True
    '''
    for i in s:
        if not i.isalnum() and i != '_':
            return False
    return True


def check_non_desc(string: str) -> bool:
    '''Returns True only if the characters are non-descending (ascending
    but with ties allowed)
    >>> check_non_desc('abc')
    True
    >>> check_non_desc('acb')
    False
    >>> check_non_desc('Abc')
    True
    >>> check_non_desc('aBc')
    False
    >>> check_non_desc('BCa')
    True
    '''
    current_ord = ord(string[0])
    for i in string:
        if ord(i) > 0: # starts after the first character
            if ord(i) < current_ord:
                return False
            current_ord = ord(i)
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()