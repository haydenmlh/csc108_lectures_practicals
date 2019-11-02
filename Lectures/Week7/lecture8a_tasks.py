from typing import TextIO

def highest_rated_band(file:TextIO) -> int:
    '''Given a file of bands, return the rating of the highest rated band in
    the file'''
    file.readline()
    highest = -1
    for i in file:
        i_split = i.rstrip().split(',') #need to strip the right EOL character
        value = int(i_split[1])
        if value > highest:
            highest = value
    file.close()
    return highest

def highest_rated_bandname(file: TextIO) -> str:
    '''Given a file of bands, return the name of the highest rated
    band in the file. In the case of ties, return the one with more plays'''
    file.readline()
    highest_rating, highest_view, highest_bandname = 0, 0, ''
    for i in file:
        i_split = i.rstrip().split(',')  # need to strip the right EOL character
        (name, value, view) = (i_split[0], int(i_split[1]), int(i_split[2]))
        if value > highest_rating or \
                (value == highest_rating and view > highest_view):
            highest_bandname, highest_rating, highest_view = name, value, view
    file.close()
    return highest_bandname

def write_bands_by_rating(file: TextIO, outfile: TextIO) -> str:
    '''Given a file of bands, write the data in the file to outfile ordered
    by rating. In the case of ties, the one with more plays comes first.

    Assumption: No band with have both the same rating and same number of plays
    '''


if __name__ == '__main__':
    bands = open('data\\bands.csv')
    print(f'Highest bandname: {highest_rated_bandname(bands)}')