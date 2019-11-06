#writelines - have to add own end of line
from typing import List, TextIO

def freq(infile: TextIO, outfile: TextIO) -> None:
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #list with 10 integers
    # above can also use count = [0] * 10
    for line in infile:
        count[int(line)] += 1
    infile.close()
    for i in range(len(count)):
        outfile.write(f'{i} {count[i]}\n')
    outfile.close()

def freq_firstletter(infile: TextIO, outfile: TextIO) -> None:
    '''Given a infile of names, write the count of the first letters of the
    names found in that file to outfile'''
    count = {}
    for line in infile:
        letter = line[0]
        count[letter] = count.get(letter, 0) + 1
    infile.close()
    for (letter, count) in count.items():
        outfile.write(f'{letter} {count}\n')
    outfile.close()


if __name__ == '__main__':
    x = open('data\\names.txt')
    y = open('data\\names_output.txt', 'w')
    freq_firstletter(x, y)