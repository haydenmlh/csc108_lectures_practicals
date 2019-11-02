from typing import List

pets = [["Shoji", "cat", 18], ["Hanako", "dog", 15], ["Sir Toby", "cat", 10],
["Sachiko", "cat", 7], ["Sasha", "dog", 3], ["Lopez", "dog", 13]]

for i in pets:
    print(i)

for i in range(len(pets)):
    print(pets[i][1])

count_dogs = 0
for i in range(len(pets)):
    if pets[i][1] == "dog":
        count_dogs += 1
print(f'number of dogs is {count_dogs}')

total_age = 0
for i in range(len(pets)):
    total_age += pets[i][2]
print(f'total age is {total_age}')


def nested_lengths(L: List[List[str]]) -> List[int]:
    '''Return list of the length of the sublists of L
    >>> nested_lengths([[1,2],['a','b','c']])
    [2, 3]
    >>> nested_lengths([[1, 2, 3], [1, 2], [1, 1, 1]])
    [3, 2, 3]
    '''
    list_length = []
    for i in L:
        list_length.append(len(i))
    return list_length

print(f'nested_lengths([[1, 2, 3], [1, 2], [1, 1, 1]])')
nested_lengths([[1, 2, 3], [1, 2], [1, 1, 1]])


if __name__ == '__main__':
    import doctest
    doctest.testmod()