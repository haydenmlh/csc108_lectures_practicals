from typing import TextIO, Dict, List

def char_frequency(s: str) -> Dict[str, int]:
    '''Return the frequencies of the characters in s.

    >>> char_frequency('hello')
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    '''
    freq_dict = {}
    for i in s:
        i = i.lower()
        freq_dict[i] = freq_dict.get(i, 0) + 1
    return freq_dict

def char_index(s: str) -> Dict[str, int]:
    '''Return the frequencies of the characters in s.

    >>> char_index('hello')
    {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}
    '''
    freq_dict = {}
    for i in range(len(s)):
        x = freq_dict.get(s[i], []) + [i]
        freq_dict[s[i]] = x
    return freq_dict

def reverse_lookup(d: Dict, item) -> List:
    '''Returns all keys such that d[keys] == item
    >>> reverse_lookup({1: 'A', 2: 'B', -31: 'A'}, 'A')
    [1, -31]
    >>> reverse_lookup({1: 'A', 2: 'B', -31: 'A'}, 'C')
    []
    '''
    acc = []
    for i in d:
        if d[i] == item:
            acc += [i]
    return acc

if __name__ == '__main__':
    import doctest
    doctest.testmod()