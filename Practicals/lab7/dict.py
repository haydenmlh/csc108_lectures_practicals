from typing import Dict, TextIO, List


def dict_to_str(d: Dict[int, int]) -> str:
    '''Return a str containing each key and value in d. Keys and
    values are separated by a space. Each key-value pair is separated by a
    comma. 

    >>> dict_to_str({3: 4, 5: 6})
    '3 4, 5 6'
    >>> dict_to_str({3: 4, 5: 6, 2: 1})
    '3 4, 5 6, 2 1'
    '''
    acc = ''
    start = True
    for key in d:
        if start:
            acc += f'{key} {d[key]}'
            start = False
        else:
            acc += f', {key} {d[key]}'
    return acc

        
def dict_to_str_sorted(d: Dict[int, int]) -> str:
    '''(dict) -> str
    Return a str containing each key and value in d. Keys and
    values are separated by a space. Each key-value pair is separated by a
    comma, and the pairs are sorted in ascending order by key.
    
    >>> dict_to_str_sorted({5: 6, 3: 8})
    '3 8, 5 6'
    >>> dict_to_str_sorted({3: 4, 5: 6, 2: 1})
    '2 1, 3 4, 5 6'
    '''
    sorted_keys = sorted(d.keys())
    acc = ''
    start = True
    for key in sorted_keys:
        if start:
            acc += f'{key} {d[key]}'
            start = False
        else:
            acc += f', {key} {d[key]}'
    return acc


def file_to_dict(f: TextIO) -> Dict[float, int]:
    ''' Return a dict containing the number of times each rate change that 
    occurs in the open file f.  The dictionary should contain exchange rate 
    changes as keys and the number of occurrences of each change as values.
    >>> filename = 'exchange-rates-testing.dat'
    >>> x = open(filename)
    >>> y = file_to_dict(x)
    >>> print(y)
    {'0.0045': 1, '0.0160': 1, '-0.0028': 1, '-0.0157': 1, '-0.0443': 1, '-0.0232': 1, '-0.0065': 2, '-0.0080': 2, '0.0052': 1, '-0.0052': 1, '-0.0283': 1, '-0.0087': 1, '-0.0020': 1, '-0.0290': 2, '0.0180': 1, '0.0030': 1, '-0.0170': 1, '0.0000': 1, '-0.0185': 1, '-0.0055': 1, '0.0148': 1, '-0.0053': 1, '0.0265': 1, '0.0010': 1, '-0.0015': 1, '0.0137': 1, '-0.0137': 1, '-0.0023': 1, '0.0008': 1, '0.0055': 1, '-0.0025': 1, '-0.0125': 1, '0.0040': 1}
    '''
    d = {}
    for i in f:
        split = i.strip().split(' ')
        for j in split:
            if j != '':
                d[j] = d.get(j, 0) + 1
    return d


def count_data(d: Dict[float, int]) -> int:
    '''Return the total number of exchange rates (including duplicates) in 
    the dictionary d of exchange rates. 
    Note: the input to this function is the output of file_to_dict
    >>> filename = 'exchange-rates-testing.dat'
    >>> x = open(filename)
    >>> y = file_to_dict(x)
    >>> count_data(y)
    36
    '''
    count = 0
    for i in d:
        count += d[i]
    return count


def most_common_rate_change(d: Dict[float, int]) -> List[float]:
    '''Return the exchange rate changes that occur the most frequently in 
    the dictionary d of exchange rates. 
    Note: the input to this function is the output of file_to_dict
    >>> filename = 'exchange-rates-testing.dat'
    >>> x = open(filename)
    >>> y = file_to_dict(x)
    >>> most_common_rate_change(y)
    '-0.0065'
    '''
    pass
    highest = -1
    key = ''
    for i in d:
        if d[i] > highest:
            highest = d[i]
            key = i
    return key
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # filename = 'exchange-rates-testing.dat'
    # # Open the file here and call the functions above to read data from it and
    # # manipulate the data.
    # x = open(filename)
    # y = file_to_dict(x)
    # x.close()
    # print(y)
    # print(count_data(y))
    # print(most_common_rate_change(y))
