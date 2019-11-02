from typing import List

def flatten(L: List) -> List:
    '''Return a list of literals comprosing L without necessarily preserving
    ordering
    >>> flatten([[1, 2], [], [[3], [4, 5]]])
    [4, 5, 3, 1, 2]
    '''
    worklist = [L]
    flattened = []
    while worklist != []:
        curr_item = worklist.pop(0)
        for item in curr_item:
            if type(item) is list:
                worklist.insert(0, item)
            else: #not a list
                flattened.append(item)
    return flattened


def mult_table(N: int) -> int:
    '''Return a N x N list of lists containing the N x N multiplication table
    >>> mult_table(1)
    [[1]]
    >>> mult_table(3)
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    '''
    acc = []
    for i in range(N):
        acc.append([])
        for j in range(N):
            acc[i].append((i+1)*(j+1))
    return acc

def mult_table_range(N: int) -> int:
    '''Return a N x N list of lists containing the N x N multiplication table
    >>> mult_table_range(1)
    [[1]]
    >>> mult_table_range(3)
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    '''
    acc = []
    for x in range(1, N+1):
        acc.append(list(range(x, x * N + 1, x)))
    return acc

#Task 7 - Don't assume Matrix is N x N
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    '''Return the transpose of the given matrix
    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    acc = []
    for i in range(len(matrix)):
        acc.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            acc[j].append(matrix[i][j])
    return acc

# you may assume matrix is NxN for this problem
def transpose_in_place(matrix: List[List[int]]) -> None:
    '''Transpose the given matrix
    >>> AA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose_in_place(AA)
    >>> AA
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
