def longer(s1: str, s2: str) -> str:
    '''Return the length of the longer string s1 and s2
    >>> longer('hello', 'hi')
    5
    >>> longer('hi', 'hello')
    5
    >>> longer('hi', 'hi')
    2
    >>> longer('','')
    0
    '''
    if len(s1) > len(s2):
        return len(s1)
    if len(s2) > len(s1):
        return len(s2)
    if len(s1) == len(s2):
        return len(s1)

def earlier(s1: str, s2: str) -> str:
    '''Given the two strings s1 and s2, return the string that would appear
    earlier in the dictionary
    >>> earlier('abc', 'acb')
    'abc'
    >>> earlier('Abc', 'abc')
    'Abc'
    >>> earlier('abc', 'abc')
    'abc'
    '''
    if s1 > s2:
        return s1
    if s2 > s1:
        return s1
    if s2 == s1:
        return s1

def count_letter(s: str, char: str) -> int:
    '''Return the total occurences of char in s
    >>> count_letter('aaa', 'a')
    3
    >>> count_letter('a', 'a')
    1
    >>> count_letter('b', 'a')
    0
    '''
    count = 0
    for i in s:
        if char == i:
            count += 1
    return count


def repeat_character(s: str, char: str) -> str:
    ''' Given a string s, and a character char, return a string consisting of
    char repeated as many times as it occurs in s
    >>> repeat_character('abaa', 'a')
    'aaa'
    >>> repeat_character('ab', 'a')
    'a'
    >>> repeat_character('b', 'a')
    ''
    '''
    count = count_letter(s, char)
    return char * count

def where(s: str, ch: str) -> int:
    '''Return the index of the first occurrence of ch in string s
    >>> where('abc', 'a')
    0
    >>> where('baaaaa', 'a')
    1
    >>> where('bbb', 'a')
    -1
    '''
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()