'''
r - read mode is safe
w - write mode is not safe -> clears the file first if it exists.
a - append mode is safer -> adds to the end
open file object remembers where it read to
need to reset the file pointer to reset where it came from
which do we use? - partly a matter of preference
for loop: reads entire file
readline: better for multiline files
readlines:
read:

Closing files - if you do not close files, they remain open and vulnerable to
side effects. Some of your file is missing or extra bits in your file.
** Must close the file (flush the file)
file.close()
'''

from typing import TextIO
from io import StringIO # you can investigate this in your free time

def num_as(file:TextIO) -> int:
    '''Return the number of a in a given file
    >>> num_as(open('data\hello.txt'))
    2
    >>> num_as(example_f)
    4

    count = 0
    for line in file:
        for char in line:
            if char == 'a':
                count += 1
    return count
    '''
    #read
    return file.read().count('a')

def num_backn(file:TextIO) -> int:
    '''Return the number of empty lines in the open file in a given file
    >>> num_backn(open('data\hello.txt'))
    0
    >>> num_backn(empty_line_example)
    2
    '''
    count = 0
    for line in file:
        if line == '\n':
            count += 1
    return count

def sum_file(file: TextIO) -> int:
    '''Return the sum of the integers in the open file
    >>> sum_file(open('data\numbers.txt'))
    4430
    >>> sum_file(nums_example)
    45
    '''
    return sum(file.readlines())


if __name__ == '__main__':
    import doctest
    example_f = StringIO('\n\nI have lots of a characters\nLots I tell you.\n')
    empty_line_example = StringIO('\n\nNotempty\n')
    nums_example = StringIO('42\n6\n-3\n')
    doctest.testmod()